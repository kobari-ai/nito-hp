---
title: 【2026年11月】Amazon Bedrockとは？料金・始め方・AgentCoreとの違い
date: 2026-11-09
category: AI活用
description: Amazon Bedrockとは何かを公式の料金ページとドキュメントで解説。使えるモデル、東京でClaudeを使う条件と地域指定の料金、AgentCoreと旧Agentsの違い、ナレッジベース、始め方まで。
keyword: amazon bedrock
cover_tag: 導入担当向け
cover_headline: Amazon Bedrockとは
cover_sub: 料金・始め方・AgentCoreとの違い
cta: ai_agent
---

Amazon Bedrockは、AWSの上で複数の会社のAIモデルを1つの窓口から呼び出し、社内文書の検索やエージェントまで組める基盤です。製品ページによると、世界で10万を超える組織が使っています。

2026年7月30日には旧来のエージェント機能が新規の受付を止め、エージェントを作る場所はAgentCoreに移りました。この記事ではできることと料金、東京でClaudeを使うときの条件、AgentCoreとの違い、始め方を公式の料金ページとドキュメントで確かめました。

:::takeaways
- **Amazon BedrockはAIモデルと周りの部品をAWSの請求でまとめて使う基盤**。モデルは100種類以上、エージェントはAgentCoreで組む
- **料金は使ったトークンの数で決まり、東京から日本に限って呼ぶとGlobalより約1割高い**。月6,000件の社内の問い合わせの試算でClaude Sonnet 5は月66〜73ドル
- **東京でClaudeを使うならモデルごとの提供地域を先に見る**。Sonnet 5.5には日本に限る呼び方がまだ無い
:::

## Amazon Bedrockとは

### 何をするサービスか

ChatGPTやClaudeのアプリは人が画面で話しかけて使うものですが、Amazon Bedrockは自社のシステムからAPIでAIモデルを呼ぶための基盤です。2023年9月に一般提供が始まり、AWSがモデルを動かすサーバーやGPUを管理するので、利用する会社は呼び出す量に応じて払うだけで済みます。Anthropic・OpenAI・Amazonなど複数の会社のモデルを同じ書き方で呼べるうえ、社内文書を検索させるナレッジベース、入出力を絞るガードレール、エージェントを動かすAgentCoreまでが同じAWSの請求に載ります。**モデルを1社に決め打ちせず、AWSの権限・ログ・請求の中で切り替えられる点が、会社で使うときのいちばんの違いです。**

<!-- SHOT: 図 brk_overview.html → brk_01_overview.png・alt「Amazon Bedrockの3つの層を縦に並べた図。1はClaudeやGPTやNovaなど100種類以上のモデルを選んで呼ぶ層、2はナレッジベースとガードレールで業務に合わせる層、3はAgentCoreで実行環境と記憶とツールの接続を担う層」 -->

すでにAWSでS3やLambdaを使っている会社なら、文書の置き場所や業務の処理とそのままつなげます。AIのためだけに別の会社と契約し、請求と権限の管理を増やさなくて済む点も、情報システムの担当者には効いてきます。

### SageMakerとの違い

同じAWSのAmazon SageMakerは、機械学習のモデルを自分で作り、学習させ、配備するためのサービスです。インスタンスの選定やデータの準備まで自社で持つ代わりに、作り方の自由が大きくなります。Bedrockは各社が作った学習済みのモデルを呼ぶのが基本で、自社のデータで調整する機能も持っています。**自社データで一からモデルを学習させる予定が無いなら、Bedrockから始めるのが近道です。**需要予測のような従来の機械学習を自前で作るなら、SageMakerが向いています。

## Amazon Bedrockで使えるモデル

### 提供元と主なモデル

ユーザーガイドの概要はAmazon Bedrockが100を超える基盤モデルに対応していると書いています。料金ページに並ぶ提供元はAI21 Labs・Amazon・Anthropic・Cohere・DeepSeek・Google・Luma AI・Meta・MiniMax・Mistral AI・Moonshot AI・NVIDIA・OpenAI・Qwen・Stability AI・TwelveLabs・Writer・xAI・Z AIの19社です。2026年に入ってOpenAIのGPT-5.6の3モデルとGPT-6 Astra、xAIのGrok 4.6も加わり、以前の解説にある「OpenAIのモデルは一部だけ」という状況は変わりました。

