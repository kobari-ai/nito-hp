---
title: 【2026年10月】GoogleマップのGeminiはオフにできる？ナビ・マップに相談の設定とデータ
date: 2026-10-13
category: AI活用
description: GoogleマップのGeminiを止める設定をヘルプで確認。ナビ中の「OK Google」をAndroidとiPhoneで切る場所、マップに相談を切る設定がヘルプに見当たらないこと、会話と位置情報の扱い、使えないときの条件まで。
cover_tag: 設定
cover_headline: GoogleマップのGeminiを止める
cover_sub: ナビ・マップに相談・保存されるデータ
---

2026年8月7日、Googleは日本でGoogleマップの新機能「マップに相談」の提供を始め、検索バーの下にGeminiと会話するボタンが加わりました。ナビ中の音声操作も、2025年11月の発表から、Geminiを使える国で順次Googleアシスタントに代わってGeminiが受け持つようになりました。

頼んでいないのにボタンが増えた、ナビ中に話しかけたらGeminiが返事をした、という変化は、アプリを更新しただけで起きます。この記事は2026年10月13日に取得したGoogleのヘルプとブログをもとに、**GoogleマップのGeminiを入口ごとに、止められるものと止められないものに分けて**並べます。端末での操作は試していません。

:::takeaways
- GoogleマップでGeminiが出る場所は**スマホの検索バーの下の［マップに相談］・パソコン版のマップに相談（WebGLが必要）・ナビ画面のGeminiアイコンと「OK Google」・お店や施設のページの質問**の4つ
- ナビ中に声でGeminiを呼ぶ入口は、**Androidは Geminiアプリの［Gemini とハンズフリーで話す］の「OK Google」、iPhoneはマップのナビの設定の［「Ok Google」でアシスタントを利用する］**。マップのヘルプはオンにする手順だけを載せていて、オフにしたときの動きは書いていない
- **マップに相談には、2026年10月13日時点のヘルプに切る設定もボタンを消す設定も書かれていない**。会話は履歴から会話ごとに消せる
- マップに相談の回答とナビのGeminiでは**位置情報が保存されることがある**とヘルプは書いている
- 使えないときは、仕事用のプロファイルではないか・ナビゲーション モードに入っているか・マップに相談が届いているかを先に見る
:::

## GoogleマップでGeminiが出る4つの場所

「最近マップの画面が変わった」と感じたら、どの画面で変わったかで入口が分かれます。Googleのヘルプとブログを並べると、日本のGoogleマップでGeminiが動く入口は次の4つです。

<figure class="post-figure"><img src="/media/images/google-maps-gemini/01_fig_overview.png" alt="スマホのGoogleマップでGeminiが出る3つの入口を描いたイラスト（実際の画面ではない）。検索バーのすぐ下にボタンがある地図の画面がマップに相談、ナビ案内中の画面で右下に星形のアイコンがあるのがナビのGemini、お店の詳細ページで吹き出しのアイコンがあるのが場所への質問" loading="lazy"><figcaption>スマホの入口は検索バーの下・ナビの画面・場所のページの3つ（イラスト）</figcaption></figure>

| 入口 | 何をするか | 使えるようになった時期 |
|---|---|---|
| ［マップに相談］（スマホ） | 検索バーの下のボタンから、条件をまとめて話すと場所やルートを提案する | 日本で2026年8月7日から数週間かけて順に |
| ［マップに相談］（パソコン） | メニュー アイコンの［マップに相談］から質問する。ブラウザでWebGLが使える必要がある | ヘルプに時期の記載なし |
| ナビのGemini | ナビ中に「OK Google」かGeminiアイコンで呼び、ルートの変更や途中の店探しを頼む | 2025年11月5日の発表から、Geminiを使える国で順次 |
| 場所への質問 | お店や施設のページでGeminiのヒントを読み、「無料駐車場はありますか？」のように聞く | 日本のAndroidとiOSで2026年2月13日の発表から |

