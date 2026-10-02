---
title: 【2026年10月】Copilotを消す方法｜Windows・Word・Excel・Edge・Copilotキー・会社のPC
date: 2026-10-03
category: AI活用
description: Copilotを消す方法を、Windowsのアプリ・Word・Excel・Outlook・Edge・Copilotキーに分けて公式ヘルプから解説。会社のPCで自分では消せない理由と、管理者に頼むときの設定名まで。
cover_tag: 使い方
cover_headline: Copilotを消す
cover_sub: Windows・Office・Edge・会社のPC
---

「Copilotを消したい」と言っても、消す相手は1つではありません。Windowsに入っているCopilotのアプリ、WordやExcelのリボンにあるCopilot、Outlookの中のCopilot、Edgeの右上のボタン、キーボードのCopilotキーは、それぞれ消し方が違います。

さらに、会社から配られたPCでは、個人向けの手順がそもそも使えないことがあります。この記事は2026年10月3日に取得したMicrosoftの公式ヘルプをもとに、場所ごとの消し方と、自分で消せないときに誰に何を頼めばよいかを整理します。

:::takeaways
- 消し方は場所ごとに別。**Windowsのアプリはアンインストール、Word・Excel・PowerPointは［Copilot を有効にする］をオフ、Outlookはトグル、Edgeはボタンの表示をオフ**
- Word・Excel・PowerPointの設定は**アプリごと・端末ごと**。Outlookは同じアカウントの**すべての端末に反映**される
- **リボンからCopilotのアイコンを外しても、Copilotはオフにならない**（公式ヘルプ）
- Word・Excel・PowerPointのオフの手順は**個人のMicrosoftアカウントだけが対象**。職場・学校のアカウントでは使えない
- Copilotキーを右Ctrlに戻す設定は、ヘルプでは**2026年後半の更新で追加予定**の書き方のまま
:::

## 消したいCopilotがどれかを先に分ける

Copilotは同じ名前で、別々の場所に入っています。どれを消したいかで、見る設定が変わります。

<figure class="post-figure"><img src="/media/images/copilot-remove/01_fig_where.png" alt="Copilotが入っている5つの場所と消し方の図。Windowsのアプリはアンインストール、Word・Excel・PowerPointはCopilotを有効にするのチェックをオフ、Outlookは設定のトグル、Edgeはツールバーのボタンの表示をオフ、CopilotキーはWindowsの設定で割り当てを変える" loading="lazy"><figcaption>まず、どこに出ているCopilotかを確かめる</figcaption></figure>

| 消したい場所 | 消し方 | 自分でできるか |
|---|---|---|
| Windowsの Copilot アプリ | ［設定］→［アプリ］→［インストールされたアプリ］からアンインストール | 個人のPCならできる |
| Word・Excel・PowerPoint | ［ファイル］→［オプション］→［Copilot］のチェックをオフ | 個人のMicrosoftアカウントだけ |
| Outlook | ［設定］→［Copilot］のトグルをオフ | 新しいOutlookなど。従来のOutlook for Windowsは未対応 |
| Edgeのボタン | ［設定］→［Copilot と AI］で表示をオフ | できる |
| Copilotキー | ［設定］→［Bluetooth とデバイス］→［キーボード］ | 右Ctrlに戻す設定は追加予定 |

アプリをアンインストールしても、WordやExcelの中のCopilotは消えません。逆に、Wordでオフにしても、タスクバーのCopilotのアプリは残ります。**消したい場所の数だけ、設定を変える必要がある**ということです。

## WindowsのCopilotアプリを消す

