---
title: 【2026年10月】Geminiが使えない原因と対処を解説｜エラーが発生しました・アカウント・上限
date: 2026-09-27
category: AI検索対策
description: Geminiが使えない原因をアカウント・年齢・端末・使用量の上限に分けて整理。「このサービスにアクセスできない」「エラーが発生しました」の意味、アプリの動作条件、10月9日からの無料版のモデル変更をGoogleのヘルプで確かめました。
cover_tag: 使い方
cover_headline: Geminiが使えない
cover_sub: エラー・アカウント・アプリ・上限
---

Googleのヘルプ「[Gemini アプリへのログインに必要なもの](https://support.google.com/gemini/answer/13278668?hl=ja)」によると、Geminiにログインできるのは個人のGoogleアカウント、対象のWorkspaceの仕事用アカウント、管理者が許可した学校用アカウントのどれかです。年齢の条件は個人と学校のアカウントが13歳（国ごとの該当年齢）以上で、仕事用のアカウントは18歳以上です。開けない・ログインできないときは、障害を疑う前にこの条件から確かめるのが近道です。

ヘルプには2026年10月の変更も載りました。有料のプランに入っていない個人のアカウントは、10月9日から使えるモデルがFlash-Liteだけになる予定です。この記事では2026年10月7日に取得したGoogleのヘルプをもとに、Geminiが使えない原因をアカウント・端末・使用量の上限・障害に分けて整理します。

:::takeaways
- ウェブ版で「このサービスにアクセスできない」と出たら、**アカウントの種類か年齢**が条件に合っていない
- 「エラーが発生しました」は、**場所・年齢・アカウントの種類**などでそのアカウントが今は使えないという意味
- ファミリーリンクで管理している子供のアカウントは、**ウェブ版に入れずモバイルアプリだけ**で使う
- アプリはAndroid 9以降・iOS 16以降が条件で、**パソコンのアプリはRAM 8GB以上**が要る
- 使用量の上限は**5時間ごとにリセット**される。プランなしは10月9日から**Flash-Liteだけ**になる予定
:::

## 表示されるエラーで見分ける

使えない理由を分けると、アカウントの種類・年齢・端末とアプリ・使用量の上限・Google側の障害の5つです。画面にメッセージが出ているなら、まずその文言で見当を付けます。

<figure class="post-figure"><img src="/media/images/gemini-not-working/gnw_00_fig_check.jpg" alt="Geminiが使えないときに確かめる5つの場所の図。困った顔のスマホとノートパソコンのまわりに、アカウントの種類、年齢、端末とアプリ、使用量の上限、Google側の障害の5つの丸が並ぶ" loading="lazy"><figcaption>使えないときに確かめる5つ</figcaption></figure>

| 表示 | 出る場面 | 原因 | 対処 |
|---|---|---|---|
| このサービスにアクセスできない | ウェブ版のログイン | アカウントの種類か年齢が条件外 | 個人のアカウントに切り替えるか管理者に確かめる |
| エラーが発生しました | ウェブ版のアクセスやログイン | 場所・年齢・アカウントの種類など | 時間をおいて再度試す |
| Gemini はお使いのアカウントではご利用いただけません | 子供のアカウント | ファミリーリンクでオフ、または反映待ち | 保護者がオンにして数時間待つ |

<figure class="post-figure"><img src="/media/images/gemini-not-working/gnw_01_help_login.jpg" alt="Googleのヘルプの、Geminiウェブアプリにログインできないの節。このサービスにアクセスできないを開くと、個人のアカウントか管理者がGeminiを有効にした仕事用や学校用のアカウントが使え、個人と学校用は13歳以上、仕事用は18歳以上で、ファミリーリンクで管理されているアカウントはウェブアプリに入れないと書かれている。その下にエラーが発生しましたの説明がある" loading="lazy"><figcaption>Googleのヘルプのログインできないときの説明</figcaption></figure>

画像が作れない場合は「[Geminiの画像生成ができない原因](/media/gemini-image-error/)」、回答が途中で切れる場合は「[Geminiが途中で止まるときの原因と対処](/media/gemini-stops-midway/)」、会話が一覧から消えた場合は「[Geminiのチャットが消えた原因と戻し方](/media/gemini-chat-lost/)」で詳しく扱っています。

## このサービスにアクセスできないと出たとき

ウェブ版でこの表示が出るのは、ログインしたアカウントが条件に合っていないときです。ヘルプの条件をアカウントの種類ごとに並べると次のとおりです。

| アカウント | 年齢 | ほかの条件 |
|---|---|---|
| 個人のGoogleアカウント | 13歳（国ごとの該当年齢）以上 | なし |
| 仕事用のアカウント | 18歳以上 | 対象のWorkspaceのエディションで管理者が有効にしている |
| 学校用のアカウント | 13歳以上 | 管理者が利用を許可している |
| ファミリーリンクで管理しているアカウント | 13歳未満 | 保護者がオンにする。ウェブ版は使えない |

会社や学校から配られたアカウントで出るなら、組織の管理者がGeminiを有効にしていない可能性があります。ヘルプ「[仕事用または学校用の Google アカウントで Gemini アプリを利用する](https://support.google.com/gemini/answer/14620100?hl=ja)」の表では、Business StarterやEnterprise StandardなどはGeminiアプリをコアサービスとして含み、Cloud IdentityやEssentials Starterなどは追加サービスの扱いです。**個人のGmailのアカウントに切り替えて入れるなら、組織の設定か年齢の条件が原因です。**

ウェブ版の一部の機能はログインしなくても使えます。ログインが要るのはそれ以外の機能を使うときと、アクティビティを保存するときです。

<figure class="post-figure post-figure--sp"><img src="/media/images/gemini-not-working/gnw_02_sp_gemini_v2.jpg" alt="スマホのブラウザで開いたログインしていないGeminiのウェブ版。右上のログインのボタンが赤枠で囲まれ、その下にアプリで話そうの案内、中央にあなただけのAIアシスタントGeminiのご紹介、下にGeminiに相談の入力欄がある" loading="lazy"><figcaption>ログインしていないウェブ版のGemini（2026年10月7日、スマホ）</figcaption></figure>

ログインのボタンは[gemini.google.com](https://gemini.google.com/)の右上にあります。ログインなしの画面で確かめると、中央の見出しは「あなただけの AI アシスタント、Gemini のご紹介」で、上にはアプリへの案内が出ていました。対応ブラウザとしてヘルプに挙がっているのはChrome・Safari・Firefox・Opera・Edgium（ヘルプの表記のまま）の5つです。

## エラーが発生しましたと出たとき

ウェブ版を開いたときやログインしたときに「エラーが発生しました」と出る場合、ヘルプは**今そのアカウントではアプリにアクセスできない状態**だと説明しています。理由には場所・年齢・アカウントの種類などが挙がっていて、しばらくしてから試すよう案内されています。

場所の条件を載せているのは「[Gemini ウェブアプリを利用できる言語と国 / 地域](https://support.google.com/gemini/answer/13575153?hl=ja)」です。ウェブ版は40を超える言語と230を超える国と地域で使え、一覧には日本も日本語も入っています。海外にいるときや別の国を経由する接続を使っているときは、その国が一覧にあるかを見ておくと切り分けやすくなります。

ヘルプによると、GoogleはAIの製品で**実在の人が使っているアカウントかどうかを確かめる対策**を取っています。不正のない使い方が続いているアカウントかどうかも、Google側のデータで確かめているとのことです。

## 子供のアカウントで使えないとき

13歳未満の子供のアカウントでは、ファミリーリンクで保護者がGeminiアプリをオンにする必要があります。**オンにしてから使えるまで数時間かかることがあり、使えるのはモバイルアプリだけです。**欧州経済領域・スイス・英国では、子供の管理対象のアカウントでGeminiのアプリを使えません。

オンにする手順と、13歳から17歳で使えない機能は「[Geminiは何歳から使える？年齢制限を解説](/media/gemini-age-limit/)」にまとめています。13歳を過ぎているのに「お使いのアカウントでは使用できません」と出る場合の確かめ方も同じ記事にあります。

## アプリで使えないとき

アプリが入らない・開けないときは、端末が条件を満たしているかを見ます。Googleのヘルプに書かれている条件は次のとおりです。

| 端末 | 条件 | ヘルプ |
|---|---|---|
| Androidのスマホ・タブレット | Android 9以降・RAM 2GB以上。仕事用プロファイルでは使えない | [モバイルアプリの利用要件](https://support.google.com/gemini/answer/14579026?hl=ja&co=GENIE.Platform%3DAndroid) |
| iPhone・iPad | iOS 16以降 | [同（iPhone と iPad）](https://support.google.com/gemini/answer/14579026?hl=ja&co=GENIE.Platform%3DiOS) |
| Mac | macOS Sequoia（15.0）以降・RAM 8GB以上・空き容量200MB以上 | [Mac で Gemini アプリを使用する](https://support.google.com/gemini/answer/17011627?hl=ja) |
| Windows | Windows 10以降・RAM 8GB以上・空き容量200MB以上 | [Windows 向け Gemini アプリを使用する](https://support.google.com/gemini/answer/18263854?hl=ja) |

<figure class="post-figure"><img src="/media/images/gemini-not-working/gnw_04_help_req.jpg" alt="Googleのヘルプのgeminiモバイルアプリの利用要件のページ。150を超える国で利用できること、13歳以上であること、13歳未満は保護者の承認が必要なこと、仕事用や学校用のアカウントではGeminiアプリへのアクセス権が必要なこと、Androidの仕事用プロファイルでは使えないこと、Androidの端末は2GB以上のRAMとAndroid 9以降が必要なことが書かれている" loading="lazy"><figcaption>Geminiモバイルアプリの利用要件（Googleのヘルプ）</figcaption></figure>

**会社のスマホで、仕事用プロファイルの中にGeminiを入れようとしている場合は使えません。**個人用のプロファイルで開くか、会社の管理者に確かめてください。モバイルアプリは13歳以上が条件で、13歳未満は保護者の承認が要ります。iPhoneとiPadでは端末の言語をGeminiの対応言語にしておくことも条件です。

パソコンで使う手段はブラウザとMac・Windowsのアプリの2通りです。**アプリが古いと一部の機能が動かないことがある**とMac版のヘルプに書かれていて、モデルの変更のお知らせもモバイルアプリを最新にしておくよう勧めています。古いAndroidの端末でアプリが入らないなら、ウェブ版をブラウザで開く手があります。声で話すGemini Liveだけが使えないなら、[Gemini Liveが使えない原因と対処](/media/gemini-live-not-working/)で端末ごとの条件を確かめられます。

## 使用量の上限で止まったとき

使っている途中で止まり上限の通知が出たなら、使用量の上限に達した状態です。ヘルプ「[Gemini モデルへのアクセスと使用量上限の変更](https://support.google.com/gemini/answer/17004136?hl=ja)」によると、Geminiアプリの上限は回数ではなく使った量で決まり、週の上限に達するまで5時間ごとにリセットされます。同じページで使用量が多くなるものとして挙がっているのは、画像や動画・音楽の生成、Deep Research、Proモデル、拡張思考などです。プランごとの倍率と残りの確かめ方は「[Geminiの回数制限を解説](/media/gemini-limits/)」にまとめています。

<figure class="post-figure"><img src="/media/images/gemini-not-working/gnw_06_help_model.jpg" alt="GoogleのヘルプのGeminiモデルへのアクセスと使用量上限の変更のページ。2026年10月より個人アカウントで利用できるモデルが変わり、AIサブスクリプションを利用していないユーザーには10月9日から適用されるという段落が赤枠で囲まれている。下の表も赤枠で囲まれ、プランなしはFlash-Liteだけ、AI PlusはFlash-LiteとFlash、AI ProとAI Ultraは3つすべてに印が付いている" loading="lazy"><figcaption>10月9日からの使えるモデルの表（2026年10月7日取得）</figcaption></figure>

**プランなしの個人のアカウントは、10月9日から使えるモデルがFlash-Liteだけになる予定です。**表の対象は個人のアカウントで、AI Plusの利用者には適用の時期をメールで知らせるとされています。10月7日の時点ではまだ適用前でした。

| プラン | 10月9日からの予定で使えるモデル |
|---|---|
| プランなし | Flash-Lite |
| AI Plus | Flash-Lite・Flash（適用日はメールで案内） |
| AI Pro | Flash-Lite・Flash・Pro |
| AI Ultra | Flash-Lite・Flash・Pro |

予定どおり適用されれば、無料のアカウントでFlashやProを選べなくなるのはこの変更によるもので、アカウントの不具合とは別です。

Flash-LiteとFlashの違いや、無料のままFlashを使う方法は「[Gemini Flash-Liteとは](/media/gemini-flash-lite/)」で詳しく扱っています。

## 障害を確かめる

アカウントも端末も条件に合っているのに使えないなら、Google側の障害も考えられます。仕事用のアカウントなら、[Google Workspace ステータス ダッシュボード](https://www.google.com/appsstatus/dashboard/)に「Gemini」の行があります。

10月7日に見たところ、8月中旬以降でGeminiの件として載っていたのは9月11日の1件でした。日本時間の9月11日22時から12日5時22分まで、一部の利用者でGemini 3.1 Proのエラーが増えた件です。**影響はウェブ版とアプリの両方に出ていましたが、対象はGemini 3.1 Proを使う一部の利用者でした。**

## よくある質問

### Geminiが使えないのはなぜですか？

まずアカウントの種類と年齢の条件を確かめてください。個人と学校のアカウントは13歳以上、仕事用のアカウントは18歳以上で、管理者がGeminiを有効にしている必要があります。

### Geminiでエラーが発生しましたと出たらどうしますか？

場所・年齢・アカウントの種類などで、今そのアカウントが使えない状態です。ヘルプはしばらくしてから試すよう案内しています。

### 子供のアカウントでGeminiを使えますか？

13歳未満でも、保護者がファミリーリンクでGeminiアプリをオンにすれば使えます。使えるのはモバイルアプリで、ウェブ版には入れません。

### 会社のアカウントでGeminiが使えないのはなぜですか？

WorkspaceのエディションがGeminiの対象でないか、管理者がGeminiを有効にしていない可能性があります。仕事用のアカウントは18歳以上も条件です。

### Geminiのアプリはどの端末で使えますか？

AndroidはAndroid 9以降でRAMが2GB以上、iPhoneとiPadはiOS 16以降です。MacとWindowsのアプリはRAMが8GB以上必要です。

### Geminiは無料で使い続けられますか？

プランなしでも使えます。ただしヘルプの予定では、10月9日から無料で使えるモデルはFlash-Liteだけになります。

### Geminiはログインしなくても使えますか？

ウェブ版の一部の機能はログインなしで使えます。ほかの機能とアクティビティの保存にはログインが必要です。

### Geminiの障害はどこで確かめますか？

仕事用のアカウントなら、Google Workspace ステータス ダッシュボードのGeminiの行で確かめられます。

## 出典

- Google Gemini アプリ ヘルプ「[Gemini アプリへのログインに必要なもの](https://support.google.com/gemini/answer/13278668?hl=ja)」（2026年10月7日取得）
- Google Gemini アプリ ヘルプ「[Gemini モデルへのアクセスと使用量上限の変更](https://support.google.com/gemini/answer/17004136?hl=ja)」（2026年10月7日取得）
- Google Gemini アプリ ヘルプ「[お子様による Gemini アプリの利用をサポートする](https://support.google.com/gemini/answer/16109150?hl=ja)」（2026年10月7日取得）
- Google Gemini アプリ ヘルプ「[Gemini モバイルアプリの利用要件](https://support.google.com/gemini/answer/14579026?hl=ja&co=GENIE.Platform%3DAndroid)」（Android・iPhone と iPad、2026年10月7日取得）
- Google Gemini アプリ ヘルプ「[Mac で Gemini アプリを使用する](https://support.google.com/gemini/answer/17011627?hl=ja)」「[Windows 向け Gemini アプリを使用する](https://support.google.com/gemini/answer/18263854?hl=ja)」（2026年10月7日取得）
- Google Gemini アプリ ヘルプ「[Gemini ウェブアプリを利用できる言語と国 / 地域](https://support.google.com/gemini/answer/13575153?hl=ja)」（2026年10月7日取得）
- Google Gemini アプリ ヘルプ「[仕事用または学校用の Google アカウントで Gemini アプリを利用する](https://support.google.com/gemini/answer/14620100?hl=ja)」（2026年10月7日取得）
- [Google Workspace ステータス ダッシュボード](https://www.google.com/appsstatus/dashboard/)（2026年10月7日取得）
- ウェブ版の画面は、2026年10月7日にスマホ表示のブラウザでログインせずに撮影
