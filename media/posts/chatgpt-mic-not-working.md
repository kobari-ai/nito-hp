---
title: 【2026年10月】ChatGPTの音声入力ができない原因と直し方｜マイク許可・文字にならない・PC
date: 2026-10-15
category: AI検索対策
description: ChatGPTの入力欄のマイク（音声入力）が使えない原因を、ボタンが無い・マイクのアクセス・文字にならない・長く話すと失敗・誤りが多いに分けて解説。Windows 11とMacの設定、公式の更新履歴も確認。
cover_tag: 使い方
cover_headline: ChatGPTの音声入力ができない
cover_sub: マイク許可・文字にならないの直し方
---

OpenAIは2026年6月26日、ChatGPTの音声入力（入力欄のマイク）の文字起こしを新しいモデルに切り替え始め、対象を全プランとしました。その前の1月12日にも、話したのに文字起こしが空で返る失敗を大きく減らす更新が入っています。それでもマイクが反応しない・文字にならないという症状は、OSやブラウザの設定、アプリのバージョン、回線の側で起きます。

音声入力の不具合はボタンが無い・マイクのアクセスを求められる・録音されるのに文字にならない・長く話すと失敗する・誤りが多いの5つに分けると、原因を絞れます。**声で返事が来る音声会話とは別の機能**なので、確かめる場所も別です。

