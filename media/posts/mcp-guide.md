---
title: 【2026年11月】MCPとは？仕組みとMCPサーバー・会社で使うときの対応表と管理
date: 2026-11-06
category: AI活用
keyword: mcp とは
description: MCPとは何かを公式資料で解説。MCPサーバーの仕組みとできること、Claude・ChatGPT・Copilot Studio・Geminiの対応、freeeやSlackなど国内SaaSの公式MCPサーバー、管理者が決めることまで。
cover_tag: 導入担当向け
cover_headline: MCPとは
cover_sub: 仕組み・対応ツール・管理者が決めること
cta: ai_agent
---

MCP（Model Context Protocol）は、Claudeの開発元のAnthropicが2024年11月25日に公開した、AIアプリと外部のツールやデータをつなぐ共通規格です。いまはChatGPTやMicrosoft Copilot、Geminiも対応しています。

社内でAIを広げる担当者には、社員が会計や顧客のデータを勝手につないでよいのかが気になるところです。この記事ではMCPの仕組みに加えて、対応しているAIツールと国内SaaSの公式MCPサーバー、管理者が決めることを公式の資料で整理しました。

:::takeaways
- MCPはAIと外部のツールをつなぐ**共通の差し込み口**。AIツール側とサービス側がそれぞれ1回対応すれば組み合わせが広がる
- ClaudeもChatGPTも、**会社のプランで接続を足せるのは管理者やオーナー**。誰に許すかを先に決める
- freee・マネーフォワード・Slackは**提供元がホストするリモート型**、kintone・Backlogは**手元で動かすローカル型**が公式。鍵の持ち方が変わる
:::

## MCPとは何か

AIのチャットに社内の資料を貼り付けて質問した経験がある人は少なくないはずです。MCPはその貼り付けの代わりに**AIが自分で外部のシステムを読み書きできるようにするための接続の決まり**です。公式サイトはMCPをAIアプリと外部のシステムをつなぐオープンソースの標準と説明し、USB-Cの差し込み口にたとえています。

MCPが出る前はSlack・Googleドライブ・社内のデータベースと、接続先ごとに専用の連携を作る必要がありました。AIアプリが3つ、つなぎたいサービスが5つなら15通りの連携が要ります。MCPの形にそろえれば、AIアプリ側の対応3つとサービス側の対応5つの計8つで足ります。

Anthropicは2025年12月9日、MCPをLinux Foundationの下にあるAgentic AI Foundationに寄贈しました。この財団はAnthropic・Block・OpenAIが共同で設立し、Google・Microsoft・AWS・Cloudflare・Bloombergが支援しています。同じ発表の時点で公開されているMCPサーバーは1万を超えていました。**1社の製品の機能ではなく業界の共通規格になったため、特定のAIツールに縛られずに選べる**のが会社にとっての意味です。

## MCPの仕組みとMCPサーバーとは

MCPには3つの役割が出てきます。

| 役割 | 何をするか | 例 |
|---|---|---|
| ホスト | 利用者が操作するAIアプリ | Claude、ChatGPT、Copilot Studio、Cursor |
| クライアント | ホストの中でサーバーとの接続を受け持つ部品 | ホストに組み込まれている |
| サーバー | 外部のサービスの窓口。AIに使わせる操作を決める | freeeのMCPサーバー、SlackのMCPサーバー |

<!-- SHOT: 図 mcp_structure.html → mcp_01_structure.png・alt「MCPの3つの役割を上から順に並べた図。利用者が操作するAIアプリがホストで、その中のクライアントがMCPサーバーにつなぎ、MCPサーバーが会計や社内チャットなどのサービスを操作する」 -->

**MCPサーバーとは、サービスの側に置く「AI用の窓口」です。** 何を読ませ、何を書き換えさせるかはサーバーが決めます。サーバーがAIに渡せるものは3種類あり、操作を実行するツール、読み取るためのデータであるリソース、決まった頼み方のひな形であるプロンプトです。