マップに相談の始め方は、Googleマップ ヘルプの「[Google マップで質問する](https://support.google.com/maps/answer/16842041?hl=ja)」が案内しています。**ボタンの場所は検索バーの下で、押さなければGeminiとの会話は始まりません。**

店舗を運営する会社向けに、マップのAIとビジネスプロフィールの関係は[GoogleビジネスプロフィールのAI対策の記事](/media/gbp-ai-search/)で整理しています。

<figure class="post-figure post-figure--sp"><img src="/media/images/google-maps-gemini/03_help_ask.jpg" alt="Google マップ ヘルプ「Google マップで質問する」のAndroidの手順。赤い枠の1番に、検索バーの下にあるマップに相談をタップします、と書かれている。その前後に、Google マップ アプリを開く、プロンプトが表示されたら質問を入力するかマイクをタップする、送信アイコンをタップする、の手順が並ぶ" loading="lazy"><figcaption>マップに相談は検索バーの下のボタンから開く（Google マップ ヘルプ、2026年10月13日取得）</figcaption></figure>

## 何が変わったのか

ナビの「OK Google」は、以前はGoogleアシスタントが答えていました。Googleは2025年11月5日の公式ブログ「[Google Maps launches Gemini features, including landmark navigation](https://blog.google/products-and-platforms/products/maps/gemini-navigation-features-landmark-lens/)」で、**Geminiが使えるすべての地域のAndroidとiOSに、ナビ中のGeminiを順に届ける**と発表しています。2026年1月29日には[徒歩と自転車のナビにも広げました](https://blog.google/products-and-platforms/products/maps/gemini-navigation-biking-walking/)。

<figure class="post-figure"><img src="/media/images/google-maps-gemini/02_fig_timeline.png" alt="GoogleマップにGeminiが入った順番の年表。2025年11月5日にナビの音声操作をGeminiにしGeminiが使える地域のAndroidとiPhoneへ順に、2026年1月29日に徒歩と自転車のナビでもGeminiに、2026年2月13日にお店や施設のページにGeminiのヒントと質問（日本）、2026年8月7日に検索バーの下にマップに相談（日本で数週間かけて順に）、2026年9月4日にスマホのGoogleアシスタントの提供終了が始まる" loading="lazy"><figcaption>ナビ・場所のページ・検索バーの順にGeminiが入った</figcaption></figure>

マップに相談は、[Google Japan Blogの2026年8月7日の記事](https://blog.google/intl/ja-jp/products/connect-communicate/japanese-ask-maps/)が日本での提供開始を伝えました。「本日より数週間かけて順次」とあるため、同じ日に更新しても家族の端末にはボタンがあり自分には無い、ということが起こります。

**スマホのGoogleアシスタントそのものも終了が報じられています。**[ITmedia Mobileの記事](https://www.itmedia.co.jp/mobile/articles/2608/06/news064.html)によると、2026年9月4日からモバイル版のアシスタントの削除が始まると報じられました。アシスタントに戻してマップの音声操作も元に戻す、という逃げ道は使えなくなりつつあります。端末全体でGeminiが勝手に開くときの止め方は「[Geminiが勝手に起動する原因と止め方](/media/gemini-auto-launch/)」にまとめています。

## ナビ中のGeminiを声で呼ぶ設定

ナビ中のGeminiが開くのはGeminiアイコンを押すか「OK Google」と言ったときです。Googleマップ ヘルプ「[移動中に Gemini を使用する](https://support.google.com/maps/answer/6041199?hl=ja)」の手順も、ナビゲーション モードでこの2つのどちらかをする形です。**アイコンは押さなければ動かないため、止めたいのは「OK Google」の声のほうです。**

<figure class="post-figure post-figure--sp"><img src="/media/images/google-maps-gemini/04_help_nav.jpg" alt="Google マップ ヘルプ「移動中に Gemini を使用する」のAndroidの手順。赤い枠の1番に、ナビゲーション モードで「OK Google」と話しかけるかGeminiアイコンをタップします、「OK Google」が機能しない場合は「OK Google」とVoice Match（Geminiを使用）が有効になっていることを確認してください、と書かれている" loading="lazy"><figcaption>ナビのGeminiは「OK Google」かアイコンで開く（Google マップ ヘルプ、2026年10月13日取得）</figcaption></figure>

### Androidの場合

マップのヘルプは、ナビで「OK Google」が効かないときは「OK Google」とVoice Match（Geminiを使用）の設定を見るよう案内しています。声の呼び出しを受け持つのはGeminiアプリの側です。Gemini アプリ ヘルプ「[Android デバイスで Gemini アプリを管理、削除する](https://support.google.com/gemini/answer/16938321?hl=ja)」の手順は次のとおりです。

1. Geminiアプリを開く
2. 左上のメニュー、またはプロフィール写真から［設定］を開く
3. ［Gemini とハンズフリーで話す］をタップする
4. 「OK Google」をオフにする

<figure class="post-figure post-figure--sp"><img src="/media/images/google-maps-gemini/05_help_okg.jpg" alt="Gemini アプリ ヘルプの「OK Google」をオフにする手順。赤い枠の中に、「OK Google」と聞こえたときにGeminiが起動しないようにするにはGeminiアプリを残したまま「OK Google」をオフにします、1. Android スマートフォンまたはタブレットでGemini モバイルアプリを開きます、2. 左側のメニュー アイコン、プロフィール写真またはイニシャル、設定、Gemini とハンズフリーで話すをタップします、3. 「OK Google」を無効にします、と書かれている" loading="lazy"><figcaption>Androidは Geminiアプリの設定で「OK Google」を切る（Gemini アプリ ヘルプ、2026年10月13日取得）</figcaption></figure>

Gemini アプリ ヘルプはこの手順を、「OK Google」と聞こえたときにGeminiが起動しないようにする方法として載せています。マップに限った設定ではなく、**マップのナビでオフにしたときの動きはヘルプに書かれていません。**2025年10月にはベータ版のアプリを解析した[記事](https://tech.yahoo.com/ai/gemini/articles/google-maps-gemini-during-navigation-121143743.html)で、ナビの設定にGeminiの項目が加わる様子が報じられています（今の版にあるかは確かめていません）。ナビの設定にGeminiを起動するスイッチがあるという[コミュニティの投稿](https://support.google.com/maps/thread/420390834?hl=ja)もあります。nitoはその画面を確かめていないので、ここではGeminiアプリの側の手順を載せました。

### iPhoneの場合

iPhoneはマップの中の設定が入口です。同じヘルプのiPhoneのページには、ハンズフリーで使うときはナビゲーション設定の［「Ok Google」でアシスタントを利用する］をオンにする、とあります。**声で呼ぶ入口はこの項目です（オフにしたときの動きはヘルプに書かれていません）。**

<figure class="post-figure post-figure--sp"><img src="/media/images/google-maps-gemini/06_help_ios.jpg" alt="Google マップ ヘルプ「移動中に Gemini を使用する」のiPhoneのページ。赤い枠の1番に、重要: 現在のところ、CarPlay では Gemini をご利用いただけません、赤い枠の2番に、ヒント: ハンズフリーで操作するには、ナビゲーション設定で［「Ok Google」でアシスタントを利用する］をオンにします、と書かれている" loading="lazy"><figcaption>iPhoneはナビの設定の項目で「OK Google」を切り替える（Google マップ ヘルプ、2026年10月13日取得）</figcaption></figure>

nitoはこの項目をオフにしたあとの動きを試していません。同じページは**CarPlayでは今のところGeminiを使えない**とも書いています。車の画面で動くGeminiは「[Android AutoのGemini](/media/android-auto-gemini/)」の記事で扱っています。

## マップに相談はオフにできるか

使わないので検索バーの下のボタンごと消したい、という人もいるでしょう。ところが、Googleマップ ヘルプの「Google マップで質問する」にも、データの扱いを書いたページにも、**2026年10月13日の時点でマップに相談を切る設定やボタンを消す設定は書かれていません。**

<figure class="post-figure"><img src="/media/images/google-maps-gemini/07_fig_stop.png" alt="GoogleマップでGeminiを呼ぶ入口とヘルプの記載の表。ナビのGemini（Android）の声で呼ぶ入口はGeminiアプリの設定のGemini とハンズフリーで話すの「OK Google」。ナビのGemini（iPhone）の声で呼ぶ入口はマップのナビの設定の「Ok Google」でアシスタントを利用する。マップに相談は切る設定がヘルプに無く、押さなければ動かず、会話は履歴アイコンから会話ごとに削除。マップに相談で受け取った回答は保存され、位置情報を含む可能性がある。オフにしたときの動きはヘルプに書かれていない" loading="lazy"><figcaption>声で呼ぶ入口はナビの2つで、マップに相談を切る設定はヘルプに無い</figcaption></figure>

ボタンを消せない代わりに残る会話は選べます。ヘルプの手順はマップに相談を開いて履歴アイコンを押し、会話の横の削除アイコンで消す流れです。**消せるのは会話全体だけで、会話の一部だけを消すことはできません。**

<figure class="post-figure post-figure--sp"><img src="/media/images/google-maps-gemini/08_help_del.jpg" alt="Google マップ ヘルプ「Google マップで質問する」のチャット履歴から会話を削除するの手順。1. Google マップ アプリを開く、2. 検索バーの下にあるマップに相談をタップ、3. 履歴アイコンをタップ、赤い枠の1番に、4. 削除する会話の横にある削除アイコンをタップします、重要: 削除できるのは会話全体のみです。会話の一部だけを削除することはできません、と書かれている" loading="lazy"><figcaption>会話は履歴から会話ごとに消す（Google マップ ヘルプ、2026年10月13日取得）</figcaption></figure>

Gmailとのつなぎ込みは最初からオフです。Google Japan Blogは、マップに相談がGmailの予約情報を読む「パーソナル インテリジェンス」について、**Gmailとの連携はデフォルトでオフ**で、つなぐかどうかは自分で選べると書いています。

<figure class="post-figure post-figure--sp"><img src="/media/images/google-maps-gemini/09_help_blog.jpg" alt="Google Japan Blog「Google マップの新機能「マップに相談」を日本で提供開始」の段落。赤い枠の1番に、マップに相談のパーソナル インテリジェンスはすべてユーザーご自身で管理することができます、Gmail との連携はデフォルトでオフ（無効）になっており連携するかどうかはご自身で自由に選択いただけます、と書かれている。その下に、履歴設定がオンになっている場合、マップに相談は過去の会話を記憶し中断したところから再開できる、とある" loading="lazy"><figcaption>Gmailとの連携は最初から切れている（Google Japan Blog、2026年8月7日）</figcaption></figure>

同じブログによると、履歴の設定がオンならマップに相談は過去の会話を覚えて途中から再開できます。Googleマップ ヘルプの「[マップ履歴を管理する](https://support.google.com/maps/answer/3137804?hl=ja)」は、検索サービス履歴に残るものの1つとして「マップに相談」での過去の会話を挙げています。マップ履歴をオフにしたときに会話がどうなるかは、ヘルプに書かれていません。**ヘルプが条件を付けずに書いているのは、「マップに相談」の回答ではこれまでに受け取った回答が保存される、というところまでです。**

## 入力や位置情報は何に使われるか

マップのAI機能のデータの扱いは、Googleマップ ヘルプ「[Google マップの AI 搭載機能によるデータの使用方法](https://support.google.com/maps/answer/16833938?hl=ja)」にあります。**日本語版のヘルプにあるのは位置情報と個人向けの扱いで、英語版には会話の利用と人によるレビューの段落もあります。**日本語版で位置情報を使ったり保存したりすると書かれているのは、次の3つの機能です。

<figure class="post-figure post-figure--sp"><img src="/media/images/google-maps-gemini/10_help_data.jpg" alt="Google マップ ヘルプ「Google マップの AI 搭載機能によるデータの使用方法」のAI 搭載機能と位置情報の節。赤い枠の1番に、「マップに相談」の回答ではこれまでにユーザーが受け取った回答が保存されますがこれには位置情報が含まれる可能性があります、Google マップのレンズでは位置情報が保存される場合があります、ナビゲーションの Gemini では位置情報が保存される場合があります、と書かれている" loading="lazy"><figcaption>位置情報が保存されることがある機能は3つ（Google マップ ヘルプ、2026年10月13日取得）</figcaption></figure>

| 機能 | ヘルプの書き方 |
|---|---|
| マップに相談 | 受け取った回答が保存され、位置情報を含む可能性がある |
| Google マップのレンズ | 位置情報が保存される場合がある |
| ナビゲーションのGemini | 位置情報が保存される場合がある |

英語版の同じページ「[How AI-powered features use your data in Google Maps](https://support.google.com/maps/answer/16833938?hl=en)」は、製品の改善のためにGoogleがAI機能でのやり取りを使うことがあり、そこにチャットの履歴も含まれうると書いています。訓練を受けた人のレビュアーが見ることもあり、レビュアーが見るデータはアカウントから切り離される、という説明です。英語版は個人向けの回答にも「一部の地域」「国で提供されている場合」という条件を付けています。日本語版にはこれらの段落が無く、日本で同じ扱いかはヘルプからは分かりません。

答えを本人向けに変える仕組みは、日本語版にも同じ説明があり、［[パーソナライズされたおすすめ表示](https://www.google.com/search-personalization/)］がオンのとき、マップは次の情報をもとにAIの回答を変えます。

- 検索した内容やルート検索した場所（マップ履歴を保存している場合）
- マップに相談での過去の会話（マップ履歴を保存している場合）
- 保存済みのリストや場所に付けたラベル
- 場所に投稿したクチコミ・評価・写真
- 検索履歴のアクティビティ
- つないでいるGoogleのアプリの情報

**どれもアカウントの設定しだいで、マップ履歴とおすすめ表示を切れば回答に使われる材料が減ります。**ただしヘルプの冒頭には、Googleの検索サービスの設定を数か月かけて更新している途中だとあります。画面の項目がヘルプと合わないときは、これまでどおり［ウェブとアプリのアクティビティ］が履歴とおすすめ表示を管理する、というのがヘルプの説明です。

## 使えないときと出ないときの条件

反対に、使いたいのにGeminiのアイコンが出ない・声に反応しないこともあります。ヘルプとGemini アプリ ヘルプ「[Gemini モバイルアプリの利用要件](https://support.google.com/gemini/answer/14579026?hl=ja)」から、出ない理由になりうる条件を並べると次のとおりです。

| 条件 | 内容 |
|---|---|
| 年齢 | Geminiモバイルアプリは13歳以上が要件で、13歳未満は保護者の承認があれば使える |
| 仕事用・学校用のアカウント | 管理者がGeminiアプリの利用を許可している必要がある |
| Androidの仕事用プロファイル | Geminiモバイルアプリを使えない |
| ナビの状態 | ヘルプの手順はナビゲーション モードに入ってから話しかける前提 |
| 提供の順番 | マップに相談は数週間かけて順に届く |
| 車の画面 | CarPlayでは今のところGeminiを使えない |
| 声で呼ぶとき | Androidは「OK Google」とVoice Matchの両方がオン |

Googleマップのヘルプ コミュニティには、[Pixel 10 Proでナビ中のGeminiアイコンが消え、以前のアシスタントのマイクに戻った](https://support.google.com/maps/thread/420390834?hl=ja)という2026年3月の投稿があります。回答したプロダクト エキスパートは、端末のデジタル アシスタントの設定と、Geminiアプリの［Gemini とハンズフリーで話す］の「OK Google」を確かめるよう案内していました。**上で止め方として書いた設定は、裏返すと「使えない」ときの確認先にもなります。**

## よくある質問

### GoogleマップのGeminiはオフにできますか？
声で呼ぶ入口はナビ中のGeminiの2つです。Androidは Geminiアプリの［Gemini とハンズフリーで話す］の「OK Google」、iPhoneはマップのナビの設定の［「Ok Google」でアシスタントを利用する］です（オフにしたときの動きはヘルプに書かれていません）。2026年10月13日時点のヘルプに、マップに相談を切る設定はありません。

### Googleマップのマップに相談のボタンは消せますか？
ヘルプにボタンを消す手順はありません。押さなければ会話は始まらないため、使わないなら触らずにおくのがヘルプの範囲でできることです。過去の会話は履歴アイコンから会話ごとに消せます。

### GoogleマップのGeminiはいつから日本で使えますか？
ナビ中のGeminiは2025年11月5日の発表から、Geminiを使える国のAndroidとiOSへ順次届いています。お店や施設のページの質問は2026年2月13日、マップに相談は2026年8月7日に日本での提供が発表されました。

### GoogleマップのGeminiが使えないのはなぜですか？
Androidの仕事用プロファイル、管理者が許可していない仕事用のアカウント、ナビゲーション モードに入っていない、マップに相談がまだ届いていない、のどれかに当たっていないかを先に見てください。CarPlayでは今のところ使えません。

### iPhoneのGoogleマップでGeminiは使えますか？
使えます。ヘルプのiPhoneのページにも、ナビゲーション モードで「OK Google」と言うかGeminiアイコンを押す手順があります。マップに相談もiPhoneのGoogleマップで使える機能です。

### Googleマップのマップに相談の会話は保存されますか？
マップ履歴を保存している場合、マップに相談での過去の会話は検索サービス履歴に残ります。受け取った回答は保存され位置情報を含む可能性がある、とデータのヘルプは書いています。

### マップに相談はGmailを読みますか？
マップに相談のGmailとの連携は、最初はオフです。自分でつないだ場合に限り、フライトやホテルの予約情報を回答に使います。

### Googleアシスタントに戻せますか？
スマホのGoogleアシスタントは2026年9月4日から提供の終了が始まると報じられており、戻す方法はあてにできません。Androidでナビ中に声でGeminiを呼ぶ入口は、Geminiアプリの「OK Google」です。

## 出典

本文の手順と条件は2026年10月13日に取得した次の公式ページで確認しています。Googleマップの画面は端末で試していないため、項目の名前がアプリの版で違うことがあります。

- [Google マップで質問する](https://support.google.com/maps/answer/16842041?hl=ja)（Google マップ ヘルプ。マップに相談の始め方と会話の削除、パソコン版の WebGL）
- [移動中に Gemini を使用する](https://support.google.com/maps/answer/6041199?hl=ja)（Google マップ ヘルプ。ナビ中のGemini、iPhoneの「Ok Google」の設定、CarPlay）
- [Google マップの AI 搭載機能によるデータの使用方法](https://support.google.com/maps/answer/16833938?hl=ja)（Google マップ ヘルプ。位置情報とパーソナライズ）
- [How AI-powered features use your data in Google Maps](https://support.google.com/maps/answer/16833938?hl=en)（Google Maps Help、英語版。会話の利用と人によるレビュー）
- [マップ履歴を管理する](https://support.google.com/maps/answer/3137804?hl=ja)（Google マップ ヘルプ。検索サービス履歴に残るもの）
- [Android デバイスで Gemini アプリを管理、削除する](https://support.google.com/gemini/answer/16938321?hl=ja)（Gemini アプリ ヘルプ。「OK Google」をオフにする）
- [Gemini モバイルアプリの利用要件](https://support.google.com/gemini/answer/14579026?hl=ja)（Gemini アプリ ヘルプ。年齢・アカウント・端末）
- [Google マップの新機能「マップに相談」を日本で提供開始](https://blog.google/intl/ja-jp/products/connect-communicate/japanese-ask-maps/)（Google Japan Blog、2026年8月7日）
- [Google マップの新機能で、お出かけをもっとスムーズに](https://blog.google/intl/ja-jp/products/explore-get-answers/maps-gemini-tips/)（Google Japan Blog、2026年2月13日）
- [Google Maps launches Gemini features, including landmark navigation](https://blog.google/products-and-platforms/products/maps/gemini-navigation-features-landmark-lens/)（Google 公式ブログ、2025年11月5日）
- [Gemini in navigation is now available for walking and cycling in Google Maps](https://blog.google/products-and-platforms/products/maps/gemini-navigation-biking-walking/)（Google 公式ブログ、2026年1月29日）
- [「Googleアシスタント」モバイル版が終了へ 9月4日からアクセス削除開始、Geminiに一本化](https://www.itmedia.co.jp/mobile/articles/2608/06/news064.html)（ITmedia Mobile、2026年8月6日）
