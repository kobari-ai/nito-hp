---
title: 【2026年9月】Google AIモードを消す方法を解説｜Chromeのアドレスバー・新しいタブ・スマホ・Pixel
date: 2026-09-30
category: AI検索対策
description: Google AIモードの入口を消す方法を、Chromeのアドレスバー・新しいタブ・スマホ・Pixelに分けて解説。公式ヘルプの手順と、Chrome 154のchrome://flagsで確かめた結果から、消せるもの・消せないものを整理しました。
cover_tag: 使い方
cover_headline: Google AIモードを消す
cover_sub: アドレスバー・新しいタブ・スマホ・Pixel
---

Google検索のAIモードには、機能そのものを止める公式の設定がありません。2026年9月30日時点のGoogleのヘルプを読むと、非表示にする手順が書かれているのは**パソコンのChromeのアドレスバーに出るボタンと、Pixelの検索バーのショートカット**の2つです。

「AIモードを消す」と検索したときに出てくる手順には、今のChromeでは使えないものが混ざっています。ネットでよく紹介されている `chrome://flags` の項目は、9月30日に Chrome 154 で確かめたところ見つかりませんでした。この記事ではAIモードの入口を場所ごとに分けて、消せるもの・消せないもの・代わりの手を整理します。

:::takeaways
- AIモードそのものをオフにする公式の設定は無い。**消せるのはボタンやショートカットなどの入口**
- パソコンのChromeは、**アドレスバーを右クリックして［AI モードを常に表示する］の選択を外す**とボタンが消える（Chromeの公式ヘルプ）
- Pixelは、Googleアプリの**［設定］、［Pixel Search Box をカスタマイズ］で［AI モード］をオフ**にする
- `chrome://flags` の「AI mode」「AI Mode Omnibox entrypoint」は **Chrome 154 にも無い**。今ある4項目はボタンの挙動を変えるもので、消すスイッチではない
- 検索結果のタブ列の［AI モード］は消せない。AIの要約を見たくないなら［ウェブ］タブか `udm=14` を使う
:::

## AIモードの入口は5か所

AIモードに入る場所はブラウザと端末によって違います。消したいと感じているのがどの入口かで、取れる手が変わります。

<figure class="post-figure"><img src="/media/images/ai-mode-remove/01_fig_where.png" alt="AIモードの入口と消せるかどうかの図。Chromeのアドレスバーは右クリックでAIモードを常に表示するを外せば消せる。Pixelの検索バーはPixel Search Boxをカスタマイズでオフにできる。新しいタブの検索ボックスは公式の非表示の設定が無く、既定の検索エンジンをGoogle以外にすると出ない。検索結果のタブ列とAIモードそのものは消せない" loading="lazy"><figcaption>入口ごとの消せる・消せない（公式ヘルプとChrome 154で確認）</figcaption></figure>

| 入口 | 場所 | 消し方 | 公式の手順 |
|---|---|---|---|
| アドレスバーのボタン | パソコンのChrome | 右クリックで［AI モードを常に表示する］を外す | あり |
| 検索バーのショートカット | Pixelのホーム画面 | ［Pixel Search Box をカスタマイズ］でオフ | あり |
| 新しいタブの検索ボックスのボタン | Chrome（パソコン・スマホ） | 既定の検索エンジンを変える | なし |
| 検索結果のタブ | どのブラウザでも | 消せない。［ウェブ］タブや `udm=14` で避ける | なし |
| AIモードの画面 | google.com/ai など | 消せない | なし |

**公式の手順があるのは上の2つだけです。**それ以外は入口を使わずに済む形にするか、画面の見た目を拡張機能で変えることになります。

## Chromeのアドレスバーのボタンを消す