流れは次のとおりです。利用者が「先月の〇〇社への請求書を探して」と頼むと、AIが使うツールを選び、クライアントが会計サービスのMCPサーバーに依頼します。サーバーがサービスのAPIを呼んで結果を返し、AIがそれを読んで答えます。通信はJSON-RPCという形式で、手元のパソコンでサーバーを動かすローカル型と、インターネット上のサーバーにつなぐリモート型があります。

気をつけたいのは**MCPそのものはAIエージェントの作り方を決めるものではない**ことです。どのツールをいつ呼ぶかを判断するのはAIの側で、MCPはつなぎ方をそろえるだけです。AIエージェントの考え方は[AIエージェントとは](/media/ai-agent-guide/)にまとめています。

## MCPでできること

できることは大きく3つで、外部のデータを探して読む・データを書き換える・会話の中に操作画面を出す、に分かれます。業務に置き換えると次のような使い方です。

- 会計ソフトの仕訳を探し、試算表をまとめてレポートにする
- 課題管理ツールの未対応の課題を拾い、担当ごとに一覧にする
- 社内チャットの過去のやり取りから、決まったことを探して要約する
- 社内の文書を探して、提案書の下書きの材料をそろえる

公式サイトはこのほかに、Figmaのデザインからウェブアプリを作る、社内の複数のデータベースにチャットで質問する、といった例を挙げています。**大事なのは読むだけか書き換えまでかで、書き換えを許すと誤操作の影響が実際の業務データに及びます。** この区別は後の管理の節でも使うので、覚えておいてください。

## APIやRAGとの違い

「APIがあるならAIにAPIを使わせればよいのでは」とよく聞かれます。APIは人の開発者が仕様書を読んで呼び出すものです。AIにその場で仕様を読ませてコードを書かせると、同じ依頼でも日によって動きが変わりかねません。**MCPはAIが読める形で操作と認証の方法をあらかじめ決めておく**ので、AIは決まった手順を呼ぶだけで済みます。実際には多くのMCPサーバーが中でサービスのAPIを呼んでおり、APIの上にかぶせる層と考えると分かりやすくなります。

RAGは社内の文書を検索して答えの材料にする仕組みでした。MCPは情報を取るだけでなく、登録や更新のような操作まで含みます。社内文書の検索だけが目的ならRAGで足りることも多く、作り方は[RAG構築とは](/media/rag-build/)で比べています。

## MCPに対応しているAIツール

会社でよく検討されるAIツールについて、各社の公式ドキュメントで確かめた対応状況です。

| AIツール | MCPサーバーの追加 | 会社のプランで足せる人 |
|---|---|---|
| Claude（claude.ai・Desktop） | カスタムコネクタでリモートのサーバーを追加 | Teamはオーナー、Enterpriseはオーナーと管理権限のあるロール |
| ChatGPT | カスタムMCPサーバーを追加（ウェブ版のみ） | Businessは管理者とオーナー、Enterpriseは権限を与えたメンバーも作成可 |
| Copilot Studio | エージェントのツールとして追加 | エージェントを作る人 |
| Gemini Enterprise | コネクタの一覧からカスタムMCPサーバーを接続 | 管理者 |
| Gemini CLI | 設定ファイルにサーバーを書く | 使う人それぞれ |

Claudeのカスタムコネクタは、無料プランを含む全プランで使えます（無料は1つまで）。TeamとEnterpriseでは管理者側が組織に追加し、社員は一覧から自分のアカウントで接続します。**接続がAPIキーのような共有の認証情報だと、使う人全員がそのキーの権限を持つ**ので、渡すキーは社員に見せてよい範囲に絞る必要があります。また、ClaudeはAnthropicのクラウドからサーバーにつなぐため、社内ネットワークの中のサーバーにはそのままでは届きません。

ChatGPTでMCPの全機能を使えるのはBusinessとEnterprise・Eduで、Proは読み取りと取得だけです。管理者が承認した時点のツールの一覧が固定され、サーバー側でツールが増えても管理者が更新して公開するまで反映されません。反対にCopilot Studioは、サーバー側の変更がそのままエージェントに反映されると説明しています。**同じMCPサーバーでも、変更を止めて確かめる作りと自動で追う作りがある**ため、書き込みのあるサーバーをつなぐときは差を知っておく必要があります。

