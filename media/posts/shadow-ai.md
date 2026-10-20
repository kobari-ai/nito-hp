---
title: 【2026年10月】シャドーAI対策とは？会社がやること｜個人のChatGPT・社内ルール・検知
date: 2026-10-21
category: AI活用
description: シャドーAI対策をIPA・個人情報保護委員会・AI事業者ガイドラインと各社の公式ヘルプで解説。個人のChatGPTやGeminiで起きること、会社がやる5つの順番、誰が決めるか、移行とブロックでつまずく所まで。
cover_tag: 管理者向け
cover_headline: シャドーAI対策で会社がやること
cover_sub: 個人のChatGPT・社内ルール・検知・移行
cta: ai_agent
---

IPAが2026年1月に公表した「情報セキュリティ10大脅威 2026」で、AIの利用をめぐるサイバーリスクが組織向けの3位に初めて入りました。解説書は社員が個人で使うAIサービスを業務に使う状態をシャドーAIと呼び、会社がそれを認識できないこと自体もリスクに挙げました。

社員が個人のChatGPTに議事録や顧客の資料を貼っているかもしれないが、禁止すべきか会社で契約すべきか決めきれない、という担当者向けに、公的な資料と各社の公式ヘルプで会社がやることを順に書きます。

:::takeaways
- **会社の管理者は個人用ワークスペースに入れず、Businessでは統合も削除も求められない**
- IPAの解説書は、未許可のAIの禁止を、**シャドーAIを避けるためのAIサービス利用の検討の項目に置き、個人アカウントの業務利用の制限と並べている**
- **Defenderの自動ブロックが効くのは会社が登録した端末だけで、登録していない私物のスマホは残る**。移行は本人の操作が要るので、段取りを先に決める
:::

<figure class="post-figure"><img src="/media/images/shadow-ai/shai_00_steps.png" alt="シャドーAIに会社がやる5つの順番。使われているかを調べる、会社の契約を用意する、社内ルールを書く、止める、個人アカウントから移す" loading="lazy"></figure>

## シャドーAIとは

