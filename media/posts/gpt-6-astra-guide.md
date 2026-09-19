---
title: 【2026年9月】GPT-6 Astraとは？ChatGPTで使えるプラン・上限・料金・GPT-5.6との違い
date: 2026-09-17
category: AI検索対策
description: OpenAIが2026年9月3日に発表したGPT-6 Astraについて、公式の発表ページ・ヘルプ・モデルページを一次ソースに、ChatGPTのどのプランで使えるか、画面のどこに出るか、上限と料金、GPT-5.6 Solとの違いをまとめました。無料プランの実画面も載せています。
cover_tag: 解説
cover_headline: GPT-6 Astraとは
cover_sub: 使えるプラン・上限・料金を公式で確認
---

OpenAIは2026年9月3日（米国時間）に新しい最上位モデル「GPT-6 Astra」を発表し、翌4日から有料プランへ順次展開を始めました。発表ページの冒頭は「世界で最も知的で、最もアラインメントの取れたモデル」で、力を入れているのは回答の賢さよりも、**フォーム入力やCRMの更新のようにパソコンの画面を操作して作業を終わらせる力**です。

一方で、ChatGPTを開いても「GPT-6」という名前のモデルが見当たらない、という声が多く出ています。OpenAIの発表ページ・ヘルプセンター・モデルページ（いずれも2026年9月17日取得）を一次ソースにして、GPT-6 Astraが何を変えたのか、ChatGPTのどのプランでどこに出るのか、上限と料金、GPT-5.6 Solとどう使い分けるかを書きます。

:::takeaways
- ChatGPTの画面では**「GPT-6 Pro」という名前**で出る。思考レベルの「Pro」を選ぶと使える
- 通常チャットで使えるのは**Pro（月100ドル・200ドル）・Business・Enterprise**。Plusは Work と Codex でだけ使える
- 上限は Pro 200ドルで週200回、Pro 100ドルで週50回、Business Standard で**月15回**
- API は入力$10・出力$50（100万トークン）で、GPT-5.6 Sol の2.5倍
- 得意なのはPC操作・資料作成・長い作業。知識問題では第三者指標で首位ではない
:::

## GPT-6 Astraとは

GPT-6 AstraはGPT-5.6 Sol・Terra・Luna（2026年7月公開）の次にあたるOpenAIの旗艦モデルです。9月3日に一部の組織へ限定公開され、9月4日から ChatGPT Plus・Pro・Business・Enterprise と OpenAI API、Microsoft Azure、AWS Bedrock に広がりました。OpenAIのGreg Brockman社長は「世代の飛躍」と呼び、AGIの到来と見なされる可能性に言及しています（Axios、2026年9月3日）。

<figure class="post-figure"><img src="/media/images/gpt-6-astra-guide/astra_05_openai_announce.jpg" alt="OpenAIの発表ページ「GPT-6 Astra：新世代の応答性能」の冒頭" loading="lazy"><figcaption>OpenAIの発表ページ（2026年9月17日撮影）。ベンチマークの表もここに載っている</figcaption></figure>

### 名前が2つある

GPT-6 Astra には呼び名が2つあります。APIのモデルIDと ChatGPT Work・Codex での表示は「GPT-6 Astra」、**ChatGPTの通常チャットでの表示は「GPT-6 Pro」**です。OpenAIのヘルプは「GPT-6 Pro は GPT-6 Astra を基盤としている」と説明しています。

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

## 何が変わったか

発表ページは数学やコーディングより先に画面操作の話から始まります。

### PC操作が主役になった

OpenAIはAstraを「コンピュータ操作の速度・正確性・安全性における新しい到達点」と位置づけ、例としてオンラインフォームの入力、CRMの顧客レコード更新、カレンダーの整理を挙げています。デスクトップ操作の評価 OSWorld 2.0（オフライン版）は72.6%で、GPT-5.6 Sol の65.7%から上がり、**1タスクあたり約47%短い時間**で終えるとしています。画面上の要素を正しく指せるかを測る ScreenSpot-Pro は76.9%から92.7%です。

