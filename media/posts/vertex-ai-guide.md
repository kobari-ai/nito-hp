---
title: 【2026年11月】Vertex AIとは？新名称・料金とGemini APIとの違い
date: 2026-11-09
category: AI活用
description: Vertex AIとは何かを公式ページで解説。2026年4月のGemini Enterprise Agent Platformへの改名とできること、料金と月額の試算、Gemini アプリ・Gemini APIとの違い、始め方まで。
keyword: vertex ai
cover_tag: 導入担当向け
cover_headline: Vertex AIとは
cover_sub: 新しい名前と料金・Gemini APIとの違い
cta: ai_agent
---

Vertex AIは、Google Cloudの上でAIのモデルを選んで自社のアプリやエージェントに組み込み、本番で動かすための開発基盤です。2026年4月22日（米国時間）にGemini Enterprise Agent Platformへ切り替わり、製品ページは日本語・英語とも「Gemini プラットフォーム（Gemini platform）」の名前になりました。

社内の資料やAPIの名前にはVertex AIが残り、検索で見つかる説明と今の画面の名前が合わないことがあります。この記事では今の名前とできること、料金、Gemini アプリ・Gemini APIとの違い、始め方までを公式のページで確かめました。

:::takeaways
- Vertex AIは2026年4月22日（米国時間）から**Gemini Enterprise Agent Platform**。機能は引き継がれ、新しい機能はAgent Platformでだけ出る
- 料金はモデルのトークン単価が中心。**東京などのリージョンを指定すると約1.1倍**で、Gemini 3.8 Flashの今の単価は12月31日までのクレジット還元つき
- Gemini APIの公式ドキュメントは、**企業向けの管理が要らなければGemini APIを勧めている**。データの扱い・処理する地域・社内の権限を説明する必要があるときにAgent Platformを選ぶ
:::

## Vertex AIとは

### 何をする基盤か

Agent Platformは、Google Cloudの上でAIのモデルを選び、自社のアプリやエージェントに組み込んで、本番で動かし続けるための開発基盤です。社員が画面で質問するチャットの製品ではなく、開発者やデータの担当が使う土台にあたります。概要ページは機能を「ビルド」「スケーリング」「管理」「最適化」の4つの柱に分けていて、作る段階から本番での監視までが1か所にそろいます。

### 2026年4月に名前が変わった

Google Cloudは2026年4月22日（米国時間）、Gemini Enterprise Agent Platformを「Vertex AIの進化形」として公開しました。Vertex AIのサービスとロードマップは今後すべてAgent Platformを通して届け、単独のサービスとしては出しません。以前のVertex AIのURLも製品ページへ転送されます。**Vertex AIで使えていたモデルやエージェントの部品は、Agent Platformの中にそのまま続いています。** 

<figure class="post-figure"><img src="/media/images/vertex-ai-guide/vtx_product.png" alt="Google Cloudの日本語の製品ページ。以前Vertex AIと呼ばれていた製品の見出しがGemini プラットフォームになっている" loading="lazy"><figcaption>Google Cloudの製品ページ（2026年11月9日）</figcaption></figure>

名前が変わっていない所もあります。Google Apps Scriptから呼ぶ機能は今も「Vertex AI サービス」で、APIのアドレスはaiplatform.googleapis.comのままです。社内文書を検索させる部品は2026年4月からAgent Searchと呼ばれます。**社内の資料にVertex AIとAgent Platformが混ざっていても、同じ基盤を指していると読んでかまいません。** ドキュメントとリリースノートでは「Gemini Enterprise Agent Platform」の名前が使われています。この記事では今の名前のAgent Platformを使い、旧名は必要な所だけ添えます。

### これまでの経緯

Vertex AIは2021年5月18日に、それまで別々だったAutoMLとAI Platformをまとめた機械学習の基盤として一般提供が始まりました。2023年6月に生成AIの機能が一般提供になり、2024年4月にはエージェントを作るVertex AI Agent Builderが加わっています。**予測や分類のモデルを作る基盤から、生成AIとエージェントの基盤へと中心が移ってきた流れの先に、今回の改名があります。**

## Vertex AIでできること

今の公式の名前と2026年4月までの名前を、よく使われる機能ごとに並べると次のとおりです。

