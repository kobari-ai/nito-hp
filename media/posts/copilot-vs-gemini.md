---
title: 【2026年10月】CopilotとGeminiの違い｜会社に入れるならどっち？料金・データ・管理
date: 2026-10-25
category: AI活用
description: Microsoft 365 CopilotとGoogle WorkspaceのGeminiを会社で入れる前提で比較。込みか足すかで変わる料金と50人の月額、Outlook・Gmailでの機能、社内データ、日本に保存できるか、管理の設定まで。
cover_tag: 導入担当向け
cover_headline: CopilotとGeminiの違い
cover_sub: 料金・社内データ・管理で比べる
cta: ai_agent
---

Google Workspaceの料金ページでは、Business Standardが1ユーザー月1,600円（年間プラン・税別）で、GmailやGoogleドキュメントのGeminiが含まれています。MicrosoftはBusiness StandardとCopilot Businessの組み合わせを月3,523円（年払い・税抜）と表示しています。いずれも2026年10月25日の表示です。

同じStandardでも、AIが月額に込みなのか、あとから足すのかが違います。この記事は会社でAIを入れる担当者に向けて、CopilotとGeminiのどちらを選ぶかの判断に要る違いを公式の資料で並べます。

:::takeaways
- **どちらを選ぶかの大半は、社員が今Microsoft 365とGoogle Workspaceのどちらで働いているかで決まる**。WorkspaceのGeminiは月額に込み、Microsoft 365はCopilot Chatが追加費用なしで、有料のCopilotは足す契約
- 50人に年払いで配ると、Workspace Business Standardは月80,000円、Business StandardとCopilot Businessの組み合わせは月176,150円（どちらも税抜）。Businessのプランはどちらも300人まで
- **データを日本に置く約束があるのはMicrosoft側**。Workspaceのデータ リージョンで選べるのは米国・EU・指定なしの3つ
:::

## 比べる相手をそろえる

どちらも同じ名前の下に個人向けと会社向けの製品が並びます。会社で検討の対象になるのは、Microsoft側がCopilot Chatと有料のCopilotの2段、Google側がWorkspaceのプランに入っているGeminiです。

有料のCopilotは会社の規模で2つに分かれます。[Microsoft Learnのライセンスのページ](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-licensing)によると、**Copilot BusinessはMicrosoft 365 Businessのライセンスを持つ300人までの組織向けのアドオンで、法人向けと同じCopilotの機能を提供します**。300人を超える会社ではE3やE5などに足す法人向けのライセンスを使い、種類ごとの機能の差は「[Copilotの使い方](/media/copilot-guide/)」にまとめました。

<figure class="post-figure"><img src="/media/images/copilot-vs-gemini/cvg_01_lineup.png" alt="会社で比べる5つの契約を縦に並べた図。Microsoft側はCopilot Chat（Microsoft 365に追加費用なし）、Copilot Business（300人までの会社が足す）、法人向けMicrosoft 365 Copilot（E3やE5などに足す）、Google側はWorkspaceのGemini（BusinessとEnterpriseの月額に込み）とGemini Enterprise（エージェント用の別の契約）" loading="lazy"></figure>