### 仕事の成果物を作る力

既存のテンプレートに沿ったスライド、構造の整った文書、Excelの分析、複数の資料を照合して数字の食い違いを見つける作業について、OpenAIは自社で最も優れたモデルだと書いています。事務作業の完遂率を測る AutomationBench は18.1%から41.4%に上がりました。残りの**6割は途中で止まるか間違える**ので、成果物の確認は人の仕事のままです。

### コーディングと長い作業

Terminal-Bench 4.0 は37.3%から57.9%、社内のデータベース移行タスクは42.7%から63.9%です。Codexにはコンテキストが埋まったときに要約で圧縮する代わりに**メモを持ち越して過去のやり取りを検索する方式**が入り、長い作業で詳細が落ちにくくなりました。

### 数学と長文脈

最難関の数学ベンチマーク FrontierMath Tier 4 は83.0%から97.6%、100万トークン付近の長文検索（MRCR v2 8-needle 512K〜1M）は73.8%から96.3%です。

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

**伸びているのは手順を最後まで遂行する系の項目**で、知識寄りの GPQA は1.4ポイントしか動いていません。Humanity's Last Exam では Claude Fable 5.1 に負けており、OpenAI自身がその行を表に載せています。第三者機関 Artificial Analysis の総合指数も61.2で、Claude Fable 5.1 の65.7を下回ります。ARC-AGI-3 の99.9%は、OpenAIの応答API向けの実行環境で測った値で、汎用の実行環境では62.7%だったとARC Prize側が公表しています。

## ChatGPTのどのプランで使えるか

Googleサジェストでも「gpt-6 astra 料金」「使い方」「いつ」が並び、検索で最も多い問いです。OpenAIヘルプ「GPT-5.6 and GPT-6 Pro in ChatGPT」（2026年9月17日時点）の記載を表にしました。

| プラン | 通常チャット（GPT-6 Pro） | Work・Codex（GPT-6 Astra） | 上限（チャット） |
|---|---|---|---|
| 無料・Go | 使えない | 使えない | - |
| Plus（月20ドル） | **使えない** | 使える | Work・Codex の枠内 |
| Pro 100ドル | 使える | 使える | 週50回（GPT-5.6 Sol Pro と共有） |
| Pro 200ドル | 使える | 使える | 週200回（Sol Pro は別枠で1日170回） |
| Business Standard | 使える | 使える | **月15回**（Sol Pro と共有） |
| Business Premium | 使える | 使える | 週50回（Sol Pro と共有） |
| Enterprise | 管理者の設定次第 | 管理者の設定次第 | 契約による |

<figure class="post-figure"><img src="/media/images/gpt-6-astra-guide/astra_06_help_limits.jpg" alt="OpenAIヘルプのGPT-6 ProとGPT-5.6 Sol Proの上限表" loading="lazy"><figcaption>OpenAIヘルプの上限表（2026年9月17日撮影）</figcaption></figure>

Plusの扱いは発表ページとヘルプで表現が違う点に注意が要ります。発表ページは「Plusを含む有料プランへ展開」と書き、ヘルプの記載は「Plusは Work と Codex で使える」です。**Plusで通常チャットのモデル一覧を探しても出てこないのは正常**で、Work か Codex を開くと使えます。Pro 200ドルで週200回を使い切ると、ChatGPTは自動で GPT-5.6 Thinking（Medium）に切り替わります。

Business Standard の月15回は、週ではなく月です。全社に配って日常的に回す枠ではなく、難しい案件に絞って使う設計になっています。枠を超えて使いたい場合は追加クレジットを買えますが、クレジットを買っても展開の順番は早まりません。

## 使い方（Chat・Work・Codex・API）

入口は4つあります。どれもモデルを選ぶだけで、追加の設定はありません。