| やりたいこと | 今の名前 | 2026年4月までの名前 |
|---|---|---|
| モデルを選ぶ | Model Garden | 同じ |
| 画面でプロンプトを試す | Agent Studio | Vertex AI Studio |
| コードでエージェントを組む | Agent Development Kit（ADK） | 同じ |
| エージェントを動かす | Agent Runtime・メモリーバンク | Agent Engine |
| 社内文書を検索させる | Agent Search・RAG Engine・ベクトル検索 | Vertex AI Search |
| 予測や分類のモデルを作る | カスタム トレーニング・AutoML | 同じ |
| 開発の作業場 | Colab Enterprise・Workbench | Vertex AI Workbench |
| 運用 | Pipelines・Model Registry・Feature Store | Vertex AI Pipelines など |
| 守る・見張る | Agent Identity・Agent Gateway・評価 | （改名と同時に追加） |

<figure class="post-figure"><img src="/media/images/vertex-ai-guide/vtx_overview.png" alt="Agent Platform（旧Vertex AI）の4つの柱。ビルドはModel GardenとAgent StudioとADK、スケーリングはAgent Runtimeとメモリーバンク、管理はAgent IdentityとAgent Gateway、最適化は評価とシミュレーションと監視" loading="lazy"></figure>

### モデルを選んで試す

Model Gardenには、Gemini 4 ArgonなどのGoogleのモデル、AnthropicのClaude、オープンモデルのGemmaが並び、モデルとツールは200以上です。Agent Studioでは文章・コード・画像・動画を使ってプロンプトを作り、試し、保存できます。モデルを比べる部品はモデル評価サービスです。**最初の検証はコードを書かずにAgent Studioで済ませ、使うモデルを決めてから開発に移るのが向いています。**

### エージェントを作って動かす

ADKは特定のモデルに縛られないエージェントの開発の枠組みで、Agent Studioで作った処理をADKに書き出してコードで続けることもできます。Agent Runtimeはエージェントを本番で動かす場所で、1秒未満の起動と、何日も動き続けるエージェントに対応します。会話をまたいで利用者のことを覚えるメモリーバンクも同じ基盤の部品です。**作ったエージェントを社員の画面に並べるなら、管理者がGemini Enterpriseに登録します。** 社員向けのアプリの側は「[Gemini Enterpriseとは](/media/gemini-enterprise/)」に、作り方の選び方は「[AIエージェントの作り方](/media/ai-agent-build/)」にまとめています。

改名と同時に、管理の部品も増えました。Agent Identityはエージェントごとに一意のIDを付けて操作を監査できるようにし、Agent Gatewayはエージェントとツールのやり取りをまとめて通し、Model Armorでプロンプトインジェクションやデータの漏えいを防ぎます。

### 社内データを検索させる

社内の規程やマニュアルを根拠に答えさせるなら、Agent SearchかRAG Engineが候補です。標準的な文書検索は1,000クエリあたり約4ドルで、ほかにインデックスの保存料がかかります。部品の選び方と手順は「[RAG構築とは](/media/rag-build/)」で、Azure・AWSと並べて書きました。

### 予測や分類のモデルを作る

生成AI以前からある機械学習の機能は改名の後もそのまま使えます。AutoMLは選定を自動にした学習、カスタム トレーニングは学習のコードを自分で決められる学習です。作ったモデルはModel Registryで版を管理し、Pipelinesで手順を自動にし、モニタリングで入力の偏りやずれを見張ります。**学習にも計算の料金がかかるため、試すときは小さなデータから始めるのが安全です。**

## Vertex AIの料金

### 料金の決まり方

費用は使うモデルとインフラの量で決まります。モデルはトークンの量に応じて払い、標準の従量課金のほかに、遅れてもよい処理向けの割安なFlex、優先して処理するPriority、決まった処理量を契約で確保するプロビジョンド スループットがあります。エージェントをAgent Runtimeで動かすと、CPU・メモリ・ストレージの3つの量も料金の対象です。**生成AIの費用はまずモデルのトークン単価で決まり、エージェントを動かす分がその上に乗る**と考えると見積もりやすくなります。

もう1つの分かれ目が処理する場所です。料金表は「グローバル」と「非グローバル」に分かれていて、東京などのリージョンを指定すると、一般提供のGemini 3以降のモデルは2026年7月1日から約1.1倍の単価になりました。

### 主なモデルの単価

標準の従量課金の単価です。単位は100万トークンあたりのドルで、左がグローバル、右がリージョン指定の値です。

| モデル | 期間 | 入力 | 出力 |
|---|---|---|---|
| Gemini 4 Argon | 11月30日まで | 2.00／2.20 | 10.00／11.00 |
| Gemini 4 Argon | 12月1日から | 4.00／4.40 | 20.00／22.00 |
| Gemini 3.8 Flash | 12月31日まで | 0.75／0.825 | 3.75／4.125 |
| Gemini 3.8 Flash | 2027年1月1日から | 1.50／1.65 | 7.50／8.25 |
| Gemini 3.5 Flash-Lite | 期限なし | 0.30／0.33 | 2.50／2.75 |
| Gemini 3.1 Pro プレビュー | 期限なし | 2.00／なし | 12.00／なし |

