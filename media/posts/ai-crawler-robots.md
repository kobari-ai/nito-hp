---
title: 【2026年10月】GPTBotなどAIクローラーをrobots.txtで止めるかの判断と書き方
date: 2026-10-23
category: AI検索対策
description: GPTBot・ClaudeBot・Google-ExtendedなどAIのクローラーを止めるか許すかを各社の公式ページで整理。学習用と検索用の違い、CDNで止まっている場合の確かめ方まで。
cover_tag: 設定
cover_headline: AIクローラーの許可と拒否
cover_sub: 学習用と検索用を分けて決める
cta: llmo
---

OpenAI・Anthropic・Perplexity・Googleは、サイトに来るAIのボットを学習用と検索用に分けて公開し、robots.txtで別々に止められるようにしています（2026年10月23日に各社の公式ページで確認）。

社内では「AIに学習されたくない」と「AI検索に出たい」が同じrobots.txtの話として持ち込まれ、どの名前を止めるとどうなるかが分からないまま決めがちです。この記事は各社の公式に書いてあることと無いことを分け、止めるか許すかの判断、robots.txtの書き方、自社サイトで確かめる手順を扱います。

:::takeaways
- **学習用のボット（GPTBot・Google-Extendedなど）を止めても検索に出るかには影響しない、とOpenAI・Google・Appleは公式に書いている**。ただしGoogle-Extendedを止めるとGeminiアプリの回答の根拠からも外れる
- **Google-Extendedを止めてもGoogle検索のAIによる概要からは外れない**。AIによる概要とAIモードから外す設定は、Search Consoleの「検索の生成 AI」にある
- **robots.txtで許可していても、CDNで止まっていることがある**。nitoのサイトでは学習用のユーザーエージェントにだけ403が返った
:::

<figure class="post-figure"><img src="/media/images/ai-crawler-robots/acrb_01_types.png" alt="AIのクローラーは3種類。学習用はモデルの学習に使う内容を集め、検索用はAIの検索の回答に出すページを集め、利用者の操作用は質問を受けてその場でページを読む" loading="lazy"></figure>

## AIのクローラーの3つの種類

GPTBotを止めるかどうかの相談でも、実際には各社のボットをまとめて決めることになります。各社の公式ページを並べると、役割は**モデルの学習用・AIの検索用・利用者の操作用の3つ**に分かれます。

| 会社 | 学習用 | 検索用 | 利用者の操作用 |
|---|---|---|---|
| OpenAI | GPTBot | OAI-SearchBot | ChatGPT-User |
| Anthropic | ClaudeBot | Claude-SearchBot | Claude-User |
| Perplexity | 公開なし | PerplexityBot | Perplexity-User |
| Google | Google-Extended | Googlebot | Google-Agentなど |
| Apple | Applebot-Extended | Applebot | 公開なし |

PerplexityはPerplexityBotを検索結果にサイトを出すためのものとし、基盤モデルの学習には使わないと説明していて、学習用の名前は公開していません。Common Crawl（公開データセットを作る団体）の**CCBot**も、学習用のボットとしてまとめて止められることが多い名前です。

GoogleとAppleは書き方が違い、注意が要ります。**Google-ExtendedとApplebot-Extendedは巡回するボットではなく、robots.txtに書く制御用の名前**で、巡回そのものは検索用のGooglebotやApplebotがしています。Googleの[一般的なクローラーの一覧](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers?hl=ja)も、Google-Extendedには個別のユーザーエージェントが無いという説明です。

## 止めたときに起きること

どのボットを止めるかで失うものは大きく変わります。各社の公式ページの説明を止めたときに起きることで並べたのが次の表です。

| 止めるもの | 止まること | AIの回答への影響（公式の書き方） |
|---|---|---|
| GPTBot | OpenAIの基盤モデルの学習 | 検索の設定とは独立 |
| ClaudeBot | Anthropicのモデルの学習 | 将来のコンテンツを学習データから除く |
| Google-Extended | Geminiの学習とGeminiアプリの根拠づけ | Google検索には影響しない。Geminiアプリの回答の根拠には使われない |
| Applebot-Extended | Appleの基盤モデルの学習 | Siri・Spotlight・Safariでは引き続き見つかる |
| OAI-SearchBot | ChatGPTの検索 | 検索の回答に出ない |
| Claude-SearchBot | Claudeの検索用のインデックス | 検索結果での見え方が下がることがある |
| PerplexityBot | Perplexityの検索 | 検索結果に出すには許可を勧める |

