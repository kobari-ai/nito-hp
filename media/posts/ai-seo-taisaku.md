---
title: 【2026年11月】AI SEO対策とは？従来のSEOとの違いと会社が足すこと・効かない手
date: 2026-10-31
category: AI検索対策
description: AI SEO対策とは何かを2つの意味に分けて解説。Googleの公式ガイドで確かめた従来のSEOで変わらないこと・変わること、SEOの作業ごとの続ける・足す・やめるの棚卸し、効かない手と測り方まで。
keyword: ai seo対策
cover_tag: 解説
cover_headline: AI SEO対策とは
cover_sub: 今のSEOに足すこと
cta: llmo
---

Googleは2026年5月15日、検索セントラルに「[Google 検索の生成 AI 機能向けにウェブサイトを最適化する](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide?hl=ja)」というガイドを公開しました。生成AI検索でもSEOは有効かという問いに、ガイドは「手短に言えば、有効です」と答えています。

SEOを担当していて、AIの時代に今のSEOのままでよいのか、何を足せばよいのかを社内で聞かれている方に向けて書きました。従来のSEOの作業ごとに、続けるもの・足すもの・やめるものを公式の文書で分けます。

:::takeaways
- AI SEO対策には**AIを使ってSEOをする意味と、AI検索の時代のSEOという意味**の2つがある。この記事は後者が主
- Googleは生成AI向けの最適化も**SEOであることに変わりはない**と書き、llms.txt・文章の細切れ・AI向けの書き換え・生成AI用の構造化データは要らないとしている
- 足すのはGoogle以外の入口（ChatGPT・Perplexity・Copilot）のクローラーの確認と、**AIの回答そのものを記録して測る作業**
:::

## AI SEO対策とは

「AI SEO」で検索すると、上位の記事は大きく2つに分かれます。1つ目はAIのツールでキーワードの調査や構成案・記事の下書きを作り、SEOの作業を速くする話です。2つ目はGoogleのAIによる概要・AIモードや、ChatGPT・Perplexityの回答に自社のページが引用され、社名が挙がるようにする話で、AIO対策・LLMO・GEOとも呼ばれます。呼び名の成り立ちの違いは[GEO対策とは？LLMO・AIOとの違い](/media/geo-taisaku/)に書きました。

**この記事が主に扱うのは2つ目で、1つ目はAIで書いた記事をGoogleがどう扱うかの1節だけにします。** ツールの使い方を探している場合は、ほかの記事のほうが役に立つはずです。AIの回答に自社を出す取り組みの全体の進め方は[AIO対策とは？やり方の5手順](/media/aio-taisaku/)にまとめています。

<figure class="post-figure"><img src="/media/images/ai-seo-taisaku/aiseo_01_two.png" alt="AI SEO対策という言葉の2つの意味を縦に並べた図。1つ目はAIのツールでキーワード調査や記事の下書きをするAIを使ったSEO。2つ目はAIによる概要やChatGPTの回答に自社が出るようにするAI検索の時代のSEO" loading="lazy"></figure>

## 従来のSEOで変わらないこと

「AIに出るにはSEOとは別の新しい対策が要る」という提案を受けた方もいるかもしれません。Googleの最適化ガイドは、AIによる概要やAIモードが「コアとなる検索ランキングと品質システムに根差している」ため、SEOのベストプラクティスは引き続き有効だと書いています。AIの回答は検索のランキングの仕組みでインデックスから関連するページを取り出し、それを材料に組み立てる作り（検索拡張生成、RAG）だからです。

