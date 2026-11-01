---
title: 【2026年10月】Chromeの「このページについてGoogleに質問する」を消す方法・flags以外の止め方
date: 2026-10-15
modified: 2026-11-01
category: AI活用
keyword: googleに質問する 消す
description: Chromeのアドレスバーに出る「このページについてGoogleに質問する」の止め方。広まったflagsの項目はChrome 155に無く、今使えるのは検索エンジンの変更とポリシー。AIモードのボタンとの違いも。
cover_tag: 設定
cover_headline: Chromeの「Googleに質問」を止める
cover_sub: flagsが無い今の止め方
---


Chromeのアドレスバーを押すと出る［このページについて Google に質問］（Googleに質問する）は、開いているページの内容をGoogleレンズで調べ、サイドパネルに答えを返す入口です。

設定画面にこの表示だけを消すスイッチは無く、止めるなら既定の検索エンジンをGoogle以外にするか、会社のパソコンなら管理者のポリシーを使います。2025年に広まった chrome://flags の手順は、今のChromeでは項目が出てきません。

:::takeaways
- 正体は**Googleレンズの入口**。続きの質問はAIモードに進む
- **flagsの「Omnibox contextual suggestions」はChrome 155に無い**。Chromiumのソースでは期限がChrome 150まで
- 入口ごと止める条件は**既定の検索エンジンをGoogle以外にすること**
- 会社のパソコンは管理者が**SearchContentSharingSettings（Chrome 144以降）**で止められる
- スマホの下に出る「質問する」は正体が確定しておらず、Googleアプリの画面という報道もある
:::

## Googleに質問するの正体

Chromeヘルプの「Google レンズ in Chrome を使用して検索する」は、アドレスバーから選ぶ手順の中でこの項目を案内しています。**ヒントには特定のページではアドレスバーに既定で表示されることがある、と書かれています。**頼んでいないのに出てくる1行は、不具合や設定の誤りでなくGoogleが用意した表示です。

<figure class="post-figure post-figure--sp"><img src="/media/images/chrome-ask-google-page/02_help_lens.jpg" alt="Chromeヘルプ「Google レンズ in Chrome を使用して検索する」のアドレスバーから検索するの節。赤い枠に、アドレスバーでこのページについて Google に質問を選択します、質問にタブやファイルを追加するには AI モードを選択します、とある。もう1つの赤い枠はヒントで、特定のページでアドレスバーにこのページについて Google に質問がデフォルトで表示されることがあります、と書かれている" loading="lazy"><figcaption>特定のページでは既定で表示される、とヘルプのヒントにある</figcaption></figure>

選ぶとレンズの答えがサイドパネルに出て、下の［もっと聞く］に入力するとAIモードに切り替わります。**レンズでページの内容を検索すると、ページのスクリーンショットとデータがGoogleに送られます。**ページと画像は一時的な保存を除いて保存せず、学習にも使わないとヘルプは説明しています。ただしページの中で選んだ部分はGoogle検索に送られ、検索の履歴としてマイアクティビティで管理する扱いです。書かれているのはレンズで検索したときの話なので、候補に表示されているだけで送られるとは読めません。表示だけの状態についての記載はありません。

## Chromeに増えた3つのAIの入口

いまのChromeにはAIを呼ぶ入口が見た目の違う形で3つあり、名前が似ているため別の入口の消し方を読んでしまいがちです。

| 入口 | 出る場所 | 中身 | 消し方 |
|---|---|---|---|
| ［このページについて Google に質問］ | アドレスバーの候補 | Googleレンズ（続きはAIモード） | この記事の方法 |
| ［AI モード］ | アドレスバーの右・新しいタブの検索ボックス | Google検索のAIモード | アドレスバーを右クリックして［AI モードを常に表示する］を外す |
| ［Gemini に相談］ | ブラウザの上部のボタン | Gemini in Chrome | 右クリックで［Gemini の固定を解除］ |