| 用途 | 候補になる主なモデル |
|---|---|
| 込み入った判断・長い作業 | Claude Opus 5.5・Claude Fable 5.1・GPT-6 Astra |
| 社内の問い合わせ・要約 | Claude Sonnet 5.5・Claude Sonnet 5 |
| 大量の分類・抽出 | Claude Haiku 5.5・Amazon Nova 2 Lite |
| 画像・動画の生成 | Amazon Nova Canvas・Amazon Nova Reel・Stability AI |

同じ質問でもモデルによって答えの質と1件あたりの代金が10倍以上変わります。**まずはSonnetの系統とNova 2 Liteに同じ質問を送り、答えの質と使ったトークンの数を並べて比べるのがおすすめです。**モデルの得意・不得意は世代が替わるたびに入れ替わるため、古い比較記事の評価をそのまま使わない方が安全です。

### 提供が終わるときの決まり

Bedrockのモデルには、提供中・終了予定（Legacy）・終了（EOL）の3つの状態があります。2026年9月7日以降に出たモデルは、終了の前に原則6か月（一部は45日）の予告期間を置きます。予告期間に入ると新しい利用者は使えなくなり、15日間呼び出していない既存の利用者もアクセスを失うことがあります。終了日を過ぎると、すべてのリージョンで呼び出しが失敗し、新しいモデルへの切り替えは自動では起きません。

たとえばClaude Opus 5.5のモデルカードには「2027年9月22日より前には終了しない」と書かれています。**本番の仕組みでは1年ごとにモデルを乗り換える作業を最初から予定に入れておくのが無難です。**終了日はBedrockのモデルカードの日付が有効で、Anthropicなど提供元が発表する日付と違うことがあります。

## Amazon Bedrockでできること

### ナレッジベースで社内文書に答える

社内の規程やマニュアルを根拠に答えさせる仕組み（RAG）は、ナレッジベースで作ります。2026年3月2日からは保存・索引・検索の土台をBedrockが管理するマネージド型が加わりました。料金ページによると、S3・SharePoint・Confluenceなどから文書を取り込み、PDF・画像・表・音声・動画の読み取りと、検索用の変換、結果の並べ替えまでを自動で行います。答えと一緒に参照した文書の箇所も返せるので、社員が根拠を確かめられます。

従来の型ではベクトルデータベースや埋め込みのモデルを自分で選びます。どの作り方を選ぶかと、表の多いPDFや権限でつまずく点は[RAG構築とは](/media/rag-build/)で詳しく比べました。

### ガードレールで入出力を絞る

ガードレールはモデルに渡す質問と返ってくる答えの両方を検査する部品です。有害な内容のフィルター、扱わない話題の指定、個人情報の検出と伏せ字、禁止語、答えが参照文書に基づいているかの確認、ルールに沿うかを論理で確かめる自動推論チェックを組み合わせます。製品ページは有害な内容を最大88%遮断できると書いており、AWS Organizationsの中で同じ設定を複数のアカウントに共有できます。

**ガードレールはモデルを替えても同じ設定を使えるため、社内ルールを1か所で決めておけます。**問い合わせ窓口のように社外の人が入力する用途では、最初から入れておくのが安全です。

### AgentCoreでエージェントを動かす

AgentCoreはAIエージェントを本番で動かすための実行環境と部品の集まりです。社内のAPIを呼んだり、ブラウザやコードを操作したりする仕組みを、サーバーの管理なしで動かせます。旧来のAgentsとの違いと合わせた詳しい説明は次の節です。

### モデルの調整と文書の読み取り

自社データでの追加学習（ファインチューニング）、継続的な事前学習、大きなモデルの答え方を小さなモデルに移す蒸留、評価をもとにした強化学習による調整もできます。Data Automationは請求書や契約書のような文書・画像・音声・動画から決まった項目を取り出す部品で、ナレッジベースの読み取りにも使えます。処理の流れを画面でつなぐFlowsと、指示文を版ごとに保存するプロンプト管理もあります。

費用を下げる機能は同じ指示文を再利用するプロンプトキャッシュと、質問の難しさで安いモデルと高いモデルを振り分けるインテリジェントプロンプトルーティングの2つです。製品ページはルーティングで費用を最大30%下げられると説明しています。

