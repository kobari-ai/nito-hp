---
title: 【2026年10月】Claudeの法人契約の方法を解説｜請求書払い・AWS経由・代理店・稟議の準備
date: 2026-10-23
category: AI活用
description: Claude（Claude Codeを含む）を会社で契約する方法を、公式の料金ページと規約で経路ごとに整理。Teamのウェブ申し込み、営業担当経由のEnterprise、AWSなどクラウド経由、国内パートナー、学習の扱いと稟議の準備まで。
cover_tag: 導入担当向け
cover_headline: Claudeの法人契約
cover_sub: 申し込みの経路・支払い・稟議の準備
cta: ai_agent
---

Anthropicの[料金ページ](https://claude.com/ja/pricing)の比較表では、会社でClaudeを契約する入口がTeam・Enterprise（セルフサービス）・Enterprise（営業担当経由）の3列に分かれています。2026年10月23日に開いたとき、請求書払いとAWS Marketplaceでの提供に「はい」が付いていたのは営業担当経由の列だけでした。

稟議を書く担当者が迷うのは、どの経路なら社内の支払いと契約の決まりに通るかです。この記事は経路ごとに、支払い・契約の相手と規約・学習の扱い・Claude Codeの含め方・稟議で用意するものを並べます。

:::takeaways
- **カードでその場で申し込めるのはTeamとセルフサービスのEnterprise**。請求書払いは営業担当経由のEnterpriseか、AWSなどクラウドの請求に載せる経路になる
- 直接契約の相手は東京の拠点ではなく**米国のAnthropic, PBC**で、商用規約とデータ処理補遺（DPA）が同意と同時に適用される
- 会話は既定で学習に使われないが、**評価ボタンで送ったフィードバックは例外で、オーナーが組織ごと止められる**
:::

## 法人契約の経路は5つ

社員が個人でProやMaxを契約し、経費で落とす使い方は法人契約に入りません。Claude Codeの[法的および規制対応のページ](https://code.claude.com/docs/ja/legal-and-compliance)は、Free・Pro・Maxを消費者向けの利用規約、Team・Enterprise・APIを商用規約の対象と分けています。**会社として契約するなら、商用規約が適用される経路から選びます。**公式のページに出てくる経路を申し込み先と支払いで並べると、次の5つです。

<figure class="post-figure"><img src="/media/images/claude-corporate-contract/ccc_01_routes.png" alt="Claudeの法人契約の5つの経路を縦に並べた図。上からTeam、セルフサービスのEnterprise、営業担当経由のEnterprise、AWS MarketplaceのEnterprise、クラウドのAPI" loading="lazy"></figure>

| 経路 | 申し込み先 | 支払い | 席の数 |
|---|---|---|---|
| Team | 料金ページからウェブで | カード（月払い・年払い） | 2〜150席 |
| Enterprise（セルフサービス） | 料金ページからウェブで | カード・ACH（米ドル・年払い） | 20席から |
| Enterprise（営業担当経由） | 購買エージェントか営業チーム | 請求書・振込・カード | 50席から |
| AWS MarketplaceのEnterprise | AWSのコンソール | AWSの請求書 | 20席から（追加は1席から） |
| クラウドのAPI | Bedrock・Agent Platform・Foundry | 各クラウドの請求書 | 席なし（使った分） |

上の4つは社員がブラウザやアプリでClaudeと会話する席を買う契約です。5つ目はモデルを呼び出した分だけを払う経路で、チャットの画面は付きません。社内のシステムに組み込むか、Claude Codeをクラウドの認証で動かす使い方になります。プランの機能と料金は[Claude Teamプランの記事](/media/claude-team/)と[Claude Enterpriseの記事](/media/claude-enterprise/)、個人プランは[Claudeの料金の記事](/media/claude-pricing/)にまとめています。

## Teamをウェブで申し込む

Teamは料金ページの「Team plan を申し込む」から始めます。[チームプラン請求に関するよくある質問](https://support.claude.com/ja/articles/12997503)によると、支払いはクレジットカード・デビットカード・プリペイドカードだけで、ACH銀行振込などほかの方法は受け付けていません。**社内の決まりで請求書払いしか使えないなら、Teamは候補から外れます。**会社のカードで払えるなら、2人から始められるいちばん軽い経路です。

請求は請求サイクルの始めに、その時点の人数分が登録したカードに課金されます。途中で人や席を足した分は按分ですぐに請求され、メンバーを外しても返金はありません。請求書の宛名を会社名にするには、オーナーが組織設定 > 請求で支払い方法を更新するときに「請求書に別の名前を使用する」にチェックを入れます。請求先のメールアドレスの変更はサポートへの依頼で、組織のオーナーの承認が要ります。

この記事では申し込みの画面までは試していません。宛名と消費税の表示は[Claudeの領収書と請求書の記事](/media/claude-invoice/)、招待と役割は[Claude Teamのメンバー管理の記事](/media/claude-team-admin/)で扱っています。

## Enterpriseを営業経由で契約する

[エンタープライズプランとは何ですか？](https://support.claude.com/ja/articles/9797531)によると、セルフサービスと営業担当経由のEnterpriseは機能も席の単価も同じです。違うのは買い方・払い方・管理の仕方で、請求書払いと複数の通貨に対応するのは営業担当経由だけです。セルフサービスは米ドルだけで、使用量は前払いのクレジットから引かれます。

**営業担当経由では席の料金が年の初めに請求され、使用量は月ごとの後払いで、請求書はメールで届きます。**[Enterpriseの請求方法のヘルプ](https://support.claude.com/ja/articles/11526368)では、シートの請求書も使用量の請求書も支払いリンク付きで請求担当者に送られ、支払い条件は請求書に書かれます。払い方は銀行振込（ACHか海外送金）かカードで、5万ドル以上の請求書は振込だけです。料金ページの比較表でも、トライアル・コンサルテーション・AWS Marketplaceでの提供に「はい」が付くのは営業担当経由の列だけです。

問い合わせの入口は人数で変わります。[営業担当に問い合わせるページ](https://claude.com/ja/contact-sales)は、営業チームが受け持つのは500シート以上の導入やBaaSのような複雑な取引だけと書き、それ以外は購買エージェントとのチャットで見積もりを受けるよう案内しています。ヘルプが示す営業担当経由の最低席数は50席なので、**50〜499席の会社はまず購買エージェントのチャットから入る**ことになります。チャットから必要に応じて営業チームに引き継がれることも、同じページに書かれていました。

<figure class="post-figure"><img src="/media/images/claude-corporate-contract/ccc_03_contact.png" alt="Claudeの営業担当に問い合わせるページ。購買エージェントとのチャットで見積もりと購入ができ、営業チームが対応するのは500シート以上の導入やBaaSなどの複雑な取引だけと書かれている" loading="lazy"><figcaption>営業担当に問い合わせるページ（2026年10月23日、スマホ表示）</figcaption></figure>

## AWSやGoogle Cloudの請求に載せる

会社がすでにAWS・Google Cloud・Azureと契約しているなら、Claudeの費用をその請求書に載せる経路もあります。[Claude on AWSのページ](https://claude.com/ja/partners/claude-on-aws)は、AWSでの入口をClaude Platform on AWS（API）・Amazon Bedrock（API）・AWS MarketplaceのClaude Enterprise（アプリ）の3つに分けています。社員がチャットで使う席を買えるのは、このうちAWS Marketplaceだけです。

### AWS MarketplaceのEnterprise

[AWS Marketplaceの掲載ページ](https://aws.amazon.com/marketplace/pp/prodview-nnvi6wff6ef6m)では販売者がAnthropicで、12か月の契約に20席が入った単位が4,800ドルです。1席あたり月20ドルで、料金ページのEnterpriseの席の料金と同じ額になります。使用量はAPIの料金で上乗せされ、足した席は残りの期間の日割りで請求されます。条件を変えた見積もりは、ページの「Request Private Offer」から頼みます。

[Enterpriseの請求方法のヘルプ](https://support.claude.com/ja/articles/11526368)によると、AWS Marketplaceで買ったEnterpriseは、支払いをAWSを通します。AWSの掲載ページでは、席の料金は契約の条件に沿って前払いか分割で払い、後払いになるのは使用量です。[AWS Japanの税務ヘルプ](https://aws.amazon.com/jp/tax-help/japan/)では、2025年4月1日から日本の住所のAWSアカウント向けのマーケットプレイスの運営者がアマゾン ウェブ サービス ジャパン合同会社になり、10%の消費税を徴収して適格請求書を出しています。**海外の会社への送金を社内で通しにくい場合も、AWSの請求書にまとめて払えます。**

### BedrockとAgent PlatformとFoundry

Amazon Bedrock・Google CloudのAgent Platform（旧Vertex AI）・Microsoft Foundryは、モデルをAPIで使った分を各クラウドの請求書で払う経路です。[Microsoft Foundryのページ](https://claude.com/ja/partners/microsoft-foundry)は、使用量がAzureの請求書に載り、Azureの利用コミットメント（MACC）にも数えられると書いています。Claude Codeは[Bedrock](https://code.claude.com/docs/ja/amazon-bedrock)や[Agent Platform](https://code.claude.com/docs/ja/google-vertex-ai)の認証でも動き、ログイン画面で3rd-party platformを選んで設定します。データを置く地域で選ぶなら、[地域別コンプライアンスのページ](https://claude.com/ja/regional-compliance)の表ではアジア太平洋にBedrockとVertexが「含まれる」、Foundryは「含まれない」でした（10月23日）。

## 国内の代理店とパートナー

Anthropicは[サービスパートナーの一覧](https://claude.com/ja/marketplace/service-partners)を公開していて、2026年10月23日には321社が載っていました。各社のページにはオフィスの所在地・対応地域・提供するサービスが並び、日本にオフィスがあると登録している会社は33社です。321社のうち、日本に本社を置く会社は次の7社でした。

| 会社 | 一覧のティア |
|---|---|
| NEC・富士通・日立 | Global Premier |
| NTT DATA・クラスメソッド | 優先（Preferred） |
| 野村総合研究所・サーバーワークス | Select |

この一覧に並ぶのは導入の支援・研修・開発を頼める会社です。**ライセンスを売るか、請求を代わりに受けるかは一覧に書かれていません。**パートナーの手数料と、パートナー経由で買ったときの契約の相手も、Anthropicの公式ページには記載がありません。

<figure class="post-figure"><img src="/media/images/claude-corporate-contract/ccc_05_partners.png" alt="Claudeのサービスパートナーの一覧。ティアごとにパートナーが並び、Global PremierにはAccentureやBain & Companyがある" loading="lazy"><figcaption>Anthropicのサービスパートナーの一覧（2026年10月23日）</figcaption></figure>

ライセンスの買い方は、各社の発表で確かめることになります。野村総合研究所は2025年11月20日に、[Amazon Bedrock向けのAnthropic認定リセラーに国内で初めて選ばれた](https://www.nri.com/jp/news/newsrelease/20251120_1.html)と発表しました。クラスメソッドは自社の技術ブログで、[AWSの請求代行を通してAWS MarketplaceのClaude Enterpriseを買う手順](https://dev.classmethod.jp/articles/claude-enterprise-members-aws-marketplace-invoice/)を公開しています（2026年5月8日）。その記事では支払いが円建ての銀行振込で、請求書はAWS Japanから届くとしています。どちらも各社の説明で、Anthropicの公式ページでは確かめられませんでした。**パートナーに頼むなら、契約の相手・請求の通貨・手数料・サポートの窓口の4点を見積もりの時点で書面にしてもらいます。**

## 契約の相手と規約

[商用規約](https://www.anthropic.com/legal/commercial-terms)（2025年6月17日発効）は、契約の相手を顧客の所在地で決めています。欧州経済領域・スイス・英国の顧客はAnthropic Ireland, Limited、それ以外はAnthropic, PBCです。**日本の会社がTeamやEnterpriseを直接契約すると、相手は米国のAnthropic, PBCになります。**準拠法はカリフォルニア州法で、紛争はサンフランシスコで英語の仲裁によって決めると書かれています。

法務が読む項目はほかにもあります。会社を拘束する権限のない人が会社の代わりに規約へ同意することは認められていません。税は請求書に別の記載がない限り料金に含まれず、規約の改定は掲示から30日後に効力を持ちます。どちらの側からも通知で解約でき、Anthropicから解約するときは30日前の通知が必要です。

[データ処理補遺（DPA）](https://www.anthropic.com/legal/data-processing-addendum)（2025年2月24日発効）は商用規約に組み込まれていて、規約に同意すれば一緒に適用されます。データの処理を任せる委託先は別表に並び、新しく加えるときは事前に通知があります。DPAの条件を個別に変えられるかは、公式のページに書かれていません。

<figure class="post-figure"><img src="/media/images/claude-corporate-contract/ccc_06_terms.png" alt="Anthropicの商用規約の冒頭。Anthropicは顧客が欧州経済領域・スイス・英国にあればAnthropic Ireland, Limited、それ以外ならAnthropic, PBCを指すと書かれている" loading="lazy"><figcaption>商用規約の冒頭（2026年10月23日）</figcaption></figure>

Anthropicは2025年10月29日に[東京オフィスの開設](https://www.anthropic.com/news/opening-our-tokyo-office)を発表し、日本の代表は東條英俊氏と紹介されています。ただし、2026年10月23日時点の商用規約が挙げる契約の相手は上の2社だけで、日本の拠点の名前はありません。日本向けに分けた営業窓口のページも見当たらず、問い合わせは料金ページか問い合わせのページからです。消費税は2026年4月1日から請求されていて、適格請求書の登録番号は[Claudeの領収書と請求書の記事](/media/claude-invoice/)に載せています。

## 学習に使われるか

サービスを通じて受け取った顧客のコンテンツをモデルの学習に使うことは、商用規約でAnthropicに禁じられています。[プライバシーセンターの記事](https://privacy.claude.com/ja/articles/7996868)（2026年3月13日更新）も、Claude for Work（TeamとEnterprise）・API・Claude Govの入力と出力は既定で学習に使わないとしています。料金ページのTeamの欄にも、デフォルトでコンテンツをモデルのトレーニングに使用しないと書かれていました。

例外は社員が自分から送ったデータです。**同じ記事によると、サムズアップとサムズダウンのボタンで送ったフィードバックは学習に使われることがあり、その会話全体が最大5年保存されます。**TeamとEnterpriseのプライマリオーナーとオーナーは、組織設定 > データとプライバシーの「チャットを評価」で、このボタンを組織ごと止められます。

<figure class="post-figure"><img src="/media/images/claude-corporate-contract/ccc_07_privacy.png" alt="Anthropicのプライバシーセンターの記事。商用製品の入力と出力は既定でモデルの訓練に使わないが、評価ボタンなどで送ったフィードバックは訓練に使うことがあると書かれている" loading="lazy"><figcaption>学習の扱いの記事（2026年10月23日、スマホ表示）</figcaption></figure>

Claude Codeの[データ使用のドキュメント](https://code.claude.com/docs/ja/data-usage)も同じ扱いです。Team・Enterprise・API・サードパーティのクラウドで使ったコードとプロンプトは学習に使わず、例外はDevelopment Partner Programに参加した組織だけです。稟議書には学習に使われないことと一緒に、評価ボタンを止めるかどうかも決めて書いておきます。

## Claude Codeを含めるには

**TeamとEnterpriseのどの席にもClaude Codeが含まれます。**料金ページのTeamの欄は、スタンダードとプレミアムの両方の機能にClaude CodeとCoworkを挙げています。2つの違いは使える量で、料金ページではプレミアムがスタンダードの5倍の使用量です。開発者だけプレミアムにする組み合わせもできます。

Enterpriseの今の席は1種類で、ウェブ・デスクトップ・モバイルのClaudeにClaude CodeとCoworkが付きます（[Enterpriseの請求方法のヘルプ](https://support.claude.com/ja/articles/11526368)）。Claude Codeで使った分もAPIの料金で請求されるので、長く使う人が多いほど使用量の請求が膨らみます。APIとクラウドの経路では、[法的および規制対応のページ](https://code.claude.com/docs/ja/legal-and-compliance)が、社員の使うAPIキーを会社で用意して配ることを認めています。プランごとの使用量の上限は[Claude Codeの料金の記事](/media/claude-code-pricing/)で比べられます。

## 稟議に書くこと

法務・情シス・経理がそれぞれ別の資料を求めるため、稟議はそこで止まりがちです。公式のページで裏付けが取れる項目を、直接契約とAWS Marketplace経由に分けて並べました。

| 項目 | Anthropicと直接 | AWS Marketplace経由 |
|---|---|---|
| 契約の相手 | Anthropic, PBC（米国） | 販売者はAnthropic・請求はAWS Japan |
| 同意する規約 | 商用規約とDPA | 掲載ページのEULA |
| 支払い | Teamはカード・営業担当経由は請求書 | AWSの請求書（12か月分の席＋使用量） |
| 契約期間 | Teamは月か年・Enterpriseは年 | 12か月 |
| 適格請求書 | Anthropicの登録番号 | AWS Japanの登録番号 |

<figure class="post-figure"><img src="/media/images/claude-corporate-contract/ccc_08_ringi.png" alt="Claudeの法人契約の稟議で確かめる人と項目を縦に並べた図。法務は規約と準拠法、情シスはSSOと学習の設定、経理は通貨と請求書、決裁者は経路と年額を見る" loading="lazy"><figcaption>稟議で確かめる人と項目（公式の規約・ヘルプから作成）</figcaption></figure>

### 決める人と役割

社内で先に決めるのは、誰を組織のプライマリオーナーにするかです。[シートの購入と管理のヘルプ](https://support.claude.com/ja/articles/13393991)によると、Enterpriseのシートを買えるのはオーナーとプライマリオーナーだけで、Teamの請求書を開けるのも組織のオーナーです。法務は商用規約の準拠法と仲裁、情シスはSSOとドメインの確認と評価ボタンの設定、経理は通貨と消費税の扱いを見ます。セキュリティの資料は[Anthropicのトラストセンター](https://trust.anthropic.com/)にまとまっています。

### かかる日数

公式に日数が書かれているのは一部だけです。問い合わせのページによると、セルフサービスのEnterpriseはカードなら数分で決済できます。ACH銀行振込を選ぶと入金が確かめられるまでプランが有効にならず、最大5営業日かかることがあります（[Enterpriseのヘルプ](https://support.claude.com/ja/articles/9797531)）。営業担当経由の日数は記載がなく、AWS Marketplace経由で新しくAWSアカウントを作る場合はクラスメソッドの記事が3〜4営業日としています。

### つまずきやすい点

- 社員の個人Proの経費精算は消費者向けの規約で、学習の設定も1人ずつ違う
- Teamは150席まで。TeamからEnterpriseへの移行は元に戻せない（[Enterpriseの記事](/media/claude-enterprise/)）
- セルフサービスのEnterpriseは、年間の契約の途中で席を減らせない

## よくある質問

### Claudeの法人契約は何人からできますか？

Teamは2人から150人まで、セルフサービスのEnterpriseは20席から、営業担当経由のEnterpriseは50席からです。AWS MarketplaceのEnterpriseは20席からです。

### Claudeは請求書払いで契約できますか？

営業担当経由のEnterpriseならできます。AWS MarketplaceのEnterpriseはAWSの請求書で払います。TeamとセルフサービスのEnterpriseは料金ページの比較表で「いいえ」です。

### Claudeの法人契約は日本円で払えますか？

セルフサービスのEnterpriseは米ドルだけです。営業担当経由は複数の通貨に対応しますが、日本円を選べるかは公式のページに書かれていません。消費税の額は適格請求書に円で表示されます。

### Claudeの法人契約に代理店はありますか？

Anthropicのサービスパートナーの一覧にはNEC・富士通・日立・NTT DATA・クラスメソッド・野村総合研究所・サーバーワークスなど日本の会社が載っていますが、ライセンスの販売や手数料は書かれていません。野村総合研究所はAmazon Bedrock向けの認定リセラーになったと発表しています。

### Claudeの契約の相手は日本法人ですか？

直接契約の相手は米国のAnthropic, PBCです。商用規約は欧州経済領域・スイス・英国以外の顧客の相手をAnthropic, PBCと定めています。

### Claude Codeは法人契約に含まれますか？

含まれます。Teamはスタンダードとプレミアムの両方の席、Enterpriseは1種類の席にClaude Codeが付きます。APIやBedrock・Agent Platform・Foundryの認証でも使え、その場合の支払いは席ではなく使ったトークンの量です。

### Claudeの法人プランの会話は学習に使われますか？

既定では使われません。評価ボタンで送ったフィードバックは学習に使われることがあり、TeamとEnterpriseのオーナーが組織設定で止められます。

## 出典

すべて2026年10月23日に取得。

- Claude「[料金](https://claude.com/ja/pricing)」Team & Enterpriseタブ、プラン間の機能の比較表
- Claude「[営業担当に問い合わせる](https://claude.com/ja/contact-sales)」
- Anthropic ヘルプセンター「[チームプラン請求に関するよくある質問](https://support.claude.com/ja/articles/12997503)」
- Anthropic ヘルプセンター「[Teamプランとは？](https://support.claude.com/ja/articles/9266767)」
- Anthropic ヘルプセンター「[エンタープライズプランとは何ですか？](https://support.claude.com/ja/articles/9797531)」
- Anthropic ヘルプセンター「[エンタープライズプランの請求方法は？](https://support.claude.com/ja/articles/11526368)」
- Anthropic ヘルプセンター「[エンタープライズプランでシートを購入・管理する](https://support.claude.com/ja/articles/13393991)」
- Anthropic「[Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms)」（2025年6月17日発効）
- Anthropic「[Data Processing Addendum](https://www.anthropic.com/legal/data-processing-addendum)」（2025年2月24日発効）
- Anthropic プライバシーセンター「[私のデータはモデルトレーニングに使用されていますか？](https://privacy.claude.com/ja/articles/7996868)」
- Claude Code ドキュメント「[法的および規制対応](https://code.claude.com/docs/ja/legal-and-compliance)」「[データ使用](https://code.claude.com/docs/ja/data-usage)」「[Amazon Bedrock 上の Claude Code](https://code.claude.com/docs/ja/amazon-bedrock)」「[Google Cloud の Agent Platform 上の Claude Code](https://code.claude.com/docs/ja/google-vertex-ai)」
- Claude「[Claude on AWS](https://claude.com/ja/partners/claude-on-aws)」「[Claude in Microsoft Foundry](https://claude.com/ja/partners/microsoft-foundry)」「[地域別コンプライアンス](https://claude.com/ja/regional-compliance)」「[サービスパートナー](https://claude.com/ja/marketplace/service-partners)」
- AWS Marketplace「[Claude Enterprise](https://aws.amazon.com/marketplace/pp/prodview-nnvi6wff6ef6m)」
- AWS「[AWS Japan 税務ヘルプページ](https://aws.amazon.com/jp/tax-help/japan/)」
- Anthropic「[Anthropic officially opens Tokyo office](https://www.anthropic.com/news/opening-our-tokyo-office)」（2025年10月29日）
- 野村総合研究所「[野村総合研究所、日本国内初のAnthropic認定リセラーに選定](https://www.nri.com/jp/news/newsrelease/20251120_1.html)」（2025年11月20日）
- クラスメソッド DevelopersIO「[クレカなし・AWSスキルなしでも Claude for Enterprise を導入できる話](https://dev.classmethod.jp/articles/claude-enterprise-members-aws-marketplace-invoice/)」（2026年5月8日）
