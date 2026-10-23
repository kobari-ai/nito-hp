---
title: 【2026年10月】Gemini・Perplexityに自社が引用されるには？公式の仕組みと確かめ方
date: 2026-10-24
category: AI検索対策
description: GeminiとPerplexityに自社サイトが引用される条件を各社の公式資料で整理。Google検索の索引との関係、Perplexityの自前の索引とBing、Google-Extendedの扱い、社内での引用の確かめ方まで。
cover_tag: 実務
cover_headline: Gemini・Perplexityの引用
cover_sub: 引用元の探し方と社内での測り方
cta: llmo
---

HubSpot Japanが2026年7月に公表した調査では、BtoBの購買に関わる1,573人のうち51.2%が、業務用の商品やサービスの情報収集にGeminiを使うと答えました（頻繁に使うとときどき使うの合計）。

ChatGPTの対策を進めた会社でも、GeminiとPerplexityは引用元を探しに行く先が違い、同じ手当てでは足りないことがあります。この記事は2つのAIについて公式の資料に書いてあることと無いことを分け、引用されるページの書き方と、社内で引用を確かめる方法を書きます。

:::takeaways
- **Geminiアプリの回答の一部はGoogle検索の結果に基づく**とGoogleは書いている。Google-Extendedを止めると、Geminiアプリの回答の根拠に自社のページが使われなくなる
- **Perplexityは2,000億を超えるURLを追う自前の索引を持つ**と公表している。今もBingなどの外部の検索を併用しているかは、公式の資料に書かれていない
- 回答は聞くたびに変わるため、**同じ質問をログインの状態とモードをそろえて何回か聞き、記録した割合で判断する**。GA4とSearch Consoleでは2つのAIの引用回数は見えない
:::

## GeminiとPerplexityの違い

2つのAIはどちらも回答に出典のリンクを付けますが、**引用元を探しに行く先が違うため、直す場所も確かめ方も分けて考えます**。GeminiはGoogle検索の索引を使い、Perplexityは自社で作った索引を使うと、それぞれの公式の資料にあります。社内ではまとめてAI検索と呼ばれがちな2つを、公式の記述で並べると次のとおりです。

| 項目 | Gemini（アプリ） | Perplexity |
|---|---|---|
| 引用元を探す先 | Google検索の索引 | 自前の索引（2,000億超のURLを追跡） |
| 出典の見せ方 | 回答の下か中のソースボタン。出ない回答もある | 各回答に番号つきの引用 |
| サイト側で外す設定 | Google-Extended（Google検索には影響しない） | PerplexityBotをrobots.txtで止める |
| 引用の回数を見る管理画面 | 公式の案内なし | 一般のサイト向けの案内なし |
| 公式の資料に書かれていないこと | 引用元を選ぶ基準 | 今もBingなど外部の検索を使うか |

ChatGPTの検索で引用元に出る条件は[ChatGPT検索で引用元に出る条件](/media/chatgpt-search-citation/)に、Google検索のAIによる概要は[AI Overviewsに引用されるには？](/media/cited-by-ai-overviews/)に分けて書いています。AIによる概要とAIモードはGoogle検索の中の機能で、この記事ではGeminiアプリと別の製品として扱います。

<figure class="post-figure"><img src="/media/images/gemini-perplexity-citation/gpc_01_overview.png" alt="GeminiとPerplexityが引用元を探す先の違い。GeminiはGoogle検索の索引から、Perplexityは自前の索引から読み、サイト側で外す設定はGoogle-ExtendedとPerplexityBot" loading="lazy"></figure>

## Geminiが引用元を選ぶ仕組み

Geminiアプリに引用されるかどうかは、**Google検索の索引に載り、検索で読まれるページであることが出発点です**。引用元を選ぶ基準そのものは公開されていませんが、Geminiアプリと検索のつながりを書いた公式の記述は2つです。

### Google検索の索引との関係

