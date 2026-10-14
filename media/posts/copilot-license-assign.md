---
title: 【2026年10月】Copilotのライセンスを割り当てる方法｜グループ・反映時間・使えないとき
date: 2026-10-15
category: AI活用
description: Microsoft 365 Copilotのライセンスを管理センターで割り当てる手順を公式ドキュメントから解説。グループでの割り当て、表示まで最大24時間かかる場合、割り当てたのにCopilotが出ないときに見る順番まで。
cover_tag: 管理者向け
cover_headline: Copilotのライセンスの割り当て
cover_sub: グループ・反映時間・使えないとき
---

Microsoft 365 Copilotのライセンスは、Microsoft 365 管理センターの［課金］＞［ライセンス］から、1人ずつかグループ単位で割り当てます。Microsoftのドキュメントには、割り当てたあとWordやExcelにCopilotが表示されるまで、一部のアプリでは最大24時間かかる場合があると書かれています。

導入の担当者がつまずきやすいのは、割り当てたのにCopilotが出ないと利用者に言われたときです。原因は管理センターの設定のほか、利用者のアカウントや更新チャネル、社内の回線にもあります。この記事では2026年10月15日に取得したMicrosoft LearnとMicrosoftサポートの記事をもとに、割り当ての手順・グループでの割り当て・反映までの時間・出ないときに見る順番を整理します。管理センターの操作はこちらでは試していないので、手順は公式の手順をもとにしています。

:::takeaways
- 割り当ては**管理センターの［課金］＞［ライセンス］で［Microsoft Copilot］を選び、［ライセンスの割り当て］**。一度に追加できるのは20人またはグループまで
- 割り当てられるのは**ライセンス管理者かユーザー管理者以上**。AI 管理者は利用者のライセンスを管理しない
- グループで割り当てても、**入れ子のグループの下にいる人にはライセンスが付かない**。異動は新しいグループに先に入れてから元のグループを外す
- 一部のアプリでは**表示まで最大24時間**。待っても出なければ、利用者のアプリで［ライセンスの更新］をしてから再起動する
- 出ないときは**管理センター・利用者の端末・社内の回線**の順に見る。1人ずつ要件を調べるならCopilot ライセンス詳細診断
:::

<figure class="post-figure"><img src="/media/images/copilot-license-assign/cla_01_overview.png" alt="Copilotのライセンスを割り当ててから使えるまでの流れの図。前提のライセンス、Copilotを割り当て、最大24時間、ラベルで確認の4段階" loading="lazy"><figcaption>前提のライセンスを確かめてから割り当て、反映を待って利用者のラベルで確かめる（24時間は一部のアプリの上限）</figcaption></figure>

## 割り当てる前にそろえるもの

Copilotのライセンスは単体では使えず、土台になるMicrosoft 365などのライセンスに足すアドオンです。[Microsoft Copilot のライセンス オプション](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-licensing)には前提のプランとしてMicrosoft 365 E3・E5やBusiness Standardなどが並び、Microsoft 365 E7には最初からCopilotが含まれます。

[セットアップの手順](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-setup)は、**Copilotのライセンスより先に、利用者をテナントに追加してMicrosoft 365のライセンスを割り当てておく**順番です。割り当ての前に確かめることを、公式の記事ごとに並べると次のとおりです。

| 確かめること | 中身 | 書かれている記事 |
|---|---|---|
| 前提のライセンス | 利用者に対象のMicrosoft 365などのライセンスが付いている | ライセンス オプション |
| 職場のアカウント | Microsoft Entra IDの職場または学校のアカウントがある | 要件 |
| ゲストではない | ゲストを含む別のテナントの利用者への割り当ては対象外 | セットアップ |
| 使用場所 | 割り当ての前に利用者の場所を設定する | グループのライセンス |
| ユーザー単位の契約 | Microsoft 365 Apps for enterpriseのデバイス単位のライセンスではCopilotを使えない | 要件 |
| 割り当てる人のロール | ライセンス管理者かユーザー管理者以上 | ライセンスの割り当て |