**レンズとAIモードはGoogle検索の機能、Gemini in ChromeはGeminiの機能**で、管理者向けのポリシーも別々です。ほかの入口の手順を試して表示が消えなくても、手順の誤りとは限りません。［Gemini に相談］は[Chromeの「Geminiに相談」を消す方法](/media/chrome-gemini-remove/)にまとめています。

## flagsで消す方法が使えなくなった

日本語で読める手順の多くは2025年8月から11月のもので、Qiitaやnoteの記事は chrome://flags で「Omnibox contextual suggestions」を［Disabled］にして再起動する手順です。2025年11月12日のChromeヘルプ コミュニティでは、Windowsの安定版で効かなかったという質問に、Chromeの仕様で削除できないとプロダクト エキスパートが答えています。

2026年10月15日に新しいプロファイルでMacのChrome 155.0.8059.40を開き、chrome://flags の検索欄に Omnibox contextual suggestions と入れた結果が次の画面です。

<figure class="post-figure"><img src="/media/images/chrome-ask-google-page/03_flags_nomatch.jpg" alt="Chrome 155.0.8059.40のchrome://flagsの画面。検索欄にOmnibox contextual suggestionsと入力してあり、使用可能のタブの下に赤い枠でNo matching experimentsと表示されている" loading="lazy"><figcaption>Chrome 155のflagsでは項目が見つからない（2026年10月15日）</figcaption></figure>

［利用不可］のタブまで含めても、637ある項目の中に omnibox-contextual-suggestions はありませんでした。**Chromiumのソースでは、この項目の期限（expiry_milestone）はChrome 150で、期限を過ぎたflagは画面に出ず、前に［Disabled］にした設定も使われなくなります。**Chrome 156のソースでも期限は150のままでした。

**2025年の記事の手順どおりに探して見つからないのは、手順の誤りでなく項目そのものが期限で消えたためです。**古い手順で時間を使う必要はなく、知恵袋の回答にある「項目が出ない場合は最新版に更新して」も当てはまりません。名前の近い「WebUI Omnibox Ask G About This Page」は残っていますが、選んだときの行き先を切り替える項目で、表示を消すものではありません。

## Googleに質問するを消す方法

Chrome 155の［AI イノベーション］［検索エンジン］［サイトの設定］を開いた範囲では、この項目だけを消すスイッチは見当たりませんでした。flagsが使えなくなった今、仕組みとして残る止め方は検索エンジンの変更とポリシーです。

**個人のパソコンなら、まず①の右クリックでAIモードのボタンを隠すのがおすすめです。**すぐ戻せる操作ですが、［このページについて Google に質問］自体は消えません。それでも表示が気になるなら②の検索エンジンの変更に進み、会社のパソコンなら管理者に③のポリシーを頼むのが向いています。

<figure class="post-figure"><img src="/media/images/chrome-ask-google-page/07_fig_choose_1101.png" alt="Googleに質問するの止め方の順番の図。表示されるだけで困っていないなら設定は変えない。個人のパソコンはまずアドレスバーの右クリックでAIモードのボタンを隠すが、Googleに質問するは残る。それでも表示が気になるなら既定の検索エンジンをGoogle以外にし、アドレスバーの検索先も変わる。会社のパソコンは管理者にSearchContentSharingSettingsを1にしてもらう" loading="lazy"></figure>

### ① AIモードのボタンを隠す

Chromeヘルプの「Chrome で AI モードを使用する」によると、**アドレスバーを右クリックして［AI モードを常に表示する］の選択を外すと、［AI モード］と［タブなどを追加］が非表示になります。**隠れると書かれているのはその2つだけで、［このページについて Google に質問］も消えるという記載はありません。アドレスバーまわりのボタンが減れば十分という人向けの方法で、同じメニューで選び直せば戻ります。

### ② 既定の検索エンジンを変える

レンズのヘルプは使う前提として「Google を既定の検索エンジンとして設定します」と書いています。管理者向けのポリシーの説明はもっとはっきりしていて、**Google検索が既定の検索エンジンでない場合、ページの内容をAIモードやレンズと共有する機能は無効になる**とあります。