パソコンのChromeでは、アドレスバーの右端に［AI モード］のボタンが出ます。文字を打ち始めたときに目に入るため、「邪魔」と感じる人がいちばん多いのがこの入口です。Chromeのヘルプ「[Chrome で AI モードを使用する](https://support.google.com/chrome/answer/16704170?hl=ja&co=GENIE.Platform%3DDesktop)」に、非表示にする手順が書かれています。

1. パソコンでChromeを開く
2. アドレスバーの上で右クリックする
3. 出てきたメニューで［AI モードを常に表示する］のチェックを外す

<figure class="post-figure"><img src="/media/images/ai-mode-remove/02_help_hide.jpg" alt="Google Chromeヘルプのアドレスバーから操作する場合の節。ヒントとして、アドレスバーのAIモードとタブなどを追加を非表示にするには、アドレスバーを右クリックして、AIモードを常に表示するの選択を解除すると書かれている" loading="lazy"><figcaption>Chromeのヘルプのヒント（2026年9月30日取得）</figcaption></figure>

**これで消えるのは、アドレスバーの［AI モード］と［タブなどを追加］のボタンです。**AIモードそのものは残るため、アドレスバーで Tab キーと Enter キーを押すと、これまでどおりAIモードで質問できます。元に戻したいときは同じメニューで［AI モードを常に表示する］を選び直します。

Chromeの機能はアカウントや地域ごとに段階的に届きます。nitoが9月17日に Chrome 153 で見たときは、このメニューの項目がありませんでした。右クリックしても項目が出ない場合は、Chromeを最新版に更新してから、もう一度試してください。更新は右上の3点メニューの［ヘルプ］、［Google Chrome について］から行えます。

## 新しいタブの検索ボックスのボタン

Chromeで新しいタブを開くと、検索ボックスの右にも［AI モード］のボタンが出ます。アドレスバーのボタンと違い、**この入口を非表示にする手順はChromeのヘルプに書かれていません。**同じヘルプには新しいタブから開く手順と、キーボードの Tab キーと Enter キーで開く手順だけが載っています。

1つだけ効く手があります。既定の検索エンジンをGoogle以外にすると、新しいタブの検索ボックスがGoogleのものではなくなるため、AIモードのボタンも出なくなります。ChromeのAIモードは Google を既定にしているときの機能で、Chrome 154 の `chrome://flags` にある「AIM 3P entrypoint」は、Google以外の検索エンジンでもアドレスバーにAIモードの入口を出すための試験項目です。

ただし、検索エンジンを変えると検索結果そのものが変わります。**ボタンを消すためだけに検索エンジンを替えるのは、代わりに失うものが大きい方法です。**Googleの検索結果を使い続けたいなら、ボタンは残したまま押さない、という扱いが現実的です。

## chrome://flags では消せない

「AIモード 消し方」で上位に出る記事の多くが、`chrome://flags` で「AI mode」と「AI Mode Omnibox entrypoint」を Disabled にする手順を載せています。2025年12月から2026年8月に書かれたもので、当時のChromeでは効いた手順です。

**2026年9月30日に Chrome 154.0.8037.58 で `chrome://flags` を開き、検索窓に「AI mode」と入れたところ、この2つの項目は出てきませんでした。**表示されたのは次の4つです。

<figure class="post-figure"><img src="/media/images/ai-mode-remove/03_chrome154_flags.png" alt="Chrome 154.0.8037.58 の chrome://flags で AI mode を検索した画面。AIM 3P entrypoint、Omnibox Dynamic AI Mode Button、NTP Realbox Dynamic AI Mode Button、Omnibox AI Mode Space Does Not Activate の4項目だけが表示されている" loading="lazy"><figcaption>Chrome 154 の chrome://flags（2026年9月30日）。記事で紹介されている2つの項目は無い</figcaption></figure>

| 項目 | 説明文の中身 |
|---|---|
| AIM 3P entrypoint | Google以外の検索エンジンでもアドレスバーにAIモードの入口を出す |
| Omnibox Dynamic AI Mode Button | アドレスバーのAIモードのボタンを状況で出し分ける |
| NTP Realbox Dynamic AI Mode Button | 新しいタブの検索ボックスのボタンを状況で出し分ける |
| Omnibox AI Mode Space Does Not Activate | ボタンにフォーカスがあるときにスペースキーで起動しない |

どれもボタンの挙動を変える項目で、入口を消すスイッチではありません。9月17日の Chrome 153 でも同じ4項目でした。**`chrome://flags` はChromeの更新で項目が予告なく消えるため、古い記事の手順は今の画面と合わないことがあります。**アドレスバーのボタンを消したいなら、前の節の右クリックの設定を使ってください。

## スマホでは入口を消せるか

Chromeのヘルプを Android と iPhone の表示に切り替えると、新しいタブとアドレスバーからAIモードを開く手順は書かれていますが、**非表示にする手順はどちらにもありません。**パソコンの右クリックに当たる設定は、2026年9月30日時点のヘルプには見当たりませんでした。

### Pixelの検索バー

Pixelのホーム画面にある検索バーには、AIモードのショートカットが出ます。こちらは Google Pixel のヘルプ「[Google Pixel で検索する](https://support.google.com/pixelphone/answer/15629302?hl=ja)」に、無効にする手順が載っています。

1. 検索バーの G アイコンをタップする
2. プロフィールアイコンから［設定］、［Pixel Search Box をカスタマイズ］をタップする
3. ［AI モード］をオフにする

<figure class="post-figure"><img src="/media/images/ai-mode-remove/04_help_pixel.jpg" alt="Google Pixelヘルプの AI モードを使用する の節。AIモードのショートカットを無効にするには、検索バーでGアイコンをタップし、プロフィールアイコン、設定、Pixel Search Box をカスタマイズ とタップして、AIモードをオンまたはオフにすると書かれている" loading="lazy"><figcaption>Google Pixelのヘルプ（2026年9月30日取得）</figcaption></figure>

### Googleアプリと Search Labs

iPhoneやAndroidのGoogleアプリでは、画面上部のフラスコのアイコン（Search Labs）からAIモードをオフにする手順が紹介されることがあります。Googleのヘルプ「[Search Labs の「AI モード」](https://support.google.com/websearch/answer/16296315?hl=ja)」によると、**このスイッチが対象にしているのは試験運用版のAIモードだけです。**［AI モード］の横に Search Labs のアイコンが出ていない人は試験運用版を使っていないため、オフにしても検索のAIモードは残ります。

### SafariとiPhoneのブラウザ

iPhoneのSafariには、AIモードに関わる設定はありません。Google検索の結果にはタブ列の［AI モード］が出ますが、これは次の節のとおり消せない入口です。Safariの設定の［検索エンジン］でGoogle以外を選ぶと出なくなるのは、新しいタブの節と同じ理屈です。

## 検索結果のタブは消せない

Google検索の結果の上に並ぶタブ列には、［すべて］［画像］などと並んで［AI モード］が出ます。**このタブを消す公式の設定はなく、`udm=14` を付けた検索結果でも［AI モード］のタブは残ります。**

ここで多い混同が、AIモードとAIによる概要です。検索結果の一番上に出るAIの要約は「AIによる概要」という別の機能で、こちらは［ウェブ］タブに切り替えるか、URLに `udm=14` を付けると出なくなります。AIモードのタブは押さなければ開かないため、**邪魔に感じているのが検索結果の上のAIの文章なら、消したいのはAIによる概要のほうです。**手順は[Google AIモードの使い方](/media/google-ai-mode-guide/)の消し方の章にまとめています。

<figure class="post-figure"><img src="/media/images/ai-mode-remove/05_fig_choose.png" alt="消したいものごとの方法の図。AIモードのボタンはパソコンのChromeは右クリックの設定、Pixelは検索バーの設定で非表示にし、chrome://flagsでは消せない。AIによる概要はウェブタブかudm=14で出ない画面にし、AIモードとは別の機能。LINEのAIボタンはGoogleのAIモードではなくLINEのAgent iで、プラスメニューで表示をオフにすると30日間出ない" loading="lazy"><figcaption>消したいものごとの方法</figcaption></figure>

## LINEのAIボタンは別の機能

「AIモード 消す」と一緒に「LINE」が検索されていますが、LINEのトーク画面の入力欄の下に出るAIのボタンは、GoogleのAIモードではありません。LINEの「Agent i」という機能で、返信の提案や話題の提案をするものです。

LINEのヘルプ「[トークルームのAgent iとは？](https://help2.line.me/line/smartphone?contentId=200001143&lang=ja)」に表示の切り替えが載っています。トークルーム下部のプラスメニューを開き、［トークルームのAgent iを表示］をオフにします。**オフにした表示は30日間出なくなり、その間はすべてのトークルームでAgent iの機能が使えません。**設定はメッセージ入力欄の左側のボタンを押したときに反映されます。

## 効かない方法

入口を消そうとして試されることが多いものの、効果が無い方法をまとめます。

| 方法 | 結果 | 理由 |
|---|---|---|
| `chrome://flags` の「AI mode」「AI Mode Omnibox entrypoint」 | 項目が無い | Chrome 153・154 では見つからない |
| キャッシュや閲覧履歴の削除 | 効かない | 表示の設定ではなく保存データを消すだけ |
| シークレットモードで開く | 効かない | ボタンもタブもそのまま出る |
| Search Labs のAIモードをオフ | 検索のAIモードは残る | 対象は試験運用版だけ |
| `udm=14` を付ける | タブは残る | 消えるのはAIによる概要だけ |

**画面の見た目ごと消したいなら、拡張機能でページの表示を書き換える方法もあります。**ただし拡張機能は開発者が更新を止めると効かなくなり、Chromeのアドレスバーのような画面の外枠には手が届きません。まずは右クリックの設定とPixelの設定を使い、それで消えない入口は押さない、という順で考えるのが安全です。

## AI検索での見え方は別の話

自分の画面から入口を消すことと、会社やお店がAIモードの回答にどう出てくるかは別の問題で、後者は[AI検索対策](https://nito-0210.com/llmo/)として扱います。

## よくある質問

### Google AIモードを完全にオフにできますか？
できません。2026年9月30日時点で、AIモードそのものを止める公式の設定はありません。パソコンのChromeのアドレスバーのボタンと、Pixelの検索バーのショートカットだけは、公式の手順で非表示にできます。

### 右クリックしても項目が出ないのはなぜですか？
Chromeの機能は段階的に届くため、バージョンやアカウントによってはまだ項目がありません。右上の3点メニューの［ヘルプ］、［Google Chrome について］で最新版に更新してから、もう一度アドレスバーを右クリックしてください。

### chrome://flags でAIモードを消せますか？
Chrome 154 では消せません。記事で紹介されている「AI mode」と「AI Mode Omnibox entrypoint」の項目は見つからず、残っている4項目はボタンの挙動を変えるものでした。

### iPhoneでAIモードを消せますか？
iPhoneのChromeとSafariには、AIモードの入口を非表示にする設定がありません。検索結果の上のAIの要約を出したくない場合は、［ウェブ］タブを使うか、`udm=14` を付けたURLをブックマークしておく方法があります。

### AndroidでAIモードのアイコンを消せますか？
Pixelなら、Googleアプリの［設定］から［Pixel Search Box をカスタマイズ］を開き、［AI モード］をオフにできます。Pixel以外のAndroidのChromeには、2026年9月30日時点で非表示にする手順がヘルプにありません。

### Search LabsでAIモードをオフにすれば消えますか？
消えるのは試験運用版のAIモードだけです。［AI モード］の横に Search Labs のアイコンが出ていなければ、試験運用版を使っていないため、オフにしても検索のAIモードは残ります。

### AIモードのボタンを消すと履歴も消えますか？
消えません。ボタンを非表示にしても、これまでAIモードで話した内容は履歴に残ります。履歴を消す手順は[Google AIモードの履歴の見方と消し方](/media/ai-mode-history/)にまとめています。

### LINEのAIのボタンはGoogleのAIモードですか？
別の機能です。LINEの入力欄の下に出るのは「Agent i」で、トークルーム下部のプラスメニューから［トークルームのAgent iを表示］をオフにすると、30日間表示されなくなります。

## 出典

- Google Chrome ヘルプ「[Chrome で AI モードを使用する](https://support.google.com/chrome/answer/16704170?hl=ja&co=GENIE.Platform%3DDesktop)」（パソコン・Android・iPhone の表示、2026年9月30日取得）
- Google Pixel ヘルプ「[Google Pixel で検索する](https://support.google.com/pixelphone/answer/15629302?hl=ja)」（2026年9月30日取得）
- Google 検索 ヘルプ「[Search Labs の「AI モード」](https://support.google.com/websearch/answer/16296315?hl=ja)」（2026年9月30日取得）
- LINE ヘルプセンター「[トークルームのAgent iとは？](https://help2.line.me/line/smartphone?contentId=200001143&lang=ja)」（2026年9月30日取得）
- `chrome://flags` の画面と項目の説明文は、2026年9月30日に Chrome 154.0.8037.58（macOS）で確認
