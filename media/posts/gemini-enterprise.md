---
title: 【2026年10月】Gemini Enterpriseとは？料金とWorkspaceのGeminiとの違い
date: 2026-10-26
category: AI活用
description: Google CloudのGemini Enterpriseを公式のページとドキュメントで解説。エディションごとの料金と割り当て、WorkspaceのGeminiで足りる範囲、申し込みの2通り、社内データのつなぎ方、データの扱いまで。
cover_tag: 導入担当向け
cover_headline: Gemini Enterpriseとは
cover_sub: 料金とWorkspaceのGeminiで足りる範囲
cta: ai_agent
cta_eyebrow: Gemini Enterpriseを検討している方へ
cta_title: どの業務をエージェントに任せるかまで決まっていますか
cta_text: ライセンスを買っても、どの業務のどの手順を任せるかは社内で決めることになります。nito は業務の棚卸しから、指示しなくても動く AI エージェントの構築まで一緒に進めます。
---

Gemini Enterprise Businessエディションのページは、料金を1シートあたり月額21ドルからと表示しています（2026年10月26日）。Workspaceの管理者ヘルプには、Gemini EnterpriseはGoogle Workspaceのサブスクリプションに含まれていないと書かれています。

GmailやドキュメントのGeminiをもう使っている会社では、別の契約を足す理由があるかが判断の中心です。この記事は公式のページとドキュメントをもとに、できること・料金・Workspaceで足りる範囲・入れる前に決めることを並べます。契約と管理画面の操作は試していません。

:::takeaways
- **Gemini Enterpriseは社内外のデータを横断して答え、エージェントを作って配るための別契約**。Workspaceのプランには含まれない
- 公開されているシートの金額はBusinessの月額21ドルからだけ。**Standard・Plusの金額は公式の公開ページに無く、営業担当者への問い合わせになる**
- **Workspaceの中の自動化なら、WorkspaceのBusinessの全プランに込みのWorkspace Studioで足りることがある**。Microsoft 365やSalesforceのデータを読ませる・全社に配るならGemini Enterpriseが候補
:::

## Gemini Enterpriseとは

名前にGeminiが付くGoogleの会社向けの製品は、いま少なくとも4つあります。WorkspaceのプランについてくるGemini、Workspaceの中でエージェントを作るWorkspace Studio、Google CloudのGemini Enterprise、開発者向けのGemini Enterprise Agent Platformです。

<!-- SHOT: 図 gee_position.html → gee_01_position.png・alt「Googleの会社向けのGemini 4つを縦に並べた図。WorkspaceのGeminiはプランに込みでGmailやドキュメントの中で使う。Workspace StudioはWorkspaceのBusinessの全プランに込みでWorkspaceの中の作業を自動化する。Gemini Enterpriseは別の契約で社内外のデータを横断しエージェントを配る。Agent Platformは開発者向けの従量課金でエージェントを組む」 -->

