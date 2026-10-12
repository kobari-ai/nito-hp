---
title: 【2026年10月】Claude Enterpriseとは？料金の仕組み・Teamとの違い・20席から
date: 2026-10-13
category: AI活用
description: Claude EnterpriseとTeamの違いを公式の料金ページとヘルプで整理。席料US$20に使った分のAPI料金が乗る仕組み、20席からの条件、SCIM・監査ログ・データ保持の差、申し込みと移行の注意まで。
cover_tag: 法人
cover_headline: Claude Enterpriseとは
cover_sub: 料金の仕組み・Teamとの違い・申し込み
---

Claude Enterpriseは、Anthropicの[料金ページ](https://claude.com/ja/pricing)のTeam & Enterpriseタブで「大規模に事業を展開する大企業向け」とされている法人向けのプランです。金額の欄には1席あたり月US$20（年払い）と、APIレートでの使用量が並んでいます。席の料金に使える量が含まれるTeamとは、お金のかかり方が根本から違います。

検討する側が迷うのはTeamとEnterpriseのどちらにするかです。**会社で毎月の金額を席の数で固定できるのはTeamだけで、Enterpriseは席の料金とは別に、使った分を全員分まとめて払う契約です。**この記事は2026年10月13日に取得した料金ページの比較表とヘルプセンターをもとに、料金の数え方・何人から契約できるか・Enterpriseにしかない管理機能・申し込みと移行の注意を整理します。

:::takeaways
- Enterpriseは**1席あたり月US$20（年払いのみ）に、使った分のAPI料金が乗る**。席に含まれる使用量はない
- **毎月の金額を席の数で決められるのはTeamだけ**。Enterpriseの費用は管理者が決める支出上限で抑える
- 最低席数は**セルフサービスが20席、営業担当経由が50席**。Teamは2〜150席
- SSOとドメイン確認はTeamにもある。**SCIM・監査ログ・カスタムデータ保持・コンプライアンスAPIは比較表でEnterpriseだけ**（ロールベースの権限は、Teamのヘルプにも項目がある）
- セルフサービスは**米ドル払いで使用量は前払いのクレジット**。期中に席を減らせず、Teamからの移行は元に戻せない
:::

<figure class="post-figure"><img src="/media/images/claude-enterprise/cent_01_overview.jpg" alt="TeamとEnterpriseの関係を示した概要図。左の青緑のカードにTeamと使用量込みの定額、右のオレンジのカードにEnterpriseと席料と使った分、右下に20席からのバッジがあり、左から右へ矢印が向いている" loading="lazy"><figcaption>TeamとEnterpriseの違い（Claudeの料金ページとヘルプから作成）</figcaption></figure>

## Claude Enterpriseとは

ヘルプ「[エンタープライズプランとは何ですか？](https://support.claude.com/ja/articles/9797531)」は、Enterpriseを高度なセキュリティとコンプライアンスの管理が要る組織向けのプランと説明しています。Teamのすべての機能に、監査ログやSCIMなどの管理機能が加わります。1つの席でウェブ・デスクトップ・モバイルのClaudeに加えて、Claude CodeとCoworkも使えます。

Teamにはスタンダードとプレミアムの2種類の席がありますが、今のEnterpriseの席は1種類だけです。以前のEnterpriseにはスタンダード・プレミアムの席や、チャットだけの席とClaude Code付きの席がありました。**これらは新しい契約では選べず、今使っている組織も次の契約更新で1種類の席に切り替わります。**HIPAA対応の組織は例外です。

買い方はセルフサービスと営業担当経由の2つです。ヘルプによると、どちらも機能と席の単価は同じで、違うのは購入の方法・支払い方法・プランの管理の仕方です。

## 料金は席料と使った分

料金ページのEnterpriseの欄には「シート料金 + APIレートでの使用量」と書かれ、その下に1席あたり月US$20（年払い）と、使用コストはモデルとタスクに応じて変動するという注記があります。月払いの選択肢はありません。

<figure class="post-figure post-figure--sp"><img src="/media/images/claude-enterprise/cent_02_pricing_sp.jpg" alt="Claudeの料金ページのTeam & Enterpriseタブをスマホで開き、Enterpriseのカードを表示した画面。Enterprise plan を申し込むと購入スペシャリストとチャットのボタンの下に、シート料金とAPIレートでの使用量、US$20/シート/月（年払い）の表示があり、そこを赤枠1で囲んでいる" loading="lazy"><figcaption>料金ページのEnterpriseの欄（2026年10月13日、スマホ表示）</figcaption></figure>

### 定額の枠がない

ヘルプ「[Enterprise プランの請求方法について](https://support.claude.com/ja/articles/11526368)」によると、席の料金はClaudeを使える権利の分だけです。チャット・Claude Code・Coworkで使ったトークンは、すべて標準のAPIレートで別に請求されます。**席ごとの使用量の上限も、席に含まれるトークンの枠もないため、同じ人数でも毎月の金額は使い方で変わります。**

<figure class="post-figure"><img src="/media/images/claude-enterprise/cent_03_cost.jpg" alt="TeamとEnterpriseの毎月の請求の中身を比べた図。Teamは席の料金に使える量を含み、超えた分は任意で使用クレジット。Enterpriseは使える量を含まない席の料金US$20に、APIの単価で全員分を合算した使った分が加わる。下にEnterpriseの金額を抑えるのは管理者が決める支出上限と書かれている" loading="lazy"><figcaption>席の料金に何が含まれるか（Claudeの料金ページとヘルプから作成）</figcaption></figure>

費用を抑える手段は支出上限です。オーナーなどの権限を持つ人が、組織全体と人ごとの2段階で上限を決められ、低いほうの上限で止まります。上限を「無制限」にもできますが、使用量の請求そのものを切ることはできません。

セルフサービスでは使用量を前払いのクレジットで買います。**クレジットは組織で1つの残高を共有しているので、1人が多く使えば全員の残高が早く減り、ゼロになると追加で買うまで組織の全員が使えなくなります。**営業担当経由は月ごとの後払いで、使った分が請求書に積み上がる形です。

使用量の単価は[APIの料金ページ](https://platform.claude.com/docs/ja/about-claude/pricing)のモデルごとの金額です。処理を米国内に限る設定をオンにすると、Claude Opus 4.6・Sonnet 4.6とそれ以降のモデルの使用量は標準の1.1倍で請求されます。

### 日本の料金ページの税の表示

日本向けの料金ページには「Prices include 10% JCT」という注記があり、Teamのスタンダードシートは年払いで$22と出ています。米国向けの[料金ページ](https://claude.com/pricing)では同じ席が$20で、表示に税を含まないと書かれています。**Teamの金額は日本の消費税込みに直してある一方、Enterpriseの欄は日本向けも米国向けも同じUS$20です。**

料金ページの日本の表示には、TeamとEnterpriseの下に共通で「Prices include 10% JCT」とありますが、EnterpriseのUS$20は米国の表示と同じ額で、消費税を含むかは読み取れません。予算を組むときは見積もりか最初の請求書で税の扱いを確かめてください。請求書の消費税の表示は[Claudeの領収書と請求書の記事](/media/claude-invoice/)で扱っています。

### コンテキストの長さの書き方の違い

料金ページの比較表でコンテキストウィンドウを見ると、TeamとEnterpriseの3列とも「最大100万（モデルによって異なる）」です。Teamのヘルプ「[Team プランとは何ですか？](https://support.claude.com/ja/articles/9266767)」には「200k コンテキストウィンドウ」とあります。今のEnterpriseは長い文章を読めることが売りのプランではないので、選ぶ理由は管理機能と人数で考えます。

## 何人から契約できるか

Enterpriseのシートのヘルプ「[エンタープライズプランでシートを購入・管理する](https://support.claude.com/ja/articles/13393991)」には、最低20席が必要とあります。営業担当経由は最低50席です。

| 項目 | Team | Enterprise（セルフサービス） | Enterprise（営業担当経由） |
|---|---|---|---|
| 席の数 | 2〜150席 | 20席から | 50席から |
| 支払い方法 | クレジットカード | クレジットカード・ACH（米ドルのみ） | クレジットカード・ACH・請求書（複数の通貨） |
| 請求の周期 | 月払い・年払い | 年払い | 年払い |
| 使用量の請求 | 席に含まれる | 前払いのクレジット | 月ごとの後払い |
| トライアル | なし | なし | あり |

**20席から150席までの組織はTeamとEnterpriseのどちらも選べ、150席を超えるならEnterpriseしかありません。**20席より少ないなら、選べるのはTeamだけです。Teamの料金と席の数え方は[Claude Teamプランの記事](/media/claude-team/)にまとめました。

席はいつでも足せて、残りの期間の分が日割りですぐに請求されます。**セルフサービスでは年間の契約期間の途中で席を減らせず、減らせるのは更新のときだけです。**メンバーを組織から外しても席の数と請求は変わらず、空いた席をほかの人に割り当てられるだけです。

## Teamとの違い

料金ページの「プラン間の機能を比較」には、Team・Enterprise（セルフサービス）・Enterprise（営業担当経由）の3列が並んでいます。チャットやClaude Code、Claude in Chromeなどの使える機能は3列ともほぼ同じです。違いが集まっているのはセキュリティと管理の行です。

<figure class="post-figure"><img src="/media/images/claude-enterprise/cent_04_compare.jpg" alt="Claudeの料金ページのプラン比較表のセキュリティと管理の部分。シングルサインオン、ドメイン確認、組織の作成を制限、一元的な請求と管理などは3列とも黒丸で、ドメインキャプチャ、ロールベースのアクセス制御、SCIM、監査ログ、コンプライアンスAPI、カスタムデータ保持コントロール、HIPAA対応オプションはTeamの列だけがバツになっている。ただしドメインキャプチャとロールベースの権限は、Teamのヘルプにも項目がある" loading="lazy"><figcaption>比較表のセキュリティと管理（2026年10月13日）</figcaption></figure>

TeamとEnterpriseで印が違う行だけを抜き出すと、次のとおりです。

| 項目 | Team | Enterprise |
|---|---|---|
| SCIM（名簿との自動同期） | なし | あり |
| 監査ログ・コンプライアンスAPI | なし | あり |
| カスタムデータ保持 | なし | あり |
| ロールベースのアクセス制御 | 比較表は「いいえ」（ヘルプに権限設定の項目あり） | あり |
| ドメインキャプチャ・ドメインのアカウントの移行 | 比較表は「いいえ」（ヘルプにドメインキャプチャの記載あり） | あり |
| HIPAA対応のオプション | なし | あり |
| Claude Security（ベータ）・Inference hooks | なし | あり |
| 毎月のAPIクレジット | 組織で月$500まで | なし |

料金ページのEnterpriseのカードには、このほかにネットワークレベルのアクセス制御とIPアローリストが挙がっています。顧客が管理する暗号化キーと処理を米国内に限る設定も、ヘルプにEnterpriseの機能として書かれています。

### SSOはTeamにもある

シングルサインオン（SSO）・ドメイン確認・組織の作成を制限の3つは、比較表でもTeamで使える機能です。[SSOの設定のヘルプ](https://support.claude.com/ja/articles/13132885)も、SSOはTeamプランとEnterpriseプランの両方で使えると書いています。**SSOが要るという理由だけなら、Enterpriseにする必要はありません。**

差が出るのはアカウントの作り方と消し方です。ログインしたときに自動でアカウントを作るJITは、[JITとSCIMのヘルプ](https://support.claude.com/ja/articles/13133195)でTeamでも使えるとされています。ただしJITでは、社内のID管理（OktaやMicrosoft Entra IDなど）から外した人はログインできなくなるだけで、メンバーの一覧に残ります。**ID管理から外した人を自動で組織から消せるのはSCIMで、SCIMはEnterpriseだけです。**

役割の設定も分かれます。Teamのヘルプにも「ロールベースの権限設定」という項目がありますが、比較表ではロールベースのアクセス制御のTeamの列は「いいえ」です。機能ごとに使える人を分けるカスタムロールのヘルプは、Enterpriseのプランで使えると書いています。

### 監査ログとデータ保持

監査ログを使えるのはEnterpriseの組織だけです（[監査ログのヘルプ](https://support.claude.com/ja/articles/9970975)）。書き出せるのはオーナーとプライマリオーナーで、場所は組織設定のデータとプライバシーです。記録されるのは誰がいつどの操作をしたかで、日時・IPアドレス・端末の情報が付きます。チャットとプロジェクトのタイトルや中身は含まれず、出るのは識別子だけです。会話の中身まで社内の監視の仕組みに取り込むなら、コンプライアンスAPIを使います。

[データ保持のヘルプ](https://support.claude.com/ja/articles/10440198)では、Enterpriseのオーナーが会話とプロジェクトを残す期間を決められます。既定は無期限で、短くできるのは30日までです。数え始めは最後のやり取りからで、期間を過ぎたデータは消えて戻せません。Claude DesignやClaude Codeのウェブ版をもとにした機能など、この設定が効かないものもあります。

会話をモデルの学習に使わないのは、比較表ではTeamを含む3列とも既定の扱いです。学習の設定はTeamとEnterpriseで差がつく項目ではありません。

## 申し込みの流れ

セルフサービスは料金ページの「Enterprise plan を申し込む」か[claude.ai/create/enterprise](https://claude.ai/create/enterprise)から始めます。ログインせずに開くと、最初に「チームにこれらのいずれかが必要ですか？」という確認が出ます。2026年10月13日に開いたときの選択肢は「500シート以上」「カスタム契約（使用量コミットメント、製品バンドル）」「上記のいずれでもない」の3つでした。

<figure class="post-figure post-figure--sp"><img src="/media/images/claude-enterprise/cent_06_create_sp.jpg" alt="claude.aiのEnterpriseの申し込み画面をスマホで開いた画面。チームにこれらのいずれかが必要ですか、はいの場合は営業チームにお問い合わせくださいという見出しの下に、500シート以上、カスタム契約（使用量コミットメント、製品バンドル）、上記のいずれでもない、の3つのチェック欄が赤枠1、続けるボタンが赤枠2で囲まれている" loading="lazy"><figcaption>Enterpriseの申し込みの最初の画面（2026年10月13日、スマホ表示）</figcaption></figure>

1. 当てはまる項目にチェックを入れる（画面には、当てはまるなら営業チームに問い合わせるよう書かれている）
2. 「続ける」を押し、席の数と支払い方法を決める（ヘルプの説明による）

支払いはクレジットカード・デビットカード・ACH（米国の銀行振込）で、通貨は米ドルだけです。ACHを選んだ場合、入金が届くまでプランは有効にならず、最大5営業日かかることがあります。この記事ではこの先の画面には進んでいません。

<figure class="post-figure"><img src="/media/images/claude-enterprise/cent_05_selfserve.jpg" alt="Claudeのヘルプのセルフサービス対営業支援エンタープライズの表。購入方法はオンラインと営業チーム、最小シート数は20と50、支払い方法はクレジットカードとACHに対し営業支援は請求書も可、受け入れ通貨はUSDのみと複数通貨対応、使用量請求は事前購入クレジットと月次後払い請求、HIPAA対応はどちらも利用可能" loading="lazy"><figcaption>ヘルプのセルフサービスと営業担当経由の比較（2026年10月13日）</figcaption></figure>

営業担当経由にするのは、請求書払い・一定の支出基準に達した場合のカスタマーサクセスサポート・米ドル以外の通貨が要るときです。料金ページの「購入スペシャリストとチャット」か営業への問い合わせから始めます。$50,000以上の請求書は銀行振込でしか払えません。トライアル・コンサルテーション・AWS Marketplaceでの購入も、比較表では営業担当経由だけに付いています。

### Teamから移るとき

[Teamから移行するヘルプ](https://support.claude.com/en/articles/13779868)（英語）は、今のTeamの組織のまま上げることを勧めています。同じ組織なら会話・プロジェクト・メンバーと役割が残り、新しく組織を作ると移りません。セルフサービスの手順は、claude.ai/upgradeからEnterpriseを選び、既存の組織を選んで、20席以上の席数と1人あたりの支出上限、最初の使用量の残高を決めて確定する流れです。

**この経路での移行は元に戻せません。**移った直後はスキル・コード実行とファイル作成・Claude Design・Claude in ChromeなどがEnterpriseでは既定でオフになり、席が割り当てられないメンバーが出ることもあります。ヘルプは切り替えのあとに機能の設定と席の割り当てを見直すよう書いています。

[MaxとTeamのAPIクレジットのドキュメント](https://platform.claude.com/docs/ja/about-claude/api-credits-for-subscribers)のとおり、毎月のAPIクレジットはMaxとTeamだけが対象で、Enterpriseは含まれません。Teamで受け取っていた組織は、移行すると新しいクレジットが止まります。手元に残っている分は期限まで使えて、Teamで買った使用クレジットの残りも引き継がれます。

## Enterpriseにするかの目安

決め手になるのは人数よりも、社内の規程が求める管理と、毎月の金額をどこまで読めるかです。Teamの席には使える量が含まれるので、予算は席の数でほぼ決まります。Enterpriseは使った分の請求になるため、Claude Codeを長く使う人が多い組織ほど、席の料金との差が開きやすくなります。

<figure class="post-figure"><img src="/media/images/claude-enterprise/cent_07_when.jpg" alt="条件ごとに向くプランを並べた図。毎月の金額を席の数で決めたい、使う人が20人より少ないはTeam。150人を超えて配る、SCIMや監査ログが社内の規程で要るはEnterprise。請求書払いや米ドル以外で払いたい、500席以上や使用量を約束する契約はEnterpriseの営業担当経由" loading="lazy"><figcaption>条件ごとの選び方（Claudeの料金ページ・ヘルプ・申し込み画面から作成）</figcaption></figure>

社員のID管理と連動させたい、操作の記録を残す決まりがある、会話の保存期間を短くしたいといった要件があれば、20席以上でEnterpriseを考える段階です。こうした要件がなく、全員が同じくらい使うなら、Teamのほうが予算を立てやすくなります。

SCIMや権限、使用量の上限を整えたあと、決まった仕事をClaudeに任せる仕組みづくりは、[AIエージェント構築支援](/ai-agent/)で相談を受けています。

## よくある質問

### Q. Claude Enterpriseの料金はいくらですか？

1席あたり月US$20（年払い）の席の料金と、使った分のAPI料金の合計です。席に含まれる使用量はなく、チャット・Claude Code・Coworkで使ったトークンは標準のAPIレートで請求されます。料金ページの日本の表示には、TeamとEnterpriseの下に共通で「Prices include 10% JCT」とありますが、EnterpriseのUS$20は米国の表示と同じ額で、消費税を含むかは読み取れません。見積もりで確かめてください。

### Q. Claude Enterpriseは何人から契約できますか？

セルフサービスは最低20席、営業担当経由は最低50席です。申し込み画面では500席以上なら営業への問い合わせを案内しています（2026年10月13日）。20席より少ないならTeam（2〜150席）を選びます。

### Q. Claude EnterpriseとTeamの違いは何ですか？

お金のかかり方と管理機能です。Teamは席の料金に使える量が含まれ、Enterpriseは席の料金とは別に使った分を払います。SSOとドメイン確認はTeamにもあり、SCIM・監査ログ・カスタムデータ保持・コンプライアンスAPIは比較表でEnterpriseだけです。ロールベースの権限も比較表ではEnterpriseだけですが、Teamのヘルプにも項目があります。

### Q. Claude TeamでもSSOは使えますか？

使えます。料金ページの比較表でもSSOのヘルプでも、SSOとドメイン確認はTeamとEnterpriseの両方の機能です。ID管理から外した人を自動で組織から消すSCIMは、Enterpriseだけです。

### Q. Claude Enterpriseの会話は学習に使われますか？

比較表によると、TeamとEnterpriseのどちらも会話は既定でモデルの学習に使われません。Enterpriseにするとさらに、会話とプロジェクトを残す期間を30日以上の範囲で決められます。

### Q. Claude Enterpriseに使用量の上限はありますか？

プランや席ごとの使用量の上限はありません。かわりに管理者が、組織全体と人ごとに支出上限を決められます。セルフサービスは前払いのクレジットが尽きたときにも止まります。

### Q. Claude Enterpriseは請求書払いできますか？

営業担当経由のEnterpriseならできます。セルフサービスはクレジットカード・デビットカード・ACHで、通貨は米ドルだけです。Teamは請求書払いに対応していません。

### Q. Claude EnterpriseにAPIクレジットは付きますか？

付きません。毎月のAPIクレジットの対象はMaxとTeamで、Enterpriseは対象外です。TeamからEnterpriseに移ると、新しいクレジットは止まります。

## 出典

すべて2026年10月13日に取得。

- Claude「[料金](https://claude.com/ja/pricing)」Team & Enterpriseタブ、プラン間の機能の比較表、FAQ
- Claude「[Pricing](https://claude.com/pricing)」（米国向け）Team & Enterpriseタブ
- Anthropic ヘルプセンター「[エンタープライズプランとは何ですか？](https://support.claude.com/ja/articles/9797531)」
- Anthropic ヘルプセンター「[Enterprise プランの請求方法について](https://support.claude.com/ja/articles/11526368)」
- Anthropic ヘルプセンター「[エンタープライズプランでシートを購入・管理する](https://support.claude.com/ja/articles/13393991)」
- Anthropic ヘルプセンター「[Migrate your organization from Team to Enterprise](https://support.claude.com/en/articles/13779868)」
- Anthropic ヘルプセンター「[Team プランとは何ですか？](https://support.claude.com/ja/articles/9266767)」
- Anthropic ヘルプセンター「[シングルサインオン（SSO）の設定](https://support.claude.com/ja/articles/13132885)」
- Anthropic ヘルプセンター「[JIT または SCIM プロビジョニングの設定](https://support.claude.com/ja/articles/13133195)」
- Anthropic ヘルプセンター「[エンタープライズプランでカスタムロールを管理する](https://support.claude.com/ja/articles/13930452)」
- Anthropic ヘルプセンター「[監査ログへのアクセス](https://support.claude.com/ja/articles/9970975)」
- Anthropic ヘルプセンター「[エンタープライズプランのカスタムデータ保持制御を設定する](https://support.claude.com/ja/articles/10440198)」
- Claude Platform ドキュメント「[MaxプランおよびTeamプランのAPIクレジット](https://platform.claude.com/docs/ja/about-claude/api-credits-for-subscribers)」
- Claude Platform ドキュメント「[料金](https://platform.claude.com/docs/ja/about-claude/pricing)」
- claude.ai「[Enterpriseの申し込み](https://claude.ai/create/enterprise)」（ログインせずに表示した最初の画面）
