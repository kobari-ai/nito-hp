---
title: 【2026年10月】GoogleメッセージのGeminiを消す方法｜ボタン・チャット削除・データの扱い
date: 2026-10-10
category: AI活用
description: AndroidのGoogleメッセージに出るGeminiを消す方法を公式ヘルプで解説。ボタンを非表示にする設定、チャットの削除で消える範囲、送った内容の扱い、出ない条件まで。
cover_tag: 使い方
cover_headline: GoogleメッセージのGeminiを消す
cover_sub: ボタンの非表示・チャットの削除・データの扱い
---

AndroidのGoogleメッセージに出るGeminiのボタンは、アプリの［メッセージの設定］にある［Gemini in Google メッセージ］から消せます。Googleのヘルプ「[Gemini in Google メッセージを使用する](https://support.google.com/android/answer/14599070?hl=ja)」が「無効にする」手順として案内しているのは、［Gemini ボタンを表示する］のスイッチをオフにする操作です。

ただしヘルプでは、ボタンの表示を切る手順と会話を削除する手順が別々に書かれていて、消す場所によって消える範囲も変わります。この記事は2026年10月10日に取得したGoogleのヘルプをもとに、ボタンの消し方、チャットの消し方、送った内容がどう扱われるかを順に整理します。

:::takeaways
- ボタンは**［プロフィール写真］から［メッセージの設定］の［Gemini in Google メッセージ］を開き、［Gemini ボタンを表示する］をオフ**にすると消える
- **ボタンをオフにする手順と会話の削除は別。**消すならGeminiとのチャットを開いて［会話を削除］を選ぶ
- メッセージで消すとGeminiアプリ アクティビティからも消えるが、**アクティビティ側で消してもメッセージのチャットは残る**
- **Geminiとのチャットはエンドツーエンドの暗号化の対象外**で、アクティビティの設定によっては人のレビュアーが読むことがある
- 仕事用・学校用・ファミリーリンクのアカウント、18歳未満、RCSチャットがオフのときはGeminiが出ない
:::

## GoogleメッセージにGeminiが出た理由

GoogleメッセージはPixelをはじめ多くのAndroidスマホに入っている標準のSMSアプリです。ITmediaの2024年10月1日の記事「[Google「メッセージ」アプリでGeminiと日本語で会話可能に](https://www.itmedia.co.jp/mobile/articles/2410/01/news097.html)」によると、この時期から日本語でGeminiと話せるようになり、使えるようになった端末にはGeminiからメッセージが届きました。一覧の右下にある新しい会話のボタンの上に、Geminiのアイコンが常に出るようになったとも書かれています。

**自分で設定しなくても、条件を満たした端末にはGeminiが届く**ので、「Geminiへようこそ」という見覚えのない会話が一覧に並んで戸惑う人が出ました。Googleのコミュニティにも、2024年12月にこのメッセージが消せないという質問が投稿されています。

<figure class="post-figure"><img src="/media/images/google-messages-gemini/01_help_requirements.jpg" alt="Googleのヘルプ、Gemini in Google メッセージを使用するの必要なものの節。Androidスマートフォン、対応言語の設定、最新バージョンのGoogleメッセージ、自分で管理している個人のGoogleアカウント、18歳以上、RCSチャットがオンの6つが並ぶ" loading="lazy"><figcaption>ヘルプの「必要なもの」</figcaption></figure>

ヘルプに書かれた条件は次の6つです。対応している国と地域の一覧には日本が、対応言語には日本語が入っています。

| 条件 | ヘルプの書き方 |
|---|---|
| 端末 | Android スマートフォン |
| 言語 | スマートフォンが対応言語に設定されていること |
| アプリ | 最新バージョンの Google メッセージ |
| アカウント | 自分で管理している個人の Google アカウント |
| 年齢 | 18 歳以上 |
| 通信 | RCS チャットがオン |

2024年のITmediaの記事にはRAMが6GB以上という条件がありますが、2026年10月10日のヘルプの「必要なもの」にRAMの項目はありません。提供は段階的に進むとヘルプに書かれているので、条件を満たしていても届く時期は端末ごとに違います。

## Geminiのボタンを消す手順

ヘルプの「Gemini in Google メッセージを無効にする」の手順はスマホの中だけで終わります。

1. [Googleメッセージ](https://play.google.com/store/apps/details?id=com.google.android.apps.messaging)を開く
2. 上部のプロフィール写真またはイニシャルを押し、［メッセージの設定］から［Gemini in Google メッセージ］を開く
3. ［Gemini ボタンを表示する］をオフにする

<figure class="post-figure post-figure--sp"><img src="/media/images/google-messages-gemini/02_help_off_sp.jpg" alt="スマホで開いたGoogleのヘルプのGemini in Google メッセージを無効にする手順。1の赤枠はプロフィール写真またはイニシャルからメッセージの設定、Gemini in Google メッセージをタップする手順、2の赤枠はGeminiボタンを表示するをオフにする手順" loading="lazy"><figcaption>ヘルプの無効にする手順（スマホで表示）。1で設定を開き、2をオフにする</figcaption></figure>

アプリの版によっては、［メッセージの設定］を開いたあと［全般］の下を下までたどると［Gemini in Messages］が出てきます。解説動画（WebPro Education）の画面ではこの並びで、オフにすると一覧の右下にあった星形のボタンが消えていました。別の解説動画（Datyell Close）では、オフにしたあとGeminiとのチャットが一覧からアーカイブに移っています（どちらも投稿者の端末の画面）。

**ヘルプで「無効にする」と呼んでいるのは、このボタンの表示のスイッチ1つです。**Geminiとの会話の中身や、Geminiアプリ アクティビティに残った記録は、この操作では消えません。過去の会話も消したい人は次の節の手順に進みます。

Geminiとの会話画面の右上のメニューにある［Geminiを非表示にする］から隠す方法も、ITmediaの記事に載っています。2024年の記事なので、今の画面で同じ名前の項目があるかは端末で確かめてください。

## Geminiとのチャットを消す手順

Geminiとの会話はGoogleメッセージの中のチャットとGeminiアプリ アクティビティの2か所に残るため、ヘルプも消し方を2つに分けて書いています。

<figure class="post-figure"><img src="/media/images/google-messages-gemini/03_fig_delete.png" alt="どこで消すと何が消えるかの表。ボタンの表示をオフにするのは削除ではない。メッセージで会話を削除するとメッセージのチャットとGeminiアプリ アクティビティの両方から消える。アクティビティで項目を削除するとアクティビティからは消えるがメッセージのチャットは残る" loading="lazy"><figcaption>操作ごとに消える範囲が違う</figcaption></figure>

Googleメッセージで消すときは、Geminiとのチャットを開き、上部のその他のアイコンから［会話を削除］を選んで画面の指示に進みます。**メッセージで消すと、チャットの内容がすべて消え、Geminiアプリ アクティビティからも消えます。**一部のやり取りだけを選んで消すことはできません。

<figure class="post-figure"><img src="/media/images/google-messages-gemini/04_help_delete.jpg" alt="Googleのヘルプのチャットを削除する節の画面。メッセージで消す場合とGemini アプリ アクティビティで消す場合の手順が上下に並ぶ" loading="lazy"><figcaption>ヘルプの削除の手順。上がメッセージ、下がアクティビティ</figcaption></figure>

特定の質問だけを消したいなら、[Geminiアプリ アクティビティ](https://myactivity.google.com/product/gemini)を開きます。Googleメッセージから送った項目には「Google メッセージ」のラベルが付いていて、横の削除のアイコンで1件ずつ消せます。ただしこちらで消しても、**Googleメッセージの中のチャットとAndroidのバックアップに残ったメッセージは消えません。**両方から消すなら、最後にメッセージ側で［会話を削除］を選ぶのが確実です。

別の端末にまだチャットが見えるときは、削除に使った端末がインターネットにつながっていて、RCSチャットがオンになっているかを確かめるよう、ヘルプは案内しています。アクティビティ全体の消し方や自動削除の期間の変え方は[Geminiの履歴の削除](/media/gemini-history-delete/)にまとめました。

## Geminiに送った内容の扱い

Geminiに送った内容は普段の友だちとのメッセージとは別のルールで扱われ、ヘルプのチャットを始める手順の冒頭にも注意が1行置かれています。

<figure class="post-figure"><img src="/media/images/google-messages-gemini/05_help_e2e.jpg" alt="Googleのヘルプのチャットを開始する手順の画面。手順の上の赤枠に、暗号化についての重要な注意がある" loading="lazy"><figcaption>チャットを始める手順の上の注意</figcaption></figure>

**Geminiとのチャットは、エンドツーエンドの暗号化の対象外です。**送った内容はGeminiアプリ アクティビティに記録され、Geminiアプリと同じ[プライバシー ハブ](https://support.google.com/gemini/answer/13594961?hl=ja)の決まりで扱われます。プライバシー ハブが対象のサービスとして挙げる中に「Gemini in Google メッセージ アプリ（一部の地域）」が入っています。

| 項目 | プライバシー ハブの説明 |
|---|---|
| 人のレビュー | ［アクティビティの保存］がオンだと、トレーニングを受けたレビュアーがチャットの一部を読むことがある |
| レビュー済みのチャット | アカウントから切り離して最長3年保存。アクティビティを消しても残る |
| アクティビティの保存がオフ | チャットは72時間アカウントに保持される |
| 自動削除 | 既定は18か月。3か月・36か月・自動削除なしに変えられる |
| 位置情報 | 正確な位置にはアクセスしない。IPアドレスやアカウントの自宅・職場の住所からおおよその場所を使う |

**レビュアーに見られたくない内容は、Geminiとのチャットに入れない**のが、プライバシー ハブの案内です。Geminiの学習に使わせたくなければ、Geminiアプリ アクティビティで［アクティビティの保存］をオフにします（フィードバックを送った場合を除く）。Geminiアプリには一時チャットもありますが、[Geminiのシークレットモード](/media/gemini-temporary-chat/)で書いたとおり、Googleメッセージからは使えないと英語版のヘルプにあります。

ヘルプで説明されているのはGeminiとのチャットに自分で書いた内容で、友だちとの会話の中身をGeminiに渡す設定や手順は、2026年10月10日のヘルプに見当たりませんでした。

## メッセージのAI機能はGeminiだけではない

Googleメッセージの周りには、名前の似たAIの機能が3つあります。止める場所がそれぞれ違うので、どれのことかを先に分けておきます。

<figure class="post-figure"><img src="/media/images/google-messages-gemini/07_fig_features.png" alt="メッセージまわりの3つのAI機能の表。Gemini in メッセージは内容がGoogleに送られ、メッセージの設定で止める。文章マジックはAICoreを積んだ端末なら端末の中で処理され、書き換えの候補は英語のみで、使わなければ動かない。Geminiアプリからの送信はGeminiアプリが送り、Geminiのアプリ連携で止める" loading="lazy"><figcaption>3つの機能の違い</figcaption></figure>

1つ目はこの記事で扱ってきたGemini in Google メッセージです。2つ目の[文章マジック](https://support.google.com/messages/answer/13632636?hl=ja)は、返信の候補を出したり下書きを書き換えたりする試験運用の機能です。下書きを書き換える候補はヘルプでは英語のみ・18歳以上・AICoreを積んだ端末に限られています。

<figure class="post-figure"><img src="/media/images/google-messages-gemini/06_help_magic.jpg" alt="Googleのヘルプの文章マジックの画面。データの取り扱いについてと会話のプライバシーの2つの見出しが並ぶ" loading="lazy"><figcaption>文章マジックのデータの扱い</figcaption></figure>

**AICoreを積んだ端末では、文章マジックはGemini Nanoで端末の中だけで処理され、メッセージはGoogleに送られません。**候補を作るときに直近の20件のメッセージを使う、とヘルプに書かれています。

3つ目はGeminiアプリに「〇〇さんにメッセージを送って」と頼むと、Googleメッセージを通じて送る機能です。これはGeminiアプリ側の機能で、プライバシー ハブによると通話とメッセージのログ、連絡先を使います。止めるのはGoogleメッセージの設定ではなく、Geminiアプリの［アプリ連携］の設定です。電源ボタンの長押しで勝手にGeminiが起動する話は[Geminiが勝手に起動する原因と止め方](/media/gemini-auto-launch/)にまとめました。

## Geminiが出ない・使えないとき

反対に「Geminiを使いたいのにボタンが出ない」場合は、ヘルプの条件のどれかが外れています。

<figure class="post-figure"><img src="/media/images/google-messages-gemini/09_fig_reasons.png" alt="Geminiが出ない主な条件の図。アカウントは仕事用・学校用・ファミリーリンク、年齢は18歳未満、RCSチャットはオフになっている、アプリと言語は古い版・対応外の言語、提供の順番は段階的なリリースでまだ届いていない" loading="lazy"><figcaption>Geminiが出ない主な条件</figcaption></figure>

ファミリーリンクで管理しているアカウントとGoogle Workspaceのアカウントでは、Gemini in Google メッセージを使えないというのがヘルプの説明です。ヘルプの条件は自分で管理している個人のアカウントなので、仕事のアカウントでは出ません。

RCSチャットがオフでも出ませんが、**Geminiを消すためだけにRCSチャットを切るのはおすすめしません。**Googleメッセージの[RCSのヘルプ](https://support.google.com/messages/answer/7189714?hl=ja)には、オンとオフを切り替えるとグループ チャットから外れると書かれています。

<figure class="post-figure"><img src="/media/images/google-messages-gemini/08_help_rcs.jpg" alt="Googleメッセージのヘルプ、RCSチャットをオンまたはオフにするの節。赤枠の中に、重要: RCS チャットのオンとオフを切り替えることはおすすめしません。切り替えると、グループ チャットから削除されます、とある" loading="lazy"><figcaption>RCSの切り替えについての注意</figcaption></figure>

ボタンを消したいだけなら、前の節の［Gemini ボタンを表示する］のスイッチで足ります。RCSは既読通知や入力中の表示など、Gemini以外の機能にも使われているので、切ると失うものが大きくなります。

## よくある質問

### GoogleメッセージのGeminiとは何ですか？

Googleメッセージのアプリの中でGeminiと話せる機能で、正式な名前はGemini in Google メッセージです。メッセージの下書き、アイデア出し、予定の相談などをチャットの形で頼めます。条件を満たした端末には自分で設定しなくてもGeminiとのチャットとボタンが届くので、見覚えのない会話が増えたように見えます。

### GoogleメッセージのGeminiは消せますか？

ボタンは消せます。［メッセージの設定］の［Gemini in Google メッセージ］で［Gemini ボタンを表示する］をオフにするだけです。Googleメッセージというアプリの中の機能なので、Gemini in Google メッセージだけをアンインストールする方法はヘルプにありません。

### Geminiへようこそのメッセージは消せますか？

消せます。そのチャットを開き、上部のその他のアイコンから［会話を削除］を選びます。ボタンも出したくなければ、先に［Gemini ボタンを表示する］をオフにしておきます。

### GoogleメッセージのGeminiの料金はかかりますか？

Gemini in Google メッセージの料金について、ヘルプに記載はありません。必要なものとして挙がっているのは個人のGoogleアカウントとRCSチャットで、RCSのヘルプではWi-Fiかモバイルデータでメッセージを送ると説明されています。

### メッセージのGeminiとの会話は暗号化されますか？

エンドツーエンドの暗号化はされません。ヘルプのチャットを始める手順の冒頭にそう書かれています。Geminiアプリ アクティビティの設定によっては、レビュアーがチャットの一部を読むこともあります。

### メッセージのGeminiは友だちとの会話を読みますか？

Gemini in Google メッセージについては、友だちとの会話をGeminiに渡す設定や手順はヘルプにありません。別の機能のGeminiアプリは、メッセージを送るときに端末のメッセージのログを使うとプライバシー ハブにあり、これはGeminiアプリの［アプリ連携］で止められます。返信の候補を出す文章マジックは直近の20件のメッセージを使いますが、AICoreを積んだ端末では端末の中だけで処理されます。

### メッセージにGeminiのボタンが出ないのはなぜですか？

仕事用・学校用・ファミリーリンクのアカウント、18歳未満、RCSチャットがオフ、アプリが古い、端末の言語が対応外のどれかです。提供は段階的なので、条件を満たしていてもまだ届いていない端末もあります。

### メッセージで消した会話はGeminiアプリに残りますか？

メッセージで［会話を削除］を選ぶと、Geminiアプリ アクティビティからも消えます。反対にアクティビティで項目を消しても、メッセージのチャットとAndroidのバックアップには残ります。

## 出典

- Android ヘルプ「[Gemini in Google メッセージを使用する](https://support.google.com/android/answer/14599070?hl=ja)」（2026年10月10日取得。英語版も参照）
- Gemini アプリ ヘルプ「[Gemini アプリのプライバシー ハブ](https://support.google.com/gemini/answer/13594961?hl=ja)」（同）
- Google メッセージ ヘルプ「[文章マジックでメッセージの下書きを作成する](https://support.google.com/messages/answer/13632636?hl=ja)」（同）
- Google メッセージ ヘルプ「[Google メッセージで RCS チャットをオンにする](https://support.google.com/messages/answer/7189714?hl=ja)」（同）
- ITmedia Mobile「[Google「メッセージ」アプリでGeminiと日本語で会話可能に](https://www.itmedia.co.jp/mobile/articles/2410/01/news097.html)」（2024年10月1日）
- 解説動画: WebPro Education「[GoogleメッセージからGeminiを削除する方法](https://www.youtube.com/watch?v=e3Jd5dDgpVs)」、Datyell Close「[Google メッセージで Gemini ボタンを削除/非表示にする](https://www.youtube.com/watch?v=dkvU5nLb4P4)」（英語。投稿者の端末の画面）
- ヘルプの画面は、2026年10月10日にパソコンとスマホのブラウザで撮影