期限つきの安い単価は対象期間の費用の50%をクレジットで戻す形で提供されます。プロモーションはGemini 3.8 Flashなどが2026年8月13日から12月31日まで、Gemini 4 Argonが10月13日から11月30日までです。**12月と1月に単価が2倍に戻るモデルがあるため、年間の予算は戻った後の単価で組むほうが安全です。**

ほかにも細かい決まりがあります。長いコンテキストの単価があるモデル（表ではGemini 3.1 Pro プレビュー）は、入力が20万トークンを超えると、そのリクエストの全トークンがその単価になります。バッチはGemini 4 Argonで入力1.00ドル・出力5.00ドルと標準の半額で、優先度の高い処理は1.8倍です。400番台と500番台のエラーで失敗したリクエストは課金されません。ただしGemini 4は11月13日から、出力が3万2,000トークンを超えたリクエストは、タイムアウトで失敗しても取り出せた分のトークンが課金されます。

### 検索とランタイムの料金

Google検索で回答の根拠を取るグラウンディングは、Gemini 3と4を合わせて月5,000件まで無料で、超えると1,000件あたり14ドルです。Googleマップのグラウンディングも同じ条件で、自社のデータを根拠にする場合は1,000件あたり2.50ドルです。Agent Runtimeには請求先アカウントごとに月の無料枠があり、CPUは最初の50時間、メモリは最初の100時間、ストレージは最初の1GiBまでかかりません。

### 無料クレジットで試せる範囲

新しくGoogle Cloudを使う場合は、90日間有効な300ドルのウェルカム クレジットがあり、自動で請求に切り替わることはありません。ただし対象外があります。**300ドルのクレジットはAI StudioのGemini APIの費用にも、マネージドAPIとして出ているパートナーのモデルにも使えません。** Model GardenのClaudeを試すには、有料の請求先アカウントへ切り替える必要があり、300ドルのクレジットはClaudeの費用には充てられません。

無料トライアルの請求先アカウントでは、GPUの追加やMarketplaceの利用もできません。90日の間に有料へ切り替えないか、クレジットを使い切ると、プロジェクトとリソースが止まります。検証を止めたくなければ、期限の前に切り替えるかを決めておきます。

### 月額の試算

社内の問い合わせに答えるアプリで、1日1,000回、1回あたり入力3,000トークン・出力500トークン、月22日動かす場合を、Gemini 3.8 Flashの標準の単価で計算しました。入力は月6,600万トークン、出力は1,100万トークンです。

| 条件 | 12月31日まで | 2027年1月から |
|---|---|---|
| グローバル | 90.75ドル | 181.50ドル |
| 東京などのリージョン指定 | 99.83ドル | 199.65ドル |

モデルの費用だけを見ると、この規模なら月200ドル前後です。キャッシュを使えば入力の単価は10分の1になり、毎回同じ規程集を前に付ける使い方ほど下がる計算です。一方でGoogle検索のグラウンディングを毎回使うと、月2万2,000回のうち無料の5,000件を超えた1万7,000件で約238ドルが加わります。1回の質問で検索が何回か走れば、その分だけ増える計算です。**検索を毎回使うと、モデルの費用と同じくらいの額が上乗せされます。**

## Gemini アプリ・Gemini APIとの違い

GoogleのGeminiを会社で使う入口は大きく3つあり、同じGeminiのモデルでも契約・認証・データの扱いが違います。社員が使うチャットのGemini アプリ、開発者がAI Studioで使うGemini API、Google Cloudの上のAgent Platformです。

| 項目 | Gemini アプリ（Workspace） | Gemini API（AI Studio） | Agent Platform |
|---|---|---|---|
| 使う人 | 社員がチャットで | 開発者が自社のアプリで | 開発者とデータの担当が業務システムで |
| 始め方 | Workspaceの契約と管理者の設定 | AI StudioでAPIキーを作る | Google Cloudのプロジェクトで有効にする |
| 認証 | 社員のGoogleアカウント | APIキー | サービスアカウントなどのIAM |
| 学習への利用 | 対象のエディションは人がレビューせず許可なくドメイン外の学習に使わない | 無料枠は改善に使われ人が読むこともある・有料枠は使わない | 事前の許可なく学習やファインチューニングに使わない |
| 払い方 | Workspaceの契約 | 前払いのクレジットが既定 | Google Cloudの通常の請求 |
| 管理 | Workspaceの管理コンソール | AI Studioとプロジェクト | IAM・組織のポリシー・監査ログ |

