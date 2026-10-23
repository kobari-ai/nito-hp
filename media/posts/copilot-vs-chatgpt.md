---
title: 【2026年10月】CopilotとChatGPTの違い｜会社に入れるならどっち？料金・データ・管理
date: 2026-10-24
category: AI活用
description: Microsoft 365 CopilotとChatGPT Businessを会社に入れる前提で比べます。円と米ドルで違う料金と消費税、最低席数、Teams・Outlookとの連携、社内データへのつなぎ方、学習と保存場所、管理者の設定まで。
cover_tag: 導入担当向け
cover_headline: CopilotとChatGPTの違い
cover_sub: 料金・社内データ・管理で比べる
cta: ai_agent
---

MicrosoftのCopilot Businessの価格ページは、1人あたり月2,698円（年払い・税抜）と円で表示しています。OpenAIのビジネス向け料金ページでは、ChatGPT Businessの標準シートが1人あたり月20ドル（年額課金）です。どちらも2026年10月24日に開いたときの表示です。

1人あたりの金額は近くても、税の扱い・前提になる契約・社内データへの届き方は違います。この記事は会社でAIを入れる担当者に向けて、どちらを選ぶかの判断に要る違いを公式の資料で並べます。

:::takeaways
- すでにMicrosoft 365を使っている会社には**Copilot Chatが追加費用なしで入っている**。有料のCopilotは300人までならCopilot Business、それより多い会社やE3・E5の会社は法人向けのMicrosoft 365 Copilot
- **ChatGPT Businessは米ドル建てで、直接の購入には消費税10%が加わる**。2席から200席までで、データを日本に置けるのはEnterpriseだけ
- 違いの芯は社内データへの届き方。**Copilotは本人が開ける範囲のMicrosoft 365全体を読み、ChatGPTはSharePointなどをアプリでつなぎ、組織の設定によってはEntraの管理者の同意が要る**
:::

## 比べる相手を先にそろえる

「Copilot」と呼ばれる製品はいくつもあり、比べる相手を決めないと話がかみ合いません。会社で検討の対象になるのは、Microsoft 365の利用者に追加費用なしで付くCopilot Chatと、有料のCopilotの2段です。プログラミング用のGitHub Copilotは別の製品で、この記事では扱いません。

有料のCopilotは会社の規模で2つに分かれます。[Microsoft Learnのライセンスのページ](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-licensing)によると、**Copilot BusinessはMicrosoft 365 Businessのライセンスを持つ300人までの組織向けのアドオンで、法人向けと同じCopilotの機能を提供します**。300人を超える会社ではE3やE5などに足す法人向けのライセンスを使います。

LearnではMicrosoft 365 CopilotがMicrosoft Copilotに名前を変えたと書かれていますが、日本の価格ページは旧名のままなので、この記事は価格ページの名前で呼びます。

<figure class="post-figure"><img src="/media/images/copilot-vs-chatgpt/ccv_01_lineup.png" alt="会社で比べる5つの契約を縦に並べた図。Microsoft側はCopilot Chat（Microsoft 365に追加費用なし）、Copilot Business（300人まで）、法人向けMicrosoft 365 Copilot（E3・E5などに追加）、OpenAI側はChatGPT Business（2〜200席）とChatGPT Enterprise（営業経由）" loading="lazy"></figure>