## AgentCoreと旧Agentsの違い

2023年11月に始まったAmazon Bedrock Agentsは、今はAgents Classicという名前になっています。ユーザーガイドの更新履歴によると、2026年7月30日から新しい利用者は登録できなくなりました。すでに使っている会社はそのまま使い続けられ、似た機能を求める会社にはAgentCoreが案内されています。

| | AgentCore | Agents Classic | ナレッジベース |
|---|---|---|---|
| 役割 | エージェントの実行と運用の部品 | 画面で組むエージェント | 社内文書の検索 |
| 作り方 | コードか1回のAPI呼び出し | コンソールで設定 | コンソールかAPI |
| モデル | Bedrockの外のモデルも可 | Bedrockのモデル | Bedrockのモデル |
| 新規の利用 | できる | できない | できる |

AgentCoreの中身は、エージェントを1回のAPI呼び出しで定義して動かすHarness、隔離された環境で動かすRuntime、会話をまたいで覚えるMemory、社内のAPIやLambdaをMCPのツールに変えるGateway、利用者の権限で外部につなぐIdentityなどです。ツールの呼び出しをルールで止めるPolicy、動きを追うObservability、品質を測るEvaluationsもあります。LangGraph・CrewAI・Strands Agents・OpenAI Agents SDKといったフレームワークに対応し、OpenAIやGoogleのGeminiなどBedrockの外のモデルとも組めます。

<!-- SHOT: 図 brk_agents.html → brk_02_agents.png・alt「エージェントを作る場所の選び方を3段で示した図。これから作るならAgentCore、文書に答えるだけならナレッジベースを単体で使う、旧Agentsは2026年7月30日に新規受付を終了し既存の利用者だけが使える」 -->

### どれを選ぶか

**これから作るならAgentCoreを選び、社内文書に答えるだけならナレッジベースを単体で使うのが基本です。**問い合わせへの回答のように検索して答えるだけの用途では、エージェントの仕組みまで要りません。社内システムの更新や申請の代行のように複数の手順を自分で進めさせるときに、AgentCoreの出番が来ます。マネージド型のナレッジベースはAgentCoreと組み合わせる前提で作られていて、Gateway経由で呼ぶ場合はGatewayの料金が加わります。

AgentCoreの主な部品は東京リージョンで使えます。ただしエージェントに支払いをさせるpaymentsとWeb Searchのツールは、東京に来ていません。エージェントの設計で先に決めることは[AIエージェントの作り方](/media/ai-agent-build/)にまとめています。

## Amazon Bedrockの料金

### 料金の決まり方

文章のモデルは入力と出力のトークンの数に単価をかけて数えるのが基本です。単価はモデルごとに違い、さらに呼び出すリージョンと、処理する場所を限るかどうかで変わります。ナレッジベースやガードレールなどの部品は、保存量や回数で別に数えます。**ClaudeやGPTのような他社のモデルはAWS Marketplace経由の請求になり、Cost Explorerでは提供元の名前で表示され、Amazon Bedrockの行には含まれません。**費用を部門ごとに見たいなら、IAMのユーザーやロールにタグを付けて集計できます。

### 4つの階層とバッチ

呼び出すたびに速さと値段の違う4つの階層から選べます。

| 階層 | 中身 | 向く処理 |
|---|---|---|
| Standard | 既定の従量課金 | ふだんの問い合わせや要約 |
| Priority | 割増で優先して処理 | 顧客が待つ画面 |
| Flex | 割引で処理を待てる | 評価や夜間の要約 |
| Reserved | 1か月か3か月で処理量を予約 | 止められない基幹の処理 |

Reservedは1分あたり入力10万トークン・出力1万トークンからの予約で、稼働の目標は99.5%です。申し込みはAWSのアカウントチーム経由で、予約を消すまで請求が続きます。別にバッチ推論があり、対応するモデルはオンデマンドの半額です。ただしバッチは既定で24時間、最長168時間で打ち切られ、完了は保証されません。**Claudeの5.5の世代は、モデルカードではStandardだけの対応です。**

### 地域を限ると約1割高い

