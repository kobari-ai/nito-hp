---
title: 【2026年10月】ChatGPT検索で引用元に出る条件とは？OAI-SearchBotと流入の見方
date: 2026-10-22
category: AI検索対策
description: ChatGPTの検索で自社サイトが引用元に出る条件をOpenAIの公式ページで整理。OAI-SearchBotとGPTBotの違い、robots.txtとCDNの確かめ方、GA4での流入の見え方まで。
cover_tag: 設定
cover_headline: ChatGPT検索の引用元
cover_sub: OAI-SearchBotの許可と流入の見方
cta: llmo
---

OpenAIのクローラーの公式ページは、ChatGPTの検索結果に出たいサイトにOAI-SearchBotをrobots.txtで許可し、OpenAIが公開するIPアドレスからの通信も通すよう勧めています（2026年10月22日に確認）。

ところが社内では、robots.txtは制作会社、CDNは情報システムの担当、GA4はマーケ担当と持ち主が分かれがちで、どこで止まっているかが見えません。この記事は公式に書いてあることと無いことを分けたうえで、確かめる順番と社内の分担を書きます。

:::takeaways
- ChatGPTの検索の引用元に出る公式の条件は、**OAI-SearchBotを許可することと、サーバーやCDNがOpenAIのIPアドレスを通すことの2つ**。掲載の位置は保証されない
- 学習用のGPTBotと検索用のOAI-SearchBotは別々に設定でき、**GPTBotを止めても検索には出られる**。Bingの索引に載ることが条件とは公式に書かれていない
- 流入はutm_source=chatgpt.comとGA4のAIアシスタントのチャネルで見る。**utmを説明していた公式のFAQは、10月22日に開くと別の記事に替わっていた**
:::

<!-- SHOT: 図1 引用元に出るまでの4つの関門（robots.txt・CDNとサーバー・ページの中身・計測）を縦4段で。HTML 図 brain/scripts/seo/fig/cscit_gates.html を描画して /media/images/chatgpt-search-citation/cscit_01_gates.png。alt「ChatGPTの検索で引用元に出るまでの4つの関門。robots.txtでOAI-SearchBotを許可する、CDNとサーバーがOpenAIのIPを通す、ページに答えがある、流入を計測する」 -->

## ChatGPT検索が引用元を選ぶ仕組み