1. Chromeの右上の︙（その他）から［設定］を開く
2. 左のメニューの［検索エンジン］を選ぶ
3. 検索エンジンの欄の［変更］を押し、Google以外を選ぶ

<figure class="post-figure"><img src="/media/images/chrome-ask-google-page/04_set_search.jpg" alt="Chromeの設定の検索エンジンの画面。検索エンジンの欄にGoogleと表示され、右端の変更ボタンが赤い枠と番号1で示されている" loading="lazy"><figcaption>［設定］の［検索エンジン］で［変更］を押す</figcaption></figure>

**仕組みの上で入口ごと止まる個人向けの方法はこれだけで、代わりにアドレスバーの検索先が変わり、AIモードのボタンも使えなくなるのが代償です。**アドレスバーからGoogle検索することが多い人には向きません。画面から項目が消えるところまでは試していません。ただしChromiumのソースでも、この項目はレンズが使えるときだけ出る作りで、レンズはGoogleが既定の検索エンジンでないと有効になりません。

### ③ ポリシーで止める

会社のパソコンなら、管理者がChromeのポリシーで止められます。Chrome Enterpriseのポリシー一覧で、この入口にかかわるのは次の4つです。

| ポリシー | 止める対象 | 止める値 | 対応する版 |
|---|---|---|---|
| SearchContentSharingSettings | ページやファイルの内容をAIモードとレンズに渡す入口とサイドパネル | 1 | Chrome 144以降 |
| AIModeSettings | アドレスバーと新しいタブの検索ボックスのAIモード | 1 | Chrome 138以降 |
| GenAiDefaultSettings | 個別に決めていない生成AIの機能の既定 | 2 | Chrome 130以降 |
| LensOverlaySettings | レンズのオーバーレイ | 1 | Chrome 147から非推奨 |

**SearchContentSharingSettingsを1にすると、ページの内容を共有する入口とサイドパネルは無効になるか、非表示になります。**AIModeSettingsとは別に動き、Gemini in Chromeには影響しません。GenAiDefaultSettingsは生成AIの機能をまとめて止めるため、この表示だけが目的ならSearchContentSharingSettingsのほうが影響の小さい選び方です。

自分のパソコンにも入れられ、Windowsはレジストリの Software\Policies\Google\Chrome に SearchContentSharingSettings をREG_DWORDの1で作ります。Macは構成プロファイルで同じ名前の設定に1を入れ、chrome://policy で効いているかを確かめられます。**ただし設定画面に「お使いのブラウザは組織によって管理されています」と出続けるので、それが気にならない人向けです。**この方法も手元では試していません。

## スマホで下に出てくる質問するの消し方

スマホの画面の下に出る［質問する］は、Chromeのヘルプに説明が無く、正体を一次情報で確かめられていません。報道と相談から考えられる候補は次の3つで、どれもテスト中と報じられた機能か個人の相談です。

- **Googleアプリで検索結果から開いたページ**：開いたページに「Ask」のボタンを加えるテストをしていると報じられた（Android Authority、2026年5月。Android）
- **AndroidのChromeの下のバー**：アドレスバーを下に移した人にGeminiのボタンを出すテストをしていると報じられた（Android Headlines、2026年7月）
- **Chromeの下のツールバー**：一番下に［質問する］［新しいタブ］［すべてのタブ］が並ぶようになったという相談（知恵袋、2026年9月）

知恵袋の［質問する］［新しいタブ］［すべてのタブ］の並びは、海外で報じられたiPhone版の新しいツールバーと同じです。iPhoneのChromeで chrome://flags の ChromeNextIa を［Disabled］にすると元のツールバーに戻る、とPiunikaWebが報じています。この項目はChromiumのソースにもあります。nitoでは試しておらず、flagsは予告なく消えることがあります。

**どのアプリの画面かを先に確かめるのが近道です。**ChromeはiPhoneでもAndroidでもアドレスバーを画面の下に移せるため、アドレスバーの位置では見分けられません。ホーム画面のChromeとGoogleアプリのどちらから開いたかを見ます。Googleアプリの画面なら、Chromeの設定とは別の話です。