東京から呼ぶとき処理する場所の決め方は3つあります。東京のリージョンだけで処理するIn-Region、日本の中（東京と大阪）で振り分けるGeo、世界の商用リージョンに振り分けるGlobalです。ユーザーガイドはGlobalを標準料金より約10%安いと書き、Anthropicのドキュメントは地域を限る呼び方に10%の割増があると書いています。振り分けの転送料はかからず、料金は呼び出し元のリージョンの単価で数えます。

<!-- SHOT: 図 brk_region.html → brk_03_region.png・alt「東京からClaudeを呼ぶ2つの道を縦に並べた図。jp.を付けると東京と大阪で処理しGlobalより約1割高い。global.を付けると世界で処理し単価はClaude APIと同じ水準」 -->

**社外に出せない情報を扱うならjp.を付けた日本の中の呼び方、そうでなければglobal.を付けた安い呼び方、と用途ごとに分けられます。**どこで処理したかはCloudTrailの記録で後から確かめられます。

### 主なモデルの単価

東京のリージョンから呼んだときの単価です。100万トークンあたりの米ドルで、Standardの階層の値です。

| モデル | Global（入力/出力） | 地域を限る（入力/出力） |
|---|---|---|
| Claude Opus 5.5 | 4 / 20 | 4.4 / 22 |
| Claude Sonnet 5 | 2 / 10 | 2.2 / 11 |
| Claude Sonnet 4.6 | 3 / 15 | 3.3 / 16.5 |
| Amazon Nova 2 Lite | 0.36 / 3.01 | 0.396 / 3.311 |

Claude Sonnet 5.5は、料金ページの東京の欄が空いています（米国東部からのGlobalは入力2ドル・出力10ドル）。Claude Fable 5.1はGlobalだけで入力10ドル・出力50ドルです。**Globalの単価はAnthropicが直接売るClaude APIの単価と同じです。**旧い世代ほど高いことも多く、Sonnet 4.6はSonnet 5の1.5倍です。単価と割引の仕組みは[Claude APIの料金](/media/claude-api-pricing/)で詳しく扱いました。

<!-- SHOT: 画面 https://aws.amazon.com/jp/bedrock/pricing/ ・Anthropicのタブを開き地域の選択をAsia Pacific (Tokyo)にする・探す語「Global Cross-region Inference」・赤枠にする語「Claude Opus 5.5」の行・PC・alt「Amazon Bedrockの料金ページのAnthropicの表。東京から呼ぶGlobalの単価でClaude Opus 5.5は入力が100万トークンあたり4ドル、出力が20ドル」・figcaption「Amazon Bedrockの料金ページ（2026年11月9日）」 -->

### 部品の料金

| 部品 | 単価 |
|---|---|
| ナレッジベース（マネージド）の保存 | 元データ1GBあたり月5ドル |
| ナレッジベースの検索 | 1,000回1ドル（エージェント型は1,000回4ドル＋内部の検索代） |
| ガードレールの内容フィルター | 1,000テキスト単位0.15ドル |
| ガードレールの個人情報の検出 | 1,000テキスト単位0.10ドル |
| Data Automationの文書 | 1ページ0.01ドル |
| AgentCore Runtime | 1vCPU時間0.0895ドル・1GB時間0.00945ドル |
| AgentCore Gateway | 1,000回の呼び出しで0.005ドル |

ガードレールの1テキスト単位は1,000文字までで、5,600文字なら6単位です。ナレッジベースのマネージド型は、文書の読み取り・検索用の変換・並べ替えに標準のモデルを使う限り追加の代金がかかりません。AgentCore Runtimeは1秒単位で、モデルの返事を待つ間のCPUは数えません。**AgentCore Memoryの短期の記憶は2026年10月6日から数え方が変わり、10月5日までは1,000件0.25ドル、6日からは1GBあたり1ドルです。**10月分の請求は前半と後半で数え方が違うので、明細を前月と比べるときに注意が要ります。

### 月額の試算

社内の問い合わせに1日300件、月20日で6,000件答える仕組みを想定しました（試算）。1件に入力3,000トークン、出力500トークンを使うとして、月に入力1,800万トークン・出力300万トークンです。円は三菱UFJ銀行の2026年11月6日の仲値、1ドル157.77円で換算しています。