ChatGPTに最新の情報が要る質問をすると、ChatGPTは自分でWebを検索し、回答に出典のリンクを付けます。OpenAIのヘルプ「[Searching the web with ChatGPT](https://help.openai.com/en/articles/9237897-chatgpt-search)」によると、検索は無料プランでも、ログインしていない人でも使えます。回答の下に「情報源」が出ているときは、押すと引用したページとほかの関連リンクが並びます。

同じヘルプによると、**ChatGPTは外部の検索の提供元と組み、質問を検索向けの語に書き換えて送ることがあります**。ヘルプはがんの治療薬についての質問を例に、「CCR8 immunotherapy drug development 2025」のような語に直して送り、結果を見てからさらに細かい語で検索し直す流れを示しています。並べ方は複数の要素で決まり、掲載の位置は保証されないという説明です。

解説記事で条件のように書かれる話には、公式のページに無いものも混ざっています。

| 項目 | 公式に書いてあること | 書いていないこと |
|---|---|---|
| 載る条件 | OAI-SearchBotの許可と、ホストやCDNがOpenAIのIPを通すこと | 何をすれば上に出るか |
| 並び順 | 複数の要素で決め、位置は保証しない | 要素の中身 |
| 検索の提携先 | 外部の検索の提供元に語を送る | Bingの索引に載ることが条件か |
| 学習 | GPTBotを止めると学習に使わない合図になる | 学習を止めると検索で不利になるか |
| 流入の計測 | 参照URLにutm_source=chatgpt.comを付ける（10月4日に保存されたFAQ） | 今読める公式ページでの記載 |

### Bingの索引との関係

ChatGPTの対策はBingの対策から始まると書く解説記事もあります。ヘルプが検索の提供元のプライバシーの案内として挙げるのはMicrosoftとShopifyの2社で、**MicrosoftのBingが提供元の一つである強い示唆にはなりますが、Bingの索引に載っていないと引用されないとは書かれていません**。OpenAIの出版社向けのFAQ（2026年10月4日に保存された版）には、robots.txtで止めたページのURLを外部の検索の提供元から得ることがあるという文もありました。

そのため、Bing Webmaster Toolsに登録して索引の状態を見ておくことは損になりませんが、条件として社内に説明するのは公式の文を超えます。Bingの管理画面で見られる引用の数はCopilotなどの分で、ChatGPTが入るとは書かれていない点は[Bing Webmaster ToolsのAIパフォーマンスの記事](/media/bing-ai-performance/)にまとめています。

## OpenAIの3つのクローラー

OpenAIのサイトに来るボットは用途ごとに名前が分かれていて、robots.txtでも別々に指定します。[Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)（2026年10月21日更新）が挙げる3つの違いは次のとおりです。

| 名前 | 何のために来るか | robots.txtで止めたとき |
|---|---|---|
| OAI-SearchBot | ChatGPTの検索結果にサイトを出す | 検索の回答には出ない。ナビゲーション用のリンクとしては出ることがある |
| GPTBot | 基盤モデルの学習に使う内容を集める | 学習に使わない合図になる。検索の表示とは別 |
| ChatGPT-User | 利用者の質問やGPTの操作でページを読みに行く | 利用者の操作なので効かない場合がある。検索に出すかの判断には使わない |

このほかに、ChatGPTの広告として入稿したページだけを確かめに来るOAI-AdsBotがあります。**検索に出すかどうかを決めるのはOAI-SearchBotの設定だけ**で、公式ページはChatGPT-Userを検索の止め方に使わないよう書いています。

<!-- SHOT: 図2 OpenAIの3つのクローラー（OAI-SearchBot＝検索・GPTBot＝学習・ChatGPT-User＝利用者の操作）を縦3段で。HTML 図 brain/scripts/seo/fig/cscit_bots.html を描画して /media/images/chatgpt-search-citation/cscit_02_bots.png。alt「OpenAIのクローラーは3つ。OAI-SearchBotはChatGPTの検索に出すため、GPTBotはモデルの学習のため、ChatGPT-Userは利用者の操作でページを読むため」 -->

### 学習は断って検索に出る書き方

公式ページによると3つの設定は互いに独立していて、OAI-SearchBotを許可したままGPTBotだけを止められます。学習には使わせず、検索には出したい会社のrobots.txtの例が次の形です。

```
User-agent: OAI-SearchBot
Allow: /

User-agent: GPTBot
Disallow: /
```

robots.txtを直してから検索の側に反映されるまでは約24時間かかると書かれています。両方を許可しているサイトでは、1回の巡回の結果を検索と学習の両方に使うことがあるとも説明されているため、**学習を断るならGPTBotの行を明示しておく**のが確実です。

### Disallowとnoindexの違い

robots.txtのDisallowは巡回を止める合図で、ページの存在を消すものではありません。今の公式ページも、OAI-SearchBotを止めたサイトがナビゲーション用のリンクとしては出ることがあると書いています。10月4日に保存された出版社向けのFAQは、リンクとページ名だけが出るのを防ぎたいならnoindexのメタタグを使い、**そのタグを読めるようにクローラーの巡回は許可しておく**よう案内していました。止めたいページを両方で塞ぐと、noindexが読まれないまま残ります。

## CDNとサーバーの設定

robots.txtで許可していても、手前のCDNやセキュリティの設定が通信を止めていれば巡回できません。ヘルプはサイトを検索の対象にする条件として、ホストやCDNが[OpenAIの公開するIPアドレス](https://openai.com/searchbot.json)からの通信を通すことを挙げています。このリストは2026年10月22日に開くと作成日時が2026年1月2日でした。

CDNの既定も変わっています。Cloudflareの「[Block AI Bots](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/)」によると、2026年9月15日から新しく登録したドメインの既定は、学習（Training）と利用者の代わりに動くボット（Agent）を広告のあるページで止め、検索（Search）は許可する設定になりました。Cloudflareの[robots.txtの設定](https://developers.cloudflare.com/bots/additional-configurations/managed-robots-txt/)を有効にすると、GPTBotやGoogle-Extendedなどを止める行が既存のrobots.txtの前に足されます。

nitoのサイト（Cloudflareを通して配信、robots.txtはすべて許可）で、2026年10月22日に名乗り（ユーザーエージェント）だけを変えて記事一覧のページを取得してみました。OAI-SearchBot・ChatGPT-User・bingbotの名乗りでは200が返り、GPTBotの名乗りでは403で拒否されました。OpenAIのIPアドレスから来ていない偽の名乗りなので本物のクローラーの扱いと同じとは限りませんが、**robots.txtが許可していても、CDNの側で特定のボットを止めていることがある**のは確かめられました。

<!-- SHOT: 図3 robots.txtとCDNの2段の関門。robots.txtは許可、CDNで止まると届かない。HTML 図 brain/scripts/seo/fig/cscit_cdn.html を描画して /media/images/chatgpt-search-citation/cscit_03_cdn.png。alt「OAI-SearchBotはrobots.txtとCDNの2か所を通ってページに届く。robots.txtで許可していてもCDNで止めていると巡回できない」 -->

<!-- SHOT: Cloudflare Docs「Block AI Bots」の New defaults on September 15, 2026 の節・https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/・PC・赤枠は Search will remain allowed を含む段落。figcaption「Cloudflare Docs（2026年7月1日更新）の新しい既定の説明」 -->

### 自社サイトで確かめる順番

確かめる場所は4つで、上から順に見ると止まっている場所を絞れます。

1. ブラウザで `https://自社のドメイン/robots.txt` を開き、`User-agent: OAI-SearchBot` か `User-agent: *` の下に `Disallow: /` が無いかを見る
2. CDNやWAFの管理画面でAIのボットの扱いを見る。Cloudflareなら「Security Settings」の「Configure AI bot policies」でSearchが許可になっているか
3. サーバーのアクセスログで `OAI-SearchBot` を検索し、来ていれば送信元のIPが公開リストの範囲かを見る
4. ChatGPTで検索を選び、自社の社名とサービス名で質問して、情報源に自社のページが出るかを見る

1と3は社内の誰でも見られますが、2はCDNの契約者の権限が要ります。4は回答が毎回変わるため、1回出なかったことで止まっていると決めず、2と3の結果と合わせて読みます。

<!-- SHOT: ChatGPTの回答の下の「情報源」ボタンと引用の一覧・https://chatgpt.com/・スマホ・未ログイン・中立の質問（例: 国民の祝日の一覧）・赤枠①情報源ボタン ②引用の一覧。figcaption「回答の下の情報源を押すと、引用したページが並ぶ」 -->

## ChatGPTからの流入の見え方

ChatGPTの引用元のリンクから来た人のURLには、`utm_source=chatgpt.com` が付きます。この仕組みを公式に説明していたのは、OpenAIのヘルプの「Publishers and Developers - FAQ」でした。Internet Archiveが2026年10月4日に保存した版には、OAI-SearchBotを許可したサイトはGoogleアナリティクスなどでChatGPTからの流入を追え、ChatGPTが参照URLにこのパラメータを自動で付けると書かれています。

**同じURLを2026年10月22日に開くと、ChatGPT Atlasの提供終了を案内する記事に替わっていました。** このFAQはAtlasの項目の下に置かれていたため、Atlasの終了と一緒に差し替わったとみられますが、OpenAIからの説明は見つけられませんでした。上位の解説記事が根拠に引くページが今は読めないので、社内の資料に引くときは保存版の日付を添えるのが無難です。utmが今も付くかどうかは、自社のGA4に `chatgpt.com` の参照元が届いているかで確かめられます。

GA4の[デフォルト チャネル グループのヘルプ](https://support.google.com/analytics/answer/9756891?hl=ja)には「AI アシスタント」のチャネルがあります。ChatGPT・Gemini・Deepseek・Copilot・Grokなどから来た分を集め、GoogleのAIによる概要とAIモードは除くという定義です。参照元のURLがAIアシスタントのリストに一致すると、メディアが `ai-assistant` に置き換わります。

数字ごとに見る場所が違うため、月次の報告では混ぜないようにします。

| 知りたいこと | 見る場所 | 分かること |
|---|---|---|
| ChatGPTから来た人 | GA4の参照元とAIアシスタントのチャネル | 引用を押して来た訪問 |
| クローラーが来ているか | サーバーやCDNのアクセスログ | OAI-SearchBotの訪問とIP |
| Copilotでの引用 | Bing Webmaster Tools | 出典として示された回数 |
| 回答で名前が挙がるか | ChatGPTに実際に質問する | 自社が紹介されるか・どのページが引かれるか |

GA4で正規表現を使ってAIの参照元をまとめる手順は[AI検索対策の効果の測り方](/media/ai-search-measurement/)に書きました。Search ConsoleではChatGPTからの分は見られないことも、[サーチコンソールの生成AIレポートの記事](/media/gsc-ai-mode/)で触れています。

## 社内で決めること

ここまでの設定はどれも費用をかけずに直せるため、止まりやすいのは技術より、**誰が持っていて誰が決めるかが社内で決まっていないこと**です。

### 設定の持ち主

| 設定 | 持ち主の例 | 決めておくこと |
|---|---|---|
| robots.txt | 制作会社・Webの担当 | OAI-SearchBotとGPTBotをそれぞれ許可するか |
| CDN・WAF | 情報システムの担当・ホスティング会社 | Search・Agent・Trainingの分類ごとの扱い |
| サーバーのログ | 情報システムの担当・制作会社 | OAI-SearchBotの訪問を月に1回見るか |
| GA4 | マーケ担当 | AIアシスタントのチャネルを月次の数字に入れるか |

制作会社が持っているサイトでは、robots.txtの1行の修正でも作業の依頼になることがあります。CDNの設定はセキュリティの方針と結びつくため、マーケ担当が自分で変えるより、情報システムの担当に「検索用は許可、学習用は会社の方針で」と分けて頼むほうが話が通りやすくなります。

### 学習を許すかの判断

検索に出すかと、学習に使わせるかは別の判断です。検索の許可は集客の判断なのでマーケ担当が決められますが、学習の許可は自社の文章や資料をモデルの学習に渡すかどうかの話で、広報や法務の確認が要る会社もあります。公式ページの範囲でいえば**GPTBotを止めても検索の表示には影響しない**ため、迷っているあいだは学習だけ止めておく選び方もできます。

### ありがちな失敗

- AIのボットをまとめて止める設定やプラグインを入れ、その中にOAI-SearchBotも入っていた
- robots.txtだけを見て問題なしと判断し、CDNやセキュリティ製品のボット対策で止まっていたのに気づかなかった
- 公開前の検証用サイトに入れた `Disallow: /` が、本番に移したあとも残っていた
- 検索に出したくないページをrobots.txtで止め、noindexが読まれずにリンクだけ出続けた

## 引用元に出ることとAIの回答で名前が挙がること

OAI-SearchBotを許可するのは、ChatGPTが自社のページを読める状態にするところまでです。公式ページも掲載の位置は保証しないと書いているとおり、許可しただけで「〇〇に強い会社は？」という質問の答えに社名が挙がるわけではありません。回答は検索で集めたページをもとに書かれるため、**そのページに自社のことが何と書かれているかで社名が挙がるかどうかが変わります**。

そのため、引用元に出る条件を整えたあとに見るのは、自社の見込み客がAIに聞きそうな質問で実際に社名が出るか、どのページが引かれているかです。回答は同じ質問でも毎回変わるので、何度か聞いて出た回数で見ます。自社のサイト以外にどんな第三者の記事が要るかは[サイテーションの増やし方](/media/citation-for-ai/)、名前が出ない原因の切り分けは[ChatGPTに自社が出てこない原因](/media/chatgpt-not-appearing/)に書いています。

## よくある質問

### Q. ChatGPTの検索に出るにはBingへの登録が必要ですか？

公式のページに、Bingへの登録が必要とは書かれていません。OpenAIのヘルプは外部の検索の提供元と組むと説明し、プライバシーの案内にMicrosoftとShopifyを挙げています。Bing Webmaster Toolsへの登録は無料なので、索引の状態を確かめる目的で入れておくのは損になりません。

### Q. GPTBotをブロックするとChatGPTの検索に出なくなりますか？

出なくなりません。OpenAIの公式ページは、OAI-SearchBotを許可して検索に出しながら、GPTBotを止めて学習に使わない合図を出せると書いています。

### Q. OAI-SearchBotを許可すればChatGPTで必ず引用されますか？

必ずではありません。OpenAIのヘルプによると検索結果は複数の要素で並べられ、掲載の位置は保証されません。許可は引用元の候補に入るための条件です。

### Q. ChatGPTの検索に出したくないページはどうすればいいですか？

robots.txtでOAI-SearchBotを止めると検索の回答には出ませんが、ナビゲーション用のリンクとしては出ることがあります。2026年10月4日に保存されたOpenAIのFAQは、リンクも出したくない場合はnoindexのメタタグを使い、タグを読めるようにクローラーの巡回は許可するよう案内していました。

### Q. robots.txtを直してからChatGPTに反映されるまでどれくらいかかりますか？

OpenAIの公式ページによると、検索の結果に反映されるまで約24時間かかります。

### Q. ChatGPTからの流入はGA4のどこで見られますか？

既定のチャネルの「AI アシスタント」か、参照元の `chatgpt.com` で見られます。GA4のヘルプによると、このチャネルはChatGPT・Gemini・Copilotなどから来た分を集め、GoogleのAIによる概要とAIモードは含みません。

### Q. ChatGPT-Userはrobots.txtで止められますか？

止まらない場合があります。OpenAIの公式ページは、ChatGPT-Userは利用者の操作で動くためrobots.txtのルールが適用されないことがあると書き、検索に出すかの管理にはOAI-SearchBotを使うよう案内しています。

## 出典

- OpenAI「[Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)」2026年10月21日更新（2026年10月22日取得）
- OpenAI Help Center「[Searching the web with ChatGPT](https://help.openai.com/en/articles/9237897-chatgpt-search)」（同）
- OpenAI Help Center「Publishers and Developers - FAQ」の[Internet Archiveの保存版](https://web.archive.org/web/20261004224023/https://help.openai.com/en/articles/12627856-publishers-and-developers-faq)2026年10月4日保存（同）。[同じURL](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq)は10月22日にChatGPT Atlasの提供終了の記事を表示
- OpenAI「[searchbot.json](https://openai.com/searchbot.json)」作成日時2026年1月2日（同）
- Google アナリティクス ヘルプ「[[GA4] デフォルト チャネル グループ](https://support.google.com/analytics/answer/9756891?hl=ja)」（同）
- Cloudflare Docs「[Block AI Bots](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/)」2026年7月1日更新（同）
- Cloudflare Docs「[robots.txt setting](https://developers.cloudflare.com/bots/additional-configurations/managed-robots-txt/)」2026年10月8日更新（同）
