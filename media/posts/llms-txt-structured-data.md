---
title: 【2026年10月】llms.txtとは？意味ないと言われる理由・書き方・置くかの決め方
date: 2026-07-16
modified: 2026-10-26
category: AI検索対策
description: llms.txtとは何かを提案者の仕様（2026年8月の第2版）で確認。意味ないと言われる理由をGoogle・OpenAI・Anthropicの公式と13.7万サイトのログ調査で確かめ、書き方の例、置くかの決め方、構造化データの扱いまで。
cover_tag: 解説
cover_headline: llms.txtとは
cover_sub: 意味ない説と置くかの決め方
cta: llmo
---

llms.txtは、2024年9月にAnswer.AIのJeremy Howard氏が提案したファイルで、2026年8月に第2版が出ました。Google検索はこのファイルを使わないと公式ガイドに書く一方で、同じGoogleのChromeは開発者向けの検査ツールLighthouseの確認項目に入れています。

制作会社やSEOツールに「置いたほうがいい」と言われて迷っているサイト担当者・マーケ担当者に向けて、仕組み、意味ないと言われる理由の事実、書き方、置くかどうかの決め方を書きます。

:::takeaways
- **Google検索（AIによる概要・AIモードを含む）はllms.txtを使わないと公式ガイドに書いている**。OpenAI・Anthropic・Perplexityのクローラーの公式ページにも、llms.txtを読むという記載は無い（2026年10月26日確認）
- **Ahrefsの13.7万ドメインの調査では、置いたサイトの97%が2026年5月の1か月に1回も取得されなかった**。取りに来た中で大きいのはAIと関係のないボットで、AI検索のボットは1.1%
- 置くかは**AIエージェントに読ませたい資料があるか**で決める。AI検索に名前を出したいなら、先に本文と測り方を整える
:::

## llms.txtとは

サイトのルート（`https://自社のドメイン/llms.txt`）に置く、Markdownで書いたテキストファイルです。サイトが何者か、どのページに何が書いてあるかを短くまとめ、AIのエージェントが必要なページへたどり着けるようにする目的で提案されました。**robots.txtと名前は似ていますが、何かを止めたり許したりする働きはありません。**

### 提案の出どころと第2版