<!-- SHOT: 画面 https://help.openai.com/ja-jp/articles/12584461・本文だけにある探す語「提供対象と要件」・赤枠にする語「ChatGPT Business および Enterprise/Edu のお客様がウェブ版 ChatGPT で利用できます」・PC・alt「OpenAIのヘルプ。カスタムMCPサーバーへの接続とMCPの全機能はChatGPT BusinessとEnterprise・Eduのウェブ版で使えると書かれている」・figcaption「ChatGPTでカスタムMCPサーバーを使えるプラン（OpenAIヘルプ、2026年11月6日）」 -->

ChatGPTのアプリ全体の管理画面は[ChatGPTコネクタの管理者設定](/media/chatgpt-connectors-admin/)、Claude Codeでの接続の手順は[Claude MCPとは](/media/claude-mcp-guide/)で扱っています。

## 国内でよく使うSaaSの公式MCPサーバー

日本の会社でよく使うSaaSのうち、提供元が公式にMCPサーバーを出しているものをまとめました。

| サービス | 提供の形 | 主にできること | 認証 |
|---|---|---|---|
| freee | リモート（推奨）とローカル | 会計・人事労務・請求書など12のAPIとサイン | OAuth |
| マネーフォワード クラウド会計 | リモート（2026年3月26日から全プラン） | 仕訳入力・帳簿検索・レポート作成 | OAuth |
| kintone | ローカル | アプリとレコードの取得・追加・更新・削除 | パスワードかAPIトークン |
| Backlog | ローカル（自前でHTTP化も可） | 課題・Wiki・プルリクエストの操作 | APIキー（自前のOAuthも可） |
| Slack | リモート | メッセージの検索・送信、キャンバス、リスト | OAuth（登録済みのアプリ） |
| Notion | リモート | ページの検索・作成・編集、データベース | OAuth |

**リモート型は提供元がサーバーを動かし、社員は自分のアカウントでログインして使います。** freeeは公式のURLを示したうえで、公式以外のURLを入れないよう注意を書いています。マネーフォワードはそれまでプラチナランク以上の士業事務所向けのβ版だったリモートMCPサーバーを全プランに広げました。

**ローカル型は社員のパソコンでサーバーを動かし、パスワードやAPIキーを設定ファイルに書きます。** kintoneの公式サーバーはレコードの削除やアプリ設定の本番反映のツールも持っており、使ったユーザーの権限でそのまま動きます。社員それぞれが自分の鍵を置く形になるため、誰のパソコンにどの鍵があるかを会社がつかみにくいのが難点です。

SlackのMCPサーバーは、Slackに登録されたアプリを通す決まりで、ワークスペースの管理者が承認し、操作は監査ログで追える作りです。使っているSaaSが対応しているかは、公式のヘルプで「MCP」と検索する、使っているAIツールのコネクタ一覧を見る、提供元に聞く、の順で確かめられます。

<!-- SHOT: 画面 https://github.com/freee/freee-mcp・本文だけにある探す語「方法 1: Remote MCP で接続する（推奨）」・赤枠にする語「freee 公式以外の URL を入力しないようにご注意ください」・PC・alt「freee公式のMCPサーバーの説明。推奨はfreeeが提供するリモートMCPサーバーに接続する方法で、freee公式以外のURLを入力しないよう注意がある」・figcaption「freee公式MCPサーバーの接続方法（GitHub、2026年11月6日）」 -->

## 会社で使うときに管理者が決めること

MCPは便利な半面、決めごとのないまま広がれば社員が個人で会社のデータをつなぐ状態になりかねません。上位のAIツールとSaaSの公式の説明から、管理者が先に決めることを5つに分けました。

<!-- SHOT: 図 mcp_admin.html → mcp_02_admin.png・alt「会社でMCPを使うときに管理者が決める5つを縦に並べた図。接続を足せる人、つなぐサーバー、読むだけか書き換えるか、実行前の確認、記録の残し方」 -->

### 接続を足せる人

ClaudeのTeamとEnterprise、ChatGPTのBusinessは、最初から管理者側しか組織のコネクタを足せない作りです。Enterpriseはロールで作れる人を広げられるので、**開発部門だけに作成を許し、公開は情報システムの担当が見る**、といった分け方ができます。