| モデル | 日本に限る | Global |
|---|---|---|
| Claude Opus 5.5 | 145.2ドル（約2.3万円） | 132ドル（約2.1万円） |
| Claude Sonnet 5 | 72.6ドル（約1.1万円） | 66ドル（約1.0万円） |
| Amazon Nova 2 Lite | 17.06ドル（約2,700円） | 15.51ドル（約2,400円） |

文書2GBのナレッジベースで月6,000回検索すると、保存10ドルと検索6ドルで16ドル（約2,500円）が加わります。質問と答えを2テキスト単位としてガードレールの内容フィルターをかけても、月1.8ドルほどです。**金額の差を生むのはモデルの選び方で、地域を限るかどうかの差は1割にとどまります。**実際の予算を左右するのは、答えを確かめて直し続ける人の時間の方です。

### 無料で試せる範囲

製品ページによると、AWSの新しい利用者は最大200米ドル分のクレジットを受け取れます。上の試算ならSonnet 5を3か月近く動かせる額です。クレジットの対象と期限はAWSの無料利用枠のページで確かめてから使うのが確実です。

## ClaudeをBedrockで使う条件

### 東京で使えるClaudeのモデル

同じClaudeでも、モデルごとに東京から呼べる方法が違います。モデルカードの地域の表を3つ確かめました。

| モデル | 東京からの呼び方 | Bedrockでの公開日 |
|---|---|---|
| Claude Opus 5.5 | jp.とglobal. | 2026年9月22日 |
| Claude Sonnet 5.5 | global.だけ | 2026年9月28日 |
| Claude Haiku 5.5 | jp.とglobal. | 2026年10月7日 |

<!-- SHOT: 画面 https://docs.aws.amazon.com/ja_jp/bedrock/latest/userguide/model-card-anthropic-claude-sonnet-5-5.html （日本語の版が無ければ英語の版）・探す語「ap-northeast-1」・赤枠にする語「ap-northeast-1 (Tokyo)」の行・PC・alt「Claude Sonnet 5.5のモデルカードの地域の表。東京の行はIn-RegionとGeoが対応外で、Globalだけが対応」・figcaption「Amazon BedrockのClaude Sonnet 5.5のモデルカード（2026年11月9日）」 -->

**Sonnet 5.5を日本の中だけで処理させる呼び方は、まだありません。**社内の規程で日本国外での処理を避けたい会社は、Opus 5.5かHaiku 5.5、またはSonnet 5を選ぶことになります。jp.を付けた呼び方は東京から呼んでも大阪から呼んでも東京と大阪の2か所で処理されます。In-Regionで呼べるOpus 5.5はロンドンだけです。

### 初回の利用目的フォーム

ほとんどのモデルは2025年10月15日から正しいIAMの権限があれば最初から使える状態です。以前の解説によくある「モデルアクセス」の画面から申請する手順は、今は米国の政府向けリージョン（GovCloud）だけで使う手順です。ただしAnthropicのモデルは、初めて使う前に会社名・ウェブサイト・用途を書くフォームを1回出す必要があります。組織の管理アカウントで出せば、同じ組織のほかのアカウントにも引き継がれます。

出した後に保留の状態になることがあり、その間の呼び出しは拒否され、エラーが返るだけで処理は通りません。設定が終わるとAWSからメールが届きます。モデルごとの条件も違い、AnthropicのドキュメントではClaude Fable 5.1・Sonnet 5・Opus 4.8などはすべての利用者に開かれたモデルです。Opus 5.5・Sonnet 5.5・Haiku 5.5はコンソールで条件を確かめるよう案内されています。

### Bedrockで使えないClaudeの機能

Anthropicのドキュメントによると、Bedrock経由のClaudeでは使えない機能があります。

- Files APIとURLで渡す画像・文書
- コード実行・Web検索・Web取得などAnthropic側で動くツール
- Agent Skills・MCPコネクタ・プログラムによるツール呼び出し
- Claude Managed Agents
- 自動のプロンプトキャッシュ（区切りを明示する方式は使える）

どれもAnthropicのAPIに直接つなげば使える機能です。

**Web検索させたいエージェントなら、AgentCoreのWeb Searchか自前の検索ツールを組み合わせることになります。**AgentCoreのWeb Searchは東京リージョンに来ていない点も、設計の前に押さえておきたいところです。

### Claude Platform on AWSとの違い