<figure class="post-figure"><img src="/media/images/gpt-6-astra-guide/astra_00_fig_where.png" alt="GPT-6 Astraの4つの入口。Chat（GPT-6 Pro表示）、Work、Codex、API" loading="lazy"><figcaption>4つの入口と、使えるプランの対応</figcaption></figure>

### 通常チャットで使う

入力欄の右にある思考レベル（Instant・Medium・High・Extra High・Pro）で**「Pro」を選ぶ**と、対象プランでは GPT-6 Pro が使えます。GPT-5.6 Sol Pro を使いたいときはモデルメニューで GPT-5.6 Sol を選んでから Pro を選びます。「もっと考えて」と頼んでも思考レベルは自動では上がりません。

無料プランで同じ場所を押すと、次のように「Plus にアップグレード」の案内が出るだけで、Pro の選択肢はありません。

<figure class="post-figure"><img src="/media/images/gpt-6-astra-guide/astra_01_free_think.jpg" alt="無料プランのChatGPTで思考ボタンを押したときの画面。より賢い回答を得るという案内とPlusへのアップグレードボタン" loading="lazy"><figcaption>無料プランで「思考」を押した画面（2026年9月17日）。Proの選択肢は出ない</figcaption></figure>

### ChatGPT Work で使う

Work は、資料を読んで調べて、スライドや表などのファイルを作るところまでを1回の依頼で進めるモードです。画面上部の「Chat／Work」の切り替えで開き、モデル一覧から GPT-6 Astra を選びます。Plus でも使えますが、通常チャットとは別の利用枠です。無料プランでは Work のトライアル案内が出ます。

<figure class="post-figure"><img src="/media/images/gpt-6-astra-guide/astra_03_free_work_intro.jpg" alt="ChatGPTのWorkを無料プランで開いたときの紹介画面" loading="lazy"><figcaption>Work の紹介画面。ChatGPT は背景情報を集め、ドキュメント・スライド・スプレッドシートを作ると説明している</figcaption></figure>

依頼するときは、完成形のファイル形式と用途、参照してほしい資料を先に伝えます。

### Codex で使う

Codex のデスクトップ・CLI・IDE拡張でモデルに GPT-6 Astra を選びます。**CLI は 0.153.0 以上**が必要です。5時間あたりに送れるローカルメッセージの目安は、ChatGPT料金ページによると Plus で5〜45、Pro 100ドルで25〜225、Pro 200ドルで100〜900で、GPT-5.6 Sol の半分です。ローカルとクラウドのチャットは枠を共有し、別に週の上限もかかります。

### API で使う

モデルIDは `gpt-6-astra` で、Responses API を使います。reasoning.effort の none は使えず、temperature・top_p は指定できません。Microsoft Azure と Amazon Bedrock からも呼べ、対象顧客は Zero Data Retention を選べます。

## 表示されないときの確認

「対象プランのはずなのに出ない」ときに見る順番です。

| 確認すること | よくある原因 | 対処 |
|---|---|---|
| 契約とログイン先 | 無料・Go、または別アカウント | 契約中のアカウントとワークスペースで開く |
| 開いている画面 | Plus で通常チャットを探している | Work か Codex を開く |
| アプリの版 | 古いデスクトップアプリ・CLI | メニューの「アップデートを確認」を手動で押す。CLI は 0.153.0 以上 |
| 会社の管理者設定 | Enterprise は公開時の初期設定で無効 | 管理者にモデルの有効化を頼む |
| 段階展開 | 条件を満たしていても順番待ち | 従来モデルで作業して待つ。クレジット購入では早まらない |

ヘルプは「自動更新の通知で更新した直後でも、手動で更新を確認してほしい」と書いています。

## 料金

ChatGPT側とAPI側で考え方が違います。

### ChatGPT は月額据え置き

Astra の追加で ChatGPT の月額は変わっていません。日本の料金ページ（2026年9月17日）では、無料0円・Go 1,400円・Plus 3,000円・Pro 16,800円からで、**Pro の項目に「GPT-6 Astra による Pro 推論」**と書かれています。機能比較表では GPT-6 Astra の行が Plus は「上限あり」、Pro は「拡張」です。