タスクバーやスタートメニューに出てくるCopilotは、独立したアプリとして入っています。MicrosoftのIT管理者向けの文書「[更新された Windows および Microsoft Copilot Chat エクスペリエンス](https://learn.microsoft.com/ja-jp/windows/client-management/manage-windows-copilot)」には、アプリを消す手順が次のように書かれています。

1. ［設定］→［アプリ］→［インストールされたアプリ］を開く
2. 一覧の「Copilot」の右にある［…］を押す
3. ［アンインストール］を選ぶ

<figure class="post-figure"><img src="/media/images/copilot-remove/02_learn_uninstall.jpg" alt="Microsoft Learnの文書。Microsoft Copilotアプリの削除またはインストールの禁止の節に、設定からアプリ、インストールされたアプリに移動してCopilotアプリをアンインストールできると書かれている" loading="lazy"><figcaption>Microsoft Learn「更新された Windows および Microsoft Copilot Chat エクスペリエンス」</figcaption></figure>

タスクバーからアイコンだけを消したいなら、アンインストールしなくても、アイコンを右クリックして［タスク バーからピン留めを外す］で足ります。

### 更新のあとにまた出てくるとき

インストールを防ぐ設定をしていないPCでは、Windowsの更新プログラムを入れたときにCopilotのアプリが自動で有効になる、と同じ文書に書かれています。これは2024年9月からの更新についての説明ですが、**アンインストールしただけでは、次の更新で戻ってくることがある**と考えておくのが安全です。

戻ってこないようにする方法として文書が挙げているのは、AppLockerというアプリの実行を制御する仕組みで、Copilotのアプリ（パッケージ名 MICROSOFT.COPILOT）を止める設定です。ただしこれは主に組織のPCの管理者が使うもので、家庭用のWindowsで気軽に触る設定ではありません。

2026年4月の更新で管理者がCopilotのアプリを自動で消すための設定（グループポリシーの［Microsoft Copilot アプリの削除］）が正式に入った、とマイナビニュースが[Windows Latestの調査として報じています](https://news.mynavi.jp/techplus/article/20260527-4505438/)。消える条件は3つで、Microsoft 365 CopilotとMicrosoft Copilotの両方が入っている、利用者が自分でアプリを入れていない、過去28日間アプリを起動していない、のすべてを満たすときです。

## WordとExcelのCopilotを消す

WordやExcelのCopilotは、アプリの中の設定で消します。公式ヘルプ「[Microsoft 365 Apps で Copilot をオフにする](https://support.microsoft.com/ja-jp/privacy/turn-off-copilot-in-microsoft-365-apps)」の手順は次のとおりです。

- Windows: アプリの［ファイル］→［オプション］→［Copilot］を開き、［Copilot を有効にする］のチェックを外す
- Mac: アプリのメニュー→［基本設定］→［作成および校正ツール］→［Copilot］を開き、［Copilot を有効にする］のチェックを外す

どちらも、チェックを外したらアプリを閉じて開き直します。オフにすると、リボンのCopilotのアイコンが使えなくなり、そのアプリでCopilotの機能を使えなくなります。

<figure class="post-figure"><img src="/media/images/copilot-remove/03_help_m365.jpg" alt="Microsoftの公式ヘルプ「Microsoft 365 Apps で Copilot をオフにする」。この記事の情報はMicrosoftアカウントでサインインしている場合にのみ適用され、職場または学校アカウントでは使えないと書かれている" loading="lazy"><figcaption>公式ヘルプの冒頭。対象は個人のMicrosoftアカウントだけ</figcaption></figure>

### アプリごと・端末ごとに設定する

このチェックは、**その端末のそのアプリにだけ効きます**。WordでオフにしてもExcelには残り、会社のPCでオフにしても自宅のPCには残ります。3つのアプリを2台で使っているなら、6か所で外すことになります。

### リボンのアイコンを外すだけではオフにならない

リボンをカスタマイズしてCopilotのアイコンを消す方法もありますが、公式ヘルプは**アイコンを消してもCopilotはオフにならない**と書いています。右クリックのメニューなど、ほかの入口から引き続き使える状態です。見た目だけ消したいならリボン、機能ごと止めたいならチェック、と使い分けてください。

### チェックが見当たらないとき

アプリに［Copilot を有効にする］がまだ無い場合、公式ヘルプはアカウントのプライバシー設定でオフにする方法を案内しています。Windowsなら［ファイル］→［アカウント］→［アカウントのプライバシー］→［設定の管理］で、［コンテンツを分析するエクスペリエンスを有効にする］のチェックを外します。

ただし、この方法は**Copilot以外の機能も一緒に止まります**。ヘルプが例に挙げているのは、Outlookの返信の候補、Wordの予測入力、PowerPointのデザイナー、画像の自動代替テキストです。使っている機能があるなら、アプリを更新してチェックが出るのを待つほうが影響は小さくなります。

## OutlookのCopilotを消す

Outlookは手順が別で、チェックボックスではなく［Copilot を有効にする］のトグルで切り替えます。公式ヘルプによれば、2025年6月3日の時点で次の場所にトグルがあります。

| Outlook | 場所 |
|---|---|
| Windows（新しいOutlook） | ［設定］→［Copilot］ |
| Mac | ［クイック設定］→［Copilot］ |
| Web | ［Settings］→［Copilot］ |
| iPhone・Android | ［クイック設定］→［Copilot］ |

WordやExcelとの大きな違いは、**同じアカウントでサインインしていれば、どの端末でオフにしても全部の端末のOutlookに反映される**ことです。Macでオフにすれば、iPhoneのOutlookでもオフになります。

一方で、従来のOutlook for Windowsでは、オンとオフを切り替えられるようになる時期は示されていません（2026年10月3日時点のヘルプ）。

## EdgeのCopilotボタンを消す

Edgeの右上にあるCopilotのボタンは、Edgeの設定で表示を切り替えます。バージョン149の画面を解説した[初心者のためのOffice講座](https://hamachan.info/win11-edge-sidebar/)によれば、［設定］→［Copilot と AI］にある［ツールバーに［Copilot］ボタンを表示する］をオフにすると、ツールバーから消えます。

ボタンを消しても、ショートカットキーの［Ctrl］+［Shift］+［.］（ピリオド）でCopilotのパネルは開きます。**消えるのはボタンだけで、Copilotの機能は残る**点はWordのリボンと同じです。

なお、Microsoftの公式ヘルプ「[Microsoft Edge で Copilot を使ってみる](https://support.microsoft.com/ja-jp/microsoft-copilot/getting-started-with-copilot-in-microsoft-edge)」の［Copilot と AI］の説明は、ページの内容を読ませるかどうかと新しいタブの設定が中心で、ボタンを消す手順は書かれていません（10月3日に確認）。

## Copilotキーを別のキーとして使う

2024年以降に出たWindows 11のPCには、右Ctrlキーやアプリケーションキーの代わりにCopilotキーが付いているものがあります。公式ヘルプ「[Windows デバイスの Copilot キーの更新について](https://support.microsoft.com/ja-jp/accessibility/windows/copilot/understand-updates-to-the-copilot-key-on-windows-devices)」は、ショートカットや読み上げソフトで右Ctrlを使っていた人が困っていると認めたうえで、次の更新を予告しています。

<figure class="post-figure"><img src="/media/images/copilot-remove/04_help_key.jpg" alt="Microsoftの公式ヘルプ「Windows デバイスの Copilot キーの更新について」。今年後半にリリース予定のWindows 11の更新で、Copilotキーをコンテキストメニューキーまたは右Ctrlキーとして動作するように再マップできる設定を追加すると書かれている" loading="lazy"><figcaption>公式ヘルプ。右Ctrlに戻す設定は「今年後半」の更新で追加予定</figcaption></figure>

- 場所は［設定］→［Bluetooth とデバイス］→［キーボード］
- Copilotキーを右Ctrlかアプリケーションキー（コンテキストメニューキー）として動かせるようになる
- 右Ctrlにした場合、右Ctrl+Windowsキーと右Ctrl+Shiftの組み合わせは通常どおり動かないので、左Ctrlを使う

**10月3日時点のヘルプは「今年後半にリリースされる予定」の書き方のままです。**手元のWindowsの［キーボード］に右Ctrlの選択肢が無ければ、まだ届いていません。

PCのメーカーが独自にキーの割り当てを変える設定を用意している場合もあります。ヘルプはWindowsの設定とメーカーの設定の**どちらか一方だけを使い、両方は使わない**ように案内しています。

## 会社のPCで自分では消せないとき

会社から配られたPCだと、ここまでの手順が使えないことがよくあります。理由は2つです。

<figure class="post-figure"><img src="/media/images/copilot-remove/05_fig_work.png" alt="個人のアカウントと職場のアカウントでCopilotの消し方が違う図。個人のMicrosoftアカウントならWord・Excel・PowerPointのチェックやアプリのアンインストールを自分でできる。職場や学校のアカウントではチェックの手順が使えず、アプリの削除やピン留めは管理者がポリシーで決める" loading="lazy"><figcaption>職場のアカウントでは、管理者の設定が決め手になる</figcaption></figure>

ひとつは、Word・Excel・PowerPointの［Copilot を有効にする］の手順が、**個人のMicrosoftアカウントでサインインしている場合だけのもの**だからです。公式ヘルプの冒頭に、職場または学校のアカウントでサインインしている場合は使えない、と明記されています。

もうひとつの理由として、Copilotのアプリをタスクバーに置くかどうかや、Copilot Chatを使えるようにするかどうかを、**組織の管理者が決める仕組み**になっているからです。Microsoft Learnの文書では、管理者はMicrosoft 365 管理センターでピン留めの扱いを設定でき、アプリのインストールはAppLockerで止められる、と説明されています。

「Copilotというソフトが勝手に会社のPCに入っていた」という質問は、Yahoo!知恵袋で[5万回以上閲覧されています](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q11293737631)。会社のPCなら、自分で設定を探す前に、社内の情報システムの担当者に「Copilotを使わない設定にしたい」と伝えるのが早道です。そのとき、上の設定の名前（Microsoft 365 管理センターのピン留め、AppLocker、［Microsoft Copilot アプリの削除］のポリシー）を添えると話が通りやすくなります。

## AI検索での見え方は別の話

Copilotを自分の画面から消しても、Copilotが答えの中で自社をどう紹介するかは変わりません。そちらは[AI検索対策](https://nito-0210.com/llmo/)として扱います。

## よくある質問

### Copilotを消すとOfficeは使えなくなりますか？
Copilotのアプリはほかのアプリと同じようにアンインストールの一覧に並び、Word・Excel・PowerPointのCopilotはチェックひとつでオフにできる設計です。ただし、チェックが無いときに使うプライバシー設定の方法は、Outlookの返信の候補やWordの予測入力など、Copilot以外の機能も一緒に止めます。

### Copilotが勝手にインストールされたのはなぜですか？
Microsoft Learnの文書には、インストールを防ぐ設定をしていないPCでは、Windowsの更新プログラムを入れるとCopilotのアプリが自動で有効になると書かれています。自分で入れていなくても、更新で入ってくることがあります。

### アンインストールしたCopilotがまた出てきますか？
更新で戻ってくる可能性はゼロではありません。止めるにはAppLockerなどの管理者向けの設定が必要で、組織のPCなら情報システムの担当者に頼むのが確実です。

### ExcelだけCopilotを消せますか？
消せます。［Copilot を有効にする］のチェックはアプリごとなので、Excelで外せばExcelだけがオフになり、WordやPowerPointはそのままです。

### Outlookのオフはスマホにも反映されますか？
同じアカウントでサインインしていれば、スマホのOutlookもオフです。Outlookのトグルはどの端末で切り替えても全部の端末に反映されます。

### Copilotキーを無効にできますか？
Windowsの設定でCopilotキーを右Ctrlかアプリケーションキーとして動かせるようにする更新が、2026年後半に予定されています。10月3日時点の公式ヘルプは予定の書き方のままで、それより前はPCのメーカーの設定が頼りになります。

### 会社のPCのCopilotを自分で消してもいいですか？
Word・Excel・PowerPointのオフの手順は、職場や学校のアカウントでは使えません。アプリの削除も管理者の設定で決まることが多いので、社内の担当者に確かめてから進めてください。

### Edgeのボタンを消してもCopilotは開きますか？
開きます。ボタンを消しても、［Ctrl］+［Shift］+［.］でCopilotのパネルが開きます。

## 出典

本文の手順は2026年10月3日に取得した次のページで確認しています。

- [Microsoft 365 Apps で Copilot をオフにする](https://support.microsoft.com/ja-jp/privacy/turn-off-copilot-in-microsoft-365-apps)（Word・Excel・PowerPoint・Outlookの手順、個人のアカウントだけが対象、リボンのアイコン、プライバシー設定）
- [Windows デバイスの Copilot キーの更新について](https://support.microsoft.com/ja-jp/accessibility/windows/copilot/understand-updates-to-the-copilot-key-on-windows-devices)（Copilotキーの再割り当ての予定）
- [更新された Windows および Microsoft Copilot Chat エクスペリエンス](https://learn.microsoft.com/ja-jp/windows/client-management/manage-windows-copilot)（アプリのアンインストール、更新での有効化、AppLocker、管理センターのピン留め）
- [Microsoft Edge で Copilot を使ってみる](https://support.microsoft.com/ja-jp/microsoft-copilot/getting-started-with-copilot-in-microsoft-edge)（［Copilot と AI］の設定）
- [サイドバー廃止後のCopilotとAIの設定](https://hamachan.info/win11-edge-sidebar/)（初心者のためのOffice講座。Edge 149のボタンの表示とショートカット）
- [Microsoft、Windows 11のCopilot削除機能を正式リリース](https://news.mynavi.jp/techplus/article/20260527-4505438/)（マイナビニュース TECH+。管理者向けの削除の設定と条件）
- [Copilotというソフトが勝手にパソコンに入っていました](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q11293737631)（Yahoo!知恵袋）