Chromeの画面でも、ヘルプに表示を切る手順はありません。5月の知恵袋のベストアンサーが挙げたAndroidのflagsも、ソースではパソコン版と同じ項目・同じ期限です（Androidの画面では確かめていません）。会社が管理するスマホでも、どのポリシーが効くかはボタンの正体しだいです。GeminiのボタンならGeminiSettings、AIモードならAIModeSettingsが対象で、SearchContentSharingSettingsはGeminiを止めません。

## まとめ

- **表示されるだけで困っていない場合**：設定は変えなくてよい。選ばなければレンズは起動しない
- **個人のパソコンで消したい場合**：既定の検索エンジンをGoogle以外にする。AIモードのボタンを隠すだけでは［このページについて Google に質問］は残る
- **Google検索を既定のまま使いたい場合**：設定画面では消せない。自分でポリシーを入れれば止まるが、「組織によって管理されています」と出続ける
- **会社のパソコンの場合**：管理者にSearchContentSharingSettingsを1にしてもらう
- **スマホの場合**：先にChromeの画面かGoogleアプリの画面かを確かめる

## よくある質問

### ChromeのGoogleに質問するは非表示にできますか？
設定画面に、この表示だけを消すスイッチはありません。入口ごと止めるなら、既定の検索エンジンをGoogle以外にするか、管理者のポリシー（SearchContentSharingSettings）を使います。

### Chromeのflagsで消す方法は今も使えますか？
2026年10月15日にMacのChrome 155で確かめたところ、項目がありませんでした。Chromiumのソースでは期限がChrome 150で、期限を過ぎたflagは画面に出ません。

### ChromeのGoogleに質問するでページは送られますか？
レンズでページの内容を検索すると、ページのスクリーンショットとデータがGoogleに送られるとヘルプにあります。一時的な保存を除いて保存されず、学習にも使われないという説明です。ページの中で選んだ部分はGoogle検索に送られ、マイアクティビティで管理・削除できます。

### Googleに質問するとGeminiに相談は同じですか？
別の機能です。前者はGoogleレンズで、続きの質問はAIモードに進みます。後者はGemini in Chromeで、右クリックの［Gemini の固定を解除］でボタンを消せます。

### ChromeのAIモードのボタンは消せますか？
アドレスバーを右クリックして［AI モードを常に表示する］を外すと、［AI モード］と［タブなどを追加］が隠れます。［このページについて Google に質問］はこの操作の対象外です。

### 検索エンジンを変えてもGoogle検索できますか？
google.com を開けば今までどおり検索できます。変わるのはアドレスバーに打った言葉の検索先と、Googleが既定であることを前提にしたレンズやAIモードの入口です。

### Chromeで質問するの項目が出ないことはありますか？
あります。管理者がポリシーで止めている場合と、既定の検索エンジンがGoogle以外の場合です。chrome://policy で、SearchContentSharingSettingsやGenAiDefaultSettingsが入っているかを確かめられます。

### iPhoneのChromeで下に出る質問するは消せますか？
Chromeのヘルプに、画面の下の［質問する］を切る手順は見当たりません。Googleアプリの画面のこともあるので、先にどのアプリかを確かめます。会社が管理するiPhoneなら、GeminiのボタンはGeminiSettings、AIモードのボタンはAIModeSettingsが管理者向けのポリシーです。

## 出典

ヘルプとポリシーの記述、Chromiumのソースは2026年11月1日に取り直して確認しています（ポリシーは一覧の元データのChromiumのソースで照合）。flagsと設定画面は2026年10月15日にMacのChrome 155.0.8059.40で開いて確かめました。

