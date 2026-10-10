---
title: 【2026年10月】WorkspaceのGeminiを無効化する方法 管理コンソール・組織部門・Gmail
date: 2026-10-10
category: AI活用
description: Google WorkspaceのGeminiを管理者が止める・許可する方法を管理者ヘルプで解説。Geminiアプリのオンとオフ、Gmailなどで止められるエディション、組織部門ごとの設定、日本の既定の状態、利用者の見え方まで。
cover_tag: 法人
cover_headline: WorkspaceのGeminiを止める
cover_sub: 管理コンソール・組織部門・既定の状態
---

Google Workspaceの管理コンソールには、Geminiを止めるスイッチが1つではなく、Geminiアプリ・Gmailなどの中のGemini・Workspaceとの連携の3か所に分かれています。しかもGmailやドキュメントの中のGeminiをアプリごとに止める設定は、管理者ヘルプの対応エディションにBusinessが入っていません。

試す部署を絞りたい管理者が迷うのは、**どのスイッチが何を止めるのかがヘルプの別々のページに書かれている**ためです。この記事は2026年10月10日に取得した管理者ヘルプとGeminiアプリ ヘルプをもとに、止める場所と手順・組織部門ごとの分け方・日本の既定の状態・利用者の画面・データの扱いを説明します。

<figure class="post-figure"><img src="/media/images/google-workspace-gemini-admin/gwa_00_overview.jpg" alt="管理コンソールの3つのスイッチと題した図。管理画面のパネルに、Geminiアプリ、GmailなどのGemini（Enterpriseのみ）、Workspaceとの連携の3つのスイッチが縦に並び、3つともオンになっている" loading="lazy"><figcaption>Geminiを止める設定は3か所に分かれている。どれも最初はオン</figcaption></figure>

:::takeaways
- Geminiアプリは**［生成AI］［Geminiアプリ］の［サービスのステータス］**で切り替える
- GmailなどのGeminiをアプリごとに止める［機能へのアクセス］は、**対応エディションにBusinessが含まれない**
- ドメインの拠点が日本の組織は**スマート機能が既定でオフ**で、GmailなどのGeminiは管理者か利用者がオンにするまで動かない
- Geminiアプリと［Gemini for Workspace］の設定は組織部門かグループごとに分けられ、**グループの設定が組織部門より優先**される。Geminiアプリの設定の反映は最長24時間
- **ライセンスの無い人に使わせる設定をオンにすると、その人には個人と同じ規約が適用される**
:::

## 管理者が止められる3つの範囲

「Geminiをオフにしたのに、Gmailにはまだ出る」という相談は、止めた場所と出ている場所が違うときに起きます。管理者ヘルプはgemini.google.comで会話するGeminiアプリと、GmailやドキュメントなどWorkspaceのアプリの中で動くGeminiを別のサービスとして扱っています。**Geminiアプリの設定はWorkspaceのアプリの中のAI機能に影響しない**と、ヘルプにも書かれています。

| 止めたいもの | 管理コンソールの場所 | 既定 | 対応エディション |
|---|---|---|---|
| Geminiアプリ（ウェブ・スマホ・Chrome・Mac） | ［生成AI］［Geminiアプリ］［サービスのステータス］ | オン | Business・Enterpriseのほとんど |
| Gmail・ドキュメント・Meetなどの中のGemini | ［生成AI］［Gemini for Workspace］［機能へのアクセス］ | オン | Enterprise Standard・Enterprise Plusなど |
| GeminiアプリからGmailやドライブを読む連携 | ［生成AI］［Geminiアプリ］［アプリ］ | オン | Geminiアプリを使えるエディション |

このほか、旧NotebookLMのGemini Notebookは［生成AI］［Gemini Notebook］、MeetのAIによるメモ作成は［アプリ］［Google Workspace］［Google Meet］の［Gemini の設定］と、それぞれ別の場所です。Geminiのベータ版の機能は既定でオフで、管理者がオンにしない限り組織では使えません。

## Geminiアプリをオンまたはオフにする手順

