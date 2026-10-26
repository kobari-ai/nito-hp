---
title: 【2026年10月】Difyの料金を解説｜プランの選び方・API代・セルフホスト
date: 2026-10-27
category: AI活用
description: Difyの料金を公式の料金ページ・利用規約・ライセンスから解説。クラウド版3プランの違い、クレジットの減り方、モデルのAPI代の見積もり、セルフホストとEnterpriseの条件、商用利用の注意まで。
cover_tag: 導入担当向け
cover_headline: Difyの料金
cover_sub: プランの選び方・API代・セルフホスト
cta: ai_agent
---

Difyのクラウド版はProfessionalが月59ドル、Teamが月159ドルで、どちらもワークスペースごとの料金です。人数で月額は増えませんが、モデルを呼ぶ代金は別にかかります。

社内のチャットボットやエージェントをDifyで作る話が出ると、担当者は年間の予算とプランを聞かれます。この記事は2026年10月27日に取得した料金ページ・利用規約・ライセンスをもとに、プランの選び方とAPI代の見積もり、セルフホストとEnterpriseの条件を扱います。契約とセルフホストの構築は試していません。

:::takeaways
- **クラウド版はワークスペースごとの月額で、Professionalは月59ドルで3人まで、Teamは月159ドルで50人まで**。税は別で、請求書払いはまだ無い
- **付いてくるクレジットはモデルによって減り方が違い、月5,000でもGPT-5.5なら200回分**。本番は自社のAPIキーで各社に払う前提で見積もる
- **セルフホストのコミュニティ版は無料だが、サーバーと更新の人手は自社持ち**。顧客ごとにワークスペースを分けて売るなら商用ライセンスが要る
:::

## Difyの費用は3つに分かれる