Agent Platformも試すだけならAPIキーで呼べますが、移行ではサービスアカウントでの認証が前提です。

### 公式が勧める選び方

Gemini APIの公式ドキュメントが示す2つのAPIの選び方は次のように示されています。

> Most developers should use the Gemini Developer API unless there is a need for specific enterprise controls.

特定の企業向けの管理が必要でない限り、ほとんどの開発者はGemini Developer APIを使うべき、という意味です。**データの保持や処理する地域を契約と設定で説明する必要がある会社、BigQueryの社内データとつなぐ会社にはAgent Platformが向いています。**

<figure class="post-figure"><img src="/media/images/vertex-ai-guide/vtx_choose.png" alt="Googleの3つの入口の選び方。社員がチャットで使うならWorkspaceのGeminiアプリ、自社のアプリに早く組み込むならGemini API、企業の管理と地域が要るならAgent Platform" loading="lazy"></figure>

WorkspaceのGeminiの料金と設定は「[Google WorkspaceのGeminiとは](/media/google-workspace-gemini/)」、Gemini APIの無料枠と単価は「[Gemini APIの料金](/media/gemini-api-pricing/)」で詳しく書いています。

### 移るときに変わること

Gemini APIからAgent Platformに移る場合も、コードの書き換えは小さく済みます。どちらもGoogle GenAI SDKとInteractions APIで呼べるためで、変わるのは認証と設定の部分です。移行の注意は次のとおりです。

- 認証はGoogle Cloudのサービスアカウントに変わる
- APIキーを作ったのと同じプロジェクトを使ってよい
- 対応するリージョンが2つのAPIで違い、プレビュー中のInteractions APIはグローバルだけ
- AI Studioで作ったモデルはAgent Platformで作り直す
- 使わなくなったAPIキーは削除する

## 会社で使うときに決めること

### データを残さない設定

Agent Platformは、事前の許可や指示なしに顧客のデータを学習やファインチューニングに使いません。**ただし学習に使われないことと、データが一定期間残ることは別の話です。** 保持をゼロにするには次の点を1つずつ確かめる必要があります。

- 不正利用を見つけるためのプロンプトの記録：利用規約にもとづいて記録されることがある
- Google検索のグラウンディング：最大3日のログが残り止められない。保持ゼロが要るならWeb Grounding for Enterprise
- Googleマップのグラウンディング：30日保存され止められない
- リクエストとレスポンスの記録：既定でオフ。有効にするとBigQueryに書き込まれる
- Interactions API：storeの既定がtrueで会話が保存される。falseを明示する
- 暗黙のキャッシュ：既定で有効、24時間以内に削除。プロジェクトごとに無効にできる

キャッシュを止める操作には、Agent Platformの管理者のロールが要ります。永続キャッシュは顧客管理の暗号鍵（CMEK）に対応していない点も、暗号鍵を自社で持つ方針の会社は押さえておく必要があります。

### 処理する地域

データ所在地やリージョン内の ML 処理は、エンドポイントでは保証されません。グローバルのエンドポイントは、どのリージョンで処理されるかを選べません。**社内規程で国内での処理を求めているなら、東京（asia-northeast1）を指定したうえで、データ所在地のページまで確かめる必要があります。** グローバルではチューニング、AnthropicのモデルのバッチやRAGのコーパスが使えないという制限もあります。

### 権限と費用の管理

Agent Platformの権限はGoogle CloudのIAMで分け、閲覧だけの担当、使う担当、設定を変える管理者のロールが用意されています。費用は公式の料金計算ツールで試算でき、規模が大きい場合はGoogleの営業から見積もりを取る流れです。

**検証用と本番用のプロジェクトを分けておくと、権限と費用の両方を分けて見られるので便利です。**

## Vertex AIの始め方

Google Cloudのアカウントがあれば、検証は1日で始められます。Apps Scriptから呼ぶときの前提も、課金を有効にしたプロジェクトとAPIの有効化の2つです。

1. Google Cloudにログインし、請求先アカウントを作る（新規なら無料トライアルを選べる）
2. 検証用のプロジェクトを作るか選ぶ
3. プロジェクトを開き、Google Cloudのコンソールで[Agent Platform API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com)（旧Vertex AI API）を有効にする
4. Agent Studioでプロンプトを試し、使うモデルを決める
5. Google GenAI SDK（Python・JavaScript・Java・Goなど）で自社のアプリから呼ぶ