<figure class="post-figure"><img src="/media/images/gpt-6-astra-guide/astra_04_pricing.jpg" alt="ChatGPTの日本の料金ページ。無料0円、Go 1,400円、Plus 3,000円、Pro 16,800円から" loading="lazy"><figcaption>ChatGPT の料金ページ（2026年9月17日）。Pro の項目に GPT-6 Astra が明記されている</figcaption></figure>

### API は従量課金

100万トークンあたりの単価です（OpenAIモデルページ、2026年9月17日）。

| 区分 | 入力 | キャッシュ読み取り | 出力 |
|---|---|---|---|
| Standard（入力272K以下） | $10 | $1 | $50 |
| Standard（入力272K超） | $20 | $2 | $75 |
| Fast mode | Standard の2倍 | 2倍 | 2倍 |

GPT-5.6 Sol の Standard は入力$4・出力$20なので、単純比較で2.5倍です。ただし OpenAI は Astra が同じ作業を少ないトークンで終えるとしており、単価だけで費用が2.5倍になるとは限りません。キャッシュ書き込みは入力単価の1.25倍、Fast mode は EU データレジデンシーでは使えません。急がない処理は Batch や Flex に回すと下がります。

## GPT-5.6 Sol との違いと使い分け

GPT-5.6 Sol は引き続き使えます。無料と Go の既定モデルは GPT-5.6 Luna、有料プランの Instant から Extra High までは GPT-5.6 Sol が動いています。

| | GPT-6 Astra | GPT-5.6 Sol |
|---|---|---|
| 向いている作業 | 画面操作、複数資料の照合、長い多段階の作業、3D・フロントエンドの見た目の判断 | 短い定型文、要約、日常の質問、コスト重視の処理 |
| API単価（入力／出力） | $10／$50 | $4／$20 |
| コンテキスト | 105万トークン | 従来どおり |
| 利用枠 | Codex で Sol の半分 | 広い |

短い要約や定型文で困っていないなら、すべてを Astra に切り替える理由はありません。**複数の資料を見比べる仕事や、何度も修正を頼んでいる仕事**から試すと、手直しの回数で差が見えます。

## 安全面で知っておくこと

Astra は OpenAI の Preparedness Framework でサイバーセキュリティ能力が初めて「Critical」に分類されたモデルです。未知の脆弱性を見つけて突く能力があるため、一般提供版は攻撃コードの作成のような依頼を拒否し、監視システムが作業を止めることがあります。ChatGPT や Codex で止まったときは操作の確認を求められ、API では処理が停止します。正当な業務でも止まる場合があると OpenAI 自身が書いています。

ブラウザやPCを操作させるときは利用者側の注意も欠かせません。ログイン中のサイトはそのまま操作できるので、**銀行や決済のタブは閉じてから作業させる**こと、閲覧先のページに埋め込まれた指示に従ってしまう可能性（間接的なプロンプトインジェクション）があること、送金やパスワード入力を伴う作業は画面から離れないことが、OpenAI の案内と解説動画の両方で挙げられています。

Astra は書かれた推論を人が監視しにくくなったと OpenAI が明記している点も見ておく必要があります。OpenAI は本番環境でも推論の監視を続けると書いていますが、利用者の側で確かめられるのは出力そのものだけです。

## AI検索での見え方は変わるのか

モデルが GPT-6 になると ChatGPT での自社の出方が変わるのか、という質問を AI検索対策の相談で受けます。

**ChatGPT で自社が引用されるかどうかを決めているのは、モデルの賢さより検索の側**です。ChatGPT は質問を受けると、まず Bing などの検索で候補ページを集め、その中から回答に使うページを選びます。この候補集めと選び方は GPT-5.6 でも Astra でも同じ仕組みで動いており、候補に入っていないページはどのモデルでも引用されません。Astra で変わるのは集めた情報の扱い方と、作業を最後まで進める力のほうです。