**Google検索のAI機能に出る土台は、インデックスに登録されてスニペットが表示されるという従来の条件そのものです。** 検索セントラルの「[AI 機能とウェブサイト](https://developers.google.com/search/docs/appearance/ai-features?hl=ja)」も、表示されるための「追加の要件はなく、別途特別な最適化を行う必要もありません」と書いています。最適化ガイドはこれに加えて、Search Consoleの検索の生成AI機能にサイトが含まれていることを条件に挙げています。

<figure class="post-figure"><img src="/media/images/ai-seo-taisaku/aiseo_04_ai-optimization.png" alt="Googleの生成AI機能向けの最適化ガイド。生成AI検索でも引き続きSEOは有効かという問いに、手短に言えば有効で、生成AI機能はコアとなる検索ランキングと品質システムに根差していると書かれている" loading="lazy"><figcaption>Google 検索の生成 AI 機能向けにウェブサイトを最適化する（Google 検索セントラル、2026年10月31日）</figcaption></figure>

中身の評価の考え方も変わっていません。ガイドは誰でも書ける一般論の例に「初めて住宅を購入する人向けの 7 つのヒント」を挙げ、独自の経験や専門の見解に基づく内容を勧めています。AIは複数のページを見比べて答えを作るため、ほかのページを言い換えただけの記事は材料に選ばれる理由が薄くなります。SEOで言われてきた独自性と、AIに引用される条件はここで重なるわけです。

ガイドはクエリ ファンアウトという仕組みも説明しています。元の問いに関連する複数の検索を同時に行う仕組みで、例では「雑草だらけの芝生を直す方法」に「芝生に最適な除草剤」などの検索が加わります。狙った語そのものでなく周りの問いで拾われることがあるので、1つのテーマを深く扱ったページの価値は従来より増すと考えられます（この点はガイドの説明からの推測です）。

## AI検索で変わること

変わるのは主に2つで、Google以外に入口が増えることと、見る数字が順位から回答そのものに広がることです。

### Google以外の入口

ChatGPTの検索・Perplexity・MicrosoftのCopilotはGoogleとは別の仕組みで検索するため、Search Consoleの設定や数字はそこまで届きません。OpenAIのヘルプ「[Searching the web with ChatGPT](https://help.openai.com/en/articles/9237897-chatgpt-search)」によると、ChatGPTは外部の検索の提供元と組み、質問を検索向けの語に書き換えて送ることがあります。提供元のプライバシーの案内に挙がるのはMicrosoftとShopifyで、Bingが提供元の1つである強い示唆にはなるものの、Bingの索引に載ることが条件とは書かれていません。同じヘルプが載る条件として挙げるのは、OAI-SearchBotの許可と、ホストやCDNがOpenAIのIPアドレスからの通信を通すことです。

OpenAIの[クローラーの説明](https://developers.openai.com/api/docs/bots)によると、OAI-SearchBotを止めたサイトはChatGPTの検索の回答に出ません。学習用のGPTBotとは別々の設定です。Perplexityも[PerplexityBot](https://docs.perplexity.ai/guides/bots)を検索結果にサイトを出すためのクローラーと説明し、robots.txtでの許可を勧めています。CopilotはBingの検索の上に作られており、Bing Webmaster Toolsで引用の数が見られます。

<figure class="post-figure"><img src="/media/images/ai-seo-taisaku/aiseo_02_gates.png" alt="AI検索の入口ごとに確かめる所を縦に並べた図。GoogleのAIによる概要とAIモードはインデックス登録とSearch Consoleの検索の生成AI設定、ChatGPTの検索はOAI-SearchBotの許可、PerplexityはPerplexityBotの許可、CopilotはBingの索引" loading="lazy"></figure>

**robots.txtで許可していても、CDNやセキュリティの設定でAIのクローラーが止まっていることがあります。** Googleの「AI 機能とウェブサイト」も、robots.txtに加えてCDNやホスティングでクロールが許可されているかを確かめるよう書いています。どのクローラーが学習用でどれが検索用か、止めると何が起きるかは[AIクローラーをrobots.txtで止めるかの判断](/media/ai-crawler-robots/)、ChatGPTの条件の細部は[ChatGPT検索で引用元に出る条件](/media/chatgpt-search-citation/)が詳しいです。

GoogleのAIモードもGoogle検索の一部で、公式の条件はAIによる概要と同じページにあります。AIによる概要に絞った公式の条件は[AI Overview（AIによる概要）対策とは](/media/cited-by-ai-overviews/)にまとめました。
<!-- LINK: ai-mode-seo が公開されたら、この段落に「AIモードに絞った話は〜」の1文とリンクを足す -->

### Search Consoleの設定とレポート

2026年8月31日から、Search Consoleに[検索の生成 AI 設定](https://support.google.com/webmasters/answer/16908024?hl=ja)が全サイトで入りました。除外を選んだサイトはAIによる概要・AIモードに出なくなります。既定は含める側なので、**誰かが除外に切り替えていないかを1度だけ確かめておけば足ります。** 同じ日にはAIによる概要とAIモードで自社のページへのリンクが表示された回数を出す[生成 AI パフォーマンス レポート](https://support.google.com/webmasters/answer/16984139?hl=ja)も全サイトに広がりました。

### 見る数字

従来のSEOは語ごとの順位とクリックで成果を見てきました。AIの回答は同じ問いでも聞くたびに変わり、社名が文中に出てもリンクが押されないことが多いため、順位を計るツールだけでは追えません。問いを決めてAIに聞き、社名が出たか・どう紹介されたか・どのページが引用元に付いたかを記録する作業が新しく要ります。

## SEO作業の棚卸し

今のSEOの作業を並べ、AI検索の時代にどう扱うかを公式の文書に沿って分けると次のようになります。

| 今のSEOの作業 | AI検索の時代の扱い | 根拠 |
|---|---|---|
| キーワード調査 | 続ける。見込み客がAIに聞く問いの書き出しを足す | ガイドはロングテールの言い換えを全部押さえる心配は要らないと書く |
| 記事・ページの制作 | 続ける。独自の経験やデータを厚くする | ガイドの独自の中身の勧め |
| 言い換えごとのページ量産 | やめる | 操作が主な目的なら大量生成されたコンテンツの不正使用 |
| 内部リンク・技術の整備 | 続ける | 「AI 機能とウェブサイト」のベストプラクティス |
| 構造化データ | リッチリザルトのために続ける。AI用の特別なものは要らない | ガイド |
| llms.txt | Google検索のためには要らない。ほかのサービス用に置くのは自由 | ガイド |
| robots.txt・CDN | Googlebotに加えOAI-SearchBot・PerplexityBot・bingbotを確かめる | OpenAI・Perplexityの説明 |
| 被リンク・言及の獲得 | 不自然な言及は集めない。第三者が書ける事実を出す | ガイド |
| 順位の計測 | 続ける。AIの回答の記録とSearch Consoleのレポートを足す | 生成AIパフォーマンスレポート |
| Googleビジネスプロフィール・Merchant Center | 最新に保つ | ガイド |

**作業の大半は続けるもので、足すのは入口の確認と回答の記録、やめるのは問いの言い換えごとのページ量産です。** ガイドも結びで明示的なSEOをまったく行わなくても多くのコンテンツが成功していると書き、ガイドの全項目をやる必要はないと断っています。

<figure class="post-figure"><img src="/media/images/ai-seo-taisaku/aiseo_03_sort.png" alt="SEOの作業を3つに分けた図。続けるのはキーワード調査、独自の中身の制作、内部リンクと技術の整備、構造化データ。足すのはAIのクローラーとCDNの確認、AIに聞く問いの記録、Search Consoleの生成AIの設定。やめるのは言い換えごとのページ量産と不自然な言及集め" loading="lazy"></figure>

## AIで書いた記事のGoogleの扱い

「AIで書いた記事はGoogleに嫌われる」という説明と「AIで書いても問題ない」という説明が、上位の記事に両方並んでいるのが現状です。Googleの「[ウェブサイトで生成 AI によるコンテンツを使用するための Google 検索のガイダンス](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content?hl=ja)」は、生成AIはトピックを調べるときなどに便利だとしたうえで、ユーザーにとっての価値を付加することなく大量のページを生成すると、大量生成されたコンテンツの不正使用に関するスパムポリシーに「違反してしまう可能性があります」と書いています。

<figure class="post-figure"><img src="/media/images/ai-seo-taisaku/aiseo_05_genai-content.png" alt="Googleの生成AIによるコンテンツを使用するためのガイダンス。生成AIツールなどでユーザーにとっての価値を付加することなく大量のページを生成すると、大量生成されたコンテンツの不正使用に関するスパムポリシーに違反してしまう可能性があると書かれている" loading="lazy"><figcaption>ウェブサイトで生成 AI によるコンテンツを使用するための Google 検索のガイダンス（Google 検索セントラル、2026年10月31日）</figcaption></figure>

[スパムに関するポリシー](https://developers.google.com/search/docs/essentials/spam-policies?hl=ja)の側は、大量生成されたコンテンツの不正使用を「検索ランキングの操作を主な目的として大量のページを生成すること」と定め、価値のないコンテンツを「その作成方法は問わず」大量に作ることだと書いています。**Googleが問題にするのはAIで書いたかどうかではなく、価値を足さずに大量に作ることです。** 人が書いても同じ扱いになり、AIで書いても価値があれば当てはまりません。

ガイダンスは公開前に人の手で事実を確かめることも求めています。対象は本文だけでなく、title・メタディスクリプション・構造化データ・画像の代替テキストまで含みます。AIで記事を作る会社なら、本数の目標より先に誰が事実を確かめて公開を決めるかを決めておくと、このガイダンスに沿った運用になるでしょう。

<figure class="post-figure"><img src="/media/images/ai-seo-taisaku/aiseo_06_spam-policy.png" alt="Googleのスパムに関するポリシーの大量生成されたコンテンツの不正使用の節。検索ランキングの操作を主な目的として大量のページを生成することで、価値のないコンテンツをその作成方法は問わず大量に作ることと書かれている" loading="lazy"><figcaption>Google 検索のスパムに関するポリシー（Google 検索セントラル、2026年10月31日）</figcaption></figure>

## 今のSEOに足す5つの手順

SEOの担当にとって新しいのは最初の2つで、残りの3つは今の作業の延長です。

1. **今の答えを測る**: 見込み客がAIに聞きそうな問いを20〜30問書き出し、ChatGPT・Gemini・Perplexity・GoogleのAIモードに日を変えて2回以上聞く
2. **引用元を読む**: 回答に付いたURLを、自社・競合・比較サイト・口コミに分けて数える
3. **ページを直す**: 自社が材料に使われていない問いに答えるページを直すか足す
4. **社外の情報をそろえる**: 比較サイトやGoogleビジネスプロフィールの誤りを直す
5. **同じ問いで測り直す**: 直した日と箇所を残し、月に1回測る

**キーワードの順位表の横に、問いごとのAIの回答の記録を置くのが、今のSEOに足す作業の中心です。** 各手順の進め方と引用元の種類ごとに次の手を決める表は[AIO対策のやり方5つの手順](/media/aio-taisaku/)に書いています。

## やっても効かない手・危うい手

AI検索向けとして売られる手のうち、Googleの公式の文書と照らすと効きにくいか、ポリシーに触れるおそれがあるものを並べます。

- AIで記事を大量に書いて公開する
- 問いの言い換えごとに薄いページを作る
- llms.txtを置いて終える
- FAQの構造化データを足すだけで終える
- AIに読ませるつもりで文章を細かく切る
- 業者に頼んで社外の言及や口コミを作らせる
- 「Google内部の指標を使える」とうたうツールに頼る

最適化ガイドに書かれているのは、Google検索はllms.txtを使わない・生成AI検索に構造化データは必要ない・コンテンツを細かく分割する必要はない、の3点です。不自然な言及を探すことは「実際にはそれほど役に立ちません」とし、外部のツールは「Google 内部のランキング システムや AI システムにアクセスすることはできません」と断っています（日本語版の本文はこの言及を「不正確な」と訳していますが、英語版は inauthentic で、日本語版のまとめの節の訳どおり「不自然な」の意味です）。

ただしこれらはGoogle検索についての記述です。BingはAI Performanceの発表で、見出し・表・FAQの節が要点を見つけやすくすると書いています。**Googleが要らないとするのは形式を足すだけの手で、読者に分かりやすく整えることまでは否定していません。** ChatGPTやPerplexityで何が効くかは両社とも細かく書いていないので、自社の問いで測って確かめます。llms.txtを置くかの判断は[llms.txtとは](/media/llms-txt-structured-data/)で扱っています。

## 効いたかの測り方

入口ごとに見られる数字が違うため、1つの画面では足りません。

| 入口 | 見る場所 | 分かること |
|---|---|---|
| AIによる概要・AIモード | Search Consoleの生成AIパフォーマンスレポート | リンクが表示された回数（ページ・国・デバイス・日付別。検索語は無い） |
| Copilotなど | Bing Webmaster ToolsのAI Performance | 引用された数とページ、AIが取りに行った語句の標本 |
| ChatGPT・Perplexity | GA4の参照元と、自分で聞いた回答の記録 | リンクを押して来た数と、社名の出方 |
| すべて | 問い合わせのフォームや商談で聞く認知経路 | AIで知った人の数 |

AIの回答で社名を知った人がリンクを押さず、あとで社名を検索して来ると、GA4にはAIから来たと残りません。**nitoが支援するSaaS企業では、同じ期間のGA4でAI経由として記録された会員登録は全体の0.007%で、会員登録時のアンケートでは26.7%がAI検索で知った・比べたと答えていました。** 参照元の数字だけで判断せず、問い合わせの入口で何で知ったかを聞く仕組みを足すのが確実です。GA4の設定は[AI検索対策の効果はどう測る？](/media/ai-search-measurement/)、Search Consoleのレポートの見方は[サーチコンソールでAIモード・AIによる概要の表示を見る方法](/media/gsc-ai-mode/)にあります。

## 会社が決めること

AI SEO対策は今のSEOと作業の大半が重なるため、新しい部署や大きな予算を立てる前に決めておくことがあります。

### 誰がAIの回答を見るか

順位の報告を作っている担当が、問いごとの回答の記録も持つのが無理のない形です。問いの案はマーケ担当が作り、実際の商談で聞かれる言い方かを営業が確かめます。問いとAIを途中で入れ替えると前の月と比べられなくなるので、最初に固定しましょう。

### 外の提案を見る物差し

AEO・GEO・AI SEOの名前で、新しい施策の提案を受ける機会が増えました。Googleは[サードパーティの SEO に関するガイダンス](https://developers.google.com/search/docs/fundamentals/third-party-seo?hl=ja)で、外部の助言を公式のガイドに照らして評価するよう求めています。**提案の中の今のSEOと同じ作業と、回答の記録のように新しく足す作業を分けて見積もってもらうと比べやすくなります。**

### AIで書くときの社内の決まり

AIで記事を作るなら、事実を確かめる人と公開を決める人を先に決めておきます。本数の目標を先に置くと、価値を足さない量産に寄りがちです。

## よくある質問

### Q. AI SEO対策と従来のSEO対策は何が違いますか？

Googleの最適化ガイドによると、Google検索の観点では生成AI向けの最適化もSEOであることに変わりはありません。違いはChatGPT・Perplexity・Copilotといった入口が増えることと、順位に加えてAIの回答で社名が出たか・どう紹介されたかを見ることです。

### Q. AI SEO対策にllms.txtは必要ですか？

Google検索については必要ありません。最適化ガイドはGoogle検索がllms.txtを使わないと書いています。ほかのサービスのために置くのは問題ないとも書いていますが、ChatGPTやPerplexityが使うかは両社の公式ページに書かれていません。

### Q. AIで書いた記事はGoogleで不利になりますか？

AIで書いたこと自体を理由にするとは書かれていません。スパムポリシーが問題にするのは検索順位の操作を主な目的に価値のないページを大量に作ることで、作成方法は問わないと書かれています。公開前に人が事実を確かめることがガイダンスで求められています。

### Q. ChatGPTに自社を出すにはBingへの登録が必要ですか？

OpenAIの公式ページに、Bingへの登録が条件とは書かれていません。載る条件として書かれているのは、OAI-SearchBotをrobots.txtで許可し、ホストやCDNがOpenAIのIPアドレスからの通信を通すことです。

### Q. AI SEO対策の効果はSearch Consoleで見られますか？

AIによる概要とAIモードでリンクが表示された回数は、生成AIパフォーマンスレポートで見られます。検索語ごとの内訳は無く、ChatGPTやPerplexityの分は入りません。問いごとの出方を見る手段は、自分でAIに聞いて記録するか測るツールを使うかの2つです。

## 出典

- Google 検索セントラル「[Google 検索の生成 AI 機能向けにウェブサイトを最適化する](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide?hl=ja)」日本語版 2026年10月30日更新（2026年10月31日取得）。英語版「[Optimizing your website for generative AI features on Google Search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide?hl=en)」（同）
- Google 検索セントラル ブログ「[Google 検索の生成 AI 向けに最適化するための新しいリソース](https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing?hl=ja)」2026年5月15日（同）
- Google 検索セントラル「[AI 機能とウェブサイト](https://developers.google.com/search/docs/appearance/ai-features?hl=ja)」2025年12月31日更新（同）
- Google 検索セントラル「[ウェブサイトで生成 AI によるコンテンツを使用するための Google 検索のガイダンス](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content?hl=ja)」2026年10月6日更新（同）
- Google 検索セントラル「[Google 検索のスパムに関するポリシー](https://developers.google.com/search/docs/essentials/spam-policies?hl=ja)」2026年9月2日更新（同）
- Google 検索セントラル「[サードパーティの SEO ツール、サービス、アドバイスの使用に関する Google 検索のガイダンス](https://developers.google.com/search/docs/fundamentals/third-party-seo?hl=ja)」（同）
- Google 検索セントラル ブログ「[Search Console に検索の生成 AI のパフォーマンス レポートを導入](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports?hl=ja)」2026年6月3日（同）
- Search Console ヘルプ「[生成 AI パフォーマンス レポート（検索）](https://support.google.com/webmasters/answer/16984139?hl=ja)」（同）
- Search Console ヘルプ「[検索の生成 AI 設定](https://support.google.com/webmasters/answer/16908024?hl=ja)」（同）
- OpenAI Help Center「[Searching the web with ChatGPT](https://help.openai.com/en/articles/9237897-chatgpt-search)」（Internet Archiveの2026年10月30日の保存版で確認）
- OpenAI「[Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)」（2026年10月31日取得）
- Perplexity「[Perplexity Crawlers](https://docs.perplexity.ai/guides/bots)」（同）
- Microsoft Bing Webmaster Blog「[Introducing AI Performance in Bing Webmaster Tools Public Preview](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)」2026年2月10日（同）