<figure class="post-figure"><img src="/media/images/vertex-ai-guide/vtx_start.png" alt="Agent Platformを試すまでの4つの手順。請求先アカウントを作る、プロジェクトを選ぶ、APIを有効にする、Agent Studioで試す" loading="lazy"></figure>

スプレッドシートなどからGeminiを呼びたい場合は、Apps Scriptの高度なサービスが入口です。

## Vertex AIの活用事例

Agent Platformを使う企業の例です。ぐるなびは飲食店を探すアプリ「UMAME!」でメモリーバンクを使い、利用者の過去の行動や好みを覚えて候補を出しています。CTOの見込みは満足度の30%以上の向上です。経費精算のPayhawkは、利用者の習慣を覚えたエージェントで経費の提出時間を50%以上短くしました。

通信のComcastはADKとAgent Runtimeで顧客向けのアシスタントを作り直しました。**これらは各社が公式ブログに寄せた説明で、第三者が検証した数字ではありません。**

## まとめ

- 社員にチャットで使わせたいだけなら、WorkspaceのGeminiかGemini Enterpriseが向いています
- 自社のアプリに早く組み込み、企業向けの管理が要らないなら、Gemini APIから始めるのがおすすめです
- データの保持・処理する地域・社内の権限を説明する必要があるなら、Agent Platformで検証用のプロジェクトを作るのがおすすめです
- 予算は、12月と2027年1月に戻る単価と、検索のグラウンディングの件数で組みます

## よくある質問

### Vertex AIはなくなったのですか？

なくなってはいません。2026年4月22日（米国時間）にGemini Enterprise Agent Platformへ名前が変わり、機能は引き継がれています。

### Vertex AIは無料で試せますか？

新規なら90日間有効な300ドルのクレジットで試せます。AI StudioのGemini APIと、Claudeなどパートナーのモデルには使えません。Agent Platformで呼ぶGeminiには使えます。

### Vertex AIとGeminiは何が違いますか？

Geminiはモデルとアプリの名前で、Vertex AI（今のAgent Platform）はそのモデルを自社のシステムに組み込む基盤です。

### Vertex AIでClaudeは使えますか？

使えます。Model GardenにClaudeが並びますが、有料の請求先アカウントが必要です。

### Vertex AIに入力したデータは学習に使われますか？

事前の許可がなければ学習には使われません。ただしログが一定期間残る機能があります。

### Vertex AI Searchは今どこにありますか？

2026年4月からAgent Searchと呼ばれ、Agent Platformの部品の1つです。

## 出典

- Google Cloud ブログ「[Introducing Gemini Enterprise Agent Platform, powering the next wave of agents](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform)」（2026年4月22日（米国時間）公開、2026年11月9日取得）
- Google Cloud「[Gemini プラットフォーム](https://cloud.google.com/products/gemini-enterprise-agent-platform?hl=ja)」製品ページ（2026年11月9日取得）
- Google Cloud ドキュメント「[Agent Platform の概要](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview?hl=ja)」（同）
- Google Cloud ドキュメント「[Vertex AI の名称変更](https://docs.cloud.google.com/gemini-enterprise-agent-platform/vertex-ai-name-changes)」と「[リリースノート](https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes?hl=en)」（同）
- Google Cloud「[Agent Platform の料金](https://cloud.google.com/model-garden/pricing?hl=ja)」（同）
- Google Cloud ドキュメント「[Gemini Enterprise Agent Platform とデータの保持ゼロ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention?hl=ja)」（同）
- Google Cloud ドキュメント「[デプロイとエンドポイントのロケーション](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations?hl=ja)」（同）
- Google Cloud ドキュメント「[Google Cloud の無料プログラム](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=ja)」（同）
- Google AI Studio「[Gemini Developer API vs. Gemini platform](https://ai.google.dev/gemini-api/docs/migrate-to-cloud)」（同）
- Google AI Studio「[Gemini API Additional Terms of Service](https://aistudio.google.com/docs/terms)」（同）
- Google Workspace 管理者ヘルプ「[Google Workspace の生成 AI に関するプライバシー ハブ](https://support.google.com/a/answer/15706919?hl=ja)」（同）
- Google Apps Script「[Vertex AI サービス](https://developers.google.com/apps-script/advanced/vertex-ai?hl=ja)」（同）
- Google Distributed Cloud エアギャップ「[Vertex AI の概要](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-overview?hl=ja)」（同）
- Wikipedia「[Vertex AI](https://ja.wikipedia.org/wiki/Vertex_AI)」（2026年5月26日更新版、経緯の日付）