ChatGPTの会社向けは、自分で申し込めるBusinessと、営業を通して契約するEnterpriseの2つです。[OpenAIのビジネス向け料金ページ](https://openai.com/ja-JP/business/pricing/)はBusinessを従業員数2〜200名のチーム向けとしています。両者の差は「[ChatGPT Enterpriseとは](/media/chatgpt-enterprise/)」に書いています。

## 料金と最低席数

MicrosoftとOpenAIでは、価格の通貨と税の書き方が違います。Microsoftの価格ページはどのカードにも「価格には消費税は含まれていません」と添えた円の表示です。OpenAIの料金ページは米ドルで、[日本の消費税のヘルプ](https://help.openai.com/ja-jp/articles/10242647)によると**OpenAIから直接買う場合は10%の消費税が請求され、適格請求書には税額が円で書かれます**。Enterpriseのような個別契約の法人は、一般にリバースチャージの扱いで消費税は請求されません。

| 契約 | 年払い（1人の月額） | 月払い（1人の月額） | 人数 |
|---|---|---|---|
| Copilot Chat | 追加費用なし | 追加費用なし | 対象のMicrosoft 365の利用者 |
| Copilot Business | 2,698円（表示は3,148円からの割引） | 3,778円 | 300人まで |
| 法人向けMicrosoft 365 Copilot | 4,497円 | 4,722円（年間契約の毎月払い） | 下限なし |
| ChatGPT Business 標準シート | 20ドル | 25ドル | 2〜200席 |
| ChatGPT Business プレミアムシート | 100ドル | 125ドル | 同上 |
| ChatGPT Enterprise | 非公開（営業に見積もり） | 同左 | 営業と決める |

Microsoftの金額は税抜、ChatGPTの金額は消費税の前の値です。[ChatGPTの料金ページ](https://chatgpt.com/ja-JP/pricing)のビジネス向けタブには、標準シートが3,050円（年額課金）・3,850円（月額課金）と円でも出ていました（2026年10月4日に確認）。2026年10月24日に開いた[ビジネス向けの料金ページ](https://openai.com/ja-JP/business/pricing/)では、スタンダードシートは年額課金で月20ドル、月額課金で月25ドルです。席の数え方は「[ChatGPT Businessとは](/media/chatgpt-business/)」にまとめています。

<figure class="post-figure"><img src="/media/images/copilot-vs-chatgpt/ccv_03_ms_business.png" alt="MicrosoftのCopilot Businessの価格ページで、利用中のMicrosoft 365プランに追加するMicrosoft 365 Copilot Businessのカード。3,148円に取り消し線が引かれて2,698円、ユーザー/月相当・年払い、価格には消費税は含まれていませんと書かれている" loading="lazy"><figcaption>Copilot Businessの価格ページ（2026年10月24日）</figcaption></figure>

**Copilotの金額はCopilotだけの値段で、土台になるMicrosoft 365のライセンスは別に要ります。**Copilot BusinessならBusiness BasicやBusiness Standardなど、法人向けならE3やE5などです。価格ページには土台とCopilotを組み合わせた価格もあり、Business Standardと組み合わせると年払いで月3,523円、月払いで4,228円です。ChatGPT Businessは単独で契約でき、Microsoft 365の有無は問いません。

<figure class="post-figure"><img src="/media/images/copilot-vs-chatgpt/ccv_04_ms_enterprise.png" alt="法人向けMicrosoft 365 Copilotの価格のカード。ユーザー/月相当・年払いで4,497円、または年間契約の毎月払いで4,722円、価格には消費税は含まれていません、条件を満たすMicrosoft 365プランのライセンスが別途必要ですと書かれている" loading="lazy"><figcaption>法人向けMicrosoft 365 Copilotの価格ページ（2026年10月24日）</figcaption></figure>

最低の席数は両者で逆の向きに決まっています。Copilotは[2024年1月のMicrosoftの発表](https://www.microsoft.com/en-us/microsoft-365/blog/2024/01/15/expanding-copilot-for-microsoft-365-to-businesses-of-all-sizes/)で300席の最低購入数がなくなり、1人から買えます。ChatGPT Businessは最低2席で、1つの契約の上限が200席です。

### 50人で入れたときの月額

年払いで50人に配ったときの月額です。Copilotの土台のライセンスは含めていません。

<figure class="post-figure"><img src="/media/images/copilot-vs-chatgpt/ccv_05_cost.png" alt="50人に配ったときの月額の目安を縦に並べた図。Copilot Businessは割引の表示で134,900円、定価で157,400円、法人向けMicrosoft 365 Copilotは224,850円でいずれも税抜。ChatGPT Business標準シートは1,000ドルで消費税を足すと1,100ドル" loading="lazy"></figure>

| 契約（年払い） | 50人の月額 | 消費税を足すと |
|---|---|---|
| Copilot Business（割引の表示） | 134,900円 | 148,390円 |
| Copilot Business（定価） | 157,400円 | 173,140円 |
| 法人向けMicrosoft 365 Copilot | 224,850円 | 247,335円 |
| ChatGPT Business 標準シート | 1,000ドル | 1,100ドル |

**Copilot Businessの割引は価格ページに終了日が書かれていないため、予算は定価の3,148円で組んでおくほうが安全です。**年払いと月払いの差も大きく、Copilot Businessは年払いの2,698円に対して月払いが3,778円です。Cowork・Autopilot・Work IQ APIなどの高度な機能は従量課金で、ライセンスとは別に請求されます。エージェントの費用は「[Copilot Studioの料金](/media/copilot-studio/)」で扱っています。

## Microsoft 365を使っているか

最初に確かめたいのは社員がすでにMicrosoft 365のアカウントで働いているかどうかです。[価格ページのFAQ](https://www.microsoft.com/ja-jp/microsoft-365/copilot/pricing)では、Copilot Chatは対象のMicrosoft 365プランの利用者に追加費用なしで含まれるWebを根拠にしたAIアシスタントと説明されています。**有料の契約を決める前に、社員はもう会社の管理下にあるAIチャットを持っている**ことになります。

[Copilot Chatの概要](https://learn.microsoft.com/ja-jp/copilot/overview)にある表では、何を根拠に答えるかが入口ごとに分かれています。

| 入口 | 何を根拠に答えるか |
|---|---|
| Copilot Chat（Web・アプリ） | Web、本人が渡したファイル、対応するアプリの文脈 |
| OutlookのCopilot Chat | 受信トレイ・予定表・会議・チャットと限られた関連の内容 |
| 有料のCopilot | Microsoft Graph、Work IQ、Microsoft 365全体の索引 |

Copilot Chatのままでは、Word・Excel・PowerPoint・OneNoteの中でCopilotのチャットは使えません。ファイルのアップロードや画像の生成はできますが、混んでいるときは有料の利用者が優先されます。

<figure class="post-figure"><img src="/media/images/copilot-vs-chatgpt/ccv_06_decide.png" alt="CopilotとChatGPTのどちらを入れるかを決める順番の図。1は社員がMicrosoft 365のアカウントで働いているか、2はCopilot Chatで足りない仕事が何か、3は読ませたい社内データがどこにあるか、4はデータを日本に置く決まりがあるか" loading="lazy"></figure>

Google Workspaceで働いている会社がCopilotを入れるなら、Microsoft 365のライセンスから買う必要があり、ChatGPT Businessのほうが手前で済むでしょう。ChatGPTの料金ページにも、BusinessでGoogle Workspace・Slack・GitHub・Microsoft 365などと連携できるとの記載があります。

Microsoft 365の会社なら、Copilot Chatで足りない仕事を書き出してから有料のCopilotを配る人を選ぶと無駄が出にくくなります。配ったあとの利用の確かめ方は「[Copilotが社内で使われないときの調べ方](/media/copilot-adoption/)」で扱いました。

## TeamsとOutlookの中で使えるか

有料のCopilotはアプリの中に入ります。Microsoftの価格ページに並ぶのは、Word・Excel・PowerPoint・Outlook・Teamsなどのアプリ内のCopilotと、Teamsのチャット・通話での利用です。[ユースフルの解説動画](https://www.youtube.com/watch?v=aTEpjYBMsjc)ではCopilot ChatだとOutlookの横のチャットで下書きを作って貼り付ける手間が残り、有料版だと返信欄に直接下書きが入る違いが実演されていました。

ChatGPTはChatGPTの画面で使うのが基本です。料金ページの比較表ではBusinessでExcel・PowerPoint・Googleスプレッドシートの拡張機能が標準で付き、Microsoft 365とつなぐアプリもあります。**1日の仕事がOutlookとTeamsの中で終わる人にはCopilotが近く、資料の下調べや長い文章を別の画面で練る人にはChatGPTの使い方が合います**。

## 社内データへのつなぎ方

**Copilotが答えに使う社内のデータは、本人が少なくとも閲覧できるものだけです。**[Learnのデータとプライバシーのページ](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-privacy)によると、メール・予定表・チャット・会議・文書にMicrosoft Graphを通して届き、SharePointなどの権限をそのまま守ります。裏返すと、全社に共有されたままの人事や給与のファイルがあれば答えの材料になり得るため、導入の前にSharePointの共有設定を見直しておく必要があります。

Microsoft 365の外のシステムをつなぐ仕組みが[Copilotコネクタ](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/connectors/overview)です。中身をMicrosoft Graphに取り込む同期型と、MCPを使ってその場で取りに行く取り込まない型があり、どちらも元のシステムの権限を守ります。

<figure class="post-figure"><img src="/media/images/copilot-vs-chatgpt/ccv_07_data.png" alt="社内データへの届き方の図。Copilotは本人が閲覧できるものだけをMicrosoft Graph経由で読み、外のシステムはCopilotコネクタでつなぐ。ChatGPTはつないだアカウントの権限の範囲をSharePointアプリで読み、設定によっては先にEntraの管理者の承認が要る" loading="lazy"></figure>

ChatGPTからMicrosoft 365のファイルを読むときは、[SharePointアプリ](https://help.openai.com/ja-jp/articles/12143177)を使います。対象は職場のSharePointとOneDriveで、個人用のOneDriveは対象外です。**組織で管理者の同意が必要な設定なら、先にMicrosoft Entraの管理者が権限を承認しないと使えません。**ヘルプはライブで読むためにSites.Read.AllとFiles.Read.Allを挙げ、ChatGPTのワークスペース管理者とEntraの管理者が別の人のことがあると書いています。

読める範囲はつないだMicrosoftアカウントの権限に従うので、権限の見直しが要るのはChatGPTでも同じです。アプリを有効にする手順は「[ChatGPTのコネクタの管理](/media/chatgpt-connectors-admin/)」で扱っています。

## 学習の扱いと保存場所

入力が学習に使われない点は、どちらの会社向けの契約でも公式に書かれています。差が出るのは保存場所と、管理者が会話をどう扱えるかです。

| 項目 | Copilot | ChatGPT Business | ChatGPT Enterprise |
|---|---|---|---|
| 入力を学習に使うか | 使わない | 既定で使わない | 既定で使わない |
| データを日本に置けるか | 日本のテナントは製品条項の対象 | 対象外 | 日本を含む10地域から選ぶ |
| 会話の保持と検索 | Purviewの保持ポリシーとコンテンツ検索 | 公式の比較表に記載なし | 管理者が保持期間を設定、Compliance API |

Copilotは[製品条項のデータ所在地](https://learn.microsoft.com/ja-jp/microsoft-365/enterprise/m365-dr-product-terms)の対象に、Microsoft 365 Copilotが2024年3月1日、Copilot Chatが2025年9月1日に加わりました。**既定の地域が日本のテナントなら、Copilotとのやり取りも日本に保存される約束に入っています。**ただしWebの検索に使う短い語句はBingに送られ、Microsoft 365とは別の扱いになると[エンタープライズ データ保護のページ](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/enterprise-data-protection)にあります。

ChatGPTでデータを日本に置けるのは、新しく導入するEnterpriseとEduです。Businessは料金ページの比較表でデータレジデンシーの対象外です。

<figure class="post-figure"><img src="/media/images/copilot-vs-chatgpt/ccv_09_learn_dr.png" alt="Microsoft Learnのデータ所在地のページ。対象の地域に日本が含まれ、ワークロードの表にMicrosoft 365 Copilotの追加日が2024年3月1日、Microsoft 365 Copilot Chatが2025年9月1日と書かれている" loading="lazy"><figcaption>Microsoft Learn「製品条項のデータ所在地」（2026年10月24日）</figcaption></figure>

**ChatGPT Businessのワークスペース管理者は、メンバーの会話履歴を閲覧・エクスポート・削除できると[エンタープライズ プライバシーのページ](https://openai.com/ja-JP/enterprise-privacy/)のBusinessのFAQにあります。**[Businessのデータ共有のヘルプ](https://help.openai.com/ja-jp/articles/8798634)が書いているのは、ほかのメンバーには会話が自動で表示されないことと、利用状況の分析や支出管理の画面から会話は見えないことです。管理者がどの画面から会話を開けるかはヘルプに手順が見当たらないため、社内規程で会話の監査が要る会社は、契約の前にOpenAIの営業かサポートに確かめておくべき項目です。

## 管理者が設定するところ

**Copilotは社員のMicrosoft 365のアカウントと権限をそのまま使うため、管理の場所が増えません。**ライセンスはMicrosoft 365管理センターで割り当て、エージェントは統合アプリの画面で許可し、従量課金はCost Managementで上限を決めます。割り当ての手順は「[Copilotのライセンスを割り当てる方法](/media/copilot-license-assign/)」にあります。

ChatGPTはMicrosoft 365とは別の管理コンソールを持ちます。料金ページの比較表で、BusinessとEnterpriseの差は次のとおりです。

| 機能 | ChatGPT Business | ChatGPT Enterprise |
|---|---|---|
| SAML SSO・ドメイン認証 | あり | あり |
| SCIM（アカウントの自動追加と削除） | なし | あり |
| ロールベースのアクセス制御 | なし | あり |
| IP許可リスト | なし | あり |
| Compliance API | なし | あり |

Entra IDとSAMLでつなげばBusinessでも会社のアカウントでサインインできますが、退職者のアカウントを自動で外すSCIMはEnterpriseだけです。SCIMの無いBusinessでは退職者をワークスペースの画面で外す運用になり、その手順は「[ChatGPT Businessのメンバー招待と管理](/media/chatgpt-business-admin/)」にまとめています。

## 両方入れる会社の例

全社でCopilotを買ったあとにChatGPTも使われるようになった例は報じられています。[Bloombergの2025年6月24日の記事](https://www.bloomberg.com/news/articles/2025-06-24/chatgpt-vs-copilot-inside-the-openai-and-microsoft-rivalry)によると、製薬のAmgenは前の年の春に2万人分のCopilotの購入を発表し、13か月後には社員がChatGPTを使っていました。同じ報道を伝えた[Tom's Guide](https://tomsguide.com/ai/microsoft-reportedly-struggling-to-convince-companies-to-buy-copilot-yup-employees-prefer-chatgpt)は、社員がChatGPTも使っていると書いています。

両方を入れると費用が二重になるうえ、社員が使う画面・データの保存場所・管理の画面も2つずつです。分けるなら、全員にはCopilot Chatを使ってもらい、資料づくりが多い部署にだけChatGPT Businessを配るように、誰がどちらを使うかを先に決めておくと迷いが減ります。**どちらを入れる場合も、個人で契約したAIに業務のデータを入れてよいかを社内の規程で決めておきます。**規程の作り方は「[シャドーAIの対策](/media/shadow-ai/)」が参考になります。

## 個人の無料版の違い

個人で使う無料のCopilotアプリとChatGPTの無料版は、どちらも会社の契約の外のサービスです。上の表の学習の扱い・保存場所・管理者の設定は会社向けの契約の話で、個人のアカウントには当てはまりません。

ChatGPTの無料版・Go・Plusでは「すべての人のためにモデルを改善する」の設定がオンだと、入力が学習に使われることがあると[接続済みアプリのヘルプ](https://help.openai.com/ja-jp/articles/11487775)にもあります。個人で使い続けるなら、設定を確かめておきましょう。手順は「[ChatGPTに学習させない設定方法](/media/chatgpt-training-off/)」にあります。

## よくある質問

### CopilotとChatGPTは同じAIですか？

同じではありません。CopilotはMicrosoftの製品で、Microsoft 365の権限とデータの上で動きます。ChatGPTはOpenAIの製品で、独自の画面とワークスペースを持ちます。

### Copilotの中身はChatGPTですか？

ChatGPTそのものではありません。LearnによるとCopilotはOpenAIのモデルを使い、Anthropicのモデルも管理者が許可すれば使えます。答えの根拠になる社内データの扱いはMicrosoftの契約に従います。

### CopilotとChatGPTはどちらが安いですか？

1人あたりの年払いではCopilot Businessが2,698円（税抜、割引の表示）、ChatGPT Businessが20ドル（消費税の前）で近い金額です。Copilotは土台のMicrosoft 365のライセンスが別に要るため、Microsoft 365を使っていない会社ではChatGPTのほうが安く済みます。

### CopilotはMicrosoft 365なしで使えますか？

有料のCopilotはBusiness BasicやE3などの対象のMicrosoft 365のライセンスがある人に足す契約なので、単独では買えません。Microsoft 365を使っていない会社は、そのライセンスからの契約です。

### Copilot Chatは無料で使えますか？

対象のMicrosoft 365プランを使っている人なら、追加費用なしで使えます。Webを根拠に答え、渡したファイルも読めるものの、Word・Excel・PowerPoint・OneNoteの中のCopilotのチャットには有料のCopilotが必要です。

### ChatGPTはSharePointのファイルを読めますか？

SharePointアプリを使えば読めます。組織で管理者の同意が必要な設定なら、先にMicrosoft Entraの管理者がSites.Read.AllやFiles.Read.Allなどの権限を承認しておく形です。

### CopilotとChatGPTの入力は学習に使われますか？

会社向けの契約ならどちらも使われません。Copilotのプロンプトと応答は基礎モデルの学習に使われず、ChatGPT BusinessとEnterpriseは既定で学習に使われない設定です。

### ChatGPTのデータは日本に保存できますか？

新しく導入するChatGPT EnterpriseとEduなら日本を選べます。Businessはデータレジデンシーの対象外です。

## 出典

すべて2026年10月24日に取得。ChatGPTの料金ページの円の表示だけ2026年10月4日に確認。

- Microsoft「[Microsoft Copilot Business の価格](https://www.microsoft.com/ja-jp/microsoft-365/copilot/business)」
- Microsoft「[法人向け Microsoft 365 Copilot の価格](https://www.microsoft.com/ja-jp/microsoft-365/copilot/enterprise)」
- Microsoft「[Microsoft Copilot の価格とよくある質問](https://www.microsoft.com/ja-jp/microsoft-365/copilot/pricing)」
- Microsoft Learn「[Microsoft Copilot のライセンス オプション](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-licensing)」
- Microsoft Learn「[Microsoft Copilot Chat の概要](https://learn.microsoft.com/ja-jp/copilot/overview)」
- Microsoft Learn「[Microsoft Copilot のデータ、プライバシー、セキュリティ](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-privacy)」
- Microsoft Learn「[Microsoft Copilot および Microsoft Copilot Chat におけるエンタープライズ データ保護](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/enterprise-data-protection)」
- Microsoft Learn「[製品条項のデータ所在地](https://learn.microsoft.com/ja-jp/microsoft-365/enterprise/m365-dr-product-terms)」
- Microsoft Learn「[Copilot connectors overview](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/connectors/overview)」
- Microsoft 365 Blog「[Expanding Copilot for Microsoft 365 to businesses of all sizes](https://www.microsoft.com/en-us/microsoft-365/blog/2024/01/15/expanding-copilot-for-microsoft-365-to-businesses-of-all-sizes/)」（2024年1月15日）
- OpenAI「[ビジネス向け料金](https://openai.com/ja-JP/business/pricing/)」
- ChatGPT「[料金](https://chatgpt.com/ja-JP/pricing)」ビジネス向けタブ
- OpenAI「[エンタープライズ プライバシー](https://openai.com/ja-JP/enterprise-privacy/)」
- OpenAI ヘルプセンター「[OpenAI の請求書における日本の消費税](https://help.openai.com/ja-jp/articles/10242647)」
- OpenAI ヘルプセンター「[ChatGPT Business でのデータ共有とプライバシーの管理](https://help.openai.com/ja-jp/articles/8798634)」
- OpenAI ヘルプセンター「[ChatGPT の SharePoint アプリと設定](https://help.openai.com/ja-jp/articles/12143177)」
- OpenAI ヘルプセンター「[ChatGPT の接続済みアプリ](https://help.openai.com/ja-jp/articles/11487775)」
- OpenAI ヘルプセンター「[ChatGPT のデータレジデンシーと推論レジデンシー](https://help.openai.com/ja-jp/articles/9903489-data-residency-and-inference-residency-for-chatgpt)」
- Bloomberg「[ChatGPT vs Copilot: Inside the OpenAI and Microsoft Rivalry](https://www.bloomberg.com/news/articles/2025-06-24/chatgpt-vs-copilot-inside-the-openai-and-microsoft-rivalry)」（2025年6月24日）
- Tom's Guide「[Microsoft reportedly struggling to convince companies to buy Copilot](https://tomsguide.com/ai/microsoft-reportedly-struggling-to-convince-companies-to-buy-copilot-yup-employees-prefer-chatgpt)」（2025年6月26日）
- ユースフル「[Copilotの無償版と有償版の差](https://www.youtube.com/watch?v=aTEpjYBMsjc)」（YouTube）