Difyはチャットボット・ワークフロー・エージェントを画面上で組み立てる開発基盤で、開発元は米国のLangGenius, Inc.です。ソースは[GitHubのリポジトリ](https://github.com/langgenius/dify)で公開されていて、スターは約16万あります。作る手順は「[AIエージェントの作り方](/media/ai-agent-build/)」のノーコードの節で扱いました。

会社でDifyを使うときの費用は次の3つです。

| 費用 | 中身 | 払う先 |
|---|---|---|
| Difyの利用料 | クラウド版の月額か、Enterpriseのライセンス | LangGeniusか販売店 |
| モデルのAPI代 | OpenAI・Anthropic・Googleなどのモデルを呼ぶ代金 | 各モデルの提供元 |
| 運用の人手とサーバー | セルフホストのサーバー・更新・バックアップ | 自社とクラウド事業者 |

**月額のプラン料金だけで予算を組むと、モデルの代金と運用の人手が抜け落ちます。** クラウド版なら3つ目はほぼ要りませんが、2つ目はどのプランでも残ります。

<figure class="post-figure"><img src="/media/images/dify-pricing/dfy_01_cost.png" alt="Difyにかかる費用3つを縦に並べた図。Difyの利用料はクラウド版の月額かEnterpriseのライセンス、モデルのAPI代はOpenAIやAnthropicなど各社に払う、運用の人手とサーバーはセルフホストのときに自社が持つ" loading="lazy"></figure>

## クラウド版の3プランとEnterpriseの料金

[Difyの料金ページ](https://dify.ai/jp/pricing)は、クラウド版の3プランと、セルフホスト向けのEnterpriseとコミュニティ版を並べています。金額はドル建ての税抜きで、税は支払いの画面で足される場合があると書かれています。

| プラン | 料金（税抜き） | メンバー | アプリ | クレジット | ナレッジ |
|---|---|---|---|---|---|
| Sandbox | 無料 | 1人 | 5個 | 200（一度きり） | 50文書・50MB |
| Professional | 月59ドル（年払い590ドル） | 3人 | 50個 | 月5,000 | 500文書・5GB |
| Team | 月159ドル（年払い1,590ドル） | 50人 | 200個 | 月10,000 | 1,000文書・20GB |
| Enterprise | 問い合わせ | 記載なし | 記載なし | 記載なし | 記載なし |

**料金は「ワークスペースごと」で、Teamなら50人まで同じ月159ドルです。** 年払いにすると1年でProfessionalは118ドル、Teamは318ドル安くなり（月あたり約49ドル・約133ドル）、ページの表示は年払いで17%お得です。1ドル157.45円（欧州中央銀行の参照レート、2026年10月26日）で換算すると、Professionalは月約9,300円、Teamは月約2万5千円です。年払いならTeamは1年で約25万円になります。

<figure class="post-figure"><img src="/media/images/dify-pricing/dfy_pricing.png" alt="Difyの料金ページのクラウド版。プロフェッショナルはワークスペースごとに年590ドルで5,000メッセージクレジットとメンバー3名、チームは年1,590ドルで10,000クレジットとメンバー50名" loading="lazy"><figcaption>Difyの料金ページ（2026年10月27日）</figcaption></figure>

人数とアプリの数のほかにも、プランで変わる機能があります。料金ページの比較の表から抜き出すと次のとおりです。

| 機能 | Sandbox | Professional | Team |
|---|---|---|---|
| ロール管理（オーナー・管理者・エディター・一般） | なし | あり | あり |
| WebAppのロゴとUIの変更 | なし | なし | あり |
| SOC Type IIレポート | なし | なし | あり |
| ログの保存 | 30日 | 無制限 | 無制限 |
| サポート | コミュニティ | 優先メール | 優先メール |

社内の情報システムの審査でSOC 2の報告書を求められる会社は、TeamかEnterpriseが候補になります。

<figure class="post-figure"><img src="/media/images/dify-pricing/dfy_02_plans.png" alt="Difyクラウド版の3プランを縦に並べた図。Sandboxは無料で1人・5アプリ・200クレジットが一度きり、Professionalは月59ドルで3人・50アプリ・月5,000クレジット、Teamは月159ドルで50人・200アプリ・月10,000クレジット" loading="lazy"></figure>

## 支払いと契約の決まり

経理で引っかかりやすいのは支払い方法です。[クラウド版の料金ページ](https://dify.ai/jp/pricing/dify-cloud)のよくある質問は、個人のクレジットカードの代わりに法人口座で払えるかという問いに、**銀行振込の請求書払い（Pay by Invoice）は検討中で、まだ使えない**と答えています。検討中の案もTeamの年払いだけが対象で、請求はLangGenius, Inc.から、米国外からは海外送金で手数料は利用者の負担です。

<figure class="post-figure"><img src="/media/images/dify-pricing/dfy_invoice.png" alt="Dify Cloudの料金ページのよくある質問。法人口座で払えるかの問いに、銀行振込による請求書払いは検討中でまだ使えず、検討中の案はTeamプランの年払いだけと答えている" loading="lazy"><figcaption>Dify Cloudの料金ページのよくある質問（2026年10月27日）</figcaption></figure>

契約の条件は[利用規約](https://dify.ai/legal/terms-of-service)（2026年6月30日更新）に書かれています。稟議に書いておきたいのは次の5つです。

- 支払った料金は原則として返金されない
- 解約しなければ同じ期間で自動更新され、解約は今の期間の終わりに効く
- 料金は改定されることがあり、使っているプランの値上げは30日前に通知される
- クレジットや枠はプランに書かれていない限り、期間を越えて繰り越さない
- 税はDifyの所得税を除いて利用者の負担

もう1つ、よくある質問は**Professionalで上限に達したときにストレージやメンバーの枠だけを買い足せるかという問いに、上位のプランへの切り替えを勧めています。** Teamでも足りない場合はsupport@dify.aiに問い合わせるよう書かれています。 4人目が加わる時点でTeamに上がる計算です。請求書と領収書はオーナーと管理者が設定の請求の画面からダウンロードできます。

## メッセージクレジットの減り方

プランに付くメッセージクレジットは、料金ページの説明では「さまざまなモデルを簡単に試すため」のものです。AIが1回答えるごとに減る量は、よくある質問にモデル別で載っています。

| モデル | 1回の応答で減る量 | 月5,000で答えられる回数 |
|---|---|---|
| GPT-5.5 | 25 | 200回 |
| Claude Opus 4.7 | 20 | 250回 |
| Claude Sonnet 4.6・Gemini 3.5 Flash | 10 | 500回 |
| Claude Haiku 4.5・GPT-5 | 5 | 1,000回 |
| GPT-5-mini・Gemini 2.5 Flash | 1 | 5,000回 |

**同じ5,000クレジットでも、GPT-5.5なら200回、GPT-5-miniなら5,000回で尽きます。** Sandboxの200クレジットは、[Difyのクイックスタート](https://docs.dify.ai/en/quick-start)によると一度きりの付与で、毎月は戻りません。GPT-5.5で試すと8回で使い切る量です。

<figure class="post-figure"><img src="/media/images/dify-pricing/dfy_03_credits.png" alt="月5,000クレジットで答えられる回数の図。GPT-5.5は1回25で200回、Claude Sonnet 4.6は1回10で500回、Claude Haiku 4.5は1回5で1,000回、GPT-5-miniは1回1で5,000回" loading="lazy"></figure>

使い切った後は、自社で契約したモデルのAPIキーをDifyに登録して続けます。費用の都合でクレジットでは使えないモデルがあることも、よくある質問に書かれています。一覧には埋め込み（ナレッジを検索できる形にする処理）のモデルも載っているため、ナレッジを多く入れる使い方では、応答の回数だけで減り方を読まないほうが安全です。

<figure class="post-figure"><img src="/media/images/dify-pricing/dfy_credit_faq.png" alt="Dify Cloudの料金ページのよくある質問。メッセージクレジットはモデルごとに1回の応答で減る量が違い、GPT-5.5は25クレジット、Claude Sonnet 4.6は10クレジットと並ぶ" loading="lazy"><figcaption>メッセージクレジットの使い方（2026年10月27日）</figcaption></figure>

## モデルのAPI代の見積もり方

自社のAPIキーを使う分は、Difyではなく各モデルの提供元から請求されます。代金はトークン（文字の単位）の数で決まるので、次の掛け算で見積もれます。

- 1回の代金：入力のトークン数×入力の単価＋出力のトークン数×出力の単価
- 月の代金：1回の代金×使う人数×1日の回数×営業日

社内の文書から答えるチャットボットでは、質問に加えてナレッジから引いた文書も入力に足されます。そこで1回を入力3,000トークン・出力500トークンと置き、50人が1日10回、月20日使う場合で試算しました。単価は[Anthropicの料金ページ](https://platform.claude.com/docs/ja/about-claude/pricing)の100万トークンあたりの値です。

| モデル | 単価（入力・出力） | 1回 | 月10,000回 |
|---|---|---|---|
| Claude Sonnet 4.6 | 3ドル・15ドル | 約0.017ドル | 約165ドル（約2万6千円） |
| Claude Haiku 4.5 | 1ドル・5ドル | 約0.006ドル | 約55ドル（約8,700円） |

**この使い方ではTeamに付く月10,000クレジットはSonnet 4.6で1,000回分にとどまり、使い切った後の9,000回はAPI代になります。** 入力の長さは引く文書の量で大きく変わるため、試作のアプリで実際の質問を流し、提供元の管理画面で1回のトークン数を確かめてから掛け算すると見積もりが外れにくくなります（こちらでは試していません）。

データの扱いも費用と一緒に確かめます。LangGeniusはやり取りのデータを学習に使わないと、Difyの[プライバシーポリシー](https://dify.ai/privacy)に書かれています。自社のAPIキーを使うと、データは選んだ提供元へ直接送られ、学習に使われるかはその提供元との契約で決まります。

## プランを決める4つの条件

プランの差は月額よりも上限の差です。次の4つを順に当てはめると、候補が1つか2つに絞れます。

- **データを社外のクラウドに置けるか**：置けないならクラウド版は外れ、セルフホストかEnterpriseになる
- **Difyにログインして作る人は何人か**：1人で試すだけならSandbox（200クレジットは一度きり、アプリは5個まで）、本番で使うなら3人までProfessional、50人までTeam
- **アプリとナレッジの量**：50アプリ・500文書・5GBを超えるならTeam
- **管理の要件**：役割の分担はProfessionalから、自社のロゴとSOC 2の報告書はTeam、SSOはEnterpriseだけ

<figure class="post-figure"><img src="/media/images/dify-pricing/dfy_04_choose.png" alt="Difyのプランを決める4つの条件を順に並べた図。データを社外に置けるか、作る人は何人か、アプリとナレッジの量、SSOやロゴなど管理の要件" loading="lazy"></figure>

メンバーの数に、公開したWebアプリを使うだけの社員が入るかは、料金ページに書かれていません。部署ごとに分けて作りたい場合も、クラウド版はどのプランも1ワークスペースなので、ワークスペースの数だけ契約も増える計算です。複数の部署で1つの管理にまとめたいなら、複数のワークスペースを持てるEnterpriseの見積もりを並べて比べます。

## セルフホストにかかる費用

コミュニティ版は無料で、料金ページでは単一のワークスペースで、Dify Open Source Licenseに従うと書かれています。[Docker Composeでの構築のドキュメント](https://docs.dify.ai/ja/self-host/quick-start/docker-compose)の最小要件はCPU 2コア・メモリ4GiBで、起動すると、api・worker・webなど7つの中核のサービスに、データベース・Redis・ベクトルデータベースなど8つの部品が加わり、15のコンテナが動く構成です。

ライセンス料がかからない代わりに、次の費用は自社で持ちます。

| 費用 | 中身 |
|---|---|
| サーバー | 最小要件を満たすサーバーかクラウドの仮想マシン、保存領域 |
| モデルのAPI代 | クラウド版のクレジットは無いので、最初から自社のキーで払う |
| 更新の人手 | リリースによって手順が異なる場合があり、設定ファイルの差分を自分で当て直す |
| 守りの人手 | バックアップ・認証・脆弱性への対応 |

**更新は一度きりの作業ではないため、人手の見積もりに入れておくのが安全です。** 最新のリリースは2026年10月23日の1.18.0で、ドキュメントはアップグレードのたびに環境変数の見本と自社の設定を見比べるよう書いています。

<figure class="post-figure"><img src="/media/images/dify-pricing/dfy_selfhost_req.png" alt="DifyのドキュメントのDocker Composeでのデプロイのページ。デプロイ前の準備の節に、ハードウェアの最小要件としてCPU 2コア以上とRAM 4GiB以上が並ぶ" loading="lazy"><figcaption>Dify DocsのDocker Composeでのデプロイ（2026年10月27日）</figcaption></figure>

セルフホストが向くのは、データを自社の環境から出せない決まりがあり、サーバーの面倒を見る人がいる会社です。クラウド版のデータの置き場所について、料金ページはマネージドクラウドリージョンとだけ書き、プライバシーポリシーはウェブサイトのサーバーが米国にあるとしています。国内に置く決まりがあるなら、クラウド版より先にセルフホストを検討することになります。

## ライセンスで気をつけること

コミュニティ版のライセンスは、[DifyのLICENSE](https://github.com/langgenius/dify/blob/main/LICENSE)にあるApache License 2.0を改めたものです。ほかのアプリのバックエンドや企業のアプリ開発基盤としての利用も含め、商用での利用は認められています。そのうえで、次の2つに当たると商用ライセンスが要ります。

- **マルチテナント**：書面の許可なく、Difyのソースでマルチテナントの環境を運用できない。テナントは1つのワークスペースを指す
- **ロゴと著作権の表示**：Difyのフロントエンドを使う場合、コンソールやアプリのロゴと著作権の表示を消したり変えたりできない

<figure class="post-figure"><img src="/media/images/dify-pricing/dfy_license.png" alt="DifyのLICENSEファイル。商用利用は認めたうえで、書面の許可なくマルチテナント環境を運用できないこと、フロントエンドを使う場合はロゴと著作権の表示を消せないことを条件にしている" loading="lazy"><figcaption>GitHubのDifyのLICENSE（2026年10月27日）</figcaption></figure>

会社の使い方に当てはめると、次のように読めます。

| 使い方 | ライセンスの文言との関係 |
|---|---|
| 社内向けに1つのワークスペースで使う | 商用利用として認められている範囲 |
| 自社サービスの裏側でDifyのAPIを呼ぶ | バックエンドとしての利用が明記されている |
| 顧客ごとにワークスペースを分けて提供する | マルチテナントに当たり、書面の許可が要る |
| 画面のロゴを自社のものに替える | フロントエンドを使うなら許可が要る |

この表はライセンスの文言を読んだもので、法的な判断ではありません。受託で作って顧客に納める場合など、当てはまるか迷うときは、Enterpriseのページにある問い合わせ先（business@dify.ai）に書面で確かめておくと後で揉めません。

## Enterpriseと国内の窓口

[Enterpriseのページ](https://dify.ai/jp/pricing/dify-enterprise)の金額は「Custom」で、問い合わせて見積もりを取ります。含まれるのは商用ライセンス、複数のワークスペース、SSO（SAML・OIDC・OAuth2）、高可用性の構成、パートナーによるSLA、公式の更新と保守、技術サポートです。よくある質問によると、表示の料金はプランの中心の機能だけで、追加の機能・連携・専任のサポート・構築は別に見積もります。条件を満たすオープンソースのプロジェクト・教育機関・NGOには特別な価格があり、条件と割引の中身は問い合わせて確かめます。

<figure class="post-figure"><img src="/media/images/dify-pricing/dfy_enterprise.png" alt="DifyのEnterpriseのページ。コミュニティ版は無料で単一ワークスペース、Enterpriseは個別見積もりで商用ライセンス・複数ワークスペース・SSO・パートナーによるSLAを含む" loading="lazy"><figcaption>Dify Enterpriseのページ（2026年10月27日）</figcaption></figure>

国内では[リコージャパン](https://www.ricoh.co.jp/products/list/dify)がライセンスの販売と構築を受けています。ライセンスはコミュニティ・Essential（ワークスペース3・ユーザー20名）・Standard（ワークスペース10・ユーザー100名）・Enterpriseで、価格は問い合わせです。学校などの教育機関向けには、Enterpriseのアカデミックライセンスもあります。EssentialとStandardは[2026年6月1日に提供が始まりました](https://digitalpr.jp/r/135862)。国内の会社と契約したい場合は、販売店を通す道もあります。

もう1つ、Difyは[AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-t22mebxzwjhu6)で、自社のAWS環境に1社専用で立てるDify Premiumも出しています。[Dify Premiumのドキュメント](https://docs.dify.ai/en/self-host/deploy/platform-guides/dify-premium)によると、自社のAWSのVPCにEC2として立て、「Powered by Dify」の表示を消したり自社のロゴに替えたりできます。金額はリスティングの画面に出ますが、こちらでは読めていません。

見積もりを頼むときはワークスペースの数・使う人数・SSOの方式・SLAの要否・構築を誰が持つかをそろえて出すと、販売店どうしを比べやすくなります。

## Copilot StudioやGeminiとの違い

同じ「社内でエージェントを作る」道具でも、払い方の単位が違います。

| 製品 | 払い方 | 向く会社 |
|---|---|---|
| Dify（クラウド版） | ワークスペースごとの月額とモデルのAPI代 | モデルを選びたい・自社のサーバーにも置きたい |
| Copilot Studio | テナントで買うクレジット（1パック月29,985円で25,000） | 社員の大半がMicrosoft 365で働いている |
| Gemini Enterprise | 1人ごとのシート（Businessは月21ドルから） | Google Workspaceが土台 |

**Difyは人数で月額が増えない代わりに、モデルの代金を自分で見積もる必要があります。** それぞれの料金は「[Copilot Studioの料金](/media/copilot-studio/)」と「[Gemini Enterpriseとは](/media/gemini-enterprise/)」にまとめました。

## よくある質問

金額はすべて、2026年10月27日に見た公式ページの税抜きの表示です。

### Difyは無料で使えますか？

使えます。クラウド版のSandboxは無料で、メンバー1人・アプリ5個・200クレジット（一度きり）までです。セルフホストのコミュニティ版も無料ですが、サーバー代とモデルのAPI代は自社で払います。

### Difyの料金は1人いくらですか？

1人ごとの料金はありません。クラウド版はワークスペースごとで、Professionalは月59ドルで3人まで、Teamは月159ドルで50人までです。

### DifyのProfessionalとTeamの違いは？

メンバーはProfessionalが3人・Teamが50人、アプリは50個と200個、クレジットは月5,000と月10,000です。WebAppのロゴの変更とSOC Type IIレポートはTeamだけにあります。

### Difyの料金にAPI代は含まれますか？

付いてくるクレジットの範囲だけ含まれます。使い切った後や、クレジットで使えないモデルは、自社のAPIキーを登録して各社に払います。

### Difyは請求書払いできますか？

クラウド版はまだできません。料金ページのよくある質問は、銀行振込の請求書払いを検討中で、案ではTeamの年払いだけが対象と書いています。

### Difyを商用利用できますか？

できます。ただしコミュニティ版で顧客ごとにワークスペースを分けて提供する場合と、フロントエンドのロゴや著作権の表示を変える場合は、書面の許可が要ります。

### Dify Enterpriseの価格はいくらですか？

公開されていません。Enterpriseのページは「Custom」で、Difyかリコージャパンなどの販売店に見積もりを頼みます。

### Difyのデータは学習に使われますか？

LangGeniusはやり取りのデータを学習に使わないと、プライバシーポリシーに書かれています。自社のAPIキーを使う場合の扱いは、モデルの提供元との契約で決まります。

## 出典

- Dify「[料金](https://dify.ai/jp/pricing)」「[Dify Cloudの料金](https://dify.ai/jp/pricing/dify-cloud)」「[Dify Enterpriseの料金](https://dify.ai/jp/pricing/dify-enterprise)」
- Dify「[Terms of Service](https://dify.ai/legal/terms-of-service)」（2026年6月30日更新）「[Privacy Policy](https://dify.ai/privacy)」
- GitHub「[langgenius/dify](https://github.com/langgenius/dify)」「[LICENSE](https://github.com/langgenius/dify/blob/main/LICENSE)」
- Dify Docs「[Docker Compose で Dify をデプロイする](https://docs.dify.ai/ja/self-host/quick-start/docker-compose)」「[30-Minute Quick Start](https://docs.dify.ai/en/quick-start)」
- Anthropic「[料金](https://platform.claude.com/docs/ja/about-claude/pricing)」
- リコージャパン「[Dify](https://www.ricoh.co.jp/products/list/dify)」、リコー「[Dify Essential/Standardライセンスと、Difyアプリケーションの無償テンプレートを提供開始](https://digitalpr.jp/r/135862)」
- AWS Marketplace「[Dify Premium](https://aws.amazon.com/marketplace/pp/prodview-t22mebxzwjhu6)」
- 為替は[Frankfurter](https://frankfurter.dev/)で取得した欧州中央銀行の参照レート