Geminiアプリの[プライバシー ハブ](https://support.google.com/gemini/answer/13594961?hl=ja)は、回答の一部がGoogle検索の検索結果に基づくと説明しています。Googleの[一般的なクローラーの一覧](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers?hl=ja)はもう少し具体的で、Geminiアプリでのグラウンディングを「プロンプト入力時に Google の検索インデックスからモデルにコンテンツを提供すること」としています。

開発者向けの[Gemini APIの説明](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)には、モデルが検索の要否を判断し、検索の語を作って実行し、結果を引用つきでまとめる流れが図で示されているものの、Geminiアプリで同じ手順が動くとは書かれていません。それでも2つの記述から、**Googleの索引に無いページはGeminiアプリの回答の材料にも入らない**ことは言えます。

Search Centralの[AI 機能とウェブサイト](https://developers.google.com/search/docs/appearance/ai-features?hl=ja)は特別な構造化データは要らないとしていますが、対象はAIによる概要とAIモードです。Geminiアプリで構造化データが引用に効くかは公開されていません。

<figure class="post-figure"><img src="/media/images/gemini-perplexity-citation/gpc_02_gemini.png" alt="Geminiアプリが回答を作るときの流れ。質問を読む、Google検索の索引から内容を受け取る、回答を書く、ソースボタンにリンクを出す。Google-Extendedを止めたページは受け取る段階で外れる" loading="lazy"></figure>

### ソースボタンの見方

Geminiアプリのヘルプ「[Gemini アプリの関連ソースを表示する](https://support.google.com/gemini/answer/14143489?hl=ja)」によると、ソースがある回答では回答の下か中にソースボタンが出て、押すと右側に関連リンクのパネルが開きます。**ボタンが無いなら、Geminiアプリはその回答にリンクを出していません。** ヘルプはソースボタンのパネルを関連リンクの出る場所として説明しています。

**引用を数えるときはソースボタンのパネルに出たリンクだけを数えます。**

<figure class="post-figure"><img src="/media/images/gemini-perplexity-citation/gpc_shot_gemini_help.png" alt="Gemini アプリ ヘルプの関連ソースのページ。ソースボタンが無い回答ではGeminiアプリがリンクを出していないと書かれている" loading="lazy"><figcaption>Gemini アプリ ヘルプ『Gemini アプリの関連ソースを表示する』（2026年10月24日）</figcaption></figure>

### Google-Extendedを止めた場合

robots.txtで学習用のボットをまとめて止めている会社は、Google-Extendedを先に確かめます。一覧によるとGoogle-Extendedが管理するのはGeminiの学習とGeminiアプリでのグラウンディングで、**止めるとGeminiアプリの回答の根拠に自社のページが使われなくなります**。Google検索には影響しないため、AIによる概要とAIモードには出続けます。学習は断りつつGeminiでは見つけてもらう設定は無いので、集客を持つマーケ担当と文章の扱いを決める広報や法務で、どちらを取るかを決めます。書き方の詳細は[AIクローラーをrobots.txtで止めるかの判断と書き方](/media/ai-crawler-robots/)で扱いました。

<figure class="post-figure"><img src="/media/images/gemini-perplexity-citation/gpc_shot_google_extended.png" alt="Googleの一般的なクローラーの一覧のGoogle-Extendedの節。Geminiアプリでのグラウンディングに自社サイトの内容を使うかを管理できると書かれている" loading="lazy"><figcaption>Google 検索セントラル『Google の一般的なクローラー』のGoogle-Extendedの節（2026年10月24日）</figcaption></figure>

### 地域の質問と地図の答え

地域を付けた質問では、Geminiが出典のリンクでなく地図で答えることがあります。nitoが2026年10月7日に、ある士業の案件で地域名を付けた質問をGeminiに10回聞いたところ、9回はGoogleマップの店舗カードで答え、引用元のリンクは0件でした。1つの案件の実測ですが、**店舗や事務所に来てもらう商売では、ページより先にGoogleビジネスプロフィールの中身が読まれる**と考えて、営業時間・対応する地域・料金の目安をプロフィールにも書いておきます。口コミを増やせば紹介されるかは、nitoではまだ確かめていません。

## Perplexityが引用元を選ぶ仕組み

Perplexityは自前の索引から、文書をさらに小さく分けた単位で文を拾って採点します。nitoはここから、**ページ全体の評価より、1つの段落だけで質問の答えが閉じているかが引用に効く**と読んでいます。根拠はPerplexityが2025年9月に公開した、検索の基盤の設計についての記事です。

### 自前の索引とBingの関係

Perplexity Researchの[検索APIの設計の記事](https://research.perplexity.ai/articles/architecting-and-evaluating-an-ai-first-search-api)によると、2022年末の最初の版は公開されていた検索のAPIを組み込んでいました。高すぎた例として挙げる料金（1,000クエリ200ドル）のリンク先は、MicrosoftのBingのAPIの料金ページです。その後は自前の基盤に移り、**今の索引は2,000億を超えるURLを追っている**とあります。同じ日の[ブログ](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-search-api)によると、この基盤は一般向けの回答と同じものです。

Bingの索引も見ているとしてBing Webmaster Toolsへの登録を勧める解説記事もありますが、**今もBingなどの外部の検索を併用しているかは、公式の資料に書かれていません**。Bingへの登録は損になりませんが、Perplexityの対策として社内に説明すると公式の記述を超えてしまいます。

同じ記事によると、索引には権威のあるドメインや扱いの少ない話題の文書を優先して残し、入れ直すかはページの重要さと更新の頻度から予測するという説明です。候補は語の一致と意味の近さの両方で集め、文書と、文書を分けた小さな単位の両方で採点します。

<figure class="post-figure"><img src="/media/images/gemini-perplexity-citation/gpc_03_pplx.png" alt="Perplexityが回答を作るときの流れ。PerplexityBotが巡回して自前の索引に入れる、ページを段落ほどの単位に分ける、語の一致と意味の近さで候補を集めて採点する、番号つきの引用で回答する" loading="lazy"></figure>

### PerplexityBotとPerplexity-User

Perplexityのボットは2つあり、[Perplexity Crawlers](https://docs.perplexity.ai/guides/bots)が役割を分けて説明しています。

| 名前 | 何をするか | robots.txtとの関係 |
|---|---|---|
| PerplexityBot | Perplexityの検索結果にサイトを出してリンクする。基盤モデルの学習には使わない | 従う。検索に出したいなら許可を勧めている |
| Perplexity-User | 利用者の質問に答えるためにページを読み、回答にリンクを付ける | 利用者の求めで動くため、原則としてrobots.txtを無視する |

**検索結果に出たいなら、robots.txtでPerplexityBotを許可し、公開IPからの通信をWAFでも通します**。CloudflareとAWSのWAFでの手順も同じページにあり、反映は最大24時間です。WAFを持つ情報システムの担当や制作会社に頼むときは、[PerplexityBotのIPアドレスの一覧](https://www.perplexity.com/perplexitybot.json)のURLを添えます。

<figure class="post-figure"><img src="/media/images/gemini-perplexity-citation/gpc_shot_pplx_bots.png" alt="Perplexity CrawlersのページのPerplexityBotの行。検索結果に出すためにrobots.txtでの許可と公開IPからの通信の許可を勧め、学習には使わないと書かれている" loading="lazy"><figcaption>Perplexity『Perplexity Crawlers』（2026年10月24日）</figcaption></figure>

### 番号つきの引用とモデル

Perplexityのヘルプ「[How does Perplexity work?](https://www.perplexity.ai/help-center/en/articles/10352895-how-does-perplexity-work)」によると、回答には番号つきの引用が付き、Pro Searchでは既定のBestのほかGPT-5やClaude 4.6 Sonnetなどからモデルを選べます。

引用の数は測る条件で大きく変わります。未ログインのPerplexityは、nitoの計測だと3〜4回で登録を求める画面が出て、引用元も1回答あたり2〜3件でした。ログインしたProでは中央値39件です（計測の環境を替えたときの記録で、比較実験ではありません）。

上とは別の環境で2026年9月12日に、AI検索対策の会社を探す15の質問を4つのAIで計測したときは、1回答あたりの引用元がPerplexityで14.4件、Geminiで5.2件でした。**Perplexityは1つの回答に多くのページを並べるため、引用元に入ったかだけでなく、何番目にどの段落が引かれたかまで見ないと競合との差が分かりません。**

## 引用されるページに書くこと

他社の製品や制度についての事実は、その会社や役所のページから引かれやすく、**自社のページが引かれるのは自社にしか書けない文、つまり自社の数字と判断の基準です**。nitoが10月にGoogle検索のAIによる概要の引用元を調べたときも、他社の商品の記述はその会社のページか一覧に特化したページから引かれていました。GeminiとPerplexityで同じ調べはしていないので、ここは強い示唆にとどまります。

### 自社の数字と判断の基準

見込み客が商材の高い会社をAIで探すときの質問は、「〇〇の費用はいくらか」「どこに頼めばいいか」のような判断の問いです。その判断に使える数字と基準を書いた文が、回答の材料になります。料金なら「月額〇万円から」で止めず、どの作業が入り、どの条件で上がり、どんな会社には勧めないかまで書くと、ほかのサイトに同じ文がありません。導入の件数・対応の期間・契約の条件のように、自社の記録からしか出せない数字も同じ扱いです。

nitoが支援する士業の事務所では、手続きごとの料金と対応の範囲を書いた相続・遺言の新しいページが、公開3日後からGeminiとPerplexityの回答の引用元に入りました。

### 1段落で答えが閉じる書き方

Perplexityが文書を小さな単位に分けて採点する以上、前の段落に頼った書き方は不利になります。段落の中で「上記のとおり」「この方法なら」と書くと、その段落だけを拾われたときに意味が通りません。**見出しの問いへの答えを段落の1文目に置き、主語と数字をその段落の中で言い切ります。**

数字には取得日や更新日を添え、内容を直したら更新日も変えておくのが基本です。Perplexityは索引に入れ直すかを更新の頻度からも予測しているため、古い日付のまま中身だけ直すと、回答に届くまで時間がかかることがあります。Geminiについて同じ設計は公開されていないので、Gemini向けに書き方を変える根拠は無く、同じ書き方で足ります。

## 引用されているかを社内で確かめる方法

GeminiもPerplexityも同じ質問への回答が聞くたびに変わるため、**1回の画面ではなく、条件をそろえて同じ質問を何回か聞いた記録で判断します**。測り方の全体は[GEO対策の記事の測定の節](/media/geo-taisaku/)に書いたので、ここでは2つのAIでそろえる条件と記録の項目を書きます。

### 質問の作り方

見込み客が比べるときに打ちそうな文で質問を作り、社名を入れた質問と入れない質問を分けておきます。「〇〇社の評判は？」は紹介の中身が正しいかを見る質問で、「〇〇に強い会社は？」は候補に入るかを見る質問です。

土台の文を1つ決めて地域や予算などの条件を1か所ずつ変えると、どの条件で名前が出なくなるかが分かります。地域を付けた質問はGeminiが地図で答えることがあるので、別に数えます。自社が勝つように作った質問は見込み客の聞き方とずれるため、判断に使えません。

### 回数と条件のそろえ方

そろえる条件はAIごとに少し違います。

| 条件 | Gemini | Perplexity |
|---|---|---|
| ログイン | 測定用のアカウントか未ログイン | 測定用のアカウント（未ログインは数回で登録を求められ引用も少ない） |
| モード | 使ったモデルの名前を記録する | Pro Searchか、選んだモデル（Bestなど）を記録する |
| 回数 | 同じ質問を同じ日に2回以上 | 同じ質問を同じ日に2回以上 |

Geminiは検索やYouTubeの履歴など他のGoogleのサービスの情報を使うことがあると[プライバシー ハブ](https://support.google.com/gemini/answer/13594961?hl=ja)にあるため、担当者の個人のアカウントでは測りません。nitoは商談の前の計測で1つの質問を各AIに2回ずつ聞き、案件の毎日の計測では14の質問を4つのAIに1日1回ずつ聞いています。

<figure class="post-figure"><img src="/media/images/gemini-perplexity-citation/gpc_04_conditions.png" alt="引用を測るときにそろえる3つの条件。ログインの状態は測定用のアカウントにそろえる、モードとモデルの名前を記録する、同じ質問を同じ日に2回以上聞く" loading="lazy"></figure>

### 記録する項目

1つの回答を1行にして、次の項目を残します。

| 項目 | 書くこと |
|---|---|
| 日時 | 聞いた日付と時刻 |
| AIとモード | Gemini・Perplexityと、モデルやPro Searchの別 |
| ログインの状態 | 測定用のアカウントか未ログインか |
| 質問 | 打った文をそのまま |
| 社名 | 回答の本文に出たか、出た位置と紹介の1〜2文 |
| 引用元 | 出典のURLをすべて |
| 自社のURL | 引用元に入ったか、何番目か |

引用元に自社のURLが入ったのに社名が回答に出ないなら、ページは読まれていても紹介の材料になる文が無いということで、直すのはページの中身です。社名が出たのに自社のURLが無いなら、他社の記事や比較サイトの文から紹介されているので、その記事が自社をどう書いているかを確かめます。

<figure class="post-figure"><img src="/media/images/gemini-perplexity-citation/gpc_05_record.png" alt="引用を記録する1行の項目。日時、AIとモード、ログインの状態、質問、社名が出たか、引用元のURL、自社のURLが何番目か" loading="lazy"></figure>

### GA4とSearch Consoleで見えるもの

GeminiにもPerplexityにも、サイト運営者が引用の回数を見られる管理画面の公式の案内は見当たりませんでした。Search Consoleの[生成 AI パフォーマンス レポート](https://support.google.com/webmasters/answer/16984139?hl=ja)が数えるのはAIによる概要とAIモードの表示で、Geminiアプリは入りません。

GA4の[デフォルト チャネル グループ](https://support.google.com/analytics/answer/9756891?hl=ja)には「AI アシスタント」のチャネルがあり、ヘルプが例に挙げる参照元にGeminiは入っていますが、Perplexityの名前はありません。nitoのサイトのGA4では、2026年10月24日に見た直近7日に gemini.google.com からの18セッションがAI アシスタントに入っていました。Perplexityからの訪問はこの7日に無く、どのチャネルに入るかは確かめられていません。**自社のGA4で参照元 perplexity.ai の行がどのチャネルに入っているかを一度見ておきます。**

GA4に残るのは引用のリンクを押して来た人だけなので、記録した割合とは別の表で持ちます。GA4での見方は[AI検索対策の効果はどう測る？](/media/ai-search-measurement/)に書いています。

## 社内で決めること

質問を測る人、ページを直す人、robots.txtやWAFを持つ人は社内で別々のことが多く、**誰が何を持つかを決めないまま測り始めると、記録だけが増えて直す人に届きません**。

### 担当の分け方

| 仕事 | 持ち主の例 | 決めておくこと |
|---|---|---|
| 質問の一覧 | マーケ担当 | 何問で、いつ見直すか |
| 計測と記録 | マーケ担当・外部の支援会社 | 回数・頻度・ログインの状態 |
| ページの本文 | マーケ担当・制作会社 | 数字と基準の文を誰が書くか |
| robots.txt・WAF | 情報システムの担当・制作会社 | PerplexityBotとGoogle-Extendedの扱い |
| Googleビジネスプロフィール | 店舗や営業の担当 | 営業時間と対応する範囲の更新 |

### 手で測る場合の工数

20問をGeminiとPerplexityに2回ずつ聞くと、1回の計測で80回答になります。1回答を開いて記録するのに2分かかるとすると約2時間40分で、月に1回なら担当者の半日ほどです（見積もり）。毎週測るなら月に10時間を超えるため、決まった質問を自動で投げて記録する仕組みか、外部の支援を考える目安になります。

### ありがちな失敗

- 担当者の個人アカウントで測り、本人の履歴が入った回答を会社の数字にした
- Perplexityを未ログインで測り、引用元が2〜3件しか出ない状態で自社が出ないと判断した
- 学習を断るつもりでGoogle-Extendedを止め、Geminiアプリの回答の根拠からも外れていた
- 地域を付けた質問で地図の答えが出た回を引用0件と数え、ページの問題と取り違えた
- 1回出た・出なかったで、施策が効いたかを判断した

## よくある質問

### Q. Geminiに引用されるにはGoogle検索で上位に出る必要がありますか？

何位なら引用されるかは公開されていません。Googleはグラウンディングを、Googleの検索インデックスからモデルに内容を渡す仕組みと説明しているため、少なくとも索引に載っていることが前提です。

### Q. Geminiの回答にソースボタンが出ないのはなぜですか？

Geminiアプリのヘルプによると、ボタンが無いのはその回答にGeminiアプリがリンクを出さなかったためです。すべての回答にソースが付くわけではありません。

### Q. Google-ExtendedをブロックするとGeminiに引用されなくなりますか？

Geminiアプリの回答の根拠には使われなくなります。Google-Extendedが管理するのはGeminiの学習とGeminiアプリでのグラウンディングで、Google検索への登録には影響しないため、AIによる概要とAIモードには出続けます。

### Q. PerplexityはBingの検索結果を使っていますか？

公式の資料に書かれていません。Perplexityの研究記事によると、2022年末の最初の版は外部の検索APIを使っていましたが、今は2,000億を超えるURLを追う自前の索引を持っています。今もBingを併用しているかの記述はありません。

### Q. PerplexityBotを許可すればPerplexityで必ず引用されますか？

必ずではありません。Perplexityは検索結果に出すためにPerplexityBotの許可を勧めていますが、許可すれば引用されるとは書いていません。

### Q. GeminiやPerplexityからの流入はGA4で見られますか？

参照元の gemini.google.com や perplexity.ai で見られます。GA4の「AI アシスタント」のチャネルの例示にGeminiは入っていますが、Perplexityの名前はないため、自社のGA4でどのチャネルに入るかを確かめます。

## 出典

- Google「[Gemini アプリの関連ソースを表示する](https://support.google.com/gemini/answer/14143489?hl=ja)」Gemini アプリ ヘルプ（2026年10月24日取得）
- Google「[Gemini アプリのプライバシー ハブ](https://support.google.com/gemini/answer/13594961?hl=ja)」（同）
- Google 検索セントラル「[Google の一般的なクローラー](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers?hl=ja)」2026年10月19日更新（同）
- Google 検索セントラル「[AI 機能とウェブサイト](https://developers.google.com/search/docs/appearance/ai-features?hl=ja)」2025年12月31日更新（同）
- Google AI for Developers「[Google 検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)」（同）
- Search Console ヘルプ「[生成 AI パフォーマンス レポート（検索）](https://support.google.com/webmasters/answer/16984139?hl=ja)」（同）
- Google アナリティクス ヘルプ「[[GA4] デフォルト チャネル グループ](https://support.google.com/analytics/answer/9756891?hl=ja)」（同）
- Perplexity「[Perplexity Crawlers](https://docs.perplexity.ai/guides/bots)」（同）
- Perplexity「[PerplexityBotのIPアドレスの一覧](https://www.perplexity.com/perplexitybot.json)」（同）
- Perplexity Help Center「[How does Perplexity work?](https://www.perplexity.ai/help-center/en/articles/10352895-how-does-perplexity-work)」（同）
- Perplexity Research「[Architecting and Evaluating an AI-First Search API](https://research.perplexity.ai/articles/architecting-and-evaluating-an-ai-first-search-api)」2025年9月25日（同）
- Perplexity Blog「[Introducing the Perplexity Search API](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-search-api)」2025年9月25日（同）
- HubSpot Japan「[日本のBtoB購買に関する意識・実態調査2026](https://prtimes.jp/main/html/rd/p/000000083.000037724.html)」PR TIMES、2026年7月16日。調査期間2026年6月11日〜16日、従業員50名以上の企業でBtoB商材の購買に関わった1,573名（同）