AWSの請求でClaudeを使う道はBedrockだけではありません。AnthropicのClaude on AWSのページは、入口をClaude Platform on AWS・Claude on Amazon Bedrock・AWS MarketplaceのClaude Enterpriseの3つに分けています。Claude Platform on AWSはAnthropicが運営するClaude APIをAWSの認証と請求で使う経路で、新しい機能が同じ日に届くことが多いとされます。BedrockはAWSが管理する基盤で動き、Anthropicの社員は推論の基盤に触れられません。

**データをAWSの境界の中に置き、ナレッジベースやガードレールと組むならBedrock、Claudeの最新の機能をすぐ使いたいならPlatform on AWSが向いています。**契約の経路ごとの違いは[Claudeの法人契約](/media/claude-corporate-contract/)にまとめています。

## Amazon Bedrockの始め方

1. **AWSアカウントと権限を用意する**: 管理者がIAMでBedrockの権限を付ける。他社のモデルを初めて呼ぶ人にはAWS Marketplaceの購読の権限も要る
2. **リージョンを東京にする**: コンソールの右上でアジアパシフィック（東京）を選び、検索窓に「Bedrock」と入れて開く
3. **モデルカタログからプレイグラウンドで試す**: モデルを選んで開き、チャットの画面で質問を送る。他社のモデルは初回の呼び出しで購読が始まり、完了まで最大15分
4. **APIキーかIAMロールでSDKから呼ぶ**: 新しいアプリにはbedrock-runtimeのエンドポイントが推奨。Converse APIならモデルを替えても同じ書き方で呼べる
5. **本番の呼び方を決める**: モデルIDの頭にjp.かglobal.を付け、データの扱いと単価のどちらを優先するかを決める

<!-- SHOT: 画面 https://console.aws.amazon.com/bedrock/ （要ログイン。撮れなければ外す）・モデルカタログの一覧・赤枠にする語「モデルカタログ」・PC・alt「Amazon Bedrockのコンソールのモデルカタログ。提供元ごとにモデルが並び、選ぶとプレイグラウンドで試せる」・figcaption「Amazon Bedrockのコンソール（2026年11月9日）」 -->

プレイグラウンドではチャット・テキスト・画像の生成を試せ、回答の下に入力と出力のトークン数が出ます。この数を控えておくと、上の試算に自社の数字を入れられます。英語で答えが返ってきたら、指示に「日本語で」と書き足すだけで直ることが多いです。

## 会社で使うときに決めること

### データの扱い

製品ページはBedrockがモデルの学習のためにデータを保存したり使ったりしないと書いています。ユーザーガイドのデータ保護の章によると、モデルの提供元はBedrockが運用するアカウントに入れず、プロンプトや答えを見られません。一方でGlobalの呼び方では日本の外で処理されることがあり、乱用の検知のために保存される場合は処理したリージョンに保存されます。**社外秘の情報を流す仕組みは、jp.の呼び方とログの保存先を最初に決めておくのが安全です。**

### 権限と費用の管理

IAMで使ってよいモデルを利用者ごとに絞れます。利用規約を法務が読む前に使われたくないなら、組織のSCPで先に呼び出しを止め、読み終えてから許可する順番がユーザーガイドで勧められています。1日に使えるトークンの上限は2026年9月から、アカウントとリージョンごとに全モデルの合計で決まる形に変わりました。部門ごとの費用はIAMのタグで分けて集計できます。

### 請求と契約の窓口

支払いはAWSの請求書にまとまり、他社のモデルの代金もAWS Marketplace経由で同じ請求に載ります。Claudeの販売代理の扱いは[Claudeの法人契約](/media/claude-corporate-contract/)に書いたとおりで、野村総合研究所は2025年11月20日にBedrock向けの認定リセラーに選ばれたと発表しました。

どの業務にどの部品で組むか、jp.とglobal.のどちらで動かすかを決めきれない場合は、nitoの[AIエージェント構築支援](/ai-agent/)で要件の整理から相談できます。

## Amazon Bedrockの活用事例

製品ページには2社の事例が載っています。米国の証券会社Robinhoodは、6か月で1日の処理量を5億トークンから50億トークンに増やしながら、AIの費用を80%下げ、開発の時間を半分にしました。マーケティング会社のEpsilonは、AgentCoreでエージェントの開発を数か月から数週間に縮めています。AnthropicのClaude on AWSのページでは、旅行ガイドのLonely PlanetがClaudeで旅程づくりを自動化し、試した市場で制作費を80%下げたと紹介されています。

