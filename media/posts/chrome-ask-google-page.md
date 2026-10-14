---
title: 【2026年10月】Chromeの「このページについてGoogleに質問する」を消す方法・flags以外の止め方
date: 2026-10-15
category: AI活用
description: Chromeのアドレスバーに出る「このページについてGoogleに質問する」の止め方。広まったflagsの項目はChrome 155に無く、今使えるのは検索エンジンの変更とポリシー。AIモードのボタンとの違いも。
cover_tag: 設定
cover_headline: Chromeの「Googleに質問」を止める
cover_sub: flagsが無い今の止め方
---

Chromeのアドレスバーを押すと、候補の一番上に［このページについて Google に質問］が出ることがあります。正体はGoogleレンズで、選ぶと開いているページの内容をもとにサイドパネルで答えが返ってきます。

2025年の夏から秋にかけて、消し方として chrome://flags の「Omnibox contextual suggestions」を無効にする手順が広まりました。ところが2026年10月15日にMacのChrome 155.0.8059.40でflagsを検索すると、この項目は見つかりません。

この記事はChromeのヘルプと管理者向けのChrome Enterpriseのポリシーの説明をもとに、**今のChromeで使える止め方を止まる範囲ごとに**並べます。flagsと設定画面は実際に開いて確かめましたが、検索エンジンの変更とポリシーで表示が消えるところまでは試していません。

:::takeaways
- 正体は**Googleレンズの入口**。選ぶとページのスクリーンショットとデータがGoogleに送られ、続きの質問はAIモードに進む
- 2025年に広まった**flagsの「Omnibox contextual suggestions」はChrome 155には無い**（2026年10月15日にMacで確認）
- Chromeの設定画面には、この表示だけを消すスイッチが見当たらない
- 入口ごと止める条件は**既定の検索エンジンをGoogle以外にすること**。ヘルプとポリシーの説明は、Googleが既定であることを前提にしている
- 会社のパソコンは管理者が**SearchContentSharingSettings（Chrome 144以降）**で止められる。AIモードのボタンは右クリックで隠せる
:::

## このページについてGoogleに質問するの正体

