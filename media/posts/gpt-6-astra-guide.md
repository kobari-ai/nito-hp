---
title: 【2026年10月】GPT-6 Astraとは？ChatGPTで使えるプラン・上限・料金・GPT-5.6との違い
date: 2026-09-17
category: AI検索対策
description: OpenAIのGPT-6 Astraを公式の発表とヘルプで確認。ChatGPTのどのプランのどの画面で使えるか、上限と料金、9月に加わったGPT-6.1 SolやPro 500との関係、GPT-5.6との使い分けを整理しました。
cover_tag: 解説
cover_headline: GPT-6 Astraとは
cover_sub: 使えるプラン・上限・料金を公式で確認
---

OpenAIは2026年9月3日（米国時間）に新しい最上位モデル「GPT-6 Astra」を発表し、翌4日から有料プランへ順次展開を始めました。発表ページの冒頭は「世界で最も知能が高く、人間の意図に沿ったモデル」で、力を入れているのは回答の賢さよりも、**フォーム入力やCRMの更新のようにパソコンの画面を操作して作業を終わらせる力**です。

発表から1か月で周りの状況はかなり動きました。9月22日に弟分のGPT-6 SolとGPT-6 Lunaが加わり、29日にはGPT-6.1 Solと月500ドルの新しいProプランが出ています。一方でヘルプからはProのチャットの回数が消え、Plusの扱いも「チャットでは使えない」のまま変わっていません。