情報システムの部署が把握していないクラウドサービスを社員が使う状態は、以前からシャドーITと呼ばれてきました。[IPAの10大脅威 2026の解説書（組織編）](https://www.ipa.go.jp/security/10threats/omgdg50000008fi8-att/kaisetsu_2026_soshiki.pdf)は、職場にAIサービスが無い場合などに、社員が個人的に使っているAIサービスを業務に使うことをシャドーAIと書いています。**持ち出しが禁止されている業務データをAIに入力すれば情報漏えいにつながり、会社が個人アカウントの業務利用を認識できないこともリスクだ、というのがIPAの整理です。**

<figure class="post-figure"><img src="/media/images/shadow-ai/shai_01_ipa.png" alt="IPAの情報セキュリティ10大脅威2026の組織向けの表。3位のAIの利用をめぐるサイバーリスクは2026年の初選出" loading="lazy"><figcaption>IPA「情報セキュリティ10大脅威 2026」</figcaption></figure>

同じ解説書は米国のAI企業の調査として、生成AIにデータをコピーして貼り付けている利用者が77%いて、そのうち82%が組織に管理されていないアカウントからだったと紹介しています（米国のAI企業の調査です）。日本の会社では[総務省の令和7年版 情報通信白書](https://www.soumu.go.jp/johotsusintokei/whitepaper/ja/r07/html/nd112220.html)が、生成AIの活用方針を定めている企業は2024年度の調査で49.7%と書いています。中小企業では「方針を明確に定めていない」との回答が約半数でした。

## 個人アカウントで起きること

個人の契約は社員とサービスの会社との契約で、会社は当事者ではありません。OpenAIの[管理されたワークスペースのヘルプ](https://help.openai.com/en/articles/9672121)によると、1つのアカウントで個人用と仕事用のワークスペースを分けて持てますが、仕事用の権限で個人用の中には入れません。**ChatGPT Businessの管理者は、社員の個人用ワークスペースを統合させることも削除させることもできない、とヘルプに書かれています。**

入力した内容の扱いも、個人向けと会社向けで違います。2026年10月21日に各社の公式ページで確かめた内容を並べました。

| 項目 | 個人向け（ChatGPT・Gemini） | 会社向け（ChatGPT Business・Enterprise、WorkspaceのGemini） |
|---|---|---|
| モデルの学習 | ChatGPTは［すべての人のためにモデルを改善する］がオンなら使われる。Geminiは本人の設定で決まる | 既定では使わない。Workspaceは許可なくドメインの外で使わない |
| 人によるレビュー | Geminiはチャットの一部をレビューし、レビューしたものは最長3年保存 | WorkspaceのGeminiはレビューされない |

ChatGPTの個人向けの学習の設定は[データコントロールのヘルプ](https://help.openai.com/en/articles/7730893)、会社向けは[OpenAIのEnterprise privacy](https://openai.com/enterprise-privacy/)（2026年1月8日更新）によります。個人の設定の切り方は[ChatGPTに学習させない設定](/media/chatgpt-training-off/)にまとめました。Geminiは[Geminiアプリのプライバシー ハブ](https://support.google.com/gemini/answer/13594961?hl=ja)に、人間のレビュアーが確認したチャットはアクティビティを消しても消えず最長3年保存されるとあります。Workspaceの[Google Workspaceの生成AIに関するプライバシー ハブ](https://support.google.com/a/answer/15706919?hl=ja)には、人によるレビューも許可のない学習も無いと書かれていました。

個人情報が絡む場面について、[個人情報保護委員会の注意喚起](https://www.ppc.go.jp/news/careful_information/230602_AI_utilize_alert/)（2023年6月2日）は、個人情報取扱事業者が本人の同意なく個人データを含むプロンプトを入力し、それが応答の出力以外の目的で扱われれば、個人情報保護法の規定に違反する可能性があるとしています。**そのため、入力する前にサービスの会社が個人データを機械学習に使わないこと等を確かめるよう求めています。**社員の個人アカウントについてこの確認を会社が担保する手段はありません。

## 公的な資料が会社に求めること

IPAの解説書は対策を経営者層とシステム管理者・従業員に分けて並べ、[AI事業者ガイドライン](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/20260331_report.html)のAI利用者を想定したものだと断っています。

| 担う人 | IPAの解説書に並ぶ対策（シャドーAIに関わるもの） |
|---|---|
| 経営者層 | AIサービスの利用の検討、未許可のAIサービス利用の禁止、利用規定の整備、個人アカウントでの業務利用の制限、規程違反時の対応の明確化、学習から外すオプトアウト設定の徹底、契約時の約款の確認 |
| システム管理者・従業員 | IT資産と構成の管理、通信ログやCASBで管理されていないAIサービスの利用を把握、多要素認証、AI利用の講習、秘密情報を安易に入力しない |

**禁止の項目は「シャドーAI回避のため、AIサービス利用の検討」の下の1つです。**

総務省と経済産業省の[AI事業者ガイドライン（第1.2版）](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/20260331_report.html)（2026年3月31日公表）は、第5部でAI利用者に求めることを挙げています。個人情報を不適切に入力しないこと（U-4）と、機密情報を不適切に入力しないこと・提供者のセキュリティ上の留意点を守ること（U-5）が、社内ルールの柱になります。

## 会社がやる5つの順番

IPAの対策と各社の管理機能を、手を付ける順に並べ直しました。手順は公式の説明に沿って書いています。

### ① 使われているかを調べる

IPAが挙げる把握の手段は、通信ログとCASB（クラウドの利用を見張る仕組み）です。Microsoftの[Defender for Cloud Apps](https://learn.microsoft.com/ja-jp/defender-cloud-apps/release-note-archive)はアプリの一覧に生成AIの分類を持ち、ChatGPTなど社内で使われている生成AIのアプリを絞り込めます。検知の仕組みが無い会社なら、最初の一歩は経費精算に個人のサブスクが出ていないかの確認です。

<figure class="post-figure"><img src="/media/images/shadow-ai/shai_02_learn.png" alt="Microsoft Learnの検出されたアプリの管理のページ。アプリの承認を解除しても使用はブロックされず、ブロックするにはブロック スクリプトを生成すると書かれている" loading="lazy"><figcaption>Microsoft Learn「検出されたアプリを管理する」</figcaption></figure>

### ② 会社の契約を用意する

禁止を出す前に、使ってよいAIを決めて配ります。ChatGPT BusinessとEnterprise、Google WorkspaceのGemini、Microsoft Copilot Chatは、どれも会社のアカウントで入る点で個人の契約と違います。ChatGPT Businessの席の料金と個人のPlusとの差は[ChatGPT Businessとは](/media/chatgpt-business/)に書きました。

### ③ 社内ルールを書く

ルールに入れる項目はここまでの公的な資料から拾え、根拠ごとに並べると次の表のとおりです。

| 項目 | 根拠 |
|---|---|
| 使ってよいAIと契約の種類 | IPA（AIサービス利用の検討） |
| 個人アカウントの業務利用を制限する | IPA（個人アカウントの業務利用の制限） |
| 不適切に入れない情報（個人データ・機密情報） | 個人情報保護委員会、AI事業者ガイドライン U-4・U-5 |
| 学習のオプトアウトの設定 | IPA |
| 違反したときの対応と、誤って入れたときの報告先 | IPA（規程違反時の対応、被害を受けた後の対応） |
| 出力を確かめてから使う | IPA（ハルシネーション） |

### ④ 止める

Defender for Cloud Appsでアプリに非承認のタグを付けるだけでは使用はブロックされない、と[検出されたアプリの管理のページ](https://learn.microsoft.com/ja-jp/defender-cloud-apps/governance-discovery)に書かれています。**Defender for Endpointでクラウド保護とネットワーク保護を有効にしていれば、Defender for Endpointに登録した端末では、非承認にしたアプリが自動でブロックされます。**ブロックはデバイスグループごとに絞れるほか、ブロックの代わりに警告を出す形も選べます。Microsoftの無料のCopilot Chatを止める設定は[Copilot Chatを社内で止める方法](/media/copilot-chat-admin-block/)で扱いました。

### ⑤ 個人アカウントから移す

社員が仕事のメールアドレスで個人のChatGPTを使っている場合は、移し方を先に決めておくのが安全です。OpenAIの[既存のChatGPTアカウントを持つ社員の受け入れのヘルプ](https://help.openai.com/en/articles/10479654)にある違いをまとめました。

| 招待された先 | 社員に起きること |
|---|---|
| ChatGPT Business | 個人用ワークスペースを分けたままにするか統合するかを本人が選ぶ。管理者は統合も削除も求められない |
| ChatGPT Enterprise・Edu（認証済みのドメインで招待） | 個人用ワークスペースがあると、参加の前に移行の手順が出ることがある。統合するか、書き出して削除するか |
| 招待も承認された登録もない | 個人用ワークスペースはたいてい別のまま。Enterprise・Eduで自動のアカウント作成があると、仕事のメールでサインインしただけで移行の手順が出ることがある |



**統合すると個人用ワークスペースは使えなくなり、会社のワークスペースから個人用へ戻す手段はありません。**統合の操作の手順は[ChatGPT Businessのメンバー招待と管理](/media/chatgpt-business-admin/)にまとめました。

## 誰が決めて何にお金がかかるか

IPAの分け方に合わせると、決める人と費用の項目は次のようになります。金額は契約や席数で変わるので、項目だけ並べています。

| 決めること | 決める人 | お金や手間がかかるもの |
|---|---|---|
| 使ってよいAIと契約 | 経営者層 | 会社の契約の席代 |
| 社内ルールと罰則 | 経営者層 | ルール作りと周知の工数、必要なら専門家への相談 |
| 利用状況の把握とブロック | システム管理者 | 検知やブロックの仕組みのライセンス。今あるライセンスで何が使えるかを先に確かめる |
| 移行の段取り | システム管理者 | 社員ごとの移行の案内と問い合わせの対応 |
| 講習 | システム管理者 | 講習の準備と受講の時間 |

## 止めるときにつまずく所

### 禁止だけを出す

**IPAは職場でAIサービスの利用が無い場合などに、社員が個人のAIを業務に使うことがあると書いています。**

### 私物のスマホが残る

自動ブロックが効くのは会社がDefender for Endpointに登録した端末だけです。登録していない私物のスマホで個人のアプリを開く経路は残るため、ルールと講習で補う必要があります。

### 移行を本人任せにする

OpenAIのヘルプは招待を送る前に、社員が仕事のメールで個人・Plus・Proのアカウントを使っていないかを確かめるよう勧めています。同じヘルプによると、App StoreやGoogle Playで払ったサブスクは移行の流れで止まらない場合があり、ストアでの解約が別に要る場合があります。統合した自作のGPTは非公開になるため、共有していたものは共有し直しが必要です。

### ドメインを認証すれば片付くと考える

[ドメイン認証のヘルプ](https://help.openai.com/en/articles/8871611)によると、仕事のドメインを認証しても、既存の個人用ワークスペースは削除も統合もされません。個人のChatGPTアカウントまで制限できるのはヘルプがdomain claimingと呼ぶ別の手続きで、承認された用途に限り、サポートへの申請が要ります。Enterpriseには、仕事のメールで会社以外のワークスペースから外部アプリに新しくつなぐことを止める設定もあり、これもサポートへの依頼で有効にします。

## よくある質問

### シャドーAIはIPAの10大脅威で何位ですか？
組織向けの3位です。「情報セキュリティ10大脅威 2026」で、AIの利用をめぐるサイバーリスクとして初めて選ばれました。解説書の中でシャドーAIが名指しされています。

### 社員が個人のChatGPTに入れた内容は学習に使われますか？
個人向けのプランでは［すべての人のためにモデルを改善する］がオンなら学習に使われます。BusinessとEnterpriseは既定で学習に使いません。

### ChatGPTの管理者は個人の統合を強制できますか？
Businessではできません。OpenAIのヘルプによると、Businessの管理者は社員に個人用ワークスペースの統合も削除も求めることができず、統合するかは社員が選びます。Enterpriseで認証済みのドメインから招待した場合は、参加の前に統合するか書き出して削除するかの手順が出ることがあります。

### ChatGPTのドメイン認証で個人の会話は移りますか？
移りません。ドメインの認証だけでは個人用ワークスペースは削除も統合もされません。Enterpriseの招待や自動のアカウント作成で移行の手順が出たときに、統合を選んだ人の、移せる種類の内容だけが移ります。チャットを選んで移すことはできません。

### 個人のGeminiに入れた内容は人に見られますか？
見られることがあります。Geminiアプリのプライバシー ハブには、人間のレビュアーがチャットの一部をレビューし、レビューしたチャットは最長3年保存されるとあります。Google WorkspaceのGeminiは人によるレビューの対象になりません。

### DefenderでChatGPTの利用を見つけられますか？
通信のログをDefender for Cloud Appsにつないでいれば見つけられます。アプリの一覧に生成AIの分類があり、ChatGPTなどの利用を洗い出せます。非承認にしても、それだけではブロックされません。

### シャドーAIは個人情報保護法の違反になりますか？
個人情報取扱事業者が個人データを本人の同意なく入力し、出力以外の目的で扱われた場合は、違反になる可能性があると個人情報保護委員会が書いています。入力の前に、サービスの会社が機械学習に使わないこと等を確かめるよう求めています。

### シャドーAIの社内ルールに罰則は要りますか？
IPAの解説書は経営者層の対策に規程違反時の対応（ペナルティ）の明確化を挙げています。誤って入力したときの報告先も合わせて決めておけば、事故の後に誰へ知らせるかで迷いません。

## 出典

- IPA「[情報セキュリティ10大脅威 2026](https://www.ipa.go.jp/security/10threats/10threats2026.html)」（2026年1月29日公開、2026年10月21日取得）
- IPA「[情報セキュリティ10大脅威 2026 解説書（組織編）](https://www.ipa.go.jp/security/10threats/omgdg50000008fi8-att/kaisetsu_2026_soshiki.pdf)」（2026年3月12日公開、2026年10月21日取得）
- 総務省「[令和7年版 情報通信白書 企業におけるAI利用の現状](https://www.soumu.go.jp/johotsusintokei/whitepaper/ja/r07/html/nd112220.html)」（同）
- 個人情報保護委員会「[生成AIサービスの利用に関する注意喚起等について](https://www.ppc.go.jp/news/careful_information/230602_AI_utilize_alert/)」（2023年6月2日公表、同）
- 総務省・経済産業省「[AI事業者ガイドライン（第1.2版）](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/20260331_report.html)」（2026年3月31日公表、同）
- OpenAI「[Enterprise privacy at OpenAI](https://openai.com/enterprise-privacy/)」（同）
- OpenAI Help Center「[Data controls in ChatGPT](https://help.openai.com/en/articles/7730893)」（同）
- OpenAI Help Center「[Getting started with OpenAI identity and access for managed workspaces](https://help.openai.com/en/articles/9672121)」（同）
- OpenAI Help Center「[Onboarding employees with existing ChatGPT accounts](https://help.openai.com/en/articles/10479654)」（同）
- OpenAI Help Center「[Verifying your domain for OpenAI identity](https://help.openai.com/en/articles/8871611)」（同）
- Google「[Geminiアプリのプライバシー ハブ](https://support.google.com/gemini/answer/13594961?hl=ja)」（同）
- Google「[Google Workspaceの生成AIに関するプライバシー ハブ](https://support.google.com/a/answer/15706919?hl=ja)」（同）
- Microsoft Learn「[Microsoft Defender for Cloud Appsの過去の更新プログラムのアーカイブ](https://learn.microsoft.com/ja-jp/defender-cloud-apps/release-note-archive)」（同）
- Microsoft Learn「[検出されたアプリを管理する](https://learn.microsoft.com/ja-jp/defender-cloud-apps/governance-discovery)」（同）