アドレスバーの候補に見慣れない1行が増えたなら、それがこの項目です。Chromeヘルプの「[Google レンズ in Chrome を使用して検索する](https://support.google.com/chrome/answer/15086890?hl=ja)」は、アドレスバーから選ぶ手順の中でこの項目を案内しています。**ヒントには特定のページではアドレスバーに既定で表示されることがある、と書かれています。**頼んでいないのに出てくるのはこのためです。

<figure class="post-figure post-figure--sp"><img src="/media/images/chrome-ask-google-page/02_help_lens.jpg" alt="Chromeヘルプ「Google レンズ in Chrome を使用して検索する」のアドレスバーから検索するの節。赤い枠に、アドレスバーでこのページについて Google に質問を選択します、質問にタブやファイルを追加するには AI モードを選択します、とある。もう1つの赤い枠はヒントで、特定のページでアドレスバーにこのページについて Google に質問がデフォルトで表示されることがあります、と書かれている" loading="lazy"><figcaption>アドレスバーの項目はGoogleレンズの入口（Chromeヘルプ）</figcaption></figure>

選ぶとGoogleレンズがページの内容をもとに答えを返し、結果はサイドパネルに出ます。続けて聞きたいことはサイドパネルの下の［もっと聞く］に入力し、そこからAIモードに切り替わります。サイドパネルを閉じるのは Esc キーか閉じるボタンです。

ページのデータの扱いも同じヘルプにあります。**レンズでページの内容を検索すると、ページのスクリーンショットとデータがGoogleに送られます。**処理のための一時的な保存を除いてGoogleはデータを保存せず、ページも画像も学習には使わない、とヘルプは説明しています。ここで書かれているのはレンズを使ったときの話で、項目が候補に表示されているだけの状態については記載がありません。

## Chromeに増えた3つのAIの入口

いまのChromeにはAIを呼ぶ入口が見た目の違う形で3つあります。名前が似ているので、止め方を探す前に、どれの話かを表で分けました。

<figure class="post-figure"><img src="/media/images/chrome-ask-google-page/01_fig_overview.png" alt="ChromeのAIの入口を描いたイラスト（実際の画面ではない）。ブラウザのアドレスバーの下に候補の一覧が開き、周りにGoogleレンズ、AIモード、Geminiの3つの吹き出しが並んでいる" loading="lazy"><figcaption>アドレスバーまわりにはレンズ・AIモード・Geminiの入口がある（イラスト）</figcaption></figure>

| 入口 | 出る場所 | 中身 | 消し方 |
|---|---|---|---|
| ［このページについて Google に質問］ | アドレスバーの候補 | Googleレンズ（続きはAIモード） | この記事の方法 |
| ［AI モード］ | アドレスバーの右・新しいタブの検索ボックス | Google検索のAIモード | アドレスバーを右クリックして［AI モードを常に表示する］を外す |
| ［Gemini に相談］ | ブラウザの上部のボタン | Gemini in Chrome | 右クリックで［Gemini の固定を解除］ |

［Gemini に相談］は別の仕組みで、消し方は[Chromeの「Geminiに相談」を消す方法](/media/chrome-gemini-remove/)にまとめています。**レンズとAIモードはGoogle検索の機能、Gemini in ChromeはGeminiの機能**で、管理者向けのポリシーも別々に用意されています。

## flagsで消す方法が使えなくなった

日本語で読める手順の多くは、2025年8月から11月に書かれたものです。[Qiitaの記事](https://qiita.com/rana_kualu/items/83d1272a2f92422f9304)（2025年8月24日）と[noteの記事](https://note.com/gamecentergx/n/n552415151d7c)（2025年11月19日）は、chrome://flags で「Omnibox contextual suggestions」を探して［Disabled］にし、再起動する手順です。[なにしろパソコン](https://www.724685.com/blog/2025/09/01111545.html)も2025年9月1日に同じ方法で消えたことを確かめたうえで、flagsの設定はいつ使えなくなるか分からないと書いていました。

その心配は当たりました。2025年11月12日に[Chromeヘルプ コミュニティ](https://support.google.com/chrome/thread/387019511?hl=ja)へ投稿された質問では、Windowsの安定版で「Omnibox contextual suggestions」も「Omnibox contextual search on focus suggestions」も効かなかったと報告されています。回答したプロダクト エキスパートは、Chromeの仕様で削除できないと答えました。

2026年10月15日に新しいプロファイルでMacのChrome 155.0.8059.40を開き、chrome://flags の検索欄に Omnibox contextual suggestions と入れた結果が次の画面です。

<figure class="post-figure"><img src="/media/images/chrome-ask-google-page/03_flags_nomatch.jpg" alt="Chrome 155.0.8059.40のchrome://flagsの画面。検索欄にOmnibox contextual suggestionsと入力してあり、使用可能のタブの下に赤い枠でNo matching experimentsと表示されている" loading="lazy"><figcaption>Chrome 155のflagsでは項目が見つからない（2026年10月15日）</figcaption></figure>

**ほかのOS向けの項目が並ぶ［利用不可］のタブまで含めても、637ある項目の中に omnibox-contextual-suggestions はありませんでした。**flagsは試験運用の機能なので、予告なく消えることがあります。

名前の近い「WebUI Omnibox Ask G About This Page」という項目は残っています。この項目を選んだときの行き先を別の画面に切り替えるという説明で、表示を消すものではありません。説明を読んでも意味が分からないflagsは、触らずにおくほうが安全です。

## 今のChromeで止める4つの方法

設定画面も確かめました。Chrome 155の［AI イノベーション］［検索エンジン］［サイトの設定］を開いた範囲では、この項目だけを消すスイッチは見当たりません。海外の解説には［サイトの設定］の「ページのコンテンツ」をオフにする方法を挙げるものがありますが、パソコン版の［サイトの設定］の一覧にその名前はありませんでした。

そのため止め方は、何を止めたいかで選ぶことになります。

<figure class="post-figure"><img src="/media/images/chrome-ask-google-page/07_fig_choose.png" alt="このページについてGoogleに質問するの止め方を4つに分けた図。表示が出るだけで困っていないなら設定は変えない。AIモードのボタンも気になるならアドレスバーの右クリックでAIモードを常に表示するを外す。自分のパソコンで入口ごと止めたいなら既定の検索エンジンをGoogle以外にする。会社のパソコンをまとめて止めたいなら管理者がSearchContentSharingSettingsを1にする。アドレスバーのAIモードはAIModeSettings" loading="lazy"></figure>

### ① 既定の検索エンジンを変える

レンズのヘルプは、使う前提として「Google を既定の検索エンジンとして設定します」と最初に書いています。管理者向けのポリシーの説明はもっとはっきりしていて、**Google検索が既定の検索エンジンでない場合、この機能は無効になる**と書かれていました。

1. Chromeの右上の︙（その他）から［設定］を開く
2. 左のメニューの［検索エンジン］を選ぶ
3. 検索エンジンの欄の［変更］を押し、Google以外を選ぶ

<figure class="post-figure"><img src="/media/images/chrome-ask-google-page/04_set_search.jpg" alt="Chromeの設定の検索エンジンの画面。検索エンジンの欄にGoogleと表示され、右端の変更ボタンが赤い枠と番号1で示されている" loading="lazy"><figcaption>［設定］の［検索エンジン］で［変更］を押す</figcaption></figure>

代わりに、アドレスバーに打った言葉の検索先はGoogle以外の検索エンジンになります。Googleで調べたいときは、google.com を開けば今までどおりです。**アドレスバーのAIモードもGoogleが既定であることが条件**なので、こちらも一緒に使えなくなります。

画面から項目が消えるところまでは試していません。ヘルプとポリシーの説明から言えるのは、Googleが既定でなければこの機能が動かない、というところまでです。

### ② ポリシーで止める

会社のパソコンなら、管理者がChromeのポリシーで止められます。[Chrome Enterpriseのポリシー一覧](https://chromeenterprise.google/policies/#SearchContentSharingSettings)で、この入口にかかわるのは次の4つです。

| ポリシー | 止める対象 | 止める値 | 対応する版 |
|---|---|---|---|
| SearchContentSharingSettings | ページやファイルの内容をAIモードとレンズに渡す入口とサイドパネル | 1 | Chrome 144以降 |
| AIModeSettings | アドレスバーと新しいタブの検索ボックスのAIモード | 1 | Chrome 138以降 |
| GenAiDefaultSettings | 個別に決めていない生成AIの機能（Gemini in Chrome・レンズ・AIモード）の既定 | 2 | Chrome 130以降 |
| LensOverlaySettings | レンズのオーバーレイ | 1 | Chrome 147から非推奨 |

<figure class="post-figure post-figure--sp"><img src="/media/images/chrome-ask-google-page/05_policy_scs.jpg" alt="Chrome Enterpriseのポリシー一覧のSearchContentSharingSettingsの説明。赤い枠の1つ目に、1 = ユーザーはページやファイルのコンテンツを Google AI Mode と共有できません、コンテキストを共有するためのエントリ ポイントとサイドパネルは無効になるか非表示になります、とある。2つ目の赤い枠に、Google Search がユーザーのデフォルトの検索エンジンでない場合この機能は無効になっているため、このポリシーは無視されます、とある" loading="lazy"><figcaption>SearchContentSharingSettingsの説明（Chrome Enterprise）</figcaption></figure>

**SearchContentSharingSettingsを1にすると、ページの内容を共有する入口とサイドパネルは無効になるか、非表示になります。**ページの内容について質問する機能は、もともとLensOverlaySettingsの説明に含まれていました。そのLensOverlaySettingsはChrome 147から非推奨になり、代わりにSearchContentSharingSettingsを使うよう案内されています。AIModeSettingsとは別に動き、Gemini in Chromeには影響しないことも説明にありました。

自分のパソコンにも同じ設定は入れられます。Windowsはレジストリの Software\Policies\Google\Chrome に SearchContentSharingSettings をREG_DWORDの1で作り、Macは構成プロファイルで同じ名前の設定に1を入れます。[ライフハッカーが2026年1月に紹介した](https://www.lifehacker.jp/article/2601script-removes-ai-features-from-chrome-edge-firefox/)オープンソースのスクリプト「JustTheBrowser」も、このポリシーの仕組みを使ってブラウザのAI機能をまとめて止めるものです。

入れたあとは chrome://policy を開くと、効いているポリシーを一覧で確かめられます。ポリシーが入ったChromeは、設定画面に「お使いのブラウザは組織によって管理されています」と出るようになります。この方法も手元では試していません。

### ③ AIモードのボタンだけ隠す

アドレスバーの右にあるAIモードのボタンは、右クリックで隠せます。Chromeヘルプの「[Chrome で AI モードを使用する](https://support.google.com/chrome/answer/16704170?hl=ja)」には、**アドレスバーを右クリックして［AI モードを常に表示する］の選択を外すと、［AI モード］と［タブなどを追加］が非表示になる**とあります。

<figure class="post-figure post-figure--sp"><img src="/media/images/chrome-ask-google-page/06_help_aimode.jpg" alt="Chromeヘルプ「Chrome で AI モードを使用する」のアドレスバーから操作する場合の節。手順のあとのヒントに赤い枠があり、アドレスバーの AI モードとタブなどを追加を非表示にするには、アドレスバーを右クリックして AI モードを常に表示するの選択を解除します、と書かれている" loading="lazy"><figcaption>AIモードのボタンは右クリックで隠せる（Chromeヘルプ）</figcaption></figure>

ヘルプがこの操作で隠れると書いているのは、［AI モード］と［タブなどを追加］の2つです。［このページについて Google に質問］も一緒に消えるという記載はありません。

### ④ 選ばずに使い続ける

表示が出るだけで困っていないなら、設定を変えない手もあります。項目は候補の1行で、選ばなければレンズは起動しません。ヘルプがページのデータの送信を書いているのは、レンズでページを検索したときです。

## AndroidとiPhoneのChrome

スマホのChromeにも、開いているページについてAIに聞く入口があります。Androidのヘルプ「Chrome で AI モードを使用する」は、アドレスバーの［AI モード］から質問し、メニューの［現在のタブを追加］で開いているタブについて聞く手順を案内しています。iPhone版の[レンズのヘルプ](https://support.google.com/chrome/answer/15086890?hl=en&co=GENIE.Platform%3DiOS)（英語版）は、アドレスバーの左のGoogleレンズのアイコンからページを検索する手順です。

2026年5月19日の[Yahoo!知恵袋の質問](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q13328211688)には、Chromeの画面の下に「質問する」という表示が出るので消したい、という相談があります。回答はflagsのOmnibox contextual suggestionsを無効にする方法を挙げていましたが、**Mac版のChrome 155で見たflagsの一覧には、ほかのOS向けを含めてこの項目がありません。**Androidのヘルプにも、この表示を切る手順は見当たりませんでした。スマホの画面では試していないため、Android版で項目の名前が違う可能性は残ります。

会社が管理するスマホなら、SearchContentSharingSettingsはAndroidとiPhoneのChrome 144以降にも対応しています。

## AI検索での見え方は別の話

Chromeの入口を止めても、AIモードやGeminiが答えの中で自社をどう紹介するかは変わりません。そちらは[AI検索対策](https://nito-0210.com/llmo/)として扱います。

## よくある質問

### ChromeのGoogleに質問するの表示は消せますか？
設定画面に、この表示だけを消すスイッチは見当たりません。入口ごと止めるなら、既定の検索エンジンをGoogle以外にするか、管理者のポリシー（SearchContentSharingSettings）を使います。

### Chromeのflagsで消す方法は今も使えますか？
2026年10月15日にMacのChrome 155で確かめたところ、Omnibox contextual suggestionsの項目はありませんでした。項目があっても効かなかったという報告も、2025年11月にChromeヘルプ コミュニティに出ていました。

### ChromeのGoogleに質問するでページは送られますか？
レンズでページの内容を検索すると、ページのスクリーンショットとデータがGoogleに送られるとヘルプにあります。処理のための一時的な保存を除いて保存されず、学習にも使われないと書かれています。

### Googleに質問するとGeminiに相談は同じですか？
別の機能です。前者はGoogleレンズで、続きの質問はAIモードに進みます。後者はGemini in Chromeで、右クリックの［Gemini の固定を解除］でボタンを消せます。

### ChromeのAIモードのボタンは消せますか？
アドレスバーを右クリックして［AI モードを常に表示する］を外すと、［AI モード］と［タブなどを追加］が隠れる、というのがヘルプの説明です。

### 検索エンジンを変えてもGoogle検索できますか？
google.com を開けば今までどおり検索できます。変わるのはアドレスバーに打った言葉の検索先と、Googleが既定であることを前提にしたレンズやAIモードの入口です。

### Chromeで質問するの項目が出ないことはありますか？
あります。管理者がポリシーで止めている場合と、既定の検索エンジンがGoogle以外になっている場合です。chrome://policy を開くと、SearchContentSharingSettingsやGenAiDefaultSettingsが入っているかを確かめられます。

### スマホのChromeでもGoogleに質問するを消せますか？
Androidのヘルプに、表示を切る手順は見当たりません。会社が管理するAndroidとiPhoneなら、SearchContentSharingSettings（Chrome 144以降）で止められます。

## 出典

本文の手順と条件は2026年10月15日に取得した次のページで確認しています。flagsと設定画面はMacのChrome 155.0.8059.40で開いて確かめました。

- [Google レンズ in Chrome を使用して検索する](https://support.google.com/chrome/answer/15086890?hl=ja)（Chrome ヘルプ。アドレスバーの［このページについて Google に質問］とページのデータの処理）
- [Search with Google Lens in Chrome](https://support.google.com/chrome/answer/15086890?hl=en&co=GENIE.Platform%3DiOS)（Chrome Help、英語版。iPhoneの手順）
- [Chrome で AI モードを使用する](https://support.google.com/chrome/answer/16704170?hl=ja)（Chrome ヘルプ。AIモードのボタンの隠し方とAndroidの手順）
- [SearchContentSharingSettings](https://chromeenterprise.google/policies/#SearchContentSharingSettings)・[AIModeSettings](https://chromeenterprise.google/policies/#AIModeSettings)・[GenAiDefaultSettings](https://chromeenterprise.google/policies/#GenAiDefaultSettings)・[LensOverlaySettings](https://chromeenterprise.google/policies/#LensOverlaySettings)（Chrome Enterprise のポリシー一覧）
- [『Googleで調べる』『このページについてGoogleに質問する』を消す方法](https://support.google.com/chrome/thread/387019511?hl=ja)（Chrome ヘルプ コミュニティ、2025年11月12日）
- [【Chrome】『このページについてGoogleに質問する』を削除する](https://qiita.com/rana_kualu/items/83d1272a2f92422f9304)（Qiita、2025年8月24日）
- [「このページについてGoogleに質問する」消す方法（無効化・削除）](https://note.com/gamecentergx/n/n552415151d7c)（note、2025年11月19日）
- [Chrome で「このページについて Google に質問する」表示](https://www.724685.com/blog/2025/09/01111545.html)（なにしろパソコン、2025年9月1日）
- [下に出てくる「質問する」という表示を消したいです](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q13328211688)（Yahoo!知恵袋、2026年5月19日）
- [「ChromeのAI機能」すら消える。ブラウザのお節介な通知とAIを一掃してみた](https://www.lifehacker.jp/article/2601script-removes-ai-features-from-chrome-edge-firefox/)（ライフハッカー・ジャパン、2026年1月29日）