Geminiアプリに含まれるのはgemini.google.comのウェブアプリ・AndroidとiOSのGeminiアプリ・Gemini in Chrome・MacのGeminiです。管理者ヘルプ「[Gemini アプリをオンまたはオフにする](https://knowledge.workspace.google.com/admin/generative-ai/gemini-app/turn-the-gemini-app-on-or-off?hl=ja)」によると、ライセンスが割り当てられた18歳以上のユーザーは**最初からGeminiアプリを使える状態**です。この設定を変えるにはGeminiの「設定」の管理者権限が要ります。

1. [Google管理コンソール](https://admin.google.com/)のメニューから［生成AI］［Geminiアプリ］に進む
2. ［サービスのステータス］を押す
3. 全員を止めるなら［オフ（すべてのユーザー）］を選ぶ（戻すときは［オン（すべてのユーザー）］）
4. 一部の人だけに適用するなら、横の一覧から組織部門かグループを選んでから切り替える
5. ［保存］を押す

<figure class="post-figure"><img src="/media/images/google-workspace-gemini-admin/gwa_01_app_status.jpg" alt="Google Workspace管理者ヘルプのGeminiアプリをオンまたはオフにする節。Androidで使うには検索とアシスタントのサービスをオンにする注意、管理コンソールの生成AIからGeminiアプリに移動する手順があり、サービスのステータスと、オフ（すべてのユーザー）の2か所が赤枠で囲まれている" loading="lazy"><figcaption>管理者ヘルプの手順（2026年10月10日）。赤枠の2か所を順に押す</figcaption></figure>

保存してから利用者の画面に反映されるまでは**最長で24時間ほど**かかるため、止めた直後に社員の画面でまだ使えても設定の誤りとは限りません。Androidで使わせるなら、別のサービスの［検索とアシスタント］もオンにしておきます。

### 使える人を広げる設定の注意

同じ［Geminiアプリ］の画面にある［ユーザー アクセス］は、止める設定ではなく広げる設定です。［ライセンスの有無にかかわらず、すべてのユーザーに Gemini アプリへのアクセスを許可］にチェックを入れると、Workspaceのライセンスを持たない人もGeminiアプリを使えるようになります。

<figure class="post-figure"><img src="/media/images/google-workspace-gemini-admin/gwa_02_user_access.jpg" alt="管理者ヘルプのGeminiアプリを使用できるユーザーを選択する節。既定ではライセンスが割り当てられた18歳以上のユーザーが使えること、この設定はgemini.google.com、モバイルアプリ、Gemini in Chromeへのアクセスを管理しWorkspaceのほかのAI機能には影響しないという注意、ユーザーアクセスの手順が並び、ライセンスの有無にかかわらず全員に許可するチェックボックスの行が赤枠" loading="lazy"><figcaption>［ユーザー アクセス］のチェックボックス（2026年10月10日）</figcaption></figure>

対象のエディションを持たない人がGeminiアプリを使うと、Workspaceの規約ではなく**Googleの利用規約とGeminiアプリのプライバシーに関するお知らせが適用**されます。その場合のチャットは人のレビュアーによるレビューや、Googleの製品と機械学習の改良に使われることがあると同じヘルプに書かれています。会社のデータを守る目的なら、このチェックは外したままにします。

## GmailやドキュメントのGeminiを止める方法

Gmailの右上のGeminiのアイコンやドキュメントのサイドパネルは、Geminiアプリをオフにしても消えません。こちらは［Gemini for Workspace］の側の設定です。

### Enterpriseの機能へのアクセス

管理者ヘルプ「[Workspace サービスでの Gemini 機能へのアクセスを管理する](https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini/manage-access-to-gemini-features-in-workspace-services?hl=ja)」の手順では、［生成AI］［Gemini for Workspace］の［機能へのアクセス］で、アプリごとに［編集］から［オン］か［オフ］を選んで保存します。対象はGmail・カレンダー・ドライブとドキュメント類・Meet・チャット・Workspace Studioで、既定はオンです。

<figure class="post-figure"><img src="/media/images/google-workspace-gemini-admin/gwa_03_feature_access.jpg" alt="管理者ヘルプのWorkspaceサービスでのGemini機能へのアクセスを管理するページの冒頭。対応エディションがEnterprise Standard、Enterprise Plus、Teaching and Learningアドオン、Education Plus、Google AI Pro for Educationであることと、WorkspaceサービスでのGemini機能のデフォルト設定はオンであることの2か所が赤枠。対象のサービスとしてGmail、カレンダー、ドライブとドキュメント類、Meet、チャット、Workspace Studioが並ぶ" loading="lazy"><figcaption>対応エディションと既定の状態（2026年10月10日）</figcaption></figure>

**このページの対応エディションはEnterprise StandardとEnterprise Plus、教育機関向けの一部だけです。**あるアプリでGeminiを止めても、ほかのアプリのGeminiからそのデータを読める点にもヘルプは注意を促しています。たとえばドライブのGeminiをオフにしても、GmailのGeminiにはドライブのファイルについて質問できます。そのデータをGeminiに読ませたくないなら、アプリの中のGeminiを止めるだけでなく、すべてのアプリで止めるか、ファイルの側で閲覧を制限します。

### Businessで止めたいとき

2025年2月時点の販売代理店の記事も、Businessエディションでは［機能へのアクセス］が表示されず、サイドパネルを制御できないと案内しています。

Businessで打てる手は、次の節のスマート機能の既定の設定です。ただしこれは利用者が自分で変えられるので、強制的に止める手段にはなりません。アプリの中のGeminiを部署ごとに確実に止めたいなら、Enterpriseへの切り替えを検討することになります。

## 日本の組織の既定の状態

GmailなどのGeminiが動く条件は、利用者の［Google Workspace のスマート機能］がオンになっていることです。［機能へのアクセス］のヘルプにも「注: Gemini in Workspace を利用するには、スマート機能とカスタマイズを有効にする必要があります。」と書かれています。管理者ヘルプ「[ユーザー向けに Google Workspace のスマート機能を管理する](https://knowledge.workspace.google.com/admin/security/manage-google-workspace-smart-features-for-your-users?hl=ja)」は、この設定の既定が地域で違うと書いています。

<figure class="post-figure"><img src="/media/images/google-workspace-gemini-admin/gwa_04_smart_japan.jpg" alt="管理者ヘルプの重要という注記が赤枠で囲まれている。Workspaceのスマート機能とコントロールは、ドメインの拠点が欧州経済領域、日本、スイス、英国にある場合はデフォルトでオフ、その他の地域ではオン。管理者はこのデフォルト設定を全員に適用するかを決められるが、ユーザーは各自の設定で上書きできる" loading="lazy"><figcaption>スマート機能の既定は地域で違う（2026年10月10日）</figcaption></figure>

**ドメインの拠点が日本にある組織では、スマート機能が最初からオフです。**そのため契約しただけでは、GmailやドキュメントのGeminiは管理者か利用者がオンにするまで動きません。社員から「スマート機能を両方オンにしてと出る」と聞かれるのはこのためで、利用者側の手順は[スマート機能の設定を両方ともオンにする方法](/media/gmail-smart-features-on/)で説明しています。

管理者は［アカウント］［アカウント設定］［Google Workspace のスマート機能］で、既定のオンかオフを全員に適用できます。操作できるのは特権管理者だけです。ただし利用者は後から自分の設定で切り替えられるので、ここで止めても社員がオンに戻せば使えます。個人の側でGmailのGeminiを止める手順は[GmailのGeminiをオフにする方法](/media/gmail-gemini-off/)にまとめました。

## 組織部門とグループで分ける

全社で一度に止めるか許可するかを決めなくても、試す部署から始められます。Geminiアプリと［Gemini for Workspace］の設定には、画面の横に組織部門とグループを選ぶ一覧があります。組織部門は主に部署に使う単位で、グループは部署をまたいで人を集める単位です。

両方に設定があると、**グループの設定が組織部門の設定より優先**されます。たとえば会社全体の組織部門ではGeminiアプリをオフにし、試験導入のグループだけオンにすると、そのグループの人は所属の部署に関係なく使えます。逆に、グループでオフにした人は部署の設定がオンでも使えません。

止めたつもりの人が使えている、というときは、その人が許可したグループに入っていないかを先に見ます。Geminiアプリの設定を変えたあとは最長24時間待ってから確かめてください。組織の利用状況は［生成AI］［Gemini レポート］［組織レベルの使用状況］で、組織部門やグループごとのアクティブなユーザーの数を見られます。

試す部署で使い方が固まったあと、業務の一部をAIに任せる仕組みまで作るときの進め方は、[AIエージェント構築支援](/ai-agent/)のページにまとめました。

## Workspaceとの連携と会話履歴

利用者が許可すると、GeminiアプリはGmail・ドライブ・カレンダーなどの中身を探して答えます。管理者ヘルプ「[Gemini アプリによる Workspace サービスへのアクセスを制御する](https://knowledge.workspace.google.com/admin/generative-ai/gemini-app/turn-google-apps-in-gemini-on-or-off?hl=ja)」によると、この連携は既定でオンで、［Geminiアプリ］の［アプリ］から［Workspace アプリ］を切り替えます。マップやYouTubeなどの扱いは［その他の Google アプリ］という別の項目です。

Geminiアプリは使わせてもメールやファイルを読ませたくないなら、この連携だけをオフにします。

<figure class="post-figure"><img src="/media/images/google-workspace-gemini-admin/gwa_05_history.jpg" alt="管理者ヘルプのGeminiとの会話履歴を管理する節。会話履歴がオフのときユーザーは以前の会話にアクセスできず、会話は最長72時間ほど保存されること、会話履歴がオフのときWorkspaceアプリの連携は使えないこと、会話履歴の設定は管理者だけが変更でき既定でオンであることが書かれ、最後の文が赤枠。手順では保持期間を3か月、18か月、36か月から選び、デフォルトは18か月" loading="lazy"><figcaption>Geminiアプリの会話履歴の設定（2026年10月10日）</figcaption></figure>

会話履歴は［Gemini 会話履歴］で決め、**既定はオンで18か月たつと自動で消えます。**保存期間は3か月・18か月・36か月から選べます。オフにすると利用者は過去の会話を開けず、Gmailやドライブとの連携も止まります。反映は最長72時間です。

サイドパネルのGeminiの履歴は、［Gemini for Workspace］の［会話の履歴と削除］で別に決めます（Business Starterから）。

## 止めたときの利用者の画面

Geminiアプリを止めると、その人はgemini.google.com・スマホのアプリ・Gemini in Chromeで仕事用のアカウントのGeminiを使えなくなります。止めていないアプリの中のGeminiはそのまま残るため、Gmailのサイドパネルが消えるわけではありません。

<figure class="post-figure post-figure--sp"><img src="/media/images/google-workspace-gemini-admin/gwa_06_user_error.jpg" alt="Geminiアプリ ヘルプのGeminiモバイルアプリのエラーメッセージのトラブルシューティング。仕事用または学校用のアカウントでエラーが出たら、まずGeminiアプリが最新か確かめ、次にGoogle Workspace管理者に問い合わせてGeminiアプリへのアクセス権があるかを確認する、という2番目の手順が赤枠" loading="lazy"><figcaption>利用者向けのヘルプの案内（2026年10月10日、スマホ）</figcaption></figure>

仕事用のアカウントでスマホのアプリにエラーが出たら、アプリを最新にしたうえで管理者にアクセス権を確かめるよう、利用者向けのGeminiアプリ ヘルプは案内しています。**止める前に社員がどこに問い合わせればよいかを周知しておく**と、管理者への個別の問い合わせが減ります。

Workspaceのライセンスが割り当てられていない人には、Workspaceのアプリとの連携が出てきません。解説動画ではCloud Identity Freeのアカウントの例で、［ディレクトリ］［ユーザー］から［ライセンス］を開いて割り当てを確かめる手順が紹介されていました。

## スマホとChromeのGemini

スマホのGeminiアプリには、管理コンソールに専用の設定がありません。**会社のアカウントでスマホのアプリだけを止めたいときは、デバイス管理でGeminiアプリをブロック**します。Androidの仕事用プロファイルでGeminiアプリを開いた場合の行き先は、ブラウザのgemini.google.comです。Businessのエディションでスマホのアプリを使うには、ビジネス用のメールアドレスでの登録かドメインの所有権の証明が要ります。

Gemini in Chromeの対象は、米国でChromeにログインし既定の言語が英語（米国）の18歳以上の人です。Chrome EnterpriseのGeminiSettingsのポリシーを使えば、Gemini in Chromeだけを止められます。

## 入力したデータの扱い

データの扱いを確かめてから、止めるか許可するかを決めても遅くありません。Workspaceのコアサービスとして使うGeminiアプリについて、管理者ヘルプは**利用者のコンテンツが人にレビューされることも、許可なくドメイン外で生成AIモデルの学習に使われることもない**としています。

管理者ヘルプの[Business に関するよくある質問](https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini/gemini-for-google-workspace-faq-business?hl=ja)には、プロンプトと生成物はWorkspaceのコンテンツと一緒に保存され、組織の外に共有されないとあります。データ損失防止（DLP）など組織で設定済みの制御も、Geminiとのやり取りに自動で適用されます。保存期間の一覧は[生成 AI に関するプライバシー ハブ](https://knowledge.workspace.google.com/admin/generative-ai/generative-ai-in-google-workspace-privacy-hub?hl=ja)の表です。

<figure class="post-figure"><img src="/media/images/google-workspace-gemini-admin/gwa_07_retention.jpg" alt="プライバシーハブのGeminiデータの保持の表。Gemini in Workspaceはプロンプトと回答を90日から無期限まで管理者が設定し、管理者が禁止していなければユーザーが手で削除でき、VaultでWorkspaceデータの保持を管理できる。Geminiアプリは最大36か月まで管理者が設定する。Gemini Notebookはセッション終了後に保持されない" loading="lazy"><figcaption>プライバシーハブのGeminiデータの保持の表（2026年10月10日）</figcaption></figure>

組織で記録を残す必要があるなら、Google Vaultが使えます。Vaultのヘルプによると、**Geminiアプリのメッセージは保持・記録保持・検索・書き出しの対象**で、Vaultの権限を持つ人はアカウントや組織部門を指定して会話を検索できます。使うには管理者と対象の人の両方にVaultを含むライセンスが要り、エディションに含まれていないなら、アドオンの対象は営業担当に確かめます。

プランごとの料金や上限、個人のGoogle AI Proとの違いは[Google WorkspaceのGeminiとは](/media/google-workspace-gemini/)にまとめました。

## よくある質問

### WorkspaceのGeminiは無効化できますか？

できます。Geminiアプリは［生成AI］［Geminiアプリ］［サービスのステータス］でオフにします。GmailなどのGeminiをアプリごとに止める［機能へのアクセス］は、Enterprise StandardとEnterprise Plusなどに限られます。

### BusinessでGmailのGeminiを止められますか？

管理コンソールでアプリごとに止める設定は、Businessにはありません。スマート機能の既定をオフにして全員に適用しても、利用者が自分でオンに戻せます。

### Geminiのオフはいつ反映されますか？

Geminiアプリのオンとオフは最長24時間で、ふつうはもっと早く反映されます。会話履歴の設定は最長72時間です。

### Geminiを一部の部署だけで使えるようにできますか？

できます。設定の画面の横で組織部門かグループを選び、その単位でオンとオフを分けてください。両方に設定があるとグループが優先されます。

### Geminiアプリをオフにすると社員の画面はどうなりますか？

gemini.google.com・スマホのアプリ・Gemini in Chromeで仕事用のアカウントのGeminiを使えなくなります。GmailなどのGeminiは別の設定なので、こちらは消えません。

### 管理者はGeminiの会話を見られますか？

管理コンソールのGeminiレポートで分かるのは、使っている人の数や1日の使用量と、［ユーザーレベルの使用状況］での利用者ごとの使用レベル（高・中・低・ゼロ）とアクティブな日数です。Geminiアプリの会話は、Vaultの権限を持つ人が検索して書き出せます。Vaultを含むライセンスが要ります。

### WorkspaceのGeminiの入力は学習されますか？

コアサービスとして使う場合、人によるレビューも、許可なくドメイン外でモデルの学習に使われることもありません。ライセンスの無い人に許可した場合は個人と同じ規約になり、会話が改良に使われることがあります。

### スマホのGeminiアプリを会社で止められますか？

止められます。スマホのアプリ専用の設定はないので、デバイス管理でGeminiアプリをブロックします。Geminiアプリのサービスをオフにすれば、ウェブと一緒にスマホでも使えません。

## 出典

ヘルプは2026年10月10日に取得しました。管理コンソールの項目名はヘルプの表記に合わせています。

- Google Workspace 管理者ヘルプ「[Gemini アプリをオンまたはオフにする](https://knowledge.workspace.google.com/admin/generative-ai/gemini-app/turn-the-gemini-app-on-or-off?hl=ja)」
- Google Workspace 管理者ヘルプ「[Workspace サービスでの Gemini 機能へのアクセスを管理する](https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini/manage-access-to-gemini-features-in-workspace-services?hl=ja)」
- Google Workspace 管理者ヘルプ「[ユーザー向けに Google Workspace のスマート機能を管理する](https://knowledge.workspace.google.com/admin/security/manage-google-workspace-smart-features-for-your-users?hl=ja)」
- Google Workspace 管理者ヘルプ「[Gemini アプリによる Workspace サービスへのアクセスを制御する](https://knowledge.workspace.google.com/admin/generative-ai/gemini-app/turn-google-apps-in-gemini-on-or-off?hl=ja)」
- Google Workspace 管理者ヘルプ「[Gemini in Workspace との会話の履歴の設定を管理する](https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini/manage-gemini-in-workspace-conversation-history-settings?hl=ja)」
- Google Workspace 管理者ヘルプ「[組織での Gemini の使用状況を確認する](https://knowledge.workspace.google.com/admin/generative-ai/review-gemini-usage-in-your-organization?hl=ja)」
- Google Workspace 管理者ヘルプ「[Google Workspace with Gemini for Business に関するよくある質問](https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini/gemini-for-google-workspace-faq-business?hl=ja)」
- Google Workspace 管理者ヘルプ「[Google Workspace の生成 AI に関するプライバシー ハブ](https://knowledge.workspace.google.com/admin/generative-ai/generative-ai-in-google-workspace-privacy-hub?hl=ja)」
- Google Workspace 管理者ヘルプ「[ユーザーに対して Gemini Notebook を有効または無効にする](https://knowledge.workspace.google.com/admin/generative-ai/gemini-notebook/turn-gemini-notebook-on-or-off-for-users?hl=ja)」
- Google Workspace 管理者ヘルプ「[Google Meet の AI がユーザーに代わってメモを作成できるようにする](https://knowledge.workspace.google.com/admin/meet/let-google-meet-ai-take-notes-for-my-users?hl=ja)」
- Google Workspace 管理者ヘルプ「[Google Workspace with Gemini ベータ版へのアクセスを有効または無効にする](https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini/turn-access-to-google-workspace-with-gemini-beta-on-or-off?hl=ja)」
- Google Vault ヘルプ「[Google Vault](https://support.google.com/vault/answer/2462365?hl=ja)」「[Vault を使用して Gemini アプリを検索する](https://knowledge.workspace.google.com/vault/search/use-vault-to-search-gemini-app?hl=ja)」
- Gemini アプリ ヘルプ「[仕事用または学校用の Google アカウントで Gemini アプリを利用する](https://support.google.com/gemini/answer/14620100?hl=ja)」
- フライト「[Google Workspace に標準搭載された Gemini の管理コンソール上の設定について](https://clo-support.flight.co.jp/hc/ja/articles/43732620397465)」
- YouTube「[WorkspaceでGemini拡張機能を今すぐ使えるようにする方法](https://www.youtube.com/watch?v=5M5aYaYNo9Q)」（こーすけ先生のGoogle塾）