### 学習用を止めた場合

OpenAIの[クローラーの公式ページ](https://developers.openai.com/api/docs/bots)は、OAI-SearchBotとGPTBotの設定は互いに独立していて、検索に出ながら学習には使わせない指定ができると書いています。Anthropicの[Claudeヘルプセンター](https://support.claude.com/ja/articles/8896518)も学習用のClaudeBotと検索用のClaude-SearchBotを分けていますが、ClaudeBotを止めたときの説明は学習データから除くことだけで、検索への影響には触れていません。**学習用と検索用が別の名前なので、どの会社でも学習用だけを止める書き方はできます。**

Google-Extendedだけは扱いが違います。Googleの説明にあるGoogle-Extendedの対象は学習に加えてGeminiアプリで回答の根拠に使うことで、止めるとGeminiアプリの回答に自社のページが使われなくなります。

ただし学習を止める指定が効くのは、これから集める分です。Anthropicの説明も対象を「将来のコンテンツ」としていて、すでに学習に使った分を消す話ではありません。

### 検索用を止めた場合

検索用を止めた場合はその会社のAI検索の回答の情報源から外れてしまいます。OpenAIはOAI-SearchBotを止めたサイトは検索の回答に出ないと書き、Perplexityは検索結果に出すためにPerplexityBotの許可を勧めています。**商材が高い会社がAI検索で見込み客に見つけてもらいたいなら、検索用は許可したままにするのが前提です。**ChatGPTの検索に出る条件の細かい点は[ChatGPT検索で引用元に出る条件](/media/chatgpt-search-citation/)にまとめています。

### 利用者の操作用はrobots.txtが効かないことがある

利用者が「このページを読んで」と頼んだときに動くボットの扱いは、会社ごとにまちまちです。OpenAIはChatGPT-Userには「robots.txt rules may not apply」と書き、Perplexityも[Perplexity Crawlers](https://docs.perplexity.ai/guides/bots)でPerplexity-Userは原則としてrobots.txtを無視すると説明しています。Googleの[ユーザー トリガー フェッチャー](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers)も同じ扱いです。一方でAnthropicは、Claude-Userを止めると利用者の依頼でページを取りに行けなくなると書いていて、robots.txtの指定に従う仕様です。

## GoogleのAIだけ設定が別

Google-Extendedを止めればGoogleのAIをまとめて断れる、と考えて設定する会社は少なくありません。Googleの一覧の原文は「Google-Extended が Google 検索でのサイトの登録に影響したり、Google 検索でのランキング シグナルとして使用されたりすることはありません」です。**Google-Extendedが効くのはGeminiの学習とGeminiアプリなどの根拠づけで、Google検索のAIによる概要に出るかどうかは対象に入っていません。**

Google検索のAI機能から外す設定は、2026年8月31日に全サイトへ広がったSearch Consoleの「[検索の生成 AI 設定](https://support.google.com/webmasters/answer/16908024?hl=ja)」です。対象はAIによる概要・AIモード・Discoverの生成AI機能で、既定は「含める」になっています。除外を選ぶと、それらの機能でリンクも回答の根拠としての利用も無くなり、表示も流入も止まる仕組みです。通常の検索の順位には使わないとヘルプにあります。

<figure class="post-figure"><img src="/media/images/ai-crawler-robots/acrb_02_google.png" alt="GoogleのAIは設定が2つに分かれる。Google-ExtendedはGeminiの学習とGeminiアプリの根拠づけ、Search Consoleの検索の生成AI設定はAIによる概要とAIモード" loading="lazy"></figure>

ページ単位で抑えたいときは、検索セントラルの「[AI 機能とウェブサイト](https://developers.google.com/search/docs/appearance/ai-features?hl=ja)」が挙げるnosnippet・data-nosnippet・max-snippet・noindexを使います。Googlebot自体をrobots.txtで止めると、AIによる概要だけでなく通常の検索からも消えます。

<figure class="post-figure"><img src="/media/images/ai-crawler-robots/acrb_04_gsc_help.png" alt="Search Consoleヘルプの検索の生成AI設定のページ。2026年8月31日からすべてのウェブサイトに公開され、AIによる概要・AIモード・Discoverの生成AI機能が対象と書かれている" loading="lazy"><figcaption>Search Consoleヘルプの検索の生成 AI 設定（2026年10月23日に撮影）</figcaption></figure>

## 止めるか許すかの判断

迷ったときに使える問いは2つです。1つ目は**自社のコンテンツそのものが売り物か**、2つ目は**AI検索から見込み客に来てほしいか**です。

| 会社の状況 | 学習用 | 検索用 | 利用者の操作用 |
|---|---|---|---|
| サービスを売るための会社サイト | 方針しだい | 許可 | 許可 |
| 記事やデータそのものが商品 | 止める | 経営判断 | 経営判断 |
| 会員限定・有料の部分 | robots.txtでなくログインで守る | 同左 | 同左 |

商材が高い会社のサイトはページを読まれて問い合わせにつながるのが目的なので、検索用と利用者の操作用は許可が基本です。学習を許すかどうかは自社の文章や資料をモデルの学習に渡してよいかという話で、広報や法務の確認が要る会社もあります。**OpenAI・Google・Appleは学習を止めても検索に響かないと書いているため、方針が決まるまで学習用だけ止めておく選び方ができます。** Geminiアプリで見つけてもらいたい会社は、Google-Extendedを止める対象から外します。

### 日本の会社の設定の例

2026年10月23日に各社のrobots.txtを取得すると、判断は会社の稼ぎ方でくっきり分かれていました。

| サイト | AIのボットの指定 |
|---|---|
| 日本経済新聞・朝日新聞・読売新聞 | 学習用・検索用・利用者の操作用をまとめて拒否 |
| クックパッド | 学習用とPerplexityBotなどを拒否。OAI-SearchBotの指定なし |
| 食べログ | GPTBotとGoogle-Extendedだけ拒否 |
| freee・SmartHR・Sansan | AIのボットの個別の指定なし |

記事が商品の新聞社は検索用まで止め、食べログは学習用だけを止めています。ソフトウェアを売る会社は個別の指定を書かず、ほかのボットと同じ扱いのままでした。

### 誰が決めるか

学習の許可は広報・法務と経営、検索の許可は集客の責任者が決め、robots.txtの修正は制作会社かWebの担当に頼むのが一般的な分かれ方です。設定の持ち主の分け方は[ChatGPT検索で引用元に出る条件](/media/chatgpt-search-citation/)の表にまとめています。

## robots.txtの書き方

robots.txtはサイトのルート（`https://自社のドメイン/robots.txt`）に置くテキストファイルです。**サブドメインごとに1つずつ要る**ため、`www`と`blog`のように分かれているサイトはそれぞれに書きます。

同じくルートに置くllms.txtはAI向けにサイトを案内するファイルで、クローラーを止める働きはありません（[llms.txtとは](/media/llms-txt-structured-data/)）。

### 学習だけ止める書き方

検索用と利用者の操作用は許可したまま、学習用だけを止める形です。

```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: Applebot-Extended
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: *
Allow: /
```

この書き方でGoogle-Extendedを入れると、Geminiアプリが回答の根拠に自社のページを使わなくなります。Geminiでも見つけてもらいたい会社は、Google-Extendedの2行を外します。

### すべてのAIを止める書き方

新聞社のように検索用まで止めるなら、上の書き方の`User-agent: *`の前に次のグループを足し、検索用と利用者の操作用もまとめて止めます。

```
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: Claude-SearchBot
User-agent: Claude-User
User-agent: PerplexityBot
User-agent: Perplexity-User
Disallow: /
```

ここにGooglebotを入れると通常の検索からも消えるため、Googleの検索のAIを断るならSearch Consoleの設定が先です。Perplexity-UserやChatGPT-Userは書いても止まらない場合がある点も、先に社内に伝えておきます。

### 書くときの注意

robots.txtの規格（[RFC 9309](https://www.rfc-editor.org/rfc/rfc9309)）では、ボットは自分の名前に合うグループのルールだけに従い、合うグループが無いときに限って`User-agent: *`に従います。**GPTBot用のグループを作ると、`*`に書いた`Disallow`はGPTBotには効かなくなる**ため、止めたい場所はGPTBotのグループにも書き直します。名前の大文字と小文字は区別されません。

反映には時間がかかり、OpenAIは検索の側に約24時間、Perplexityは最大24時間と書いています。Anthropicは反映までの時間を公開していません。古い名前の`anthropic-ai`を書いているサイトもありますが、今のAnthropicのヘルプには載っていない名前です。

## CDNとrobots.txtを守らないボット

robots.txtは「来ないでほしい」という合図で、RFC 9309も「These rules are not a form of access authorization.」としています。実際に通信を止められるのは手前のCDNやWAF（不正な通信を止める仕組み）の設定です。

### Cloudflareの9月15日の変更

Cloudflareを使うサイトは、管理画面のAIボットの設定でSearch・Agent・Trainingを分けて止められます。Cloudflareの[2026年9月15日のブログ](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/)によると、**TrainingでBlockを選ぶと、検索と学習を兼ねるGooglebot・Bingbot・Applebotまで止まり、通常の検索にも影響します**。学習だけ断って検索に残すには、新しくできた「Disallow AI Training」を選びます。

同じブログによると、Cloudflare上で検索のボットを止めるサイトは1%未満、学習を止める仕組みを入れるサイトは17%でした（Cloudflareの集計）。さらに[Bot Preference Sync](https://blog.cloudflare.com/bot-preference-sync/)をオンにすると、管理画面の設定がrobots.txtの先頭に足されます。**制作会社が書いていない`Disallow`がrobots.txtに出ているときは、CDNの設定から来ていることがあります。**

### robots.txtを守らないボット

Cloudflareは[2025年8月4日のブログ](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/)で、robots.txtとWAFで止めた新しいドメインの中身をPerplexityが答えたという観測を出しました。止められるとmacOSのChromeを装うユーザーエージェントと公開範囲外のIPで取りに来た、というのがCloudflareの主張です。同じ試験のChatGPT-Userは、robots.txtを読んで止まったという結果でした。Common Crawlも、CCBotを名乗る偽のクローラーがいると[CCBotの説明](https://commoncrawl.org/ccbot)で注意しています。**確実に止めたいページはrobots.txtではなく、ログインかCDNの側で守ります。**

## 自社サイトで確かめる手順

設定したつもりでも、robots.txt・CDN・サーバーのどこかで想定と違う扱いになっている例は珍しくありません。ターミナルが使える担当者なら、次の順で10分ほどで確かめられます。

1. `curl https://自社のドメイン/robots.txt` で中身を見る。書いた覚えのない`Disallow`があればCDNの設定を疑う
2. ユーザーエージェント（ボットが名乗る文字列）だけを変えて同じページを取る。例: `curl -s -o /dev/null -w "%{http_code}" -A "GPTBot/1.4" https://自社のドメイン/`
3. 返ってきた状態コードを見る。200なら通り、403ならユーザーエージェントで止める設定がどこかにある
4. 403が出たら、CDNの管理画面（Cloudflareなら[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)）とサーバーのログで、本物のボットの扱いを確かめる
5. GoogleのAIの扱いは、Search Consoleの設定から検索の生成 AIを開いて見る

nitoのサイト（Cloudflareで配信、robots.txtは`User-agent: *`と`Allow: /`だけ）で、2026年10月23日に記事一覧のページをユーザーエージェントだけ変えて取得した結果が次の表です。

| ユーザーエージェント | 状態コード |
|---|---|
| ブラウザ・Googlebot | 200 |
| OAI-SearchBot・Claude-SearchBot・PerplexityBot | 200 |
| ChatGPT-User・Claude-User・Perplexity-User | 200 |
| GPTBot・ClaudeBot・CCBot・Bytespider | 403 |

**robots.txtはすべて許可なのに、学習用のユーザーエージェントにだけ403が返りました。** 403の中身は「Your request was blocked.」の1行で、GPTBotを名乗ってもrobots.txt自体は200で読めました。各社の公開IPから来ていない偽のユーザーエージェントなので、本物のボットが同じ扱いになるとは限りません。それでも、robots.txtだけを見て判断すると実際の扱いとずれることは確かめられます。

<figure class="post-figure"><img src="/media/images/ai-crawler-robots/acrb_03_check.png" alt="自社サイトでAIのボットの扱いを確かめる順番。robots.txtを開く、ユーザーエージェントを変えてcurlで取る、状態コードを読む、CDNの管理画面とログを見る" loading="lazy"></figure>

## よくある質問

### Q. GPTBotをブロックするとChatGPTの検索に出なくなりますか？

出なくなることはありません。OpenAIの公式ページは、GPTBotとOAI-SearchBotの設定は互いに独立していて、GPTBotを止めたまま検索に出られると書いています。

### Q. Google-ExtendedをブロックするとAIによる概要に出なくなりますか？

出なくなることはありません。Google-Extendedが管理するのはGeminiの学習とGeminiアプリなどの根拠づけで、AIによる概要とAIモードから外す設定はSearch Consoleの検索の生成 AI 設定です。

### Q. ClaudeBotをブロックするとClaudeの検索に出なくなりますか？

ClaudeBotは学習用で、Claudeの検索に使うのはClaude-SearchBotです。Anthropicのヘルプは、ClaudeBotを止めたときの影響を学習データから除くことだけで説明していて、検索への影響には触れていません。

### Q. PerplexityBotは学習に使われますか？

使われないと公式にあります。PerplexityBotは検索結果にサイトを出すためのもので、止めるとPerplexityの検索結果に出にくくなります。

### Q. robots.txtでブロックすればAIに一切使われなくなりますか？

そうはなりません。robots.txtはお願いの合図で、利用者の操作で動くChatGPT-UserやPerplexity-Userには効かない場合があると各社が書いています。確実に守るならログインかCDNの設定です。

### Q. Cloudflareの設定でGooglebotまで止まることはありますか？

あります。2026年9月15日の変更から、TrainingでBlockを選ぶとGooglebot・Bingbot・Applebotも止まる仕様です。学習だけ断るならDisallow AI Trainingを選びます。

### Q. AIのクローラーを止めると問い合わせは減りますか？

検索用を止めると、AI検索の回答の情報源から外れるため、そこから来る見込み客を失います。学習用だけを止めた場合、OpenAI・Google・Appleは検索に影響しないと説明しています。Google-ExtendedはGeminiアプリの回答の根拠からも外れる点が例外です。

### Q. robots.txtを書き換えてからAIに反映されるまでどれくらいかかりますか？

OpenAIは検索の側に約24時間、Perplexityは最大24時間です。GoogleのSearch Consoleの設定は、有効になってから1〜2日で除外され、キャッシュで遅れることもあるとヘルプにあります。

## 出典

- OpenAI「[Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)」（2026年10月23日取得）
- Google for Developers「[Google の一般的なクローラー](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers?hl=ja)」2026年10月19日更新（同）
- Google for Developers「[Google のユーザー トリガー フェッチャー](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers)」（同）
- Google 検索セントラル「[AI 機能とウェブサイト](https://developers.google.com/search/docs/appearance/ai-features?hl=ja)」2025年12月31日更新（同）
- Search Console ヘルプ「[検索の生成 AI 設定](https://support.google.com/webmasters/answer/16908024?hl=ja)」（同）
- Claude ヘルプセンター「[Anthropicはウェブからデータをクロールしていますか？](https://support.claude.com/ja/articles/8896518)」2026年4月7日（同）
- Perplexity「[Perplexity Crawlers](https://docs.perplexity.ai/guides/bots)」（同）
- Apple「[Applebotについて](https://support.apple.com/ja-jp/119829)」2026年9月7日公開（同）
- Common Crawl「[CCBot](https://commoncrawl.org/ccbot)」（同）
- IETF「[RFC 9309 Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309)」2022年9月（同）
- Cloudflare Blog「[Have it both ways: stay discoverable in search while disallowing AI training](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/)」2026年9月15日（同）
- Cloudflare Blog「[Say it once: introducing Bot Preference Sync](https://blog.cloudflare.com/bot-preference-sync/)」2026年8月21日（同）
- Cloudflare Blog「[Perplexity is using stealth, undeclared crawlers to evade website no-crawl directives](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/)」2025年8月4日（同）
- Cloudflare Docs「[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)」（同）