提案の本文は[llmstxt.org](https://llmstxt.org/)にあり、2024年9月3日に公開され、2026年8月10日に第2版へ改められました。第2版の背景説明によると、数千のサイトが置いていて、文書を公開する仕組みの多くが自動で作ります。OpenAI・Anthropic・Geminiも自社の開発者向け資料に置いているとあります。**提案者自身も、いちばん使われているのはソフトウェアの資料をコーディング用のAIが読む場面だと書いています。**

第2版で増えたのは3点です。サイトの途中のパス（`/docs/llms.txt`など）に置けばその下のページを指すと定めたこと、各ページのMarkdown版のURLに、第1版の`page.html.md`に加えて、拡張子を置き換えた`page.md`も認めたこと、HTMLの`link`要素でMarkdown版とllms.txtの場所を知らせる書き方を加えたことです。前の版にあった、ファイルを展開してAIに渡すための道具の説明は外れました。

### robots.txtやサイトマップとの違い

3つとも同じくルートに置くファイルなので、制作の現場では混同されがちです。役割を並べると次のとおりです。

| ファイル | 読む相手 | 書くこと | できること |
|---|---|---|---|
| robots.txt | 検索・AIのクローラー | どのボットにどこを見せるか | 取得を止める・許す |
| sitemap.xml | 検索エンジン | 登録してほしいURLの一覧 | 新しいページを早く見つけてもらう |
| llms.txt | AIのエージェント | サイトの概要と主なページへのリンク | 読む側が使えば道案内になる |

AIのクローラーを止めるか許すかはrobots.txtの話で、llms.txtを置いても置かなくても変わりません。止め方は[AIクローラーをrobots.txtで止めるかの判断と書き方](/media/ai-crawler-robots/)にまとめています。

## 意味ないと言われる理由

AI検索に名前を出すための施策としてllms.txtが紹介されてきたことに対し、「意味ない」という声が出ています。公式の文言と、ログを数えた調査に分けて確かめます。

### Googleの公式の書き方

Googleは[生成AI機能向けの最適化ガイド](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide?hl=ja)（2026年10月9日更新）で、対応しなくてよいことの1つ目にllms.txtを挙げました。

> Google 検索（生成 AI 機能を含む）で表示されるようにするために、機械可読ファイル、AI テキスト ファイル、マークアップ、またはマークダウンを新たに作成する必要はありません。Google 検索自体がこれらを使用しないためです。
>
> 出典：[Google 検索の生成 AI 機能向けにウェブサイトを最適化する](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide?hl=ja)

同じ節によれば、ほかのサービスのために作って維持するのは問題なく、Google検索では無視されるので表示や順位に影響しません。**置いて損をすることはないものの、AIによる概要やAIモードに出る助けにもならない、というのがGoogle検索の立場です。**

<figure class="post-figure"><img src="/media/images/llms-txt-structured-data/llt_google_guide.png" alt="Google検索セントラルの生成AI機能向けの最適化ガイド。Google検索は生成AI機能を含めてLLMS.txtなどの機械可読ファイルを使用しないと書かれている" loading="lazy"><figcaption>Google 検索セントラル 生成 AI 機能向けの最適化ガイド（2026年10月26日）</figcaption></figure>

一方、Chromeの開発チームはLighthouseの実験的な監査「エージェントによるブラウジング」に[llms.txtの確認](https://developer.chrome.com/docs/lighthouse/agentic-browsing/llms-txt?hl=ja)を入れました（2026年5月5日更新）。ファイルが無いとエージェントがサイトの把握にクロールの時間を使う可能性があると説明し、取得でサーバーエラーが出たら指摘します。ただし404のときは、現時点では任意なので「該当なし」と扱う決まりです。

GoogleのJohn Mueller氏は2025年4月、どのAIサービスもllms.txtを使うとは言っておらず、サイトの持ち主の自己申告という点でkeywordsメタタグと同じだとRedditで書きました（[Search Engine Journal](https://www.searchenginejournal.com/google-says-llms-txt-comparable-to-keywords-meta-tag/544804/)、2025年4月17日）。2026年6月にはGoogleのポッドキャストで、自己申告なのでAIがサイト同士を比べる材料にはならず、すでにサイトに来ている自動の仕組みには役立つかもしれないと話しています（[同](https://www.searchenginejournal.com/googles-mueller-says-llms-txt-cant-help-llms-differentiate-sites/566027/)、2026年6月15日）。

### OpenAIなど3社の公式ページ

ほかのAIの会社のクローラーの説明ページ（2026年10月26日時点）も見ます。

| 会社 | クローラーの公式ページ | llms.txtを読むという記載 | 自社の資料のllms.txt |
|---|---|---|---|
| OpenAI | [Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots) | 無い。管理はrobots.txt | [あり](https://developers.openai.com/llms.txt) |
| Anthropic | [クローラーのヘルプ](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) | 無い。robots.txtの指示を守ると記載 | [あり](https://platform.claude.com/llms.txt) |
| Perplexity | [Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) | 無い。管理はrobots.txt | [あり](https://docs.perplexity.ai/llms.txt) |

**3社とも自社の開発者向け資料にはllms.txtを置いていますが、自社のクローラーがほかのサイトのllms.txtを読むとはクローラーの公式ページには書いていません。**「AIの会社も使っている」という説明は、置く側としての話です。

### AIのクローラーは読みに来るか

Ahrefsは2026年6月15日に、自社の解析ツールを入れた137,210ドメインのサーバーへのリクエストを数えた[調査](https://ahrefs.com/blog/llmstxt-study/)を出しました。2026年5月に流入があったドメインが対象で、llms.txtを置いていたのは約38,000（28%。技術に詳しい利用者が多いので上限の値）です。**そのうち97%のファイルは、5月の1か月に人にもボットにも1回も取得されませんでした。**

<figure class="post-figure"><img src="/media/images/llms-txt-structured-data/llt_01_who.png" alt="llms.txtを誰が取りに来たか。Ahrefsの調査で、置いた約3.8万ドメインの97%は2026年5月に取得ゼロ。取得のうちAIのボットは19.5%で、内訳はAIエージェント10.5%、学習用5.3%、利用者の操作用2.5%、AI検索用1.1%" loading="lazy"></figure>

取得があった残り3%（約1,100ドメイン・約2.2万件）の内訳では、96%がボットでした。ただし77%はAIと関係のないボットで、SEOの監査ツール（21.7%）や技術の調査ツールが目立ちます。AIのボットは合計19.5%で、AI検索の回答のためにページを取るボット（OAI-SearchBot・PerplexityBotなど）は取得全体の1.1%にとどまりました。単体ではGPTBotが最も多く、次がAnthropicのコーディング用エージェントClaude-Codeです。

置いていないサイトの`/llms.txt`（404）に、AIのボットは1件も来ていませんでした。**AIは無いファイルを探しに来ず、リンクや利用者の指示で場所を知ったときに取りに来る**、とAhrefsは読んでいます。取得した数は読んで使ったかを示さないため、どの数字も上限だという断りも付いています。

### 引用との関係を調べた調査

SE Rankingは約30万ドメインを調べ、llms.txtを置いていたのは10.13%で、統計と機械学習のどちらでもAIに引用される回数との関係は見られなかったと[報告](https://seranking.com/blog/llms-txt/)しました（2026年10月15日更新の記事）。モデルからllms.txtの有無を外すと、予測の精度がむしろ上がったとも書いています。

## llms.txtの書き方

仕様で必須なのは1行目の見出しだけです。あとは決まった順番で、概要・補足・リンクの一覧を並べます。

1. H1（`#`）でサイト名や会社名
2. 引用（`>`）で短い概要
3. 見出しを使わない段落で補足
4. H2（`##`）で区切ったリンクの一覧。1行に`[ページ名](URL): 短い説明`

### 最小の例

BtoBの会社のサイトなら、次のくらいの長さで足ります。

    # 株式会社サンプル

    > 製造業向けの生産管理システムを開発・販売している会社です。導入は全国に対応しています。

    導入の相談は問い合わせフォームで受け付けています。料金は個別見積もりです。

    ## サービス

    - [生産管理システム](https://example.com/service/): 主な機能と対応する業種
    - [料金と導入の流れ](https://example.com/price/): 見積もりの考え方と導入までの期間

    ## 会社

    - [会社概要](https://example.com/company/): 所在地・設立・代表者
    - [導入事例](https://example.com/case/): 業種別の事例

    ## Optional

    - [お知らせ](https://example.com/news/)

**リンクの先は人が読むページそのままでかまいません。**第2版はページのMarkdown版を用意する形も勧めていますが、llms.txt自体はそれが無くても書けます。「Optional」は後回しでよいリンクを置く慣習の見出しで、第2版では特別な意味が無くなりました。作ったらllms.txtだけを渡したAIに自社のことを質問して確かめるよう、提案のページは勧めています。

### 置き場所と確かめ方

ファイル名は`llms.txt`で、サイトのルートに置きます。置いたらブラウザで`https://自社のドメイン/llms.txt`を開き、文字化けせずテキストのまま表示されるかを見てください。ターミナルが使えるなら`curl -I https://自社のドメイン/llms.txt`で、状態コードが200で返るかを確かめられます。

AIはリンクや利用者の指示で場所を知ったときに取りに来る、とAhrefsは見ています。**置くなら、HTMLの`head`に`<link rel="describedby" href="/llms.txt">`のように場所を書いておくと、第2版の仕様に沿った知らせ方になります。**CDNのボット対策でAIのユーザーエージェントを止めていると、置いても届きません。

### WordPressやWixで作る場合

WordPressなら、SEOのプラグインの[Yoast SEO](https://yoast.com/features/llms-txt/)と[AIOSEO](https://aioseo.com/features/llms-txt/)にllms.txtを作る機能があります。Yoast SEOは主なページを自動で選んで作り、更新も自動で続けます。[Wix](https://support.wix.com/en/article/understanding-your-sites-llmstxt-file)はサイトごとに自動で作り、管理画面で中身を見て直せますが、一度直すと自動の更新は止まり、初期の状態に戻すと自動の更新も再開します。

自動で作られたファイルも、公開前に中身を読むようにしてください。終わったサービスや古い料金のページが並んでいれば、それがそのままAIへの案内になります。

## 置くかどうかの決め方

ファイル自体は数十行で書けるため、迷う理由は作る手間ではありません。決めることは**誰に読ませたいのかと、内容を誰が最新に保つのか**の2つです。

### 置く意味があるサイト

調査のAIのボットの中で最も多かったのはClaude-Codeなどを含むAIエージェントの区分（取得全体の10.5%）でした。そこから考えると、置く意味の大きさはサイトの種類で分かれます。

<figure class="post-figure"><img src="/media/images/llms-txt-structured-data/llt_02_decide.png" alt="llms.txtを置くかの決め方。APIや製品の技術資料があるなら置く価値がある。AIエージェントに予約や購入をさせたいなら試す価値がある。AI検索に社名を出したいだけなら先に本文と測り方を整える" loading="lazy"></figure>

| サイトの種類 | 期待できること | 判断 |
|---|---|---|
| APIや製品の技術資料がある | コーディング用のAIが資料を探しやすくなる | 置く価値がある |
| AIエージェントに予約・購入・問い合わせをさせたい | サイトに来たエージェントの道案内になる | 試す価値がある |
| AI検索に社名やサービス名を出したい | 公式・調査ともに効果の裏づけが無い | 先に本文と測り方 |

商材の単価が高いBtoBの会社がAI検索対策として検討するなら、3つ目に当たります。この場合、llms.txtを置いたことを成果として報告されても、AIの回答に出るかどうかは変わらないと考えておくのが安全です。

### 工数と管理で決めること

置くと決めたら、robots.txtと同じくサイトの設定ファイルとして扱います。AIエージェントはこのファイルを信用して読む作りなので、書き換えられたファイルや古いファイルはエージェントを誤った先へ導く、とAhrefsは注意しています。同じ調査ではllms.txtを悪意ある指示を入れる場所として調べる研究用のボットも見つかりました。

- 編集できる人を決め、変えた履歴を残す
- 中身はページ名・リンク・短い説明だけにし、命令のような文を書かない
- リンクは自社が管理するページに限る
- サービスや料金を変えたら、同じ日にllms.txtも直す

**制作会社に頼むなら、設置の費用より誰がいつ更新するかを契約の前に決めておきましょう。**

## 構造化データの扱い

構造化データはページの中身（会社名・記事の著者・パンくずなど）を検索エンジンが読める形で書き足す仕組みです。Googleの最適化ガイドによれば、生成AI検索に構造化データは必要なく、特別なschema.orgのマークアップを足す必要もありません。そのうえで、リッチリザルトの対象になる助けになるため、SEO全体の一部として使い続けるよう勧めています。

[構造化データの説明ページ](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data?hl=ja)（2025年12月18日更新）が勧める形式は、ほとんどの場合JSON-LDです。数を増やすより、完全で正確なプロパティを優先するよう求めています。[AI機能とウェブサイト](https://developers.google.com/search/docs/appearance/ai-features?hl=ja)のページにも、構造化データをページに表示されるテキストと一致させる項目がありました。**会社のサイトなら、組織・記事・パンくずリストのように公式の一覧にある種類を、表示している中身と同じ内容で入れておけば足ります。**

## 会社として先にやること

llms.txtも構造化データも、AIに読まれる本文がある前提の補助です。AI検索に名前を出したい会社が先に手を付けるのは次の順番です。

<figure class="post-figure"><img src="/media/images/llms-txt-structured-data/llt_03_first.png" alt="AI検索に向けて会社が先にやる順番。AIのクローラーを止めていないか確かめる、答えを本文のテキストで書く、Search Consoleで生成AIでの表示を測る、実際の質問でAIの回答を見る" loading="lazy"></figure>

1. **AIのクローラーを止めていないか確かめる**。robots.txtとCDNの設定を見る（[AIクローラーの判断と書き方](/media/ai-crawler-robots/)）
2. **答えを本文のテキストで書く**。AIによる概要やAIモードにリンクとして出るには、インデックスに登録され、スニペットが表示できることが条件だとGoogleは書いています。比較の軸・費用の目安・事例を画像の中だけに置かない（[AIによる概要に引用されるには](/media/cited-by-ai-overviews/)）
3. **Search Consoleで測る**。[生成AIパフォーマンスレポート](https://support.google.com/webmasters/answer/16984139?hl=ja)で、AIによる概要とAIモードでの表示をページごとに見る
4. **実際の質問でAIの回答を見る**。顧客が聞きそうな質問をChatGPT・Gemini・AIモードに入れ、自社の名前と根拠のページが出るかを定期的に記録する

全体の考え方は[GEO対策とは](/media/geo-taisaku/)と[LLMOとは](/media/what-is-llmo/)に書いています。

## よくある質問

### Q. llms.txtを置くとChatGPTに引用されやすくなりますか？

裏づけはありません。OpenAIのクローラーの公式ページにllms.txtを読むという記載は無く、Ahrefsの調査でもAI検索のボットの取得は取得全体の1.1%でした。SE Rankingの約30万ドメインの分析でも、引用される回数との関係は見られていません。

### Q. Google検索のAIによる概要やAIモードにllms.txtは効きますか？

効きません。Googleの最適化ガイドは、生成AI機能を含むGoogle検索はllms.txtを使わず、置いても表示や順位に影響しないと書いています。

### Q. llms.txtとrobots.txtのどちらでAIのクローラーを止めますか？

robots.txtです。OpenAI・Anthropic・Perplexityはどれも、クローラーの管理をrobots.txtで行うと公式ページに書いています。llms.txtにはアクセスを止める働きがありません。ただし、利用者の質問を受けてその場でページを開く仕組み（ChatGPT-User・Perplexity-User）は、robots.txtの指示が当てはまらない場合があるとOpenAIとPerplexityは書いています。

### Q. llms.txtとllms-full.txtの違いは何ですか？

llms-full.txtはリンク先の本文まで1つにまとめたファイルで、[Mintlify](https://www.mintlify.com/docs/ai/llmstxt)のような文書の公開ツールがllms.txtと一緒に作ります。llmstxt.orgの第2版の仕様にはllms-full.txtの定めが無く、仕様で決まっているのはllms.txtだけです。

### Q. WordPressでllms.txtを作るにはどうしますか？

Yoast SEOやAIOSEOのllms.txtの機能を使うか、テキストファイルを作ってサイトのルートに置きます。プラグインで作った場合も、並んだページと説明が今のサービスに合っているかを公開前に読んでください。

### Q. Claudeのコーディング用エージェントはllms.txtを読みますか？

Ahrefsの調査でClaude-Codeは、GPTBotに次いでllms.txtを多く取得していました。ただし、取得した中身をどう使っているかまでは調査で分かっていません。

## 出典

- Jeremy Howard「[The /llms.txt file, v2](https://llmstxt.org/)」2024年9月3日公開・2026年8月10日更新（2026年10月26日取得）
- llmstxt.org「[Changes](https://llmstxt.org/changes.html)」（同）
- Google 検索セントラル「[Google 検索の生成 AI 機能向けにウェブサイトを最適化する](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide?hl=ja)」2026年10月9日更新（同）
- Google 検索セントラル「[AI 機能とウェブサイト](https://developers.google.com/search/docs/appearance/ai-features?hl=ja)」2025年12月31日更新（同）
- Google 検索セントラル「[構造化データ マークアップとは](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data?hl=ja)」2025年12月18日更新（同）
- Chrome for Developers「[llms.txt](https://developer.chrome.com/docs/lighthouse/agentic-browsing/llms-txt?hl=ja)」2026年5月5日更新（同）
- OpenAI「[Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)」（同）
- Anthropic「[Does Anthropic crawl data from the web, and how can site owners block the crawler?](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)」（同）
- Perplexity「[Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)」（同）
- Ahrefs「[We Analyzed 137K Sites: 97% of llms.txt Files Never Get Read](https://ahrefs.com/blog/llmstxt-study/)」2026年6月15日（同）
- SE Ranking「[LLMs.txt: Why Brands Rely On It and Why It Doesn't Work](https://seranking.com/blog/llms-txt/)」2026年10月15日更新（同）
- Search Engine Journal「[Google Says LLMs.Txt Comparable To Keywords Meta Tag](https://www.searchenginejournal.com/google-says-llms-txt-comparable-to-keywords-meta-tag/544804/)」2025年4月17日（同）
- Search Engine Journal「[Google's Mueller Says llms.txt Can't Help LLMs Differentiate Sites](https://www.searchenginejournal.com/googles-mueller-says-llms-txt-cant-help-llms-differentiate-sites/566027/)」2026年6月15日（同）
- Mintlify「[llms.txt](https://www.mintlify.com/docs/ai/llmstxt)」（同）
- Search Console ヘルプ「[生成 AI パフォーマンス レポート（検索）](https://support.google.com/webmasters/answer/16984139?hl=ja)」（同）
