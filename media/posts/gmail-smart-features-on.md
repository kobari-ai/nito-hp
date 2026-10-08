---
title: 【2026年10月】スマート機能の設定を両方ともオンにする方法 Gemini連携・スマホ・出ないとき
date: 2026-10-09
category: AI活用
description: Geminiに出る「スマート機能の設定を両方ともオンにします」の意味と対処を、Gmailヘルプと実際の設定画面で解説。両方が指す2つのスイッチ、パソコンとスマホの手順、オンで使われるデータ、オンにしても使えないときまで。
cover_tag: 使い方
cover_headline: スマート機能を両方ともオンにする
cover_sub: Gemini連携・スマホ・出ないとき
---

GeminiアプリにGmailやカレンダーのことを尋ねると、「必要なGmailの設定が無効になっているため、Google Workspaceは利用できません」という返事と一緒に「スマート機能の設定を両方ともオンにします」という案内が出ることがあります。**ここで言う両方はGmailの［Workspace のスマート機能の設定を管理］の中にある［Google Workspace のスマート機能］と［他の Google サービスのスマート機能］の2つです。**

Gmailにはスマート機能のスイッチが全部で3つあり、どれをオンにすればよいかが画面だけでは分かりにくい作りです。ここでは2026年10月9日のGmailヘルプとGeminiアプリ ヘルプ、同じ日に開いた設定画面をもとに、オンにする手順と使えないときの確かめ方を書いていきます。

:::takeaways
- 案内が出るのは、**GeminiアプリがGmail・カレンダー・ドライブなどを読みに行こうとして、Gmail側の設定がオフだったとき**
- 両方とは、**［Google Workspace のスマート機能］と［他の Google サービスのスマート機能］**。［Gmail、Chat、Meet のスマート機能］のチェックボックスは含まれない
- パソコンは案内の［続ける］から設定画面が開く。**2つをオンにしたら右下の［保存］を押し、Geminiに戻って［もう一度試す］**
- **日本ではスマート機能は最初からオフ**とGmailヘルプに書かれているため、日本の利用者ほどこの案内に当たる
- オンにしても使えないときは、**同じアカウントか・［アクティビティの保存］がオンか・［アプリ連携］で Google Workspace がオンか**を順に見る
:::

<figure class="post-figure"><img src="/media/images/gmail-smart-features-on/00_fig_flow.png" alt="案内が出てから使えるようになるまでの流れの図。Geminiアプリから、Gmailの設定を開き、2つをオンにして保存し、Geminiに戻ってもう一度試す" loading="lazy"><figcaption>案内が出てから使えるようになるまでの流れ</figcaption></figure>

## この案内が出る場面