OpenAIの[発表ページ](https://openai.com/ja-JP/index/gpt-6-astra/)・[ヘルプセンター](https://help.openai.com/ja-jp/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt)・[モデルページ](https://developers.openai.com/api/docs/models/gpt-6-astra)を2026年10月5日に取り直し、GPT-6 Astraが何を変えたのか、ChatGPTのどのプランでどこに出るのか、上限と料金、GPT-5.6やGPT-6.1 Solとどう使い分けるかを書きます。

:::takeaways
- ChatGPTの通常チャットでは**「GPT-6 Pro」という名前**で出る。思考レベルの「Pro」を選ぶと使える
- 通常チャットで使えるのは**Pro・Business・Enterprise**。Plusは Work と Codex でだけ使える
- チャットの回数が公開されているのは Business だけで、Standard は**月15回**、Premium は週50回
- API は入力$10・出力$50（100万トークン）。9月29日に出た GPT-6.1 Sol は同じ作業を**5分の1の単価**で受ける
- 得意なのはPC操作・資料作成・長い作業。知識問題では第三者指標で首位ではない
:::

## GPT-6 Astraとは

GPT-5.6 Sol・Terra・Luna（2026年7月公開）の次にあたるOpenAIの旗艦モデルです。9月3日に一部の組織へ限定公開され、9月4日から ChatGPT の Plus・Pro・Business・Enterprise と OpenAI API、Microsoft Azure、AWS Bedrock に広がりました。日本語の記事では「アストラ」と表記されています。

<figure class="post-figure post-figure--sp"><img src="/media/images/gpt-6-astra-guide/astra_05_announce_v2.jpg" alt="OpenAIの発表ページの冒頭。2026年9月22日更新としてGPT-6 SolとGPT-6 Lunaを追加しGPT-6ファミリーを拡充すると書かれている" loading="lazy"><figcaption>発表ページの冒頭（2026年10月5日撮影）。9月22日の更新の告知が足されている</figcaption></figure>

### 名前が2つある

GPT-6 Astra には呼び名が2つあります。APIのモデルIDと ChatGPT Work・Codex での表示は「GPT-6 Astra」、**ChatGPTの通常チャットでの表示は「GPT-6 Pro」**です。OpenAIのヘルプは「GPT-6 Astra を搭載した GPT-6 Pro」と書いており、中身は同じモデルです。

### 基本スペック

| 項目 | 内容 |
|---|---|
| 発表日 | 2026年9月3日（限定）、9月4日（一般） |
| コンテキストウィンドウ | 1,050,000トークン（入力と出力の合計） |
| 最大出力 | 128,000トークン |
| 知識の期限 | 2026年4月30日 |
| 推論の深さ（reasoning effort） | low・medium・high・xhigh・max の5段階 |
| 入力 | テキストと画像。音声・動画は非対応 |
| APIのモデルID | gpt-6-astra |

出典はOpenAIのモデルページです。105万トークンは魅力的に見えますが、後述するとおり**入力が272,000トークンを超えると単価が上がる**ので、資料を全部入れる設計はコストに直結します。

## 発表後に変わったこと

発表からの1か月で、公式の発表とヘルプには次の変化がありました。

| 日付 | 変わったこと | Astraへの影響 |
|---|---|---|
| 9月14日 | Plus・Pro の Instant から思考モデルへの自動切り替えを廃止（安全上の理由を除く） | 難しい依頼でも自分で「Pro」を選ばないと GPT-6 Pro は動かない |
| 9月22日 | GPT-6 Sol と GPT-6 Luna を Work・Codex・API に追加 | GPT-6 は3段構成に。チャットには来ていない |
| 9月29日 | GPT-6.1 Sol を Work・Codex・API に追加 | Astra に近い性能を5分の1の API 単価で |
| 9月29日 | 月500ドルの Pro 500 を新設、Pro 200 の新規受付を再開 | Astra を速く動かす Ultrafast は Pro の中では Pro 500 だけ |
| 9月29日 | Astra で動く常時稼働のエージェント「dot」を発表 | Pro と Business Premium から順次 |

出典は[ChatGPTのリリースノート](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)と各発表ページです。

### GPT-6ファミリーが3段になった

[GPT-6 Sol と Luna の発表](https://openai.com/ja-JP/index/introducing-gpt-6-sol-and-luna/)で、Astra は3段の一番上という位置づけに変わりました。Sol は日常の難しい仕事向け、Luna は大量の定型処理向けで、どちらも Astra と同じ手法で学習しています。さらに9月29日の[GPT-6.1 Sol の発表](https://openai.com/ja-JP/index/introducing-gpt-6-1-sol/)は、**エージェント型のコーディングや画面操作で Astra に迫る性能を、Astra の5分の1の単価で出す**と書いています。

この3つは今のところ ChatGPT Work と Codex と API の中だけのモデルです。**通常のチャットで動いているのは GPT-5.6 Sol のままで、チャットで GPT-6 世代を使えるのは「Pro」を選んだときの GPT-6 Pro だけ**という形は変わっていません。

### Proのチャット回数がヘルプから消えた

9月17日の時点のヘルプには「Pro 200ドルは週200回、Pro 100ドルは週50回」という表が載っていました。今のヘルプにはこの表がなく、「上位の Pro ほど Pro モデルの上限が高い」という書き方に変わっています。Pro 200 は9月29日から新規契約の利用枠が下がり、2026年9月22日から9月29日午前10時（太平洋時間）までの間にPro 200が有効だった人は、契約が続いていれば10月29日まで前の枠を使えます。

## ChatGPTのどのプランで使えるか

検索でも「chatgpt astra 使うには」「3000円プラン astra使える？」のように調べられています。ヘルプ「[ChatGPTのGPT-5.6とGPT-6 Pro](https://help.openai.com/ja-jp/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt)」と「[ChatGPT Business のモデルと上限](https://help.openai.com/en/articles/12003714)」の記載を表にしました。

| プラン | 通常チャット（GPT-6 Pro） | Work・Codex（GPT-6 Astra） | チャットの上限 |
|---|---|---|---|
| 無料・Go | 使えない | 使えない | - |
| Plus（3,000円） | **使えない** | 使える | - |
| Pro（16,800円から、$100・$200・$500） | 使える | 使える | ヘルプに回数の記載なし。上位ほど多い |
| Business Standard | 使える | 使える（枠の一部） | **月15回**（GPT-5.6 Sol Pro と共有） |
| Business Premium | 使える | 使える | 週50回（GPT-5.6 Sol Pro と共有） |
| Enterprise | 管理者の設定次第 | 管理者の設定次第 | 料金表による。クレジット払いは1回50クレジット |

<figure class="post-figure post-figure--sp"><img src="/media/images/gpt-6-astra-guide/astra_06_help_v2.jpg" alt="OpenAIヘルプのChatGPTのGPT-5.6とGPT-6 Proのページ冒頭。GPT-6 ProはPro 100ドル、Pro 200ドル、Business、Enterpriseで利用でき、PlusプランではChatGPT WorkとCodexでGPT-6 Astraを利用できると書かれている" loading="lazy"><figcaption>OpenAIヘルプの冒頭（2026年10月5日撮影）。Plusはチャットではなく Work と Codex で使える</figcaption></figure>

ヘルプの GPT-6 Pro の対象には Pro 100 と Pro 200 が名指しされ、9月29日に出た Pro 500 は料金ページの Pro の項目にまとめて載っています。

**Plusで通常チャットのモデル一覧を探しても出てこないのは正常**で、Work か Codex を開くと使えます。料金ページの比較表は Plus の GPT-6 Astra を「上限あり」としていますが、これは Work と Codex での利用を指すものです。Work のヘルプにも「Plus には Work と Codex の Astra が含まれ、チャットの GPT-6 Pro は含まれない」とはっきり書かれています。

<figure class="post-figure"><img src="/media/images/gpt-6-astra-guide/astra_07_plus_v2.jpg" alt="Plusの場合の図。チャットにはバツ印、ワークとCodexには丸印が付いている" loading="lazy"><figcaption>Plusで GPT-6 Astra を使える場所</figcaption></figure>

Pro 200ドルで GPT-6 Pro の週の上限に達すると、ChatGPTは自動で GPT-5.6 Thinking の Medium に切り替わります。Pro 100ドルと Business は GPT-6 Pro と GPT-5.6 Sol Pro が1つの枠を分け合うため、モデルを切り替えても回数は増えません。Business Standard の月15回は週ではなく月なので、全社の日常業務ではなく難しい案件に絞って使う量です。

## 使い方（Chat・Work・Codex・API）

入口は4つあり、どれもモデルを選ぶだけで追加の設定はありません。

<figure class="post-figure"><img src="/media/images/gpt-6-astra-guide/astra_00_where_v2.jpg" alt="GPT-6 Astraの4つの入口の図。チャット、ワーク、Codex、APIの4枚のカードがあり、チャットには表示名はGPT-6 Proという吹き出しが付いている" loading="lazy"><figcaption>4つの入口。チャットだけ名前が GPT-6 Pro になる</figcaption></figure>

### 通常チャットで使う

入力欄の右にある思考レベル（Instant・Medium・High・Extra High・Pro）で**「Pro」を選ぶ**と、対象プランでは GPT-6 Pro が使えます。GPT-5.6 Sol Pro を使いたいときはモデルメニューで GPT-5.6 Sol を選んでから Pro を選びます。9月14日に自動の切り替えが廃止されたので、「もっと考えて」と頼んでも思考レベルは上がりません（安全上の理由を除く）。

無料と Go では Think（GPT-5.6 Luna）は選べますが、Pro の選択肢はありません。


### ChatGPT Work で使う

Work は、資料を読んで調べて、スライドや表などのファイルを作るところまでを1回の依頼で進めるモードです。画面上部の「Chat／Work」の切り替えで開き、モデル一覧から GPT-6 Astra を選びます。Plus でも使えますが、通常チャットとは別の利用枠です。

<figure class="post-figure"><img src="/media/images/gpt-6-astra-guide/astra_03_free_work_intro.jpg" alt="ChatGPTのWorkを無料プランで開いたときの紹介画面" loading="lazy"><figcaption>Work の紹介画面（2026年9月17日撮影）。背景情報を集めてドキュメント・スライド・スプレッドシートを作ると説明している</figcaption></figure>

依頼するときは、完成形のファイル形式と用途、参照してほしい資料を先に伝えます。プランごとの Work の機能差は[ChatGPT Workが使えるプランと上限](/media/chatgpt-work-plans/)にまとめました。

### Codex で使う

Codex のデスクトップ・CLI・IDE拡張でモデルに GPT-6 Astra を選びます。**CLI は 0.153.0 以上**が必要です。ヘルプの目安では Plus と Business Standard が5時間で送れるローカルメッセージは Astra で5〜45、同じ表の GPT-6.1 Sol は15〜160です。Pro の3プランには今は5時間の上限がなく、プランに含まれる枠だけがかかります。

ヘルプは「Sol の High でうまくいっていた作業なら、Astra の Low か Medium から試す」よう勧めています。週の枠の確認やリセットの使い方は[Codexの制限とリセット](/media/codex-limits/)で詳しく書きました。

### API で使う

モデルIDは `gpt-6-astra` で、Responses API を使います。reasoning.effort の none は使えず、temperature・top_p は指定できません。Microsoft Azure と Amazon Bedrock からも呼べ、対象顧客は Zero Data Retention を選べます。

## 表示されないときの確認

「対象プランのはずなのに出ない」ときに見る順番です。

| 確認すること | よくある原因 | 対処 |
|---|---|---|
| 契約とログイン先 | 無料・Go、または別アカウント | 契約中のアカウントとワークスペースで開く |
| 開いている画面 | Plus で通常チャットを探している | Work か Codex を開く |
| アプリの版 | 古いデスクトップアプリ・CLI | メニューの「アップデートを確認」を手動で押し、アプリを完全に再起動。CLI は 0.153.0 以上 |
| 会社の管理者設定 | ワークスペースのモデルアクセス権限による | 管理者にモデルの有効化を頼む |
| 段階展開 | 条件を満たしていても順番待ち | 従来モデルで作業して待つ。クレジットを買っても使えるモデルは増えない |

ヘルプは更新を入れたあとにもう一度「アップデートを確認」を押し、続けて更新が出れば入れて再起動するよう書いています。

## 料金

ChatGPT側とAPI側で考え方が違います。

### ChatGPT は月額据え置き

Astra の追加で Plus と Pro の月額は変わっていません。日本の料金ページ（2026年10月5日）では、無料0円・Go 1,400円・Plus 3,000円・Pro 16,800円からで、**Pro の項目に「GPT-6 Astra による Pro 推論」と「3段階から選べる利用枠」**が並んでいます。「常時稼働のエージェント dot」も Pro の項目に加わりました。プラン全体の違いは[ChatGPTの料金プランを比較](/media/chatgpt-pricing/)にまとめています。

<figure class="post-figure post-figure--sp"><img src="/media/images/gpt-6-astra-guide/astra_04_pricing_pro_v2.jpg" alt="ChatGPTの日本の料金ページのProの項目。月額16,800円からで、3段階から選べる利用枠、GPT-6 AstraによるPro推論、常時稼働のエージェントDotなどが並んでいる" loading="lazy"><figcaption>料金ページの Pro の項目（2026年10月5日撮影）</figcaption></figure>

ドルでは Pro 100・Pro 200・Pro 500 の3つで、Ultrafast（Astra を速く動かす設定）が付くのは Pro の中では Pro 500 だけです。Ultrafast は通常（Standard）の8倍の速さで利用枠を減らすため、**同じ Pro でも速度を選ぶと使える量は大きく減ります**。

料金ページの比較表を見ると Plus の列で GPT-6 Astra・GPT-6.1 Sol・GPT-6 Sol・GPT-6 Luna がすべて「上限あり」です。Pro の列は「拡張」で、無料と Go の列はどれも横棒の表示です。

<figure class="post-figure post-figure--sp"><img src="/media/images/gpt-6-astra-guide/astra_08_pricing_models_v2.jpg" alt="ChatGPT料金ページの比較表のモデル欄でPlusを選んだ画面。GPT-6.1 Sol、GPT-6 Astra、GPT-6 Sol、GPT-6 Lunaが上限あり、GPT-5.6 Solなどが拡張と表示されている" loading="lazy"><figcaption>比較表のモデル欄（Plus を選んだ表示、2026年10月5日撮影）</figcaption></figure>

### API は従量課金

100万トークンあたりの単価です（OpenAIモデルページ）。

| 区分 | 入力 | キャッシュ読み取り | 出力 |
|---|---|---|---|
| Standard（入力272K以下） | $10 | $1 | $50 |
| Standard（入力272K超） | $20 | $2 | $75 |
| Batch・Flex | Standard の半額 | 半額 | 半額 |
| Fast mode | Standard の2倍 | 2倍 | 2倍 |

GPT-5.6 Sol の Standard は入力$4・出力$20なので、単純比較で2.5倍です。ただし OpenAI は Astra が同じ作業を少ないトークンで終えるとしており、単価だけで費用が2.5倍になるとは限りません。キャッシュ書き込みは入力単価の1.25倍で、急がない処理は Batch か Flex に回すと半額になります。

## GPT-5.6・GPT-6.1 Solとの違い

チャットの普段使いは今も GPT-5.6 です。無料と Go の既定モデルは GPT-5.6 Luna、有料プランの Instant から Extra High までは GPT-5.6 Sol が動いています。Work・Codex・API では GPT-6.1 Sol が新しい選択肢になりました。

| | GPT-6 Astra | GPT-6.1 Sol | GPT-5.6 Sol |
|---|---|---|---|
| 使える場所 | チャット（GPT-6 Pro）・Work・Codex・API | Work・Codex・API | チャット・Work・Codex・API |
| 向いている作業 | 画面操作、複数資料の照合、長い多段階の作業 | Astra に近い質で回数をこなしたい作業 | 短い定型文、要約、日常の質問 |
| API単価（入力／出力） | $10／$50 | $2／$10 | $4／$20 |
| Codex の5時間の目安（Plus） | 5〜45 | 15〜160 | - |

短い要約や定型文で困っていないなら、すべてを Astra に切り替える理由はありません。**複数の資料を見比べる仕事や、何度も修正を頼んでいる仕事**から試すと、手直しの回数で差が見えます。Work や Codex で Astra の枠がすぐ尽きる場合は、GPT-6.1 Sol に下ろすと同じ枠で3倍ほどの量を回せる計算です。

## ベンチマークの読み方

発表ページには他社モデルとの比較表が載っていますが、読み方に注意が要ります。GPT系の数値はOpenAIの研究環境かAPIで測ったもので、他社の値には外部の公開結果も混ざっています。主な行を抜き出しました（すべてOpenAIの発表ページ掲載値）。

| ベンチマーク | GPT-6 Astra | GPT-5.6 Sol | Claude Fable 5.1 | Claude Opus 5 |
|---|---|---|---|---|
| Agents' Last Exam（エージェント総合） | 59.3% | 53.6% | - | 55.5% |
| OSWorld 2.0 offline（デスクトップ操作） | 72.6% | 65.7% | - | 70.2% |
| AutomationBench（事務作業） | 41.4% | 18.1% | 31.4% | 26.9% |
| Terminal-Bench 4.0 | 57.9% | 37.3% | 55.8% | 52.6% |
| FrontierMath Tier 4 | 97.6% | 83.0% | 87.8% | 73.2% |
| GPQA Diamond（科学） | 96.0% | 94.6% | 93.7% | 93.7% |
| Humanity's Last Exam（ツールあり） | 57.2% | - | 65.0% | 63.6% |
| ARC-AGI-3（抽象推論） | 99.9% | 7.8% | - | 30.2% |
| Artificial Analysis 指数 v4.1.1（第三者） | 61.2 | 60.9 | 65.7 | 63.1 |

**伸びているのは手順を最後まで遂行する系の項目**で、知識寄りの GPQA は1.4ポイントしか動いていません。Humanity's Last Exam では Claude Fable 5.1 に負けており、OpenAI自身がその行を表に載せています。第三者機関 Artificial Analysis の総合指数も61.2で、Claude Fable 5.1 の65.7を下回ります。ARC-AGI-3 の99.9%は、OpenAIの応答API向けの実行環境で測った値で、汎用の実行環境では62.7%だったとARC Prize側が公表しました。

### PC操作と仕事の成果物

OpenAIはAstraを、コンピュータ操作の速度と正確性で新しい到達点と位置づけ、例としてオンラインフォームの入力、CRMの顧客レコード更新、カレンダーの整理を挙げています。発表によると OSWorld 2.0 では GPT-5.6 Sol より**1タスクあたり約47%短い時間**で、より高い点を出しました。

既存のテンプレートに沿ったスライド、構造の整った文書、Excelの分析、複数の資料を照合して数字の食い違いを見つける作業も、OpenAIは自社で最も優れたモデルだと書いています。ただし事務作業の完遂率 AutomationBench は41.4%で、残りの**6割は途中で止まるか間違える**ので、成果物の確認は人の仕事のままです。

### コーディングと長い作業

社内のデータベース移行タスクは42.7%から63.9%に上がりました。Codexにはコンテキストが埋まったときに要約で圧縮する代わりに、**メモを持ち越して過去のやり取りを検索する方式**が入り、長い作業で詳細が落ちにくくなっています。100万トークン付近の長文検索（MRCR v2 8-needle 512K〜1M）も73.8%から96.3%です。

## 安全面で知っておくこと

Astra は OpenAI の Preparedness Framework でサイバーセキュリティ能力が初めて「Critical」に分類されたモデルです。未知の脆弱性を見つけて突く能力があるため、一般提供版は攻撃コードの作成のような依頼を拒否し、監視システムが作業を止めることがあります。ChatGPT や Codex で止まったときは操作の確認を求められ、API では処理が停止します。正当な業務でも止まる場合があると OpenAI 自身が書いています。

ブラウザやPCを操作させるときは利用者側の注意も欠かせません。ログイン中のサイトはそのまま操作できるので、**銀行や決済のタブは閉じてから作業させる**こと、閲覧先のページに埋め込まれた指示に従ってしまう可能性（間接的なプロンプトインジェクション）があること、送金やパスワード入力を伴う作業は画面から離れないことが、OpenAI の案内と解説動画の両方で挙げられています。

Astra は書かれた推論を人が監視しにくくなったと OpenAI が明記している点も見ておく必要があります。OpenAI は本番環境でも推論の監視を続けると書いていますが、利用者の側で確かめられるのは出力そのものだけです。

## AI検索での見え方は変わるのか

モデルが GPT-6 になると ChatGPT での自社の出方が変わるのか、という質問を AI検索対策の相談で受けます。

**ChatGPT で自社が引用されるかどうかを決めているのは、モデルの賢さより検索の側**です。ChatGPT は質問を受けると、まず Bing などの検索で候補ページを集め、その中から回答に使うページを選びます。この候補集めと選び方は GPT-5.6 でも Astra でも同じ仕組みで動いており、候補に入っていないページはどのモデルでも引用されません。しかも通常のチャットの多くは今も GPT-5.6 Sol と Luna が答えています。

引用される側になるには検索で拾われる状態を作り、AIが本文を読める形で置くことが先になります。詳しくは[ChatGPTに自社が出てこない原因](/media/chatgpt-not-appearing/)と[LLMOとは何か](/media/what-is-llmo/)に書きました。

[blogparts:llmo-cta]

## よくある質問

プランと上限の答えはいずれも2026年10月5日に取得した OpenAI のヘルプと料金ページの記載です。

### GPT-6 Astraは何ができますか？

パソコンの画面を操作する作業（フォーム入力・CRMの更新・ブラウザ操作）、資料やスライドの作成、複数の資料を照合して数字の食い違いを見つける作業、長いコーディング作業です。OpenAIの発表ではデスクトップ操作の評価がGPT-5.6 Solから7ポイント上がり、1タスクの所要時間が約47%短くなっています。

### GPT-6 Astraを使うには？

入力欄の思考レベルで「Pro」を選ぶと、対象プランの通常チャットでGPT-6 Astra（表示名はGPT-6 Pro）が使えます。ChatGPT WorkとCodexはモデル一覧からGPT-6 Astraを直接選ぶだけです。APIはモデルID `gpt-6-astra` でResponses APIから呼び出します。

### GPT-6 Astraはいつから使えますか？

2026年9月3日に一部の組織へ、9月4日からChatGPTの有料プランとAPIに順次展開されました。段階展開なので、同じプランでも表示される時期に差があります。

### GPT-6 Astraは無料版やGoで使えますか？

使えません。無料とGoの既定モデルはGPT-5.6 Lunaです。料金ページの比較表でも、無料とGoの列は GPT-6 の4モデルがすべて横棒になっています。

### GPT-6 Astraは3,000円のPlusで使えますか？

ChatGPT Work と Codex でだけ使えます。通常チャットのモデル一覧に GPT-6 Pro が出てこないのは正常で、画面上部の「Work」に切り替えるとモデル一覧に GPT-6 Astra が出ます。

### GPT-6 ProとGPT-6 Astraは同じものですか？

中身は同じモデルです。通常チャットでの表示名が GPT-6 Pro、Work・Codex・API での名前が GPT-6 Astra です。ただし利用枠は別で、Work で Astra を使えてもチャットの GPT-6 Pro が使えるとは限りません。

### GPT-6 Astraの料金はいくらですか？

ChatGPTでは追加料金がなく、既存の月額（Plus 3,000円・Pro 16,800円から）の中でプランごとの利用枠まで使えます。APIは100万トークンあたり入力$10・出力$50で、GPT-5.6 Solの2.5倍、GPT-6.1 Solの5倍です。

### AstraとGPT-6.1 Solはどちらを使う？

画面操作や複数資料の照合のように一度で仕上げたい仕事は Astra、回数をこなしたい仕事は GPT-6.1 Sol が向いています。Plus の Codex では5時間で送れる目安が Astra の5〜45に対し GPT-6.1 Sol は15〜160なので、枠が尽きやすい人は Sol を基本にすると長く使えます。GPT-6.1 Sol が出ていなければ、まだ順番待ちです。

### GPT-6 Astraが表示されないのはなぜですか？

多い順に、無料・Goプランである、Plusで通常チャットを探している、デスクトップアプリやCodex CLI（0.153.0以上）が古い、会社の管理者がまだ有効化していない、段階展開の順番待ち、の5つです。本文の表に確認の順番をまとめました。

### GPT-6 Astraは日本語の精度が上がりましたか？

OpenAIは日本語に限った数値を公開していません。長文脈の検索精度や指示の解釈は全体として上がっていますが、日本語での効果は自社の作業で確かめる必要があります。

### GPT-6 Astraに音声や動画を入力できますか？

API ではできません。モデルページで音声と動画は「Not supported」で、入力はテキストと画像、出力はテキストです。ChatGPT の音声会話では9月9日から、検索や難しい質問のときに GPT-6 Astra を使えるようになりました。使えるモデルはプランによります。

## 出典

- OpenAI「[GPT-6 Astra：新世代の応答性能](https://openai.com/ja-JP/index/gpt-6-astra/)」（2026年9月3日、9月22日更新）
- OpenAI「[GPT-6 Sol と Luna のご紹介](https://openai.com/ja-JP/index/introducing-gpt-6-sol-and-luna/)」（2026年9月22日）、「[GPT-6.1 Sol のご紹介](https://openai.com/ja-JP/index/introducing-gpt-6-1-sol/)」（2026年9月29日）
- OpenAI ヘルプ「[ChatGPTのGPT-5.6とGPT-6 Pro](https://help.openai.com/ja-jp/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt)」「[WorkとCodexでのGPT-6 Astraの利用量管理](https://help.openai.com/ja-jp/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)」「[ChatGPT Business models and limits](https://help.openai.com/en/articles/12003714)」「[About ChatGPT Pro tiers](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)」「[ChatGPT Rate Card](https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu-credit-based-pricing)」「[ChatGPT Release Notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)」
- OpenAI [モデルページ gpt-6-astra](https://developers.openai.com/api/docs/models/gpt-6-astra)、[ChatGPT 料金ページ](https://chatgpt.com/ja-JP/pricing)
- 公式ページはすべて2026年10月5日に取得。無料プランの画面は2026年9月17日に撮影