### つなぐサーバー

使ってよいのは提供元の公式サーバーと、中身を確かめた社内のサーバーだけ、と決めます。Claudeのヘルプも、Anthropicが検証していないサービスにつながると明記し、信頼できるサーバーだけにつなぐよう求めています。

### 読むだけか書き換えるか

最初は読み取りだけで始め、効果を確かめてから書き込みを許すのが安全です。ChatGPTのEnterpriseはアプリごとに許す操作を選べ、新しい操作は既定で無効になります。Backlogの公式サーバーのように、使うツールの組を絞れるサーバーもあります。

### 実行前の確認と記録

書き換えの前に人が確かめる設定と、誰がいつ何をしたかの記録を用意します。Claudeでは調査の機能（Research）が承認なしでツールを呼ぶため、書き込みのツールは切っておくのが公式の案内です。ChatGPTのEnterpriseはCompliance APIで、アプリを使った会話も取得できます。

### ID基盤でまとめて管理する

2026年6月18日、会社のID基盤からMCPサーバーへの接続をまとめて管理するEnterprise-Managed Authorizationが安定版になりました。社員一人ひとりがサービスごとに許可していく形をやめ、**入社や退職のときの権限の付け外しをID基盤側で一度に済ませる**ための仕組みです。AIツールとサーバーの両方が対応している必要があるので、使うツールの対応を確かめてから計画に入れます。

社員が個人のAIアカウントで同じことを始めているなら、先に[シャドーAI対策](/media/shadow-ai/)の進め方で現状をつかむのが近道です。

## MCPのリスクと対策

一番よく挙がるのはプロンプトインジェクションです。**AIが読み込んだページや課題の本文に指示のような文が紛れていると、AIがそれに従って意図しない操作をすることがあります。** 悪意のあるMCPサーバーが説明文に隠れた指示を入れる手口もあり、Claudeのヘルプも注意を促しています。

次に、サーバーの中身が後から変わる問題です。一度承認したサーバーでも、提供者がツールの動きを変えれば挙動が変わります。ChatGPTが承認時のツールを固定しているのはこのためで、Claudeのヘルプもツールの動きの変化を見張るよう書いています。

MCPの公式サイトはセキュリティの手引きを公開しており、利用者の同意を飛ばして認可を奪う「混乱した代理（confused deputy）」などの攻撃と対策をまとめています。利用する会社の側でできる対策は、次のとおりです。

- 公式の提供元か、中身を確かめたサーバーだけをつなぐ
- 権限は読み取りから始め、要るものだけ広げる
- 書き換えや送信の前に人の確認を挟む
- 操作の記録を残し、定期的に見直す

## MCPサーバーの作り方の概要

自社のシステムをAIにつなぎたいなら、MCPサーバーを作ることになります。公式のSDKがPythonやTypeScriptなど主な言語で用意されており、サーバーは「どんな操作を、どんな入力で受け付けるか」を書いて公開する形です。

会社で使うなら、最初にリモート型かローカル型かを決めます。ClaudeやChatGPTの会社向けの画面からつなぐなら、インターネットから届くHTTPSのリモート型が前提です。ChatGPTには社内のサーバーを公開せずにつなぐSecure MCP Tunnelもあります。2026年7月28日の仕様改定では接続がステートレスになり、古いHTTP+SSEの方式は非推奨に整理されたため、新しく作るならHTTPの方式を選びます。

作るときに外せないのは、ツールを増やしすぎないことでしょう。**機能を全部ツールにするとAIがどれを使うか選びにくくなる**ので、業務の手順として決まっている処理は1つのツールにまとめ、AIはそれを呼ぶだけにします。社内の業務をどこまでAIに任せるかの設計から相談したい場合は、[AIエージェント構築支援](/ai-agent/)でお手伝いしています。

## まとめ

- **まず試したい**: 使っているSaaSに公式のリモート型MCPサーバーがあれば、管理者が組織に1つだけ追加し、読み取りだけで数人に使わせる
- **社員が個人で使い始めている**: 接続を足せる人を管理者に絞り、つないでよいサーバーの一覧を先に出す
- **書き込みまで任せたい**: 実行前の確認と記録を用意し、ChatGPTのように承認時のツールを固定できるかを確かめてから広げる
- **社内システムをつなぎたい**: リモート型で作り、手順の決まった処理を少数のツールにまとめる