WorkspaceのGeminiは、GmailやドキュメントなどのアプリのなかのGeminiと、gemini.google.comのGeminiアプリの2つです。[PC Watchの2025年1月16日の記事](https://pc.watch.impress.co.jp/docs/news/1654889.html)によると、GoogleはGemini BusinessとGemini Enterpriseのアドオンをやめてプランの月額に組み込み、Business Standardの年間契約を1,360円から1,600円に改めました（新料金は2025年3月17日から）。**Gemini Businessの20ドル・Gemini Enterpriseの30ドルという金額は旧アドオンのもので、今の契約には当てはまりません。**

名前の似た「Gemini Enterprise - Businessエディション」はAIエージェントを作って共有するための別の製品で、[Workspaceの管理者ヘルプ](https://knowledge.workspace.google.com/admin/generative-ai/gemini-enterprise?hl=ja)によると営業担当者かGoogle Cloudパートナーを通して申し込みます。プログラミング用のGitHub Copilotも別物で、[GitHubのドキュメント](https://docs.github.com/ja/copilot/using-github-copilot/ai-models/using-gemini-in-github-copilot)のとおりモデルの1つとしてGeminiを選べます。

## 料金と最低席数

どちらも日本の料金は円の税抜です。Microsoftの価格ページはどのカードにも「価格には消費税は含まれていません」と書き、[Google Workspaceの料金ページ](https://workspace.google.com/intl/ja/pricing)も各プランの「価格の詳細」に「（税別）」と添えているので、税抜の金額どうしでそのまま比べられます。

| 契約 | 年払い（1人の月額） | 月払い（1人の月額） | AIの扱い |
|---|---|---|---|
| Workspace Business Starter | 800円 | 950円 | Geminiは込み（Gmail・Vids・Geminiアプリ） |
| Workspace Business Standard | 1,600円 | 1,900円 | Geminiは込み |
| Workspace Business Plus | 2,500円 | 3,000円 | Geminiは込み |
| Microsoft 365 Business Basic | 1,049円 | 1,259円 | Copilot Chatは追加費用なし |
| Microsoft 365 Business Standard | 2,098円 | 2,518円 | Copilot Chatは追加費用なし |
| Business StandardとCopilot Businessの組み合わせ | 3,523円 | 4,228円 | 有料のCopilotを含む |
| Copilot Business（アドオン） | 2,698円（表示は3,148円からの割引） | 3,778円 | 土台のプランに足す |
| 法人向けMicrosoft 365 Copilot | 4,497円 | 4,722円（年間契約の毎月払い） | E3・E5などに足す |

Workspaceの月払いの列は1年の契約をしないフレキシブルプランで、Microsoftの金額は[Teamsが含まれるプランの価格ページ](https://www.microsoft.com/ja-jp/microsoft-365/business/with-teams-plans-and-pricing)と[Copilot Businessの価格ページ](https://www.microsoft.com/ja-jp/microsoft-365/copilot/business)の表示です。

<figure class="post-figure"><img src="/media/images/copilot-vs-gemini/cvg_gws_pricing.png" alt="Google Workspaceの料金ページの年間プランのカード。Starter・Standard・Plusが並び、Standardは新規向けの3か月50%オフで800円、取り消し線の定価が1ユーザー月1,600円" loading="lazy"><figcaption>Google Workspaceの料金ページ（2026年10月25日）</figcaption></figure>

**Workspaceは2025年1月からGeminiを月額に組み込んだのに対し、MicrosoftはCopilotを土台のプランに足す形のままです。**ただしMicrosoftの価格ページには、Business StandardとBusiness PremiumにCopilot Businessを組み合わせた価格があります。Business Standardの単体2,098円にCopilot Businessの定価3,148円を別に足すと5,246円、割引の表示の2,698円でも4,796円になり、組み合わせの3,523円のほうが安く済みます。

<figure class="post-figure"><img src="/media/images/copilot-vs-gemini/cvg_ms_standard_copilot.png" alt="MicrosoftのCopilot Businessの価格ページで、Teamsが含まれるプラン・年払いのMicrosoft 365 Business Standard（Copilotを含む）のカード。ユーザー/月相当・年払いで3,523円、価格には消費税は含まれていませんと書かれている" loading="lazy"><figcaption>Copilot Businessの価格ページ（2026年10月25日）</figcaption></figure>

人数の線はどちらのBusinessも300人です。料金ページによると、WorkspaceはStarter・Standard・Plusの購入で最大300人まで使え、Enterpriseのプランには上限も下限もありません。Copilotは[2024年1月のMicrosoftの発表](https://www.microsoft.com/en-us/microsoft-365/blog/2024/01/15/expanding-copilot-for-microsoft-365-to-businesses-of-all-sizes/)で300席の最低購入数がなくなり、1人から買えます。

Workspaceの最初の3か月の割引や、Copilot Businessの2,698円のように、新しい契約向けの割引の表示は時期で変わります。**予算は定価で組んでおくほうが安全です。**WorkspaceのGeminiの上限やプランごとの機能の差は「[Google WorkspaceのGeminiとは](/media/google-workspace-gemini/)」で扱っています。

### 50人で入れたときの月額

年払いの定価で、土台のプランの値段を含めた月額です。

<figure class="post-figure"><img src="/media/images/copilot-vs-gemini/cvg_02_cost.png" alt="50人に配ったときの月額を縦に並べた図。年払い・税抜の定価で、Workspace Business Standardは80,000円でGeminiは月額に込み、Business Starterは40,000円でGeminiはGmailとアプリだけ、Microsoft 365 Business Standardだけは104,900円でCopilot Chatは追加費用なし、Business StandardとCopilotの組み合わせは176,150円" loading="lazy"></figure>

| 契約（年払い・税抜） | 50人の月額 | 消費税を足すと |
|---|---|---|
| Workspace Business Starter | 40,000円 | 44,000円 |
| Workspace Business Standard | 80,000円 | 88,000円 |
| Microsoft 365 Business Standard | 104,900円 | 115,390円 |
| Business StandardとCopilot Businessの組み合わせ | 176,150円 | 193,765円 |

**同じStandardの段で比べると、有料のCopilotまで入れたMicrosoftの組み合わせはWorkspaceより月に96,150円高くなります。**CoworkやAutopilotなどの高度な機能はライセンスとは別の従量課金で、エージェントの費用は「[Copilot Studioの料金](/media/copilot-studio/)」にまとめました。

## 今使っている土台で大半が決まる

最初に確かめたいのは社員のメール・予定表・ファイルがどちらの上にあるかです。有料のCopilotはLearnのページのとおり対象のMicrosoft 365のライセンスを持つ人に足す契約で、単独では買えません。WorkspaceのGeminiも、GmailやドライブのアカウントであるWorkspaceの契約に入っているものです。**AIだけ相手の会社に合わせようとすると、メールとファイルの土台をもう1つ契約することになります。**

土台ごと乗り換えるなら、費用の中心はAIの差額ではなくメールとファイルの移行と社員の慣れです。

<figure class="post-figure"><img src="/media/images/copilot-vs-gemini/cvg_03_decide.png" alt="CopilotとGeminiのどちらを入れるかを決める順番の図。1は今の土台がどちらか（メールとファイルの置き場所）、2は込みの範囲で足りるか（Copilot ChatかStarterのGemini）、3は読ませたいデータがどこにあるか（もう一方の側にあればコネクタ）、4は日本に置く決まりがあるか（Workspaceは米国とEUだけ）" loading="lazy"></figure>

Microsoft 365の会社なら、Copilot Chatで足りない仕事を書き出してから有料のCopilotを配る人を選ぶと無駄が出にくくなります。Workspaceの会社なら、StarterのままかドキュメントやMeetのGeminiが使えるStandardにするかが分かれ目です。ChatGPTも候補に入るなら「[CopilotとChatGPTの違い](/media/copilot-vs-chatgpt/)」を同じ軸で書いています。

## Outlook・TeamsとGmail・Meetの中

どちらも、日々使うアプリの中にAIが入ります。差が出るのは追加費用なしの範囲でどこまで使えるかです。

| 場面 | Microsoft 365 | Google Workspace |
|---|---|---|
| 追加費用なしの範囲 | Copilot Chat（Web・渡したファイル、Outlookでは受信トレイと予定表） | StarterでもGmailのサイドパネル・文書作成・返信の候補・スレッドの要約・校正 |
| 文書と表計算の中 | 有料のCopilotでWord・Excel・PowerPoint | Standardからドキュメント・スプレッドシート（AI関数） |
| 会議とチャット | 有料のCopilotでTeamsのチャットと通話 | StandardからMeetの自動メモ生成とChatの要約 |

[Copilot Chatの概要](https://learn.microsoft.com/ja-jp/copilot/overview)によると、Copilot ChatのままではWord・Excel・PowerPoint・OneNoteの中のCopilotのチャットは使えません。Google側の[Businessエディションの比較](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-business-editions?hl=ja)では、Starterの列にチェックが入るGeminiの機能はGmailのものだけです。**議事録をAIに任せたい会社は、WorkspaceならStandard以上、Microsoft 365なら有料のCopilotが前提です。**

[ユースフルの解説動画](https://www.youtube.com/watch?v=3l8t64BOKfI)では、Copilotのリサーチツールが調べる範囲・まとめ方・根拠の付け方を先に質問してから動く様子が実演され、社外の調べ物はGemini、社内の資料まで使う調べ物はCopilotという分け方が勧められていました。

## 社内データへのつなぎ方

**どちらのAIも、社員が自分で開ける社内のデータしか答えに使いません。**[Learnのデータとプライバシーのページ](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-privacy)は、Copilotが表示するのは個々のユーザーが少なくとも表示アクセス許可を持っている組織データだけと書いています。Googleの[生成AIに関するプライバシー ハブ](https://support.google.com/a/answer/15706919?hl=ja)も同じで、ユーザーに閲覧権限がないファイルはAIも閲覧や使用ができません。

裏返すと、全社に共有されたままの人事や給与のファイルは、どちらのAIでも答えの材料になり得ます。SharePointやドライブの共有設定の見直しは、どちらを選んでも導入の前に必要です。

<figure class="post-figure"><img src="/media/images/copilot-vs-gemini/cvg_04_data.png" alt="社内データへの届き方の図。Copilotは本人が閲覧できるものだけをMicrosoft Graph経由で読み、GoogleドライブはCopilotコネクタでつなぐ。WorkspaceのGeminiは本人が閲覧できるものだけをGmailやドライブとの連携で読み、SharePointはGemini Enterpriseのコネクタでつなぐ" loading="lazy"></figure>

もう一方の会社のデータを読ませる道も、公式に用意されています。Microsoftの[GoogleドライブのCopilotコネクタ](https://learn.microsoft.com/ja-jp/microsoftsearch/google-drive-overview)は、ドライブのアクセス制御を保ったままファイルを索引に取り込み、Copilotで検索できるようにします。[配置の手順](https://learn.microsoft.com/ja-jp/microsoftsearch/google-drive-connector)は、Google Workspaceの管理者とMicrosoft 365の管理者の2人がかりです。

Google側でSharePoint・OneDrive・Outlook・Teamsとつなぐ道として公式に案内されているのは、WorkspaceのGeminiではなく別の製品のGemini Enterpriseです。[Gemini Enterpriseのコネクタの一覧](https://cloud.google.com/gemini-enterprise/docs/connectors/introduction-to-connectors-and-data-stores?hl=ja)に、Microsoftの4つのサービスとEntra ID、Jira、Salesforceが並びます。**WorkspaceのGeminiの機能の表にはMicrosoftのサービスとつなぐ項目が無いため、Microsoft 365のデータをGeminiに読ませるならGemini Enterpriseの契約を別に考えることになります。**

<figure class="post-figure"><img src="/media/images/copilot-vs-gemini/cvg_ge_connectors.png" alt="Gemini Enterpriseのドキュメントの左側の一覧。Microsoft Entra ID、Microsoft OneDrive、Microsoft Outlook、Microsoft SharePoint Online、Microsoft Teamsをそれぞれ接続する項目が並んでいる" loading="lazy"><figcaption>Gemini Enterpriseのコネクタの一覧（2026年10月25日）</figcaption></figure>

## 学習の扱いと保存場所

入力が学習に使われない点は、どちらの会社向けの契約でも公式に書かれています。差が大きいのはデータを日本に置けるかどうかです。

| 項目 | Copilot | WorkspaceのGemini |
|---|---|---|
| 入力を学習に使うか | 基礎LLMのトレーニングに使わない | 許可なくドメインの外でモデルのトレーニングに使わない |
| 人によるレビュー | Azure OpenAIの不正使用の監視をオプトアウト | 人間によるレビューなし |
| データを日本に置けるか | 日本のテナントは製品条項の対象 | データ リージョンは米国・EU・指定なし |
| 会話の保持と検索 | Purviewの保持ポリシーとコンテンツ検索 | Vault、Geminiアプリの会話は管理者が保存の有無と期間を決める |

表の学習の行はMicrosoftはLearnの文言、Googleはプライバシー ハブの文言です。WorkspaceのGeminiアプリでこの扱いを受けるにはドメインの所有権の確認が条件で、詳しくは「[Google WorkspaceのGeminiとは](/media/google-workspace-gemini/)」の学習の節にあります。

保存場所では両者の差がはっきり出ます。Microsoftの[製品条項のデータ所在地](https://learn.microsoft.com/ja-jp/microsoft-365/enterprise/m365-dr-product-terms)は対象の国に日本を含み、Microsoft 365 CopilotとCopilot Chatもその対象のサービスです。**既定の地域が日本のテナントなら、Copilotとのやり取りも日本に保存される約束に入っています。**

Googleの[データ リージョンの管理者ヘルプ](https://knowledge.workspace.google.com/admin/compliance/choose-a-geographic-location-for-your-data?hl=ja)では、保管場所に選べるのは米国・欧州連合・指定なしの3つです。[データ リージョンの対象となるデータ](https://knowledge.workspace.google.com/admin/compliance/data-covered-by-data-regions?hl=ja)にはGeminiのプロンプトと回答も入っていますが、選べる場所に日本はなく、Starterはデータ リージョン自体の対象外です。

<figure class="post-figure"><img src="/media/images/copilot-vs-gemini/cvg_gws_dataregion.png" alt="Google Workspace管理者ヘルプのデータリージョンのページ。対応しているエディションの一覧の下に、保管場所には米国、欧州連合（管理コンソールではヨーロッパと表示）、指定なしのいずれかを選択できますと書かれている" loading="lazy"><figcaption>Google Workspace 管理者ヘルプ「データ リージョン」（2026年10月25日）</figcaption></figure>

社内の規程や取引先との契約でデータを国内に置くと決めている会社は、Workspaceの側ではその決まりを満たせません。選ぶ前に、法務や情報システムの担当と規程の文言を確かめておきましょう。

## 管理者が設定するところ

**どちらも、今の土台の管理画面でAIを管理するため、管理の場所は増えません。**Microsoftはライセンスの割り当てをMicrosoft 365管理センターで行い、従量課金の上限はCost Managementで決めます。モデルはLearnによるとOpenAIとAnthropicのものを使い、使うかどうかも管理者が決めます。割り当ての手順は「[Copilotのライセンスを割り当てる方法](/media/copilot-license-assign/)」で解説しました。

Googleは[Google管理コンソール](https://admin.google.com/)の［生成AI］［Geminiアプリ］で、Geminiアプリを使える人と会話履歴を残す期間を決めます。部署ごとに止める方法やGmailのGeminiを止められるエディションは「[Google WorkspaceのGeminiを無効化する方法](/media/google-workspace-gemini-admin/)」にまとめました。

## 両方使う会社の考え方

前の節のとおり、両社とも相手のデータとつなぐコネクタを公式に用意しています。上で触れたユースフルの動画でも、両方を使える会社から使い分けを聞かれることが多いと話されていました。

両方を入れると、費用が二重になるうえ、データの置き場所・社内の規程・監査ログの確かめ先も2つずつになります。**分けるなら、土台の側のAIを全員に、もう一方を一部の部署や仕事にだけ配るように、誰がどちらを使うかを先に決めておくと迷いが減ります。**配ったあとの使われ方の確かめ方は「[Copilotが社内で使われないときの調べ方](/media/copilot-adoption/)」で扱いました。

どちらを入れる場合も、個人で契約したAIに業務のデータを入れてよいかは、社内の規程で決めておきます。規程の作り方は「[シャドーAIの対策](/media/shadow-ai/)」が参考になります。

## 個人の無料版の違い

個人で使う無料のCopilotアプリとGeminiアプリは、どちらも会社の契約の外のサービスです。この記事の学習の扱い・保存場所・管理者の設定は会社向けの契約の話で、個人のアカウントには当てはまりません。

無料版どうしの使える回数は「[ChatGPT・Gemini・Claude・AIモード比較](/media/ai-compare/)」、個人のGeminiの有料プランは「[Geminiの料金プラン](/media/gemini-pricing/)」で扱っています。

## よくある質問

### CopilotとGeminiはどちらが安いですか？

年払いの1人の月額で、Workspace Business Standardは1,600円（税別）、Business StandardとCopilot Businessの組み合わせは3,523円（税抜）です。Microsoft 365の会社なら、増えるのは有料のCopilotの分だけです。

### CopilotとGeminiは同じAIですか？

同じではありません。CopilotはMicrosoftの製品でOpenAIとAnthropicのモデルを使い、GeminiはGoogleの製品でGoogleのモデルを使います。

### WorkspaceでCopilotは使えますか？

有料のCopilotはMicrosoft 365のライセンスに足す契約なので、Workspaceだけの会社では使えません。両方ある会社なら、GoogleドライブのCopilotコネクタでドライブのファイルを検索できます。

### Microsoft 365でGeminiは使えますか？

WorkspaceのGeminiはWorkspaceのアカウントで使うものです。SharePointやOutlookのデータとGeminiをつなぐ道として公式に案内されているのは、別の製品のGemini Enterpriseのコネクタです。

### CopilotとGeminiの入力は学習に使われますか？

会社向けの契約ならどちらも使われません。Copilotは基礎LLMのトレーニングに使わず、Workspaceは許可なくドメインの外でモデルのトレーニングに使わないと公式に書かれています。

### Geminiのデータは日本に保存できますか？

Workspaceのデータ リージョンで選べるのは米国・欧州連合・指定なしで、日本は選べません。日本に保存する約束が要るなら、日本のテナントのCopilotが製品条項の対象です。

### CopilotとGeminiは併用できますか？

できます。両社ともコネクタで相手のデータとつなぐ道を用意していますが、費用・データの置き場所・社内の規程は2つずつになります。

### Gemini EnterpriseとCopilotの違いは？

Gemini EnterpriseはAIエージェントを作って共有するためのGoogleの製品で、Workspaceのプランとは別の契約です。そのドキュメントにはSharePointやTeamsなどMicrosoftのサービスにつなぐコネクタも並んでいます。CopilotはMicrosoft 365のアプリの中で動くAIです。

## 出典

すべて2026年10月25日に取得。

- Google Workspace「[料金](https://workspace.google.com/intl/ja/pricing)」
- Google Workspace 管理者ヘルプ「[Business エディションの比較](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-business-editions?hl=ja)」
- Google Workspace 管理者ヘルプ「[Google Workspace の生成 AI に関するプライバシー ハブ](https://support.google.com/a/answer/15706919?hl=ja)」
- Google Workspace 管理者ヘルプ「[データ リージョン: データの地理的な保管場所を選択する](https://knowledge.workspace.google.com/admin/compliance/choose-a-geographic-location-for-your-data?hl=ja)」
- Google Workspace 管理者ヘルプ「[データ リージョン ポリシーの対象となるデータ](https://knowledge.workspace.google.com/admin/compliance/data-covered-by-data-regions?hl=ja)」
- Google Workspace 管理者ヘルプ「[Gemini Enterprise - Business エディションを追加して設定する](https://knowledge.workspace.google.com/admin/generative-ai/gemini-enterprise?hl=ja)」
- Google Cloud「[Gemini Enterprise のコネクタとデータストアの概要](https://cloud.google.com/gemini-enterprise/docs/connectors/introduction-to-connectors-and-data-stores?hl=ja)」
- Microsoft「[Teams が含まれる一般法人向けプランの価格](https://www.microsoft.com/ja-jp/microsoft-365/business/with-teams-plans-and-pricing)」
- Microsoft「[Microsoft Copilot Business の価格](https://www.microsoft.com/ja-jp/microsoft-365/copilot/business)」
- Microsoft「[法人向け Microsoft 365 Copilot の価格](https://www.microsoft.com/ja-jp/microsoft-365/copilot/enterprise)」
- Microsoft Learn「[Microsoft Copilot のライセンス オプション](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-licensing)」
- Microsoft Learn「[Microsoft Copilot Chat の概要](https://learn.microsoft.com/ja-jp/copilot/overview)」
- Microsoft Learn「[Microsoft Copilot のデータ、プライバシー、セキュリティ](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-privacy)」
- Microsoft Learn「[製品条項のデータ所在地](https://learn.microsoft.com/ja-jp/microsoft-365/enterprise/m365-dr-product-terms)」
- Microsoft Learn「[Google Drive connector overview](https://learn.microsoft.com/ja-jp/microsoftsearch/google-drive-overview)」
- Microsoft Learn「[Deploy the Google Drive connector](https://learn.microsoft.com/ja-jp/microsoftsearch/google-drive-connector)」
- Microsoft 365 Blog「[Expanding Copilot for Microsoft 365 to businesses of all sizes](https://www.microsoft.com/en-us/microsoft-365/blog/2024/01/15/expanding-copilot-for-microsoft-365-to-businesses-of-all-sizes/)」（2024年1月15日）
- GitHub Docs「[Using Gemini in GitHub Copilot](https://docs.github.com/ja/copilot/using-github-copilot/ai-models/using-gemini-in-github-copilot)」
- PC Watch「[Google Workspace、追加料金なしでGemini利用可能に。ただし3月から値上げ](https://pc.watch.impress.co.jp/docs/news/1654889.html)」（2025年1月16日）
- ユースフル「[GeminiとCopilotの正しい使い分け](https://www.youtube.com/watch?v=3l8t64BOKfI)」（YouTube）