[Gemini Enterpriseの製品ページ](https://cloud.google.com/gemini-enterprise?hl=ja)は、メール・ドキュメント・データ・業務アプリを横断して動くエージェントと説明し、つなぐ先にMicrosoft 365・Slack・Salesforce・BigQueryなどを挙げています。**Gmailやドライブの中で働くWorkspaceのGeminiと違い、Gemini Enterpriseは1つの画面からいくつもの社内システムに聞く入り口になります。**

前身はGoogle Agentspaceで、Googleは[2025年10月のブログ](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise)で職場のAIの入り口として発表しました。2025年まで同じ名前で売られていたWorkspaceのアドオンとは別物で、その経緯は「[Google WorkspaceのGeminiとは](/media/google-workspace-gemini/)」で扱っています。

## 何ができるか

[Businessエディションのページ](https://cloud.google.com/gemini-enterprise/business?hl=ja)のよくある質問は、含まれる機能を次のように挙げています。

| 機能 | 中身 |
|---|---|
| 社内データの検索と回答 | つないだアプリの中身のうち、本人が見られるものから答える |
| Gemini Notebook | 最大300件の社内資料から共有できるノートブックを作る |
| Deep Research | 社内データとWebを調べて出典つきのレポートを書く |
| Workflow Builder | 繰り返しの作業を任せるエージェントを文で頼んで作る |

[Workflow Builderの概要](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder?hl=ja)によると、作れるのは会話で動くチャット エージェントと、決まった手順で動くワークフローの2種類です。ワークフローには人の承認を挟めて、決まった時刻に動かす設定もできます。製品ページには一部の機能は早期アクセス版で今は使えない場合があるという注記もあり、**ページで見た機能が自社の契約で使えるかは試用の期間に確かめるほうが確実です。**

### Agent Platformとの違い

名前の似た[Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform?hl=ja)は旧Vertex AIの新しい名前で、開発者がエージェントを組んで動かす場所です。コードで組んだエージェントは、管理者がGemini Enterpriseに登録すると社員の画面に並びます。作り方の選び方は「[AIエージェントの作り方](/media/ai-agent-build/)」にまとめました。

## エディションと料金

[エディションの比較](https://docs.cloud.google.com/gemini/enterprise/docs/editions?hl=ja)（2026年10月24日更新）には5つのエディションが並びます。金額は比較の表には無く、公開ページで確かめられたのはBusinessだけでした。

| エディション | 料金 | 人数 | ストレージと索引（1人あたり） |
|---|---|---|---|
| Business | 1シート月額21ドルから | 1〜500ユーザー | 25GiB |
| Standard | 公開ページに記載なし | 1人以上 | 30GiB |
| Plus | 公開ページに記載なし | 1人以上 | 75GiB |
| 従量課金制 | 使った分だけ | 1シートから | 1GiBあたり月5ドル |
| Frontline | 公開ページに記載なし | StandardかPlusのユーザーが150人以上 | 2GiB |

<!-- SHOT: 図 gee_editions.html → gee_02_editions.png・alt「Gemini Enterpriseの4つのエディションを縦に並べた図。Businessは月額21ドルからで1〜500ユーザーと25GiB、Standardは公開ページに金額が無く1日160クエリと30GiB、Plusは公開ページに金額が無く1日200クエリと75GiB、従量課金制は使った分だけで1シートから」 -->

Businessの人数は、比較の表が1〜500ユーザー、Businessのページが最大300名までのチームと書いていて、2つのページで数字がそろっていません。Standard・Plusの金額は、2025年10月の発表を伝えた[TechCrunchの記事](https://techcrunch.com/2025/10/09/google-ramps-up-its-ai-in-the-workplace-ambitions-with-gemini-enterprise/)では年払いで1シート月額30ドルからでした。**いまの公式のページにはこの金額が無く、料金ページだったURLも開けないため、予算は営業担当者の見積もりで組むことになります。**

<!-- SHOT: 画面 https://cloud.google.com/gemini-enterprise/business?hl=ja・本文だけにある探す語「シートあたり月額」・赤枠にする語「$21～（シートあたり月額）」・PC・alt「Gemini Enterprise Businessエディションのページの冒頭。ビジネスとチームのためのAIの見出しの下に、データを管理するのはお客様でありGoogleがトレーニングに使用することはない、21ドルからシートあたり月額と書かれている」・figcaption「Gemini Enterprise Businessエディションのページ（2026年10月26日）」 -->

金額は米ドルで、税の扱いはどのページにも書かれていません。契約は月単位と年間の2つで、[ライセンスのドキュメント](https://docs.cloud.google.com/gemini/enterprise/docs/licenses?hl=ja)によると自動更新も設定できます。

### Businessで足りない線

比較の表でBusinessに印が無いのは、データコネクタの全体・外で作ったフルコードのエージェント・エンタープライズ クラスのセキュリティなどです。SalesforceやServiceNowのコネクタも、[コネクタの一覧](https://cloud.google.com/gemini-enterprise/connectors?hl=ja)ではStandard・Plusの側にだけ載っています。[Businessのサブスクリプションの管理のヘルプ](https://knowledge.workspace.google.com/admin/generative-ai/gemini-enterprise/manage-your-gemini-enterprise-business-edition-subscription?hl=ja)によると、**BusinessのチャットはVaultの監査や保持の対象にならず、データ リージョンにも対応せず、利用状況は管理コンソールのレポートに出ません。**記録の保存や監査の決まりがある会社は、最初からStandard・Plusで見積もりを取るほうが手戻りが少なくなります。

<!-- SHOT: 画面 https://knowledge.workspace.google.com/admin/generative-ai/gemini-enterprise/manage-your-gemini-enterprise-business-edition-subscription?hl=ja・本文だけにある探す語「Workspace の機能への影響」・赤枠にする語「Vault と保持」「データ所在地」・PC・alt「Workspace管理者ヘルプのBusinessエディションのサブスクリプションの管理のページ。Workspaceの機能への影響の節に、Vaultと保持では管理者がチャットの監査や保持ポリシーの設定を行えないこと、データ所在地ではデータ リージョンとデータ保護をサポートしていないことが並ぶ」・figcaption「Workspace管理者ヘルプ（2026年10月26日）」 -->

### 割り当てと超過料金

Standard・Plusのシートには1日に使える量の割り当てがあります。同じエディションのユーザー全員で共有するプールで、戻るのは太平洋時間の午前0時です。

| 1日の割り当て | Standard | Plus |
|---|---|---|
| アシスタントへの質問 | 160件 | 200件 |
| ノーコードのエージェントの作成 | 1件 | 10件 |
| Deep Research | 3回 | 10回 |
| 開発者向けツールのクレジット | 月10ドル分 | 月15ドル分 |

<!-- SHOT: 画面 https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages?hl=ja・本文だけにある探す語「Standard エディションと Plus エディションの割り当て」・赤枠にする語「1 日あたり 160 クエリ」「1 日あたり 200 クエリ」・PC・alt「Gemini Enterpriseの割り当てと超過料金のドキュメントの表。StandardとPlusの列に、ストレージとデータ インデックス作成が30GiBと75GiB、アシスタントが1日あたり160クエリと200クエリ、ノーコードのエージェント作成が1日あたり1エージェントと10エージェントと並ぶ」・figcaption「割り当てと超過料金のドキュメント（2026年10月26日）」 -->

プールを使い切ると、管理者が超過料金を有効にしていない限りその機能は止まります。有効にすると従量課金で使い続けられ、その枠で選べるモデルにはAnthropicのClaudeも入っています。[割り当てと超過料金](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages?hl=ja)と[費用の制御のドキュメント](https://docs.cloud.google.com/gemini/enterprise/docs/manage-costs-overview?hl=ja)によると、超過分を自動で止める手段はCloud Billingで決める1か月の費用の上限です。**Gemini Enterpriseのアプリは割り当てに達したときも超過料金が始まったときもメールで知らせないため、予算のアラートはCloud Billingの側で設定しておく必要があります。**

[AI番記者の解説動画](https://www.youtube.com/watch?v=_JHBwqf1XAc)は、2026年8月26日に従量課金制と利用額の約束で割り引くFlexible Savings Plansが発表されたと伝え、エージェントが処理を重ねると請求が膨らむ点を注意に挙げていました（投稿者の解説で、第三者の検証はありません）。

## WorkspaceのGeminiで足りるか

Workspaceの会社がまず確かめたいのは、追加の契約なしで手が届く範囲です。[Businessエディションの比較](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-business-editions?hl=ja)では、エージェントを作るGoogle Workspace StudioがBusiness Starter・Standard・Plusのすべてに含まれています（ドメインの所有権の証明が条件）。

<!-- SHOT: 画面 https://knowledge.workspace.google.com/admin/getting-started/editions/compare-business-editions?hl=ja・本文だけにある探す語「Google Workspace Studio」・赤枠にする語「Google Workspace Studio」の行・PC・alt「Google WorkspaceのBusinessエディションの比較の表。Google Workspace Studioの行に、Business Starter・Business Standard・Business Plusの3列ともチェックと短剣の印が付いている」・figcaption「Businessエディションの比較（2026年10月26日）」 -->

[Workspace Studioを発表したブログ](https://workspace.google.com/blog/ja/product-announcements/introducing-google-workspace-studio-agents-for-everyday-work)によると、作ったエージェントはGmail・ドライブ・Chatの中で動き、Asana・Jira・Mailchimp・Salesforceにも手順の中でつなげます。受信したメールから請求書番号を拾ってラベルを付けるような、**Workspaceの中で完結する作業の自動化なら、Gemini Enterpriseを足さずに始められます。**

<!-- SHOT: 図 gee_decide.html → gee_03_decide.png・alt「Gemini Enterpriseを足すかを決める順番の図。1はWorkspaceの中で済むか（済むならWorkspace Studio）、2はWorkspaceの外のデータを読ませるか（Microsoft 365やSalesforce）、3は作ったエージェントを全社に配って管理するか、4は監査や保存場所の決まりがあるか（あればStandardかPlus）」 -->

Gemini Enterpriseが要るのは、答えの材料がWorkspaceの外にある場合です。SharePointやSalesforce、自社のデータベースを1つの画面から横断して聞く道は、Workspaceの機能の表にありません。作ったエージェントを全社に配って1か所で管理したい場合も同じです。Workspace側の料金とプランごとの機能の差は「[Google WorkspaceのGeminiとは](/media/google-workspace-gemini/)」に書いています。

## 申し込みは2通り

Businessの申し込み方は2つあります。[Workspace管理者ヘルプ](https://knowledge.workspace.google.com/admin/generative-ai/gemini-enterprise?hl=ja)によると、Googleの営業担当者かGoogle Cloudパートナーを通す方法と、Businessのサインアップのページから自分で申し込む方法です。

| 申し込み方 | 請求とシートの管理 |
|---|---|
| 営業担当者・パートナー経由 | Google管理コンソール（admin.google.com） |
| サインアップのページから直接 | business.gemini.google |
| Google Cloudコンソール（Standard・Plus） | Cloudの請求先アカウント |

営業・パートナー経由のときは管理者がライセンスを自分に1つ割り当て、business.gemini.googleにログインして環境を初期化します。組織ですでに別のGemini Enterpriseのプランを使っていると、Businessは買えません。

Standard・PlusをGoogle Cloudコンソールで買う場合、ライセンスのドキュメントによるとセルフサービスの請求先アカウントは25シートまでです。請求書払いのアカウントは1,000シートまでで、それより多いと営業担当者を通します。**30日間の無料の試用はBusinessとPlusにあり、Plusは製品ページの［30 日間の試用を開始］から申し込めます。**

### Workspaceの契約は要るか

Gemini Enterpriseだけを使うのに、Workspaceの契約は前提になっていません。[IDプロバイダのドキュメント](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider?hl=ja)は、Google Identityのほか、Microsoft Entra IDやOktaといったほかの会社のIDプロバイダでも入れると書いています。ただしWorkspaceのデータにつなぐならGoogle Identityが必須で、IDプロバイダを途中で変えるとチャットの履歴は引き継がれません。

## 社内データへのつなぎ方

つなぎ方は3つに分かれます。Workspaceのデータは管理コンソールで許可し、ほかの会社のサービスは用意されたコネクタでつなぎ、一覧に無い自社のシステムはMCPサーバーを用意してつなぎます。

<!-- SHOT: 図 gee_data.html → gee_04_data.png・alt「Gemini Enterpriseに社内データをつなぐ3つの道を縦に並べた図。Google Workspaceは管理コンソールで許可しGoogle Identityが必須、ほかの会社のサービスは用意されたコネクタでつなぎMicrosoft 365はEntra IDとの連携が要る、自社のシステムはカスタムのMCPサーバーでつなぐ」 -->

Microsoft 365のOneDrive・Outlook・SharePoint・Teamsは、コネクタの一覧でBusinessにもStandard・Plusにも載っています。IDプロバイダのドキュメントによると、データの取り込みの方式でSharePointなどをつなぐならMicrosoft Entra IDとWorkforce Identity連携の設定が必須です。**Microsoft 365とWorkspaceを両方使う会社では、2つのIDをどうそろえるかを情シスが先に決める必要があります。**

どの方式でも、答えに使うのは社員が元のシステムで見られるものだけで、IDプロバイダのドキュメントは元のアクセス制御を飛び越えることは無いとしています。裏返すと、全社に公開されたままの人事のファイルは答えの材料になるため、共有の設定は入れる前に見直しておく必要があります。

## エージェントを誰が作って配るか

[エージェントの概要](https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview?hl=ja)によると、エージェントの出どころは社員がWorkflow Builderで作るもの・Googleが用意したもの・開発者が作って管理者が登録するものの3つです。社員が作れるかは管理者が決め、Workflow Builderは［エンドユーザー機能コントロール］で有効にしたときだけ社員の画面に出ます。[エージェントの共有のドキュメント](https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents?hl=ja)によると、配る相手の選択肢はユーザー・グループ・組織の全員などです。

Workspace側にも止める場所があります。[エージェントへのアクセスの制御のヘルプ](https://knowledge.workspace.google.com/admin/generative-ai/gemini-enterprise/control-access-to-gemini-enterprise-agents?hl=ja)によると、管理コンソールの［セキュリティ］［エージェント アクセスの制御］の既定は「許可する」です。**Gemini EnterpriseのエージェントがWorkspaceのデータに届くかは、契約の前にWorkspaceの管理者と決めておくことになります。**

## データの扱いと保存場所

入力が学習に使われない点は、Businessのページにも製品ページのよくある質問にも書かれています。製品ページによるとプロンプトや出力はGoogleや他社のモデルの学習に使われず、広告にも使われません。

保存場所はエディションで変わります。[データ所在地のドキュメント](https://docs.cloud.google.com/gemini/enterprise/docs/locations?hl=ja)によると、Standard・Plusは米国とEUのマルチリージョンを選べて、日本のasia-northeast1も許可リスト付きの一般提供です。日本を使うにはGoogleのアカウント チームへの問い合わせが要ります。Google検索のグラウンディングを有効にすると、この保存場所の約束は当てはまりません。

Standard・Plusは、[コンプライアンスのドキュメント](https://docs.cloud.google.com/gemini/enterprise/docs/compliance-security-controls?hl=ja)でISO 27001やSOC 2などの認証とVPC Service Controlsへの対応も示しています。**Businessはデータ リージョンに対応していないため、保存場所の決まりがある会社の候補はStandard・Plusになります。**

## Copilot Studioとの違い

Microsoft側で対になるのはCopilot Studioで、払い方の考え方が違います。

| 項目 | Gemini Enterprise | Copilot Studio |
|---|---|---|
| 払い方 | 1人ごとのシート（ほかに従量課金制） | テナントで買うクレジット（1パック月29,985円で25,000） |
| 社内向けのエージェント | どのエディションでも作れる | M365 Copilotのライセンスがあれば追加費用なし |

詳細は「[Copilot Studioの料金](/media/copilot-studio/)」に、土台をどちらにするかは「[CopilotとGeminiの違い](/media/copilot-vs-gemini/)」にまとめました。**社員の大半がMicrosoft 365で働いているなら、Gemini Enterpriseは土台の外から足す道具になります。**

## 入れる前に決めること

<!-- SHOT: 画面 https://knowledge.workspace.google.com/admin/generative-ai/gemini-enterprise/turn-gemini-enterprise-on-or-off-for-users?hl=ja・本文だけにある探す語「ライセンスを取得する」・赤枠にする語「Gemini Enterprise は Google Workspace サブスクリプションに含まれていません」・PC・alt「Workspace管理者ヘルプのユーザーに対してGemini Enterpriseを有効または無効にするのページ。ライセンスを取得するの節に、Gemini EnterpriseはGoogle Workspaceサブスクリプションに含まれていない、ライセンスを購入する必要があると書かれている」・figcaption「Workspace管理者ヘルプ（2026年10月26日）」 -->

ライセンスを買う前に決めておきたいのは次の3つです。

1. **任せる業務を1つに絞る**：Workspaceの中で済むならWorkspace Studioで試し、外のデータが要る業務だけをGemini Enterpriseの試用に回す
2. **エディションを記録の決まりで選ぶ**：Vaultの保持や保存場所の決まりがあればBusinessは外し、Standard・Plusの見積もりを取る
3. **費用の止め方を決める**：超過料金を有効にするか、Cloud Billingの費用の上限とアラートを誰が受けるか

Workspaceの組織では、管理コンソールの［生成 AI］［Gemini Enterprise］でオンとオフを切り替え、組織部門やグループで使える人を分けます。反映には最長で24時間かかります。

## よくある質問

### Gemini Enterpriseの料金はいくらですか？

Businessエディションのページは、1シートあたり月額21ドルからと表示しています（2026年10月26日）。Standard・Plusの金額は公式の公開ページに無く、営業担当者への問い合わせです。

### Gemini Enterpriseは無料で試せますか？

BusinessとPlusに30日間の無料の試用があり、Businessは仕事用のメールアドレスで始められます。

### Gemini Enterpriseは別契約ですか？

別の契約です。Workspaceの管理者ヘルプは、Google Workspaceのサブスクリプションに含まれず、ライセンスを買う必要があると書いています。

### Gemini EnterpriseとGeminiの違いは？

WorkspaceのプランについてくるGeminiはGmailやドキュメントの中で働き、プランの料金に込みです。Gemini Enterpriseは別の契約で、Microsoft 365やSalesforceなどWorkspaceの外のデータも横断し、作ったエージェントを配って管理します。

### Gemini EnterpriseはM365とつながる？

つなげます。OneDrive・Outlook・SharePoint・TeamsのコネクタがBusinessにもStandard・Plusにもあり、データの取り込みの方式ならMicrosoft Entra IDとの連携の設定が前提です。

### Gemini Enterpriseは学習に使われますか？

使われません。製品ページとBusinessのページは、プロンプトや出力がGoogleや他社のモデルの学習に使われないと書いています。

### Gemini Enterpriseは日本に保存できる？

Standard・Plusなら、Googleのアカウント チームに問い合わせて日本のasia-northeast1を許可リスト付きで選べます。Businessはデータ リージョンに対応していません。

### Gemini Enterpriseのログイン先は？

Businessエディションはbusiness.gemini.googleです。Standard・Plusは、管理者がGoogle Cloudコンソールで作ったGemini Enterpriseのウェブアプリから入ります。

## 出典

- Google Cloud「[Gemini Enterprise](https://cloud.google.com/gemini-enterprise?hl=ja)」
- Google Cloud「[Gemini Enterprise Business エディション](https://cloud.google.com/gemini-enterprise/business?hl=ja)」
- Google Cloud「[Gemini Enterprise のコネクタ](https://cloud.google.com/gemini-enterprise/connectors?hl=ja)」
- Google Cloud ドキュメント「[Gemini Enterprise のエディション比較](https://docs.cloud.google.com/gemini/enterprise/docs/editions?hl=ja)」
- Google Cloud ドキュメント「[Gemini Enterprise のサブスクリプションを取得してライセンスを割り当てる](https://docs.cloud.google.com/gemini/enterprise/docs/licenses?hl=ja)」
- Google Cloud ドキュメント「[割り当てと超過料金](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages?hl=ja)」
- Google Cloud ドキュメント「[超過料金と費用の制御の概要](https://docs.cloud.google.com/gemini/enterprise/docs/manage-costs-overview?hl=ja)」
- Google Cloud ドキュメント「[ID プロバイダを構成する](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider?hl=ja)」
- Google Cloud ドキュメント「[データ所在地](https://docs.cloud.google.com/gemini/enterprise/docs/locations?hl=ja)」
- Google Cloud ドキュメント「[コンプライアンス認証とセキュリティ管理](https://docs.cloud.google.com/gemini/enterprise/docs/compliance-security-controls?hl=ja)」
- Google Cloud ドキュメント「[エージェントの概要](https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview?hl=ja)」「[Workflow Builder の概要](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder?hl=ja)」「[エージェントを共有する](https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents?hl=ja)」
- Google Workspace 管理者ヘルプ「[Gemini Enterprise - Business エディションを追加して設定する](https://knowledge.workspace.google.com/admin/generative-ai/gemini-enterprise?hl=ja)」「[ユーザーに対して Gemini Enterprise を有効または無効にする](https://knowledge.workspace.google.com/admin/generative-ai/gemini-enterprise/turn-gemini-enterprise-on-or-off-for-users?hl=ja)」「[Business エディションのサブスクリプションを管理する](https://knowledge.workspace.google.com/admin/generative-ai/gemini-enterprise/manage-your-gemini-enterprise-business-edition-subscription?hl=ja)」「[Gemini Enterprise エージェントへのアクセスを制御する](https://knowledge.workspace.google.com/admin/generative-ai/gemini-enterprise/control-access-to-gemini-enterprise-agents?hl=ja)」
- Google Workspace 管理者ヘルプ「[Business エディションの比較](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-business-editions?hl=ja)」
- Google Workspace ブログ「[Google Workspace Studio のご紹介](https://workspace.google.com/blog/ja/product-announcements/introducing-google-workspace-studio-agents-for-everyday-work)」（2025年12月10日）
- Google Cloud ブログ「[Introducing Gemini Enterprise](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise)」（2025年10月10日）
- TechCrunch「[Google ramps up its AI-in-the-workplace ambitions with Gemini Enterprise](https://techcrunch.com/2025/10/09/google-ramps-up-its-ai-in-the-workplace-ambitions-with-gemini-enterprise/)」（2025年10月9日）
- Google Cloud「[Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform?hl=ja)」