## よくある質問

### MCPとは簡単に言うと何ですか？

AIアプリと外部のツールやデータをつなぐための共通規格です。Anthropicが2024年11月に公開し、2025年12月からはLinux Foundation傘下の財団で管理されています。

### MCPサーバーとは何ですか？

外部のサービスの側に置く、AI用の窓口です。AIが使える操作（ツール）、読めるデータ（リソース）、頼み方のひな形（プロンプト）を決めて公開します。

### MCPは無料で使えますか？

規格そのものはオープンソースで無料です。ただし使うAIツールやサービスの契約は別に要り、ChatGPTでMCPの全機能を使えるのはBusinessとEnterprise・Eduです。Claudeは無料プランでもカスタムコネクタを1つ使えます。

### ChatGPTでMCPサーバーを使えますか？

使えます。BusinessとEnterprise・Eduのウェブ版でカスタムMCPサーバーを追加でき、Businessで作成と公開ができるのは管理者とオーナーです。Proは読み取りと取得の権限で接続できます。

### MCPとA2Aの違いは何ですか？

MCPはAIとツールやデータをつなぐ規格で、A2AはAIエージェント同士がやり取りするための規格です。役割が違い、組み合わせて使えます。

### MCPとRAGの違いは何ですか？

RAGは社内の文書を検索して答えの材料にする仕組みです。MCPは検索に加えて、登録や更新のような操作もAIにさせられます。

### freeeやマネーフォワードはMCPに対応していますか？

どちらも公式のMCPサーバーがあります。freeeは会計や人事労務など12のAPIに対応し、マネーフォワード クラウド会計は2026年3月26日からリモートMCPサーバーを全プランで提供しています。

### MCPを社内で使うときの一番のリスクは何ですか？

AIが読み込んだ内容に紛れた指示で意図しない操作をするプロンプトインジェクションです。信頼できるサーバーだけをつなぎ、書き換えの前に人の確認を挟むことで影響を抑えます。

## 出典

本文の内容は次の公式ページで2026年11月6日に確かめています。

- Model Context Protocol「[What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro)」
- Model Context Protocol「[Key Changes（2026-07-28）](https://modelcontextprotocol.io/specification/2026-07-28/changelog)」
- Model Context Protocol「[Security Best Practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)」
- MCP Blog「[Enterprise-Managed Authorization](https://blog.modelcontextprotocol.io/tags/oauth/)」
- Anthropic「[Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)」
- Anthropic「[Donating the Model Context Protocol and establishing the Agentic AI Foundation](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)」
- Anthropicヘルプセンター「[リモートMCPを使用したカスタムコネクタの開始](https://support.claude.com/ja/articles/11175166)」
- OpenAI ヘルプセンター「[ChatGPT でのカスタム MCP サーバーへの接続](https://help.openai.com/ja-jp/articles/12584461)」
- Microsoft Learn「[モデル コンテキスト プロトコルを使用してエージェントを拡張する](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/agent-extend-action-mcp)」
- Google Cloud「[Gemini Enterprise エディションのコネクタ](https://cloud.google.com/gemini-enterprise/connectors?hl=ja)」
- Gemini CLI「[MCP servers with Gemini CLI](https://geminicli.com/docs/tools/mcp-server/)」
- freee「[freee-mcp](https://github.com/freee/freee-mcp)」
- マネーフォワード「[『マネーフォワード クラウド会計』、リモートMCPサーバーを全プランで提供開始](https://corp.moneyforward.com/news/release/service/20260326-mf-press-1/)」
- サイボウズ「[kintone MCP Server](https://github.com/kintone/mcp-server)」
- ヌーラボ「[Backlog MCP Server](https://github.com/nulab/backlog-mcp-server)」
- Slack「[Slack MCP server overview](https://docs.slack.dev/ai/mcp-server/)」
- Notion「[Notion MCP](https://developers.notion.com/docs/mcp)」