引用される側になるには検索で拾われる状態を作り、AIが本文を読める形で置くことが先になります。詳しくは[ChatGPTに自社が出てこない原因](/media/chatgpt-not-appearing/)と[LLMOとは何か](/media/what-is-llmo/)に書きました。

[blogparts:llmo-cta]

## よくある質問

検索で「GPT-6」と一緒に出る関連質問（Googleの「他の人はこちらも質問」、2026年9月17日）を中心に答えます。

### GPT-6 Astraは何ができますか？

パソコンの画面を操作する作業（フォーム入力・CRMの更新・ブラウザ操作）、資料やスライドの作成、複数の資料を照合して数字の食い違いを見つける作業、長いコーディング作業です。OpenAIの発表ではデスクトップ操作の評価がGPT-5.6 Solから7ポイント上がり、1タスクの所要時間が約47%短くなっています。

### GPT-6 Astraはいつから使えますか？

2026年9月3日に一部の組織へ、9月4日からChatGPTの有料プランとAPIに順次展開されました。段階展開なので、同じプランでも表示される時期に差があります。

### GPT-6 Astraは無料のChatGPTで使えますか？

使えません。無料とGoの既定モデルはGPT-5.6 Lunaです。Plusは Work と Codex で、Pro・Business・Enterprise は通常チャットでも使えます。

### GPT-6 AstraはPlusで使えますか？

通常チャットでは使えず、ChatGPT Work と Codex でだけ使えます。Plusのモデル一覧に GPT-6 が出てこないのは正常で、画面上部の「Work」に切り替えるとモデル一覧に GPT-6 Astra が出ます。

### GPT-6 ProとGPT-6 Astraは同じものですか？

同じモデルです。通常チャットでの表示名が GPT-6 Pro、Work・Codex・API での名前が GPT-6 Astra で、OpenAIのヘルプは「GPT-6 Pro は GPT-6 Astra を基盤としている」と説明しています。

### GPT-6 Astraの料金はいくらですか？

ChatGPTでは追加料金がなく、既存の月額（Plus 3,000円・Pro 16,800円から）の中でプランごとの利用枠まで使えます。APIは100万トークンあたり入力$10・出力$50で、GPT-5.6 Solの2.5倍です。

### GPT-6 AstraとGPT-5.6はどちらを使う？

短い要約や定型文で困っていないならGPT-5.6 Solのままで足ります。複数の資料を見比べる仕事や、何度も修正を頼んでいる仕事、画面操作を任せたい仕事はGPT-6 Astraが向いています。利用枠はAstraのほうが少ないので、難しい案件に絞って使うのが現実的です。

### GPT-6 Astraが表示されないのはなぜですか？

多い順に、無料・Goプランである、Plusで通常チャットを探している、デスクトップアプリやCodex CLI（0.153.0以上）が古い、会社の管理者がまだ有効化していない、段階展開の順番待ち、の5つです。本文の表に確認の順番をまとめました。

### GPT-6 Astraは日本語の精度が上がりましたか？

OpenAIは日本語に限った数値を公開していません。長文脈の検索精度や指示の解釈は全体として上がっていますが、日本語での効果は自社の作業で確かめる必要があります。

### GPT-6 Astraに音声や動画を入力できますか？

できません。モデルページで音声と動画は「Not supported」です。入力はテキストと画像、出力はテキストです。

## 出典

- OpenAI「GPT-6 Astra: A new generation of intelligence」（2026年9月3日）
- OpenAI ヘルプ「GPT-5.6 and GPT-6 Pro in ChatGPT」（2026年9月17日取得）
- OpenAI モデルページ「gpt-6-astra」、ChatGPT 料金ページ（2026年9月17日取得）
- Axios「OpenAI releases new model GPT-6 Astra, says it may represent AGI」（2026年9月3日）
- 画面は2026年9月17日に無料プランのアカウントと未ログインのブラウザで撮影