ロールは取り違えやすいところです。[管理者ロールの一覧](https://learn.microsoft.com/ja-jp/microsoft-365/admin/add-users/about-admin-roles)では、AI 管理者はCopilotやAIの管理機能を扱うロールで、**利用者のライセンスは管理しない**と説明されています。割り当ての作業はライセンス管理者に任せます。

### 名前がMicrosoft Copilotに変わった

[Microsoft Copilot の要件](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-requirements)によると、Microsoft 365 Copilotは**Microsoft Copilot**に、Microsoft 365 Copilot ChatはMicrosoft Copilot Chatに名前が変わりました。セットアップの手順で製品の一覧から選ぶのも［Microsoft Copilot］です。

## 管理センターで割り当てる手順

[Microsoft 365 管理センター](https://admin.microsoft.com/)の入口は2つあり、製品から人を選ぶか、人から製品を選ぶかで分かれます。

### ライセンスのページから割り当てる

[ユーザーのライセンスの割り当てまたは割り当て解除](https://learn.microsoft.com/ja-jp/microsoft-365/admin/manage/assign-licenses-to-users)の手順は次の6つです。

1. 管理センターで［課金］＞［ライセンス］を開く
2. ［Microsoft Copilot］を選ぶ
3. 製品の詳細ページで［ライセンスの割り当て］を選ぶ
4. ユーザーかグループの名前を入力し、結果から選んで一覧に足す。**一度に足せるのは20人またはグループまで**
5. 必要なら［アプリとサービスをオンまたはオフにする］で個別の項目を外す
6. ［割り当てる］を選び、右のウィンドウを閉じる

<figure class="post-figure post-figure--sp"><img src="/media/images/copilot-license-assign/cla_03_learn_assign_sp.jpg" alt="Microsoft Learnのライセンスのページから割り当てる手順。課金のライセンスのページに移動し、製品を選び、ライセンスの割り当てを選ぶ。パネルでユーザーかグループの名前を入力して一覧に追加し、一度に最大20人のユーザーやグループを追加できる。アプリとサービスのオンとオフを選び、割り当てるを選ぶ" loading="lazy"><figcaption>Microsoft Learn「ユーザーのライセンスの割り当てまたは割り当て解除」の手順（赤枠は一度に20まで）</figcaption></figure>

5の項目について、Microsoftの解説動画「[Copilot ライセンスの割り当て方法](https://www.youtube.com/watch?v=fOvhyYUg8xY)」（Microsoft Helps）は**すべて選んだままにしておくことを勧めています**。使えないと言われたときに最初に疑うのも、外した項目です。

割り当てが終わらなかった人がいると、操作のあとに状態のメッセージが出ます。［エラーと問題の表示］で1人ずつ理由を見られます。

### アクティブなユーザーのページから割り当てる

1人なら［ユーザー］＞［アクティブなユーザー］で行を選び、［ライセンスとアプリ］でCopilotにチェックを入れて［変更の保存］です。数人なら名前の横の丸を選び、上の［製品ライセンスの管理］で既存のライセンスを残したまま割り当てます。

## グループで割り当てる

部署や役割でグループを作っておくと、異動のたびに1人ずつ付け外しをしなくて済みます。[グループにライセンスを割り当てる手順](https://learn.microsoft.com/ja-jp/microsoft-365/admin/manage/manage-group-licenses)によると、対象にできるのはセキュリティ グループ、メールが有効なグループ、Microsoft 365 グループです。

1. 少なくともライセンス管理者として管理センターにサインインする
2. ［課金］＞［ライセンス］で［ライセンスの割り当て］を選ぶ
3. サイド パネルでグループを検索して選ぶ
4. ライセンスの取得元のサブスクリプションを選ぶ
5. 必要なら［アプリとサービスのオンとオフを切り替える］で項目を外す
6. ［ライセンスの割り当て］を選ぶ

<figure class="post-figure post-figure--sp"><img src="/media/images/copilot-license-assign/cla_04_learn_group_sp.jpg" alt="Microsoft Learnのグループベースのライセンスの制限事項と手順。ライセンスは一度に最大20グループに割り当てられる。再処理は一度に最大20人のユーザーまで。正常に割り当てられないユーザーの一覧は一度に999人ずつ表示される。続けてグループにライセンスを割り当てる7つの手順" loading="lazy"><figcaption>Microsoft Learn「グループにライセンスを割り当てるか、割り当て解除する」の制限事項（赤枠）と手順</figcaption></figure>

グループで割り当てた人は、ライセンスのページの一覧には個人の名前ではなくグループ名で出ます。誰に付いているかは［チームとグループ］＞［アクティブなチームとグループ］でメンバーを開いて確かめます。

### 入れ子のグループには付かない

グループベースのライセンスは、入れ子のグループ（グループの中に別のグループがある形）に現在は対応していません。入れ子のグループに割り当てると、**ライセンスが付くのは第1レベルのグループに直接いる人だけ**です。部署のグループの中に課のグループを入れている組織では、課のメンバーにはライセンスが付きません。

### 異動のときは足してから外す

ライセンスの付いたグループから別のグループへ人を移すときは、操作の順番に気をつけます。**先に新しいグループに入れ、その人のライセンスのページで新しいライセンスが付いたのを確かめてから、元のグループから外します**。逆の順番にすると、新しいグループの処理が終わるまでのあいだ、その人はライセンスの無い状態になります。

## 反映までの時間

割り当てた直後に利用者がWordを開いても、まだCopilotが出ないことがあります。セットアップの手順によると、WordやExcelなどには割り当てるとCopilotが表示されるものの、**一部のアプリでは表示まで最大24時間かかる場合があり、アプリの再起動か更新が要る場合もある**と書かれています。

<figure class="post-figure post-figure--sp"><img src="/media/images/copilot-license-assign/cla_02_learn_setup_sp.jpg" alt="Microsoft LearnのMicrosoft Copilotを設定しライセンスを割り当てるページの手順2。Copilotライセンスは個々のユーザーかグループに割り当てられ、再割り当てもできる。課金のライセンスでMicrosoft Copilotを選ぶ手順のあと、一部のアプリではCopilotが表示されるまで最大24時間待つ必要がある場合があり、アプリの再起動または更新が必要な場合もあると書かれている" loading="lazy"><figcaption>Microsoft Learn「Microsoft Copilot を設定し、ライセンスを割り当てる」の手順2（赤枠が反映までの時間）</figcaption></figure>

割り当てると、利用者にはCopilotを紹介するメールが自動で届きます（[ユーザーを歓迎し、組織のメッセージを作成する](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-enable-users)）。**反映まで時間がかかる場合があることを、社内の案内に1行添えておきます**。

待っても出なければ利用者のアプリで［ファイル］＞［アカウント］＞［ライセンスの更新］を選び、開いているMicrosoft 365のアプリを全部閉じて起動し直してもらいます（[Microsoft 365 アプリで欠落している Copilot ボタンを見つけて有効にする方法](https://support.microsoft.com/ja-jp/office/how-to-find-and-enable-missing-copilot-button-in-microsoft-365-apps-c8482b93-4b96-4bb8-8ec9-5148f4d42441)）。Macはアプリ名のメニューの［詳細情報］から、Web版はページの更新です。

<figure class="post-figure post-figure--sp"><img src="/media/images/copilot-license-assign/cla_07_help_update_sp.jpg" alt="Microsoftサポートの手順2ライセンスを更新する。Microsoft 365アプリでファイルのアカウントに移動し、ライセンスの更新を選ぶ。製品情報の画面のUpdate Licenseのボタンに赤枠がある。ライセンスの更新が反映されるよう、開かれているすべてのMicrosoft 365アプリを閉じて再起動する" loading="lazy"><figcaption>Microsoftサポートの［ライセンスの更新］の手順（Windows）</figcaption></figure>

同じサポート記事には、**Copilotのボタンの既定の場所が文書の右下に変わった**ことも書かれています。リボンを探して無いと言われたら、先に右下を見てもらいます。

## 割り当てたのに使えないとき

Microsoftのトラブルシューティングの記事「[Copilot が見つからない、無効になっている、または正常に動作しない](https://learn.microsoft.com/ja-jp/troubleshoot/microsoft-365-apps/copilot/copilot-missing-disabled-not-work-correctly)」は、症状を2つに分けています。リボンにCopilotのボタンが無いか淡色で押せない場合と、「ライセンスを更新できませんでした」（エラー コード: 29）や「問題が発生しました。もう一度お試しください。」が出る場合です。

<figure class="post-figure post-figure--sp"><img src="/media/images/copilot-license-assign/cla_05_learn_causes_sp.jpg" alt="Microsoft LearnのCopilotが見つからない記事の原因の節。新しく割り当てられたライセンスは反映までに時間がかかる場合がある（赤枠）。個人アカウントと職場アカウントの競合、インターネット接続、Officeのリセットや更新、デバイスベースのライセンス、半期エンタープライズチャネル、プライバシー設定によるブロックが並ぶ" loading="lazy"><figcaption>トラブルシューティングの記事に並ぶ原因（赤枠は割り当てた直後の反映の遅れ）</figcaption></figure>

原因の1つ目は、割り当てた直後の反映の遅れです。残りの原因を見る場所で3つに分けると、担当を決めやすくなります。

<figure class="post-figure"><img src="/media/images/copilot-license-assign/cla_06_fig_check.png" alt="割り当てたのにCopilotが出ないときに見る順番の図。1は管理センターで一覧に本人がいるか、エラーと問題のタブ、アプリとサービス。2は待って更新で一部は最大24時間、ライセンスの更新、全部閉じて再起動。3は端末とアカウントで職場のアカウントか、半期チャネルか、デバイス単位の契約か、プライバシーの設定。4は回線とブラウザで cloud.microsoft、WebSocketの接続、Web版のCookie。1人ずつ要件を調べるときはCopilotライセンス詳細診断を使う" loading="lazy"><figcaption>管理センターから利用者の端末、社内の回線へと順に見る</figcaption></figure>

| 原因 | 見る場所 | 直し方 |
|---|---|---|
| 割り当てて間もない | 割り当てた時刻 | 最大24時間待ち、ライセンスの更新と再起動 |
| 割り当てが失敗している | 管理センターの［エラーと問題］ | 原因を直して［再処理］ |
| 個人と職場の両方でサインイン | アプリの［ファイル］＞［アカウント］ | 職場のアカウントで開く |
| 半期エンタープライズ チャネル | ［ファイル］＞［アカウント］の製品情報 | 最新チャネルか月次エンタープライズ チャネルへ |
| デバイス単位のライセンス | 契約の種類 | ユーザー単位のライセンスを割り当てる |
| プライバシーの設定 | ［アカウントのプライバシー］＞［設定の管理］ | 2つの項目をオンにする |
| 社内の回線 | プロキシ・ファイアウォール | *.cloud.microsoft とWebSocketを通す |
| Web版でだけ出ない | ブラウザのCookie | サードパーティのCookieを有効にする |

### 管理センターで見るところ

製品ごとの［エラーと問題］タブには、ライセンスを受け取れなかった人と理由が出ます。割り当てのページが挙げる主な理由は、**使えるライセンスが残っていない、競合するサービスやプランがある、使用場所が正しくない**の3つです。原因を直したら、その人を選んで［再処理］を押すと、今の設定でもう一度割り当てを試します。

### 利用者の端末で見るところ

セットアップの手順の条件は、職場のアカウントでアプリにサインインしていて、**ファイルが読み取り専用ではなく編集できる状態**であることです。個人と職場の両方のアカウントでサインインしていると、ライセンスが正しく確かめられないことがあります。

更新チャネルの種類は［ファイル］＞［アカウント］の製品情報に表示されます。セットアップの手順によると、**Copilotは半期エンタープライズ チャネル以外の更新チャネルで使えます**。半期エンタープライズ チャネルと出ていたら最新チャネルか月次エンタープライズ チャネルに移し、それまではWeb版を使ってもらいます。

プライバシーの設定は［アカウントのプライバシー］＞［設定の管理］で、［コンテンツを分析するエクスペリエンス］と［すべての接続エクスペリエンス］がオンかを見ます。組織が管理する端末なら、管理側のポリシーで決まる設定です。

### 回線とブラウザで見るところ

要件の記事が求めているのは、許可リストに*.cloud.microsoftを入れることです。**このドメインの一部のURLだけを許可する設定はサポートされていません**。端末から*.office.com・*.cloud.microsoft・copilot.cloud.microsoftへのWebSocketの接続（WSS）が通るかも確かめます。Web版のWord・Excel・PowerPointで使うなら、ブラウザのサードパーティのCookieを有効にしておくのも条件です。

### 1人ずつ調べる診断ツール

セットアップとライセンス オプションの記事はどちらも、特定の利用者がCopilotの要件を満たしているかを確かめる[Copilot ライセンス詳細診断](https://aka.ms/CopilotLicenseDetails)を勧めています。開くとMicrosoft Remote Connectivity Analyzerの英語の画面になり、グローバル管理者でサインインした場合は調べたい利用者の名前も入れられます。この記事では診断を実行していません。

<figure class="post-figure post-figure--sp"><img src="/media/images/copilot-license-assign/cla_08_diag_sp.jpg" alt="Microsoft Remote Connectivity AnalyzerのCopilot License Detailsの入力画面。このテストはアカウントがCopilotの機能を使う要件を満たしているかを確かめると書かれている。OAuthの資格情報でサインインする欄、グローバル管理者でサインインした場合に対象のユーザー名を入れる欄、ロボットでないことの確認、Perform Testのボタンがある" loading="lazy"><figcaption>Copilot ライセンス詳細診断の入力画面（ログイン前、2026年10月15日）</figcaption></figure>

## 利用者が自分のライセンスを確かめる

利用者が自分の画面で状態を確かめる方法もあります。サポート記事「[所有している Copilot ライセンスの種類](https://support.microsoft.com/ja-jp/microsoft-365-copilot/what-copilot-license-do-i-have)」によると、職場のアカウントでMicrosoft 365にサインインし、ホーム ページのいちばん下までスクロールすると、名前の下にラベルが出ます。

| ラベル | 意味 |
|---|---|
| Copilot Chat（基本） | アドオンのライセンスが無く、Word・Excel・PowerPoint・OneNoteのCopilotは使えない |
| M365 Copilot（基本） | アドオンのライセンスは無いが、アプリのCopilotに標準アクセスできる |
| M365 Copilot（プレミアム） | アドオンのライセンスがあり、アプリのCopilotの全機能に優先アクセスできる |

<figure class="post-figure post-figure--sp"><img src="/media/images/copilot-license-assign/cla_09_help_labels_sp.jpg" alt="Microsoftサポートの職場または学校アカウントでCopilotライセンスをチェックする方法。Microsoft 365にサインインしてホームページの一番下までスクロールすると、名前の下にCopilot Chat（基本）、M365 Copilot（基本）、M365 Copilot（プレミアム）のどれかのラベルが表示される。3つのラベルの見本の画像が並ぶ" loading="lazy"><figcaption>サポート記事のラベルの見本（名前はMicrosoftの例）</figcaption></figure>

サポート記事の説明では、アドオンのライセンスを持つ人のラベルはプレミアムです。**社内の案内に、確かめる場所としてこのラベルを書いておくと、利用者が自分で状態を見られます**。3つのラベルの状態でできることの違いは、[Copilotの使い方の記事](/media/copilot-guide/)にまとめています。

## 外すときと付け替えるとき

使わなくなった人のライセンスは、ライセンスのページで製品を選び、その人のチェックを入れて［ライセンスの割り当て解除］を選ぶと外せます。セットアップの手順のとおり、外したライセンスはほかの人に割り当て直せます。

**割り当てを外すだけでは契約しているライセンスの数はそのままです**。外したライセンスをほかの人に回す予定が無いなら、払いすぎないようにサブスクリプションからライセンスを減らすことを、割り当ての記事は勧めています。

利用者が自分でセルフサービスで買ったサブスクリプションのライセンスは、管理者が割り当てたり外したりできません。管理するにはそのサブスクリプションを引き継ぎます。

ライセンスを割り当てたあと、業務の一部をCopilotやほかのAIに任せる仕組みまで作るときの進め方は、[AIエージェント構築支援](/ai-agent/)のページにまとめています。

## よくある質問

### Copilotのライセンスはどこで割り当てますか？
Microsoft 365 管理センターの［課金］＞［ライセンス］で［Microsoft Copilot］を選び、［ライセンスの割り当て］から利用者かグループを選びます。1人ずつ足すなら［ユーザー］＞［アクティブなユーザー］からでも同じです。

### Copilotを割り当てたのに表示されないのはなぜ？
割り当てた直後なら反映を待っている可能性があります。それでも出なければ、管理センターの［エラーと問題］、利用者のアカウントと更新チャネル、プライバシーの設定、社内の回線の順に確かめます。

### Copilotのライセンスは反映まで何時間かかりますか？
Microsoftのセットアップの手順では、一部のアプリで表示まで最大24時間かかる場合があるとされています。アプリの再起動か更新が要る場合もあるため、待っても出なければ利用者のアプリで［ライセンスの更新］を試してください。

### Copilotのライセンスはグループに割り当てられますか？
割り当てられます。セキュリティ グループ、メールが有効なグループ、Microsoft 365 グループが対象です。入れ子のグループに割り当てた場合、ライセンスが付くのは第1レベルのグループに直接いる人だけです。

### Copilotのライセンスを割り当てる管理者は？
ライセンス管理者かユーザー管理者以上のロールです。グループへの割り当てはグループ管理者もできます。AI 管理者は利用者のライセンスを管理しません。

### Copilotのライセンスの有無はどこで確かめますか？
職場のアカウントでMicrosoft 365にサインインし、ホーム ページのいちばん下にある名前の下のラベルを見ます。アドオンのライセンスがあれば、M365 Copilot（プレミアム）と表示されます。

### Copilotのライセンスはゲストに割り当てられますか？
割り当てはサポートされていません。セットアップの手順に、ゲストを含む別のテナントの利用者への割り当てはサポートされていないと書かれています。

### Copilotのライセンスを外すと料金は下がりますか？
割り当てを外すだけでは契約の数はそのままです。使わない分はサブスクリプションからライセンスを減らすよう、Microsoftは案内しています。

## 出典

- Microsoft Learn「[Microsoft Copilot を設定し、ライセンスを割り当てる](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-setup)」（2026年10月15日取得）
- Microsoft Learn「[Microsoft Copilot のライセンス オプション](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-licensing)」（同）
- Microsoft Learn「[Microsoft Copilot の要件](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-requirements)」（同）
- Microsoft Learn「[Microsoft 365 管理センター内のユーザーのライセンスの割り当てまたは割り当て解除](https://learn.microsoft.com/ja-jp/microsoft-365/admin/manage/assign-licenses-to-users)」（同）
- Microsoft Learn「[Microsoft 365 管理センター内のグループにライセンスを割り当てるか、割り当て解除する](https://learn.microsoft.com/ja-jp/microsoft-365/admin/manage/manage-group-licenses)」（同）
- Microsoft Learn「[Microsoft 365 管理センターの管理者ロールについて](https://learn.microsoft.com/ja-jp/microsoft-365/admin/add-users/about-admin-roles)」（同）
- Microsoft Learn「[ユーザーを歓迎し、組織のメッセージを作成し、Microsoft Copilot へのフィードバックを有効にする](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-enable-users)」（同）
- Microsoft Learn「[Copilot が見つからない、無効になっている、または正常に動作しない](https://learn.microsoft.com/ja-jp/troubleshoot/microsoft-365-apps/copilot/copilot-missing-disabled-not-work-correctly)」（同）
- Microsoft サポート「[Microsoft 365 アプリで欠落している Copilot ボタンを見つけて有効にする方法](https://support.microsoft.com/ja-jp/office/how-to-find-and-enable-missing-copilot-button-in-microsoft-365-apps-c8482b93-4b96-4bb8-8ec9-5148f4d42441)」（同）
- Microsoft サポート「[所有している Copilot ライセンスの種類](https://support.microsoft.com/ja-jp/microsoft-365-copilot/what-copilot-license-do-i-have)」（同）
- Microsoft「[Copilot ライセンス詳細診断](https://aka.ms/CopilotLicenseDetails)」（同）
- Microsoft Helps「[Copilot ライセンスの割り当て方法](https://www.youtube.com/watch?v=fOvhyYUg8xY)」（YouTube、同）