この記事ではOpenAIの[音声入力 - FAQ](https://help.openai.com/ja-jp/articles/12168547-voice-dictation-faq)と[ChatGPT Release Notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)（2026年10月15日取得）、Windows・Mac・Chromeのヘルプを並べ、症状ごとに確かめる順番を書きます。

:::takeaways
- 入力欄のマイクは**音声入力（Dictation）**。声を文字にして、送る前に直せる。音声会話とは入口が別
- 「マイクのアクセスを有効に」と出たら、**OS（Windows 11・Mac・スマホ）とブラウザの両方**の許可を確かめる
- 録音されるのに文字にならないなら、**アプリの更新・使うマイクの選び直し・回線**の順に見る
- 1回に録音できる長さの上限は**公式ヘルプに書かれていない**。長い依頼は区切って録音する
- ChatGPTの側で直らないときは、**Windowsキー＋HやMacのマイクキー**で使えるOSの音声入力で代えられる
:::

## 音声入力と音声会話の違い

ChatGPTの画面には声を使う入口が2つあります。入力欄の中にあるマイクのアイコンが音声入力で、音声入力 - FAQによると、録音した声は文字起こしのためにOpenAIのモデルへ送られ、テキストになって戻ってきます。**戻った文字は送る前に入力欄で直せる**のが、音声会話との大きな違いです。

<figure class="post-figure"><img src="/media/images/chatgpt-mic-not-working/01_fig_overview.jpg" alt="ChatGPTの音声入力と音声会話を左右に並べた図。左は入力欄のマイクで、話した声が文字の行になり入力欄に入り、文字にして送る前に直せると書かれている。右は音声会話で、声で返事が返ってくると書かれている" loading="lazy"></figure>

音声会話のヘルプ（[ChatGPT 音声モード](https://help.openai.com/ja-jp/articles/20001274-chatgpt-voice)）も、録音した依頼を確認・編集してから送りたいときは音声入力、話しながら考えを整理したいときは音声会話と書き分けています。音声会話のボタンが無い・途中で切れるといった症状は、[ChatGPTの音声会話ができない原因の記事](/media/chatgpt-voice-not-working/)で扱いました。

<figure class="post-figure"><img src="/media/images/chatgpt-mic-not-working/cmn_02_composer_pc.jpg" alt="chatgpt.comをパソコンのChromeで開いた画面。どこから始めますか？の下に入力欄があり、右端の送信ボタンの左にあるマイクのアイコンに赤枠が付いている" loading="lazy"><figcaption>赤枠のマイクが音声入力のボタン（2026年10月15日に撮影）</figcaption></figure>

## 症状ごとの原因と最初の一手

自分の画面で何が起きているかを先に見分けると、確かめる場所は1つか2つに絞れます。この記事で扱う症状と最初に見るところを、下の表に並べました。

| 症状 | 主な原因 | 最初に確かめること |
|---|---|---|
| マイクのボタンが無い | ログインしていない・アプリが古い | ログインしてアプリを最新にする |
| マイクのアクセスを求められる | OSかブラウザの許可がオフ | OSの設定とブラウザのサイトの設定 |
| 録音されるのに文字にならない | 空の文字起こし・別のマイクの音を拾っている・回線 | アプリの更新と既定のマイク |
| 長く話すと失敗する | 回線の途切れ・時間切れ | 短く区切って録音する |
| 文字の誤りが多い | 背景の音・聞き取りの誤り | 送る前に入力欄で直す |
| 音声入力しかできない | 音声会話の画面に入っている | 終了のボタンで戻る |

## マイクのボタンが無いとき

2026年10月15日に、ログインしていないChromeでchatgpt.comを開いて試しました。パソコンの幅（横1400ピクセル）では入力欄に［音声入力を開始］のボタンがありましたが、スマホの幅（横390ピクセル）では＋と送信のボタンだけで、マイクは見えませんでした。

<figure class="post-figure post-figure--sp"><img src="/media/images/chatgpt-mic-not-working/cmn_03_mobileweb_sp.jpg" alt="chatgpt.comをスマホの幅で開いた画面。今日は何をしますか？の下の入力欄にはプラスのボタンとChatGPTに聞くの文字と送信のボタンだけがあり、マイクのアイコンは無い。入力欄に赤枠が付いている" loading="lazy"><figcaption>ログインしていないスマホの幅では入力欄にマイクが無かった</figcaption></figure>

**スマホのブラウザでマイクが見当たらないなら、ログインするか、ChatGPTのアプリで開き直す**のが早道です。ログインした状態のスマホのブラウザは、この日は確かめていません。アプリでもマイクが無ければ、App StoreかGoogle Playで最新のバージョンにしてから探し直してください。

## マイクのアクセスを求められるとき

2026年3月のYahoo!知恵袋には、Windows 11のパソコンでChatGPTに「音声入力をするにはマイクのアクセスを有効にしてください」と表示されるという相談がありました。この表示が出ている間、ChatGPTはマイクを使えていません。**許可はOSとブラウザ（アプリ）の2段になっている**ため、上の段から順に確かめます。

### Windows 11の設定

Microsoftの[Windows カメラ、マイク、プライバシー](https://support.microsoft.com/ja-jp/windows/privacy/windows-camera-microphone-and-privacy)の手順では、［スタート］＞［設定］＞［プライバシーとセキュリティ］＞［マイク］を開きます。そこで次の3つがオンになっているかを見ます。

1. ［マイク アクセス］
2. ［アプリがマイクにアクセスできるようにする］
3. 使うMicrosoft Storeアプリの個別の切り替え

<figure class="post-figure post-figure--sp"><img src="/media/images/chatgpt-mic-not-working/cmn_04_windows_help_sp.jpg" alt="Microsoftサポートのページをスマホで開いた画面。マイクを使うことができるアプリを管理する方法の見出しの下に、スタートから設定のプライバシーとセキュリティのマイクを選ぶ手順と、マイク アクセスとアプリがマイクにアクセスできるようにするとMicrosoft Storeアプリの切り替えを確かめる手順があり、2つに赤枠と番号が付いている" loading="lazy"><figcaption>①で［マイク］を開き、②の切り替えを確かめる</figcaption></figure>

同じヘルプによると、一覧に出てこないアプリはデスクトップ アプリの可能性があり、個別には切り替えられません。その場合は［デスクトップ アプリにマイクへのアクセスを許可する］で扱います。**ChromeやEdgeで使っていて一覧にブラウザが無いなら、このスイッチがオフになっていないか**を見てください。ChatGPTのアプリをMicrosoft Storeから入れたなら、一覧のChatGPTをオンにします。

### Macの設定

Appleの[Macのマイクへのアクセスを制御する](https://support.apple.com/ja-jp/guide/mac-help/mchla1b1e1fe/mac)の手順は3段です。

1. アップルメニュー＞［システム設定］＞［プライバシーとセキュリティ］を開く
2. ［マイク］をクリックする
3. 一覧のアプリごとにオンとオフを切り替える

<figure class="post-figure"><img src="/media/images/chatgpt-mic-not-working/cmn_05_mac_help.jpg" alt="AppleサポートのMacのマイクへのアクセスを制御するのページ。アップルメニューからシステム設定のプライバシーとセキュリティを選ぶ手順、マイクをクリックする手順、リストのアプリごとにマイクへのアクセスのオンとオフを切り替える手順に赤枠と番号が付いている" loading="lazy"><figcaption>①［プライバシーとセキュリティ］②［マイク］③アプリごとの切り替えの順に進む</figcaption></figure>

Chromeで使うならGoogle Chromeを、ChatGPTのデスクトップアプリで使うならChatGPTを一覧でオンにします。Chromeのヘルプによると、パソコンの設定で許可を変えたあとに終了を求められたら画面の指示に沿って終了するか、Chromeを再起動します。**許可を変えたのに直らないときは、ブラウザやアプリを一度終了して開き直してから試してください**。

### ブラウザの設定

OSで許可していても、ブラウザがchatgpt.comのマイクを止めていると録音は始まりません。Googleの[Chrome でカメラとマイクを使用する](https://support.google.com/chrome/answer/2693767?hl=ja)では、［設定］＞［プライバシーとセキュリティ］＞［サイトの設定］＞［権限］の［マイク］を開き、許可しないサイトにchatgpt.comが入っていないかを見ます。

<figure class="post-figure post-figure--sp"><img src="/media/images/chatgpt-mic-not-working/cmn_06_chrome_help.jpg" alt="Google ChromeヘルプのChrome でカメラとマイクを使用するのページ。サイトに対するカメラやマイクへのアクセスを変更する手順のうち、プライバシーとセキュリティからサイトの設定を選ぶ手順と、権限でマイクを選ぶ手順、開いた既定のマイクを選択するの手順に赤枠と番号が付いている" loading="lazy"><figcaption>①②でマイクの権限を開き、③で使うマイクを選べる</figcaption></figure>

同じヘルプには、許可したサイトでも**別のタブや別のアプリを使っている間は録音を始められない**と書かれています。音声入力のボタンはchatgpt.comのタブを表示した状態で押してください。職場や学校のChromeは管理者がカメラとマイクの設定を決めていることがあり、その場合は自分で変えられません。

### iPhoneとAndroidの設定

スマホのアプリで初めてマイクを使うときの確認に［許可しない］を選ぶと、OSの設定で許可し直すまで録音できません。iPhoneは［設定］＞［プライバシーとセキュリティ］＞［マイク］、Androidは［設定］＞［アプリ］＞ChatGPT＞［権限］＞［マイク］が入口です。画面つきの手順は[音声会話の記事のマイクの許可の節](/media/chatgpt-voice-not-working/)にあり、アプリのマイクの許可は音声入力と音声会話で共通です。

## 録音されるのに文字にならないとき

2025年にredditへ投稿された相談では、Windows 11のアプリやChromeで録音中の表示は出るのに、止めても入力欄に何も入らないという症状が書かれていました。マイクは音を拾っているので、許可の問題とは切り分けて考えます。

### 空の文字起こし

OpenAIは2026年1月12日のリリースノートで、音声入力を改善し、**空の文字起こしを大きく減らした**と書いています。アプリが古いバージョンのまま、またはブラウザのタブを長く開いたままなら、アプリの更新かページの再読み込みをしてから試し直すのが先です。

<figure class="post-figure"><img src="/media/images/chatgpt-mic-not-working/cmn_07_release_jan.jpg" alt="OpenAIのChatGPTリリースノートの英語のページ。January 12, 2026の見出しの下にDictation Updatesの項があり、ログインしているすべてのユーザー向けに音声入力を改善し空の文字起こしを大きく減らしたという文に赤枠が付いている" loading="lazy"><figcaption>2026年1月12日の項。空の文字起こしを減らした</figcaption></figure>

### マイクが複数あるとき

2025年にredditへ投稿された解決の報告では、WebカメラのマイクでだけChatGPTの音声入力が文字にならず、Windowsのサウンドの設定でほかのマイクを無効にしたら直ったとありました。投稿者1人の報告なので、ほかの環境でも同じ直し方が効くとは限りません。

Chromeなら、さきほどのヘルプの［既定のマイクを選択する］で、サイトが使うマイクを1つに決められます。同じヘルプのマイクのトラブルシューティングにも、**システムの設定で既定の録音デバイスに正しいマイクが選ばれているか**を確かめる手順があります。ヘッドセットを使うなら、コードのミュートスイッチが入っていないかも見てください。

### 回線と障害

2026年8月7日のリリースノートによると、iPhoneのアプリは接続の問題や時間切れで音声入力が失敗したとき**自動で1回だけ再試行する**ようになりました。それでも失敗するなら、Wi-Fiとモバイル回線を切り替えて試します。[OpenAIのステータスページ](https://status.openai.com/)でChatGPTに障害が出ていなければ、残るのは自分の側の回線や端末です。

## 長く話すと失敗するとき

音声入力 - FAQとリリースノートには、1回に録音できる長さの上限は書かれていません（2026年10月15日に確認）。[OpenAI Developer Community](https://community.openai.com/t/voice-recording-useless-over-2-and-a-half-minutes/1064914)には2024年12月に、モバイルのアプリで2〜3分を超える録音がネットワークや文字起こしのエラーで失敗するという投稿があります。今のバージョンでも同じかは確かめていません。

**長い依頼は短く区切って録音し、文字になったのを確かめてから続きを話す**と、失敗したときの言い直しが少なくて済みます。Androidのアプリは2026年8月14日の更新で、文字や添付を入れたあとも音声入力のボタンが残るようになりました。同じメッセージに、打った文字と録音を足していけます。

## 文字の誤りが多いとき

2026年6月26日のリリースノートによると、音声入力の文字起こしは新しいモデルに替わり、OpenAIの評価では日本語を含む言語で精度が上がりました。主な言語の単語誤り率は以前のモデルより10%以上低かったとされています（OpenAIの社内評価の実測値）。騒がしい場所や小さな声、英字と数字の組み合わせにも強くなったと書かれています。

<figure class="post-figure"><img src="/media/images/chatgpt-mic-not-working/cmn_08_release_jun.jpg" alt="OpenAIのChatGPTリリースノートのImproved dictation in ChatGPTの項。複数の言語やなまりで文字起こしの精度が上がり、日本語・韓国語・中国語などで改善したという段落に赤枠が付いている" loading="lazy"><figcaption>2026年6月26日の項。評価で改善した言語に日本語が入っている</figcaption></figure>

新しいモデルでも、聞き取った文字が話した内容と合わないことは避けられません。そのため**送る前に入力欄の文字を読み直す**のが確実で、音声入力 - FAQも、文字起こしはユーザーメッセージとして送信する前に編集できると説明しています。誤りが続くなら、静かな場所に移るかマイクを口に近づけてから録音し直してください。

<figure class="post-figure post-figure--sp"><img src="/media/images/chatgpt-mic-not-working/cmn_09_faq_sp.jpg" alt="OpenAI公式ヘルプの音声入力 - FAQのページをスマホで開いた画面。音声入力はどのように機能しますかの答えとして、マイクアイコンを押して録音した音声は文字起こしのためにモデルに送られ、テキストとして返され、送信する前に編集できるという段落に赤枠が付いている" loading="lazy"><figcaption>文字起こしは送信の前に編集できる</figcaption></figure>

## 音声入力しかできないとき

声の画面から文字の入力に戻れないなら、開いているのは音声入力ではなく音声会話のほうです。[ChatGPT 音声モード](https://help.openai.com/ja-jp/articles/20001274-chatgpt-voice)のヘルプでは、会話中はマイクのコントロールでミュートでき、終了のコントロールで音声会話を終えられます。

同じヘルプによると、音声モードはチャットの中で動くため、話せないときは文字で入力することもできます。**文字だけでやり取りしたいなら、終了のボタンで音声会話を終えてから入力欄に打ちます**。入力欄のマイクは録音を文字にするだけで、声の返事は返ってきません。

## OSの音声入力で代える

ChatGPTの側で直らないときの代わりの手が、入力欄にOSの音声入力で文字を入れる方法です。ChatGPTの文字起こしは使わず、OSが文字にしたものがそのまま入力欄に入ります。

### Windowsの音声入力

Microsoftの[音声入力を使用して、PC 上でタイプをする代わりに話す](https://support.microsoft.com/ja-jp/accessibility/windows/use-voice-typing-to-talk-instead-of-type-on-your-pc)によると、テキストボックスにカーソルを置いて**Windowsキー＋H**を押すと聞き取りが始まります。インターネットへの接続と動くマイクが必要で、Azure Speechサービスのオンライン音声認識を使います。

<figure class="post-figure post-figure--sp"><img src="/media/images/chatgpt-mic-not-working/cmn_10_voice_typing_sp.jpg" alt="Microsoftサポートの音声入力を使用して、PC上でタイプをする代わりに話すのページをスマホで開いた画面。インターネットに接続しマイクを動作させテキストボックスにカーソルを置く必要があるという段落と、ハードウェアキーボードでWindowsキーとHキーを押す手順に赤枠と番号が付いている" loading="lazy"><figcaption>①の条件をそろえ、②のWindowsキー＋Hで始める</figcaption></figure>

Microsoftのプライバシーのヘルプには、［デスクトップ アプリにマイクへのアクセスを許可する］をオフにすると、Windowsのディクテーションにも影響が出る場合があると書かれています。Windowsの音声入力まで反応しないなら、先にWindows 11の設定の節を見直してください。

### Macの音声入力

Appleの[Macでメッセージや書類を音声入力する](https://support.apple.com/ja-jp/guide/mac-help/mh40584/mac)では、［システム設定］＞［キーボード］で［音声入力］をオンにし、マイクキーか音声入力のキーボードショートカットで始めます。同じページには**音声入力できるテキストの長さに制限はなく、タイムアウトもない**とあり、30秒間声が検出されないと自動で止まります。ChatGPTの音声入力で長い依頼が途中で失敗する人に向いた方法です。

## よくある質問

### ChatGPTの音声入力は無料で使えますか？

使えます。2026年6月26日の新しい文字起こしのモデルは、リリースノートで全プランが対象とされています。ログインしていないスマホのブラウザではマイクが見えなかったので（2026年10月15日に試した結果）、ログインするかアプリで使ってください。

### ChatGPTの音声入力はパソコンでも使えますか？

使えます。chatgpt.comの入力欄のマイクから録音でき、試した日はログインしていないパソコンの幅のChromeにもボタンがありました。Windows 11ならOSのマイクの許可、Chromeならサイトのマイクの許可の両方がオンになっている必要があります。

### ChatGPTの音声入力に時間の上限はありますか？

音声入力 - FAQとリリースノートには上限の記載がありません。2024年12月にはモバイルのアプリで2〜3分を超える録音が失敗したという利用者の投稿があるため、長い依頼は区切って録音するほうが失敗に強くなります。

### ChatGPTの音声入力の録音は保存されますか？

音声入力 - FAQによると、録音はそのチャットが履歴にある間は保持され、チャットを消すと30日以内に削除されます（セキュリティ上・法律上の理由で残す場合などを除く）。モデルの改善に音声の共有を選んでいる個人の利用者は、学習に使われることがあります。共有を止めたいときは設定のデータコントロールで［音声録音を含める］をオフにしてください。

### ChatGPTの音声入力にショートカットはありますか？

chatgpt.comやアプリの音声入力を始めるキーボードショートカットは、OpenAIのヘルプでは見つかりませんでした（2026年10月15日に確認）。キーで始めたいなら、WindowsはWindowsキー＋H、Macはマイクキーで使えるOSの音声入力が代わりになります。

### ChatGPTで音声入力ができないのはなぜですか？

OSとブラウザのマイクの許可・ログインとアプリのバージョン・使うマイクの選択・回線の順に確かめます。「マイクのアクセスを有効にしてください」と出るなら許可の問題で、録音中の表示が出るのに文字にならないなら許可より後ろの問題です。

### ChatGPTの音声入力が文字にならないのはなぜですか？

空の文字起こし、別のマイクの音を拾っている、回線の途切れの3つを疑います。OpenAIは2026年1月12日に空の文字起こしを減らす更新を出しているので、アプリを最新にしたうえで、Chromeやシステムの設定で使うマイクを1つに決めてから試し直してください。

### ChatGPTの音声入力と音声会話の違いは何ですか？

音声入力は録音を文字にして、送る前に直せる機能です。音声会話は声で話して声で返事を聞く機能で、ヘルプによると会話の文字起こしは逐語の記録ではなく、話した内容と完全には一致しないことがあります。

## 出典

- OpenAI Help Center「[音声入力 - FAQ](https://help.openai.com/ja-jp/articles/12168547-voice-dictation-faq)」（2026年10月15日取得）
- OpenAI Help Center「[ChatGPT Release Notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)」（同。2026年1月12日のDictation Updates、6月26日のImproved dictation in ChatGPT、8月7日と8月14日のアプリの更新の項）
- OpenAI Help Center「[ChatGPT 音声モード](https://help.openai.com/ja-jp/articles/20001274-chatgpt-voice)」（同）
- Microsoft サポート「[Windows カメラ、マイク、プライバシー](https://support.microsoft.com/ja-jp/windows/privacy/windows-camera-microphone-and-privacy)」（同）
- Microsoft サポート「[音声入力を使用して、PC 上でタイプをする代わりに話す](https://support.microsoft.com/ja-jp/accessibility/windows/use-voice-typing-to-talk-instead-of-type-on-your-pc)」（同）
- Apple サポート「[Macのマイクへのアクセスを制御する](https://support.apple.com/ja-jp/guide/mac-help/mchla1b1e1fe/mac)」（同）
- Apple サポート「[Macでメッセージや書類を音声入力する](https://support.apple.com/ja-jp/guide/mac-help/mh40584/mac)」（同）
- Google Chrome ヘルプ「[Chrome でカメラとマイクを使用する](https://support.google.com/chrome/answer/2693767?hl=ja)」（同）
- OpenAI「[ステータスページ](https://status.openai.com/)」（同）
- OpenAI Developer Community「[Voice Recording Useless over 2 and a half minutes](https://community.openai.com/t/voice-recording-useless-over-2-and-a-half-minutes/1064914)」（2024年12月22日の投稿）
- reddit r/ChatGPT「[ChatGPT Dictate Not Working – Solved](https://www.reddit.com/r/ChatGPT/comments/1kox5mt/chatgpt_dictate_not_working_solved/)」「[ChatGPT Voice Input Issue](https://www.reddit.com/r/ChatGPT/comments/1nysa6f/chatgpt_voice_input_issue/)」（2025年の投稿）
- Yahoo!知恵袋「[chatgptで音声入力をしようとすると…](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q13326370408)」（2026年3月18日の質問）