GeminiアプリはGmailやGoogleカレンダー、Googleドライブの中身を読んで答えられます。この連携は[Geminiアプリ ヘルプ](https://support.google.com/gemini/answer/15229592?hl=ja)で「Google Workspace アプリ」と呼ばれ、「先週届いた学校のメールを要約して」「カレンダーに今日の予定はある？」のように尋ねると使われます。そのときにGmailの必要な設定がオフだと、返ってくるのが次の案内です。

> 必要なGmailの設定が無効になっているため、Google Workspaceは利用できません。設定を有効にしてから、もう一度お試しください。

案内の下に並ぶのは「Google Workspace スマート設定」「スマート機能の設定を両方ともオンにします」の見出しと、［もう一度試す］［続ける］の2つのボタンです。2026年1月11日の[情報科学屋さんを目指す人のメモ](https://did2memo.net/2026/01/11/google-gemini-required-gmail-settings-are-off-error/)の記事にも、同じ文言とボタンが載っていました。英語の画面では「Turn on both smart features settings」と出るそうです。

**メールや予定の話をしていなくても、この案内が出ることがあります。**2026年2月の[Yahoo!知恵袋の質問](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q14325193134)では、企業の事業内容を尋ねただけで出たという声がありました。Geminiがメールやドライブに情報が無いか探しに行こうとしているのでは、と回答者の1人は書いていました。

日本でこの案内に当たりやすい理由は、設定の初期値にあります。[Gmailヘルプのスマート機能のページ](https://support.google.com/mail/answer/15604322?hl=ja)によると、欧州経済領域・日本・スイス・英国に住んでいる場合、スマート機能の設定は最初からオフです。日本に住んでいれば、自分で切った覚えがなくてもオフの状態から始まります。

## 両方が指す2つのスイッチ

Gmailのスマート機能のスイッチは3つあり、そのうち案内の「両方」に当たるのは、同じ設定画面に並ぶ2つです。残りの1つは［全般］タブのチェックボックスで、タブの自動分類やスマート作成の担当です。

<figure class="post-figure"><img src="/media/images/gmail-smart-features-on/01_fig_need.png" alt="使いたい機能ごとに必要なスイッチの図。GeminiアプリでGmailを読むには他のGoogleサービスのスマート機能とアクティビティの保存。Gmailの中のGeminiに相談にはGoogle Workspaceのスマート機能。メールの要約にはGoogle Workspaceのスマート機能とGmail、Chat、Meetのスマート機能" loading="lazy"><figcaption>使いたい機能と必要なスイッチ（Gmailヘルプ・Geminiアプリ ヘルプから作成）</figcaption></figure>

| スイッチ | 場所 | オンで使えるもの | 案内の「両方」 |
|---|---|---|---|
| Google Workspace のスマート機能 | ［全般］の［Workspace のスマート機能の設定を管理］ | Gmailの予定をカレンダーに表示、検索のパーソナライズ、Geminiへの要約・下書きの依頼 | 入る |
| 他の Google サービスのスマート機能 | 同じ画面の下段 | マップの予約表示、ウォレットのチケット、Geminiアプリでの提案と回答 | 入る |
| Gmail、Chat、Meet のスマート機能 | ［全般］の［スマート機能］のチェックボックス | メイン・プロモーションなどの自動分類、スマート作成、スマート リプライ、概要カード | 入らない |

**GeminiアプリとGoogle Workspaceをつなぐ条件として、Geminiアプリ ヘルプが名前を挙げているのは［他の Google サービスのスマート機能］です。**ヘルプの「Google Workspace アプリを接続できない理由」の節に、このスイッチをGmailの設定でオンにする必要があるとあります。案内のほうは2つともオンにするよう求めていて、設定画面でも2つが1枚に並んでいるため、2つともオンにしてから保存するのが確実です。

2つのスイッチは別々に動き、［Google Workspace のスマート機能］をオンにして［他の Google サービスのスマート機能］だけをオフにする組み合わせもできるとGmailヘルプにあります。上だけオンにして下を見落とすと、Geminiアプリからは同じ案内が出続けるでしょう。

## パソコンでオンにする手順

前述の2026年1月の記事によると、案内の［続ける］を押すとGmailのスマート機能の画面が開きます。同じ記事が行き先として挙げているアドレス（`https://mail.google.com/mail/?ogwsfsd=true#settings`）を2026年10月9日に開くと、この画面が直接出ました。

1. Geminiの案内の［続ける］を押す。ボタンが消えていたら、[Gmailのスマート機能の画面](https://mail.google.com/mail/?ogwsfsd=true#settings)を開く
2. ［Google Workspace のスマート機能］のスイッチをオンにする
3. 下の［他の Google サービスのスマート機能］のスイッチもオンにする
4. 右下の［保存］を押す
5. Geminiの画面に戻り、［もう一度試す］を押すか同じ質問を送る

[Gmail](https://mail.google.com/)から自分で開く場合は、右上の歯車のアイコンから［すべての設定を表示］を押し、［全般］タブを下にたどります。［Google Workspace のスマート機能］の欄にある［Workspace のスマート機能の設定を管理］を押すと、同じ画面が開きます。

<figure class="post-figure"><img src="/media/images/gmail-gemini-off/ggo_01_settings.jpg" alt="Gmailの設定の全般タブの一部。スマート機能のチェックボックスの下に、Google Workspaceのスマート機能の欄があり、1のWorkspaceのスマート機能の設定を管理のボタンが赤枠で囲まれている" loading="lazy"><figcaption>設定の［全般］タブ（2026年10月4日、パソコン）。1を押すと次の画面が開く</figcaption></figure>

<figure class="post-figure"><img src="/media/images/gmail-smart-features-on/gso_01_dialog.jpg" alt="Google Workspaceのスマート機能の設定画面。上にGoogle Workspaceのスマート機能のスイッチがあり1の赤枠、下に他のGoogleサービスのスマート機能のスイッチがあり2の赤枠、右下の保存ボタンに3の赤枠" loading="lazy"><figcaption>開いた画面（2026年10月9日、パソコン）。1と2をオンにして3で保存する</figcaption></figure>

**保存を押さずに閉じると、スイッチを動かしても設定は変わりません。**下段の説明にも「Gemini アプリでの提案と回答」が並んでいて、Geminiアプリに関わるのはこちらのスイッチです。

Geminiに戻ったあと、続けて「Google Workspace に接続する必要があります」という確認と［接続］のボタンが出ることがあります。前述の2026年1月の記事では、ここで［続ける］と［接続］を押すと、カレンダーの予定を使った回答が返ってきたそうです。

## スマホのGmailアプリでオンにする手順

スマホではGmailアプリの設定から同じ2つのスイッチを変えられます。［Gmail、Chat、Meet のスマート機能］については、変更はすべての端末に反映される一方でパソコンでの変更の一部はモバイルアプリに反映されない、という注意書きがGmailヘルプにあります。2つのスイッチには同じ説明が無いため、Geminiをスマホで使うならGmailアプリでもオンになっているかを確かめましょう。

| 端末 | 開く順番 |
|---|---|
| Android | 左上のメニューから［設定］を開き、アカウントを選ぶ。［全般］の［Google Workspace のスマート機能］を開き、［Google Workspace のスマート機能］と［他の Google サービスのスマート機能］のチェックを入れる |
| iPhone・iPad | 左上のメニューから［設定］を開き、［全般］の［データのプライバシー］から［Google Workspace のスマート機能］に進む。2つのスイッチをオンにして、右上の［完了］を押す |

<figure class="post-figure post-figure--sp"><img src="/media/images/gmail-smart-features-on/gso_04_help_android.jpg" alt="GmailヘルプのAndroid版の手順。Gmailアプリを開き、左上のメニューから設定、アカウントを選び、全般でGoogle Workspaceのスマート機能をタップし、Google Workspaceのスマート機能と他のGoogleサービスのスマート機能の横のチェックボックスをタップする。最後の2項目が赤枠" loading="lazy"><figcaption>GmailヘルプのAndroidの手順（2026年10月9日）。赤枠の2つにチェックを入れる</figcaption></figure>

Androidはアカウントごとに設定が分かれているため、Geminiで使っているアカウントを選んでから開きます。複数のアカウントを入れているなら、アカウントの選択画面でメールアドレスを見比べてから進むと確実です。

<figure class="post-figure post-figure--sp"><img src="/media/images/gmail-smart-features-on/gso_05_help_ios.jpg" alt="GmailヘルプのiPhone版の手順。設定、データのプライバシー、Google Workspaceのスマート機能の順にタップし、Google Workspaceのスマート機能と他のGoogleサービスのスマート機能をオンにして完了をタップする。2つの項目が赤枠" loading="lazy"><figcaption>GmailヘルプのiPhoneの手順（2026年10月9日）。最後に［完了］を押す</figcaption></figure>

カレンダー・Chat・ドライブ・Meet・Voice で2つのスイッチを入れられるのはウェブブラウザからだけ、という注記もGmailヘルプにあります。Gmailアプリには設定があるので、スマホしか使わない人もGmailアプリなら変えられます。

## オンにすると使われるデータ

スイッチの横の説明文を読むと、オンにすることが同意として扱われているのが分かります。［Google Workspace のスマート機能］なら、Gmailやドライブの中身と使い方をWorkspace全体のパーソナライズに使うことへの同意です。［他の Google サービスのスマート機能］は、同じ中身を他のGoogleサービス（マップ・ウォレット・Geminiアプリなど）のパーソナライズに使うことへの同意になります。

| 公式の説明 | 書かれている場所 |
|---|---|
| スマート機能がオンのあいだ、機能の向上のためにデータが使われることがある | Gmailヘルプのスマート機能のページ |
| オフにすると以後は使われないが、改善の過程で学習された内容は残る場合がある | 同じページの「データの取り扱い」 |
| Googleは個人のメールでGeminiを含む基盤モデルを学習しない | [Google公式ブログ（2026年4月7日）](https://blog.google/products-and-platforms/products/gmail/privacy-in-gmail-with-gemini/) |
| Gemini in Gmailは頼まれた処理のあとデータを持ち続けない | 同じブログ |
| アクティビティの保存がオンのGeminiアプリのチャットは、一部を人間のレビュアーが見ることがある | [Geminiアプリのプライバシー ハブ](https://support.google.com/gemini/answer/13594961?hl=ja) |

**Geminiアプリから Gmail を読むには［アクティビティの保存］をオンにしておく必要があり、そのチャットはプライバシー ハブの説明どおり、一部がレビュアーに見られる対象に入ります。**連携したアプリから取り出したメールやファイルの中身も、Geminiアプリのプライバシーに関するお知らせに沿って扱うとプライバシー ハブにあります。人に見られたくないメールの中身は、Geminiアプリには尋ねないでおくのが安全です。

公式ブログのこの説明が対象にしているのは、Gmailの中で動くGeminiです。Geminiアプリのチャットの扱いは、アプリ側の設定（アクティビティの保存）で決まります。仕事用や学校用のアカウントには別の規約が適用される場合もある、とプライバシー ハブは断っています。

## オンにしても使えないとき

2つをオンにしても同じ案内が出る、または接続できないときは、下の順に見ていきます。どれもGeminiアプリ ヘルプか前述の2026年1月の記事に出てくる確かめ方です。

| 確かめること | 見る場所 | 直し方 |
|---|---|---|
| 保存したか | Gmailのスマート機能の画面 | 2つがオンのまま［保存］を押し直す |
| 同じアカウントか | Geminiの左下のアイコンとGmailの右上のアイコン | Geminiで使っているアカウントのGmailで設定する |
| アクティビティの保存 | [Geminiアプリ アクティビティ](https://myactivity.google.com/product/gemini) | ［アクティビティの保存］をオンにする |
| アプリ連携 | Geminiの［設定とヘルプ］の［アプリ連携］ | ［Google Workspace］をオンにする |
| 再読み込み | Geminiの画面 | ページを再読み込みしてもう一度接続する |
| 仕事用・学校用のアカウント | 管理者の設定 | 管理者にアプリ連携を有効にしてもらう |

<figure class="post-figure post-figure--sp"><img src="/media/images/gmail-smart-features-on/gso_03_help_reason.jpg" alt="Geminiアプリ ヘルプのGoogle Workspaceアプリを接続できない理由の節。仕事用または学校用のアカウントは管理者がまずアプリ連携を有効にする必要があること。必要な設定がGmailでオフになっている可能性があり、Gmailの設定で他のGoogleサービスのスマート機能をオンにし、Geminiアプリを再読み込みしてもう一度接続する、と書かれた段落が赤枠" loading="lazy"><figcaption>Geminiアプリ ヘルプの「接続できない理由」（2026年10月9日）</figcaption></figure>

**［アクティビティの保存］がオフのままだと、Gmailの設定を全部オンにしてもGoogle Workspaceにはつながりません。**Geminiアプリ ヘルプには、この設定がオフのときGeminiはGoogle Workspaceに接続できないとあります。プライバシー ハブの説明も同じで、Google Workspaceなどとの連携はアクティビティの保存がオフの状態では使えません。

[Geminiの［アプリ連携］の画面](https://gemini.google.com/apps)では、Google Workspaceのスイッチ1つでGmail・カレンダー・Keep・ToDo リスト・ドキュメント・ドライブがまとめてつながります。ここがオフなら、オンにして画面の指示に沿って進めてください。

<figure class="post-figure"><img src="/media/images/gmail-smart-features-on/gso_02_apps.jpg" alt="Geminiのアプリ連携の画面。Googleのアプリの欄にGoogle Workspaceの枠があり、Gmail、Google Calendar、Google Keep、Google ToDoリスト、Googleドキュメント、Googleドライブが並ぶ。右上のスイッチが赤枠で、オンになっている" loading="lazy"><figcaption>Geminiの［アプリ連携］（2026年10月9日、パソコン）。赤枠がGoogle Workspaceのスイッチ</figcaption></figure>

つながっていても答えられない質問があります。Geminiアプリ ヘルプでは、Gmailやドキュメントの画像とコメントを読むこと、受信トレイのメールの数を数えること、ストレージの空き容量を確かめることはできないとされています。「未読メールは何通？」と尋ねて答えが出なくても、設定の問題ではありません。

## Gmailの中のGeminiを使いたいとき

Gmailの右上にある「Gemini に相談」は、Geminiアプリとは別の入口です。こちらに要るのは［Google Workspace のスマート機能］で、［他の Google サービスのスマート機能］は関わりません。

[Gemini in Gmailのヘルプ](https://support.google.com/mail/answer/14355636?hl=ja)では、使うには対象のGoogle WorkspaceかGoogle AIのプランへの登録が必要とされています。Google AI Proに入ったのにGmailの中でGeminiが使えないなら、プランではなく［Google Workspace のスマート機能］がオフのままになっていないかを先に見ます。プランごとに使える範囲は[Google WorkspaceのGeminiの解説](/media/google-workspace-gemini/)にまとめました。

メールのスレッドの上に出る要約（AIによる概要）は、[AIによる概要のヘルプ](https://support.google.com/mail/answer/16561387?hl=ja)で、［Gmail、Chat、Meet のスマート機能］と［Google Workspace のスマート機能］の両方がオンのときに出るとされています。同じ「両方」でも、Geminiアプリの案内とは組み合わせが違うので注意してください。

## 仕事用や学校用のアカウント

会社や学校から配られたアカウントでは、自分の設定のほかに管理者の設定が効きます。[Geminiアプリによる Workspace サービスへのアクセスを制御するページ](https://knowledge.workspace.google.com/admin/generative-ai/gemini-app/turn-google-apps-in-gemini-on-or-off?hl=ja)によると、GeminiアプリとWorkspaceのアプリの連携は既定でオンで、管理者が組織部門ごとに切り替えられます。

スマート機能そのものについては、[管理者向けのヘルプ](https://knowledge.workspace.google.com/admin/security/manage-google-workspace-smart-features-for-your-users?hl=ja)に、ドメインの拠点が日本にある組織では既定でオフになると書かれています。管理者は既定の設定を全員に当てるかどうかを選べ、利用者はそれを自分の設定で上書きできる、という説明です。自分の画面で2つをオンにしても接続できないなら、管理者がアプリ連携を止めている可能性があります。

## オンにしたくないとき

Gmailの中身をGeminiに使わせたくない場合、案内が出てもオンにする必要はありません。Geminiアプリ ヘルプに、この案内を出さないようにする設定は書かれていません。

前述の知恵袋の質問への回答（2026年2月）では、ウェブで調べるよう質問の中で頼めば避けられるという方法が挙がっていました。「ウェブで調べて」と添えると、Geminiが自分のメールを探しに行く理由がなくなるためです。

一度オンにしたあとで戻したいときは、同じ画面で2つのスイッチをオフにして保存します。Gmailの中のGeminiも止めたいときの切り方は、[GmailのGeminiをオフにする方法](/media/gmail-gemini-off/)で説明しています。

## よくある質問

### Geminiのスマート機能の両方とはどれですか？

Gmailの［Workspace のスマート機能の設定を管理］を押して開く画面にある、［Google Workspace のスマート機能］と［他の Google サービスのスマート機能］の2つです。［全般］タブの［Gmail、Chat、Meet のスマート機能］のチェックボックスは含まれません。

### Geminiアプリは片方だけオンでも使えますか？

Geminiアプリ ヘルプが接続の条件として挙げているのは［他の Google サービスのスマート機能］です。ただ案内は2つともオンにするよう求めているため、2つともオンにして保存するのが確実です。あわせて［アクティビティの保存］もオンにしておきます。

### Gmailのスマート機能をオンにするのにお金はかかりますか？

Gmailヘルプのスマート機能のページには、オンにするための料金やプランの条件は書かれていません。Gmailの中の「Gemini に相談」は、Gemini in Gmailのヘルプによると対象のGoogle WorkspaceかGoogle AIのプランへの登録が条件になっています。

### Gmailのスマート機能はスマホからもオンにできますか？

できます。AndroidはGmailアプリの［設定］からアカウントを選んで［全般］の［Google Workspace のスマート機能］、iPhoneは［設定］の［データのプライバシー］から同じ画面に進む順番です。

### GmailのメールはGeminiの学習に使われますか？

個人のメールでGeminiを含む基盤モデルを学習しない、とGoogleは公式ブログ（2026年4月7日）で説明しました。一方でGmailヘルプには、スマート機能がオンのあいだ機能の向上にデータが使われることがあるとも書かれています。Geminiアプリのチャットは別の扱いで、アクティビティの保存がオンだと一部を人間のレビュアーが見る対象です。

### Gmailのスマート機能をオンにしたあとオフに戻せますか？

戻せます。同じ画面でスイッチをオフにして保存すれば、以後はスマート機能にデータが使われなくなります。改善の過程で学習された内容はオフにしたあとも残る場合がある、という注記もGmailヘルプにあります。

### Geminiでオンにしても案内が消えないのはなぜですか？

まず疑うのは、［保存］の押し忘れと、Geminiとは別のアカウントのGmailで設定したことの2つです。ほかに［アクティビティの保存］がオフ、［アプリ連携］のGoogle Workspaceがオフ、仕事用のアカウントで管理者が連携を止めている、のどれかも考えられます。設定を変えたら、Geminiの画面を再読み込みしてから試してください。

### 会社のGmailがGeminiにつながらないのはなぜですか？

仕事用や学校用のアカウントでは、管理者がGeminiアプリとWorkspaceのアプリの連携を組織ごとに切り替えられます。自分の画面で2つのスイッチをオンにしてもつながらないなら、管理者に連携が有効かどうかを確かめてもらいます。

## 出典

- Gmail ヘルプ「[Google Workspace とその他の Google サービスのスマート機能と設定について](https://support.google.com/mail/answer/15604322?hl=ja)」（2026年10月9日取得。パソコン・Android・iPhoneの各版）
- Gemini アプリ ヘルプ「[Google Workspace アプリを Gemini Apps に接続する](https://support.google.com/gemini/answer/15229592?hl=ja)」（同）
- Gemini アプリ ヘルプ「[Gemini でアプリ連携を利用、管理する](https://support.google.com/gemini/answer/13695044?hl=ja)」（同）
- Gemini アプリ ヘルプ「[Gemini アプリのプライバシー ハブ](https://support.google.com/gemini/answer/13594961?hl=ja)」（同）
- Gmail ヘルプ「[Gemini in Gmail を活用する](https://support.google.com/mail/answer/14355636?hl=ja)」（同）
- Gmail ヘルプ「[「AI による概要」の会話の要約を使用してメールスレッドの内容を把握する](https://support.google.com/mail/answer/16561387?hl=ja)」（同）
- Google Workspace 管理者ヘルプ「[Gemini アプリによる Workspace サービスへのアクセスを制御する](https://knowledge.workspace.google.com/admin/generative-ai/gemini-app/turn-google-apps-in-gemini-on-or-off?hl=ja)」「[ユーザー向けに Google Workspace のスマート機能を管理する](https://knowledge.workspace.google.com/admin/security/manage-google-workspace-smart-features-for-your-users?hl=ja)」（同）
- The Keyword「[Here's how we built Gmail to keep your data secure and private in the Gemini era](https://blog.google/products-and-platforms/products/gmail/privacy-in-gmail-with-gemini/)」（2026年4月7日公開）
- 情報科学屋さんを目指す人のメモ「[【Gemini】「必要なGmailの設定が無効になっているため、Google Workspaceは利用できません」エラーの対処方法](https://did2memo.net/2026/01/11/google-gemini-required-gmail-settings-are-off-error/)」（2026年1月11日公開）
- Yahoo!知恵袋「[Geminiを利用していると、唐突に「必要なGmailの設定が無効に…](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q14325193134)」（2026年2月10日の回答）
- スマート機能の画面とアプリ連携の画面は、2026年10月9日にパソコンで開いて撮影（スイッチは切り替えずに閉じた）
