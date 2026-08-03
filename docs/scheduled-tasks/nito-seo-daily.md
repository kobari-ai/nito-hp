---
name: nito-seo-daily
description: nitoのGA4推移(江東区除くオーガニックのみ)を確認しGSCから新規記事候補を3本提案する・平日朝9時・提案のみで執筆やpushはしない
---

nito（nito-0210.com）のGA4とSearch Consoleを分析し、**現状の推移を報告したうえで、新規記事の候補を3本提案する**。会話履歴は無い前提で、必ず下記どおり実行すること。

**このタスクは提案までで終了する。記事の執筆・ビルド・pushは絶対に行わない**（ユーザーが承認してから、別途おこなう）。

## 前提情報（すべて直書き。推測しない）

- サイト: `sc-domain:nito-0210.com`
- GSC/GA4のサービスアカウント鍵: `/Users/okamurakiichi/.nito/ga4-key.json`
- GA4プロパティID: `536543493`
- リポジトリ: `/Users/okamurakiichi/Downloads/Claude/260621_wordpress立ち上げ/nito-hp`
- 既存記事のmd: 上記リポジトリの `media/posts/*.md`（2026年7月末時点で50本）
- **江東区（GA4上の表記は `Koto City`）は自分たちの閲覧**。外部の実績を見るときは必ず除外する
- **Direct（直接流入）も自分たちがブックマーク等で見ている可能性が高いため、推移集計は「江東区を除いたオーガニック検索（Organic Search）」に絞る**。チャネル別内訳の表示自体は参考情報として引き続き出す

## 手順

### 1. GA4でオーガニック流入の推移を確認する（江東区を除外、Organic Searchのみ）

`mkdir -p /tmp/llmo_read` を実行してから、下記を `/tmp/llmo_read/ga4_trend.py` に書いて実行する（`python3 -P` で実行し、他スクリプトとの名前衝突を避ける）。

```python
from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (RunReportRequest, DateRange, Dimension, Metric,
    Filter, FilterExpression, FilterExpressionList)
KEY='/Users/okamurakiichi/.nito/ga4-key.json'; PID='536543493'
c=BetaAnalyticsDataClient(credentials=service_account.Credentials.from_service_account_file(KEY))
not_koto=FilterExpression(not_expression=FilterExpression(filter=Filter(
    field_name='city', string_filter=Filter.StringFilter(value='Koto City'))))
organic=FilterExpression(filter=Filter(
    field_name='sessionDefaultChannelGroup', string_filter=Filter.StringFilter(value='Organic Search')))
not_koto_organic=FilterExpression(and_group=FilterExpressionList(expressions=[not_koto, organic]))
def rep(dims, mets, ranges, limit=25, filt=not_koto_organic):
    req=RunReportRequest(property=f'properties/{PID}',
        dimensions=[Dimension(name=d) for d in dims],
        metrics=[Metric(name=m) for m in mets],
        date_ranges=ranges, dimension_filter=filt, limit=limit)
    return c.run_report(req)
def total_sessions(s,e,filt=not_koto_organic):
    r=rep([], ['sessions'], [DateRange(start_date=s,end_date=e)], filt=filt)
    return int(r.rows[0].metric_values[0].value) if r.rows else 0
cur=total_sessions('7daysAgo','yesterday')
prv=total_sessions('14daysAgo','8daysAgo')
diff = f"{(cur-prv)/prv*100:+.0f}%" if prv else "—"
print("=== オーガニック検索セッション（江東区除く）===")
print(f"  直近7日: {cur}  前7日: {prv}  ({diff})")
# 参考: チャネル別内訳（江東区除く、全チャネル）
r3=rep(['sessionDefaultChannelGroup'], ['sessions'], [DateRange(start_date='7daysAgo',end_date='yesterday')], filt=not_koto)
print("\n=== 参考：チャネル別内訳（直近7日・江東区除く全チャネル）===")
for row in r3.rows:
    print(f"  {row.metric_values[0].value:>4}  {row.dimension_values[0].value}")
# ランディングページ別（オーガニックのみ）
r4=rep(['landingPagePlusQueryString'], ['sessions'], [DateRange(start_date='7daysAgo',end_date='yesterday')], limit=12)
print("\n=== 入口ページ別（直近7日・オーガニックのみ）===")
for row in r4.rows:
    print(f"  {row.metric_values[0].value:>4}  {row.dimension_values[0].value[:60]}")
```

エラーが出たら、原因を報告したうえでGSC（手順2）は続行する。

### 2. GSCから直近28日のデータを取得する

下記を `/tmp/llmo_read/daily_report.py` に書いて実行する（既にあればそのまま実行してよい）。