- [Google レンズ in Chrome を使用して検索する](https://support.google.com/chrome/answer/15086890?hl=ja)（Chrome ヘルプ。アドレスバーの［このページについて Google に質問］とページのデータの処理）
- [Search with Google Lens in Chrome](https://support.google.com/chrome/answer/15086890?hl=en&co=GENIE.Platform%3DiOS)（Chrome Help、英語版。iPhoneの手順）
- [Chrome で AI モードを使用する](https://support.google.com/chrome/answer/16704170?hl=ja)（Chrome ヘルプ。AIモードのボタンの隠し方）
- [Chrome で AI モードを使用する（Android）](https://support.google.com/chrome/answer/16704170?hl=ja&co=GENIE.Platform%3DAndroid)・[同（iPhone・iPad）](https://support.google.com/chrome/answer/16704170?hl=ja&co=GENIE.Platform%3DiOS)（Chrome ヘルプ。［現在のタブを追加］の手順）
- [SearchContentSharingSettings](https://chromeenterprise.google/policies/#SearchContentSharingSettings)・[AIModeSettings](https://chromeenterprise.google/policies/#AIModeSettings)・[GenAiDefaultSettings](https://chromeenterprise.google/policies/#GenAiDefaultSettings)・[LensOverlaySettings](https://chromeenterprise.google/policies/#LensOverlaySettings)・[GeminiSettings](https://chromeenterprise.google/policies/#GeminiSettings)（Chrome Enterprise のポリシー一覧）
- [flag-metadata.json](https://chromium.googlesource.com/chromium/src/+/refs/tags/156.0.8078.80/chrome/browser/flag-metadata.json)・[flag_expiry.md](https://chromium.googlesource.com/chromium/src/+/refs/tags/156.0.8078.80/docs/flag_expiry.md)・[about_flags.cc](https://chromium.googlesource.com/chromium/src/+/refs/tags/156.0.8078.80/chrome/browser/about_flags.cc)（Chromium のソース、タグ 156.0.8078.80。flagsの期限と、期限切れのflagを一覧と設定から外す処理）
- [『Googleで調べる』『このページについてGoogleに質問する』を消す方法](https://support.google.com/chrome/thread/387019511?hl=ja)（Chrome ヘルプ コミュニティ、2025年11月12日。2026年10月15日に取得）
- [【Chrome】『このページについてGoogleに質問する』を削除する](https://qiita.com/rana_kualu/items/83d1272a2f92422f9304)（Qiita、2025年8月24日）
- [「このページについてGoogleに質問する」消す方法（無効化・削除）](https://note.com/gamecentergx/n/n552415151d7c)（note、2025年11月19日）
- [Chrome で「このページについて Google に質問する」表示](https://www.724685.com/blog/2025/09/01111545.html)（なにしろパソコン、2025年9月1日）
- [下に出てくる「質問する」という表示を消したいです](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q13328211688)（Yahoo!知恵袋、2026年5月19日）
- [Chromeを開いたら、急に1番下に、質問する、新しいタブ、すべてのタブと表示される様になった](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q13331282393)（Yahoo!知恵袋、2026年9月11日）
- [Google Search on Android now lets you ask AI about any link you open](https://www.androidauthority.com/google-app-android-ai-ask-questions-3668753/)（Android Authority、2026年5月19日。報道）
- [Google Chrome Android redesign Gemini AI button](https://www.androidheadlines.com/2026/07/google-chrome-android-redesign-gemini-ai-button.html)（Android Headlines、2026年7月14日。報道）
- [Chrome is testing a new bottom bar on iOS, and here's how to turn it off](https://piunikaweb.com/2026/07/01/chrome-ios-new-bottom-bar-disable/)・[Here's how to bring back Chrome's old bottom bar on iOS](https://piunikaweb.com/2026/09/14/get-rid-of-chrome-new-bottom-bar-ios/)（PiunikaWeb、2026年7月1日・9月14日。報道）
- [「ChromeのAI機能」すら消える。ブラウザのお節介な通知とAIを一掃してみた](https://www.lifehacker.jp/article/2601script-removes-ai-features-from-chrome-edge-firefox/)（ライフハッカー・ジャパン、2026年1月29日。2026年10月15日に取得）