どれも各社の発表で、条件をそろえた比較ではありません。日本の会社で始めやすいのは、社内規程の検索、問い合わせの一次回答、請求書や契約書の読み取り、開発者のコードの補助です。

## まとめ

- **社内文書に答えるボットを作るなら**、マネージド型のナレッジベースとSonnetの系統から始める。月6,000件でもモデルと検索で月100ドル前後
- **複数の手順を進めるエージェントを作るなら**、AgentCoreを選ぶ。旧Agentsは新規に使えない
- **日本の外での処理を避けたいなら**、jp.で呼べるモデルを選ぶ。Sonnet 5.5はまだglobal.だけ
- **Claudeの最新の機能が要るなら**、Bedrockで使えない機能を先に確かめ、Claude Platform on AWSと比べる

## よくある質問

### Amazon Bedrockは無料で使えますか？

使った分だけ払う従量課金です。AWSの新しい利用者は最大200米ドル分のクレジットを受け取れるので、試す段階の費用はその範囲で収まることが多いはずです。

### Amazon BedrockのClaudeは東京で使える？

使えます。Opus 5.5とHaiku 5.5は日本の中に限るjp.でも呼べますが、Sonnet 5.5は東京からはglobal.だけです。

### Bedrock Agentsは今から使えますか？

新しく登録はできません。2026年7月30日にAgents Classicとして新規の受付を終え、すでに使っている会社だけが使い続けられる状態です。これから作るならAgentCoreです。

### BedrockとClaude APIで料金は違う？

Globalで呼べば、Claude Sonnet 5.5やOpus 5.5の単価はClaude APIと同じです。jp.のように地域を限ると1割高くなります。

### Amazon Bedrockのデータは学習に使われる？

使われません。製品ページはBedrockがモデルの学習のためにデータを保存・使用しないと書き、モデルの提供元もプロンプトや答えを見られない仕組みです。

### Amazon BedrockでGPTは使えますか？

使えます。GPT-5.6 Sol・Terra・LunaとGPT-6 Astraが提供されています。モデルごとに呼べるリージョンが違うので、モデルカードで確かめてください。

### BedrockでClaude Codeは使えますか？

使えます。Claude CodeはBedrockの認証で動かせ、その場合の代金はBedrockで使ったトークンの分です。設定の手順はClaude Codeのドキュメントにあります。

## 出典

- AWS「[Amazon Bedrock](https://aws.amazon.com/jp/bedrock/)」「[Amazon Bedrock の料金](https://aws.amazon.com/jp/bedrock/pricing/)」「[Amazon Bedrock AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/)」（2026年11月9日取得）
- Amazon Bedrock ユーザーガイド「[Overview](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)」「[Request access to models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)」「[Cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)」「[Geographic cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/geographic-cross-region-inference.html)」「[Service tiers](https://docs.aws.amazon.com/bedrock/latest/userguide/service-tiers-inference.html)」「[Model lifecycle](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html)」「[Automate tasks using AI agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)」「[Data protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)」「[Document history](https://docs.aws.amazon.com/bedrock/latest/userguide/doc-history.html)」
- Amazon Bedrock モデルカード「[Claude Opus 5.5](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-opus-5-5.html)」「[Claude Sonnet 5.5](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-sonnet-5-5.html)」「[Claude Haiku 5.5](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-haiku-5-5.html)」「[Anthropic](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)」
- Amazon Bedrock AgentCore 開発者ガイド「[Overview](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)」「[Supported AWS Regions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html)」
- Anthropic「[Claude in Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)」「[Claude on Amazon Bedrock (Opus 4.6 and earlier)](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock)」「[Claude on AWS](https://claude.com/ja/partners/claude-on-aws)」
- Claude Code ドキュメント「[Amazon Bedrock 上の Claude Code](https://code.claude.com/docs/ja/amazon-bedrock)」
- 三菱UFJリサーチ＆コンサルティング「[外国為替相場](https://www.murc-kawasesouba.jp/fx/index.php)」（2026年11月6日の公示相場）