```python
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import date, timedelta
KEY='/Users/okamurakiichi/.nito/ga4-key.json'; SITE='sc-domain:nito-0210.com'
creds=service_account.Credentials.from_service_account_file(KEY,scopes=['https://www.googleapis.com/auth/webmasters.readonly'])
svc=build('searchconsole','v1',credentials=creds)
end=date.today()-timedelta(days=2)   # GSCは2-3日遅延
cur_s=end-timedelta(days=27)
prev_e=cur_s-timedelta(days=1); prev_s=prev_e-timedelta(days=27)
def q(s,e,dims,limit=1000):
    return svc.searchanalytics().query(siteUrl=SITE,body={'startDate':s.isoformat(),
        'endDate':e.isoformat(),'dimensions':dims,'rowLimit':limit}).execute().get('rows',[])
cur={r['keys'][0]:r for r in q(cur_s,end,['query'])}
prev={r['keys'][0]:r for r in q(prev_s,prev_e,['query'])}
print(f"期間 {cur_s}〜{end} / クエリ数 {len(cur)}（前期間 {len(prev)}）")
new=[(k,v) for k,v in cur.items() if k not in prev and v['impressions']>=2]
print(f"\n=== 新規クエリ {len(new)}件 ===")
for k,v in sorted(new,key=lambda x:-x[1]['impressions'])[:25]:
    print(f"  表示{v['impressions']:>3} 順位{v['position']:>5.1f}  {k}")
near=[(k,v) for k,v in cur.items() if 8<=v['position']<=30 and v['impressions']>=2]
print(f"\n=== あと一歩(8〜30位) {len(near)}件 ===")
for k,v in sorted(near,key=lambda x:x[1]['position'])[:20]:
    print(f"  表示{v['impressions']:>3} 順位{v['position']:>5.1f} クリック{v['clicks']}  {k}")
deep=[(k,v) for k,v in cur.items() if v['impressions']>=3 and v['position']>=30]
print(f"\n=== 需要あり×順位が深い(30位以下) {len(deep)}件 ===")
for k,v in sorted(deep,key=lambda x:-x[1]['impressions'])[:20]:
    print(f"  表示{v['impressions']:>3} 順位{v['position']:>5.1f}  {k}")
```

### 3. 既存記事と重複していないか必ず確認する

提案候補を思いついたら、**必ず** `media/posts/*.md` の `title:` を実際に読んで、検索意図が重複していないか確認する。推測で判断しない。

```bash
cd /Users/okamurakiichi/Downloads/Claude/260621_wordpress立ち上げ/nito-hp/media/posts && grep -h "^title:" *.md
```

重複していたら候補から外す。既存記事の強化で対応できる場合は、そのように書く。

### 4. 報告する

まず**現状**を3〜5行で簡潔に述べる。

- オーガニック検索セッション（江東区除く）の直近7日と前週比
- チャネルの内訳で目立つ動き（参考情報、Directは自社の可能性が高いため主要指標には含めない）
- 入口になっている記事があれば、その名前
- GSCで順位が上がった／表示が増えたクエリがあれば触れる

数字が動いていない場合は、無理に意味づけせず「動いていない」と正直に書く。

### 5. 候補を3本提案する

選定ルール（優先順）:

1. **需要実証ネタを優先**：GSCで既に表示されていて、順位が8〜30位のクエリ。すでに土俵に乗っている証拠なので確度が高い
2. 足りなければ**仮説ネタ**で補う（過去に効いた型＝プロンプト型の質問、業種特化）
3. **既存記事と検索意図が重複するものは除外**

狙わないもの（明確に除外する）:

- head単体（`llmo` / `llmoとは` / `llmo対策`）＝DR0では勝てない激戦区
- 競合ブランド名を含むクエリ（ブランドクラウド、バクリ等）
- 地域単体（llmo対策 東京 等）

提案は次の形式で、簡潔に出す。

| # | 記事案 | 根拠クエリ・現順位 | 既存記事との差別化 |
|---|---|---|---|

### 6. 提案したら停止する

**ここで終了。ユーザーの承認を待つ。執筆・ビルド・pushは行わない。**

## 記事を書くことになった場合の厳守ルール（承認後に参照）

- `media/WRITING_GUIDE.md` に従う
- ダッシュ（——）禁止、定型句（いかがでしたか・本記事では等）禁止
- 読点を含む見出しを避ける（列挙は「①〜」の形にする）
- 各セクションに、そのセクションの結論となるキーメッセージの太字を1つ置く
- 機械的な因果構文（「〜ためです」の連発）を避ける
- 水増し禁止。字数を増やす目的の見出し追加をしない
- ポジショニングは成果報酬×実行支援
- 実績の表記は比率中心・クライアント社名は非公開