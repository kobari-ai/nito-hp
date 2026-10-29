---
title: 【2026年10月】AEO対策とは？SEO・AIO・GEOとの違いとGoogleの見解・FAQの扱い
date: 2026-10-30
category: AI検索対策
description: AEO対策とは何かを、Googleの公式ガイドとschema.orgで確認。SEO・AIO・GEO・LLMOとの違い、AEOのハックの多くは効果がないというGoogleの記述、FAQと構造化データの今の扱い、会社がやることまで。
keyword: aeo対策
cover_tag: 解説
cover_headline: AEO対策とは
cover_sub: SEO・AIO・GEOとの違いと公式見解
cta: llmo
---

Googleは2026年5月に公開した生成AI機能向けの公式ガイドで、AEO・GEOとして提案される「ハック」の多くは効果がなく、Google検索の実際の仕組みにも支えられていないと書いています。

AEO対策の提案を受けて、SEOやAIO対策と何が違うのか、社内で説明を求められている方に向けた記事です。何が同じで何が違うか、FAQや構造化データがどこまで効くか、会社がやることを公式の文書で確かめて書きます。

:::takeaways
- AEOはAnswer Engine Optimizationの略です。**SEO・AIO・GEO・LLMOとやることはほぼ同じで、違うのは呼び名と出どころです**
- Googleの公式ガイドは、**生成AI向けの最適化もGoogle検索から見ればSEOであり、AEO・GEOの「ハック」の多くは効果がない**と書いています
- **FAQのリッチリザルトは2026年5月7日にGoogle検索での表示が終わりました。** FAQの本文は読者のために残してよく、Google検索のためにFAQPageのマークアップを新しく足す理由はなくなりました
:::

## AEO対策とは

AEO（Answer Engine Optimization）は、日本語で回答エンジン最適化と訳されます。利用者の質問に答えを直接返す仕組みの中で、自社の情報が答えの材料に使われるよう整える取り組みです。**今は主に、ChatGPTやGoogleのAIによる概要のような生成AIの回答に自社の情報を出す意味で使われています。**

### 回答エンジンとは

当初、主にGoogleの強調スニペットや音声アシスタントを念頭に使われていました。強調スニペットは検索結果の上に答えの抜き出しを出す枠で、音声アシスタントは1つの答えだけを読み上げます。リンクが10本並ぶ検索と違い、答えに選ばれるかどうかが分かれ目になるため、検索エンジン最適化とは別の呼び名が付きました。

その後、生成AIが答えを文章で組み立てるようになり、回答エンジンの中心はChatGPT・Gemini・Perplexity・GoogleのAIモードに移っています。

<figure class="post-figure"><img src="/media/images/aeo-taisaku/aeo_01_engines.png" alt="AEOが対象にしてきた回答の場を縦に並べた図。Googleの強調スニペット、音声アシスタント、生成AIの回答。どれも答えを1つに絞って返す" loading="lazy"></figure>

### 語の出どころ

誰が最初に使ったかははっきりしません。マーケターのJason Barnard氏の会社[Kalicube](https://kalicube.com/entity/answer-engine-optimization/)は、同氏が2017年に作った語だと説明しています。ただし本人の会社の説明で、同じページの中には2018年という表記もあります。

日本ではSpeeeが2025年7月30日に[AEOサービスの正式提供](https://prtimes.jp/main/html/rd/p/000000242.000014788.html)を発表しました。[同社のコラム](https://webanalytics.speee.jp/media/article/what-is-aeo/)は対話型AIのアプリ全体を指すにはLLMOでは意味が狭いとして、AEOという言葉を選んだと書いています。なお、同社のプレスリリースでのAEOはAI Engine Optimizationの略です。**同じ取り組みを会社ごとに違う名前で呼んでいるのが今の状態です。**

## SEO・AIO・GEO・LLMOとの違い

AEO対策の提案書とAIO対策の提案書を並べると、中身の項目がほとんど同じことに気づきます。呼び名ごとの出どころは次のとおりです。

| 呼び名 | 正式名 | 主に使われてきた所 | 主に指す回答 |
|---|---|---|---|
| SEO | Search Engine Optimization | 検索エンジン全般 | 検索結果の順位とクリック |
| AEO | Answer Engine Optimization | 海外のSEO業界。強調スニペット・音声検索の頃から | 強調スニペット・音声・生成AIの回答 |
| GEO | Generative Engine Optimization | 2023年11月の論文 | 生成AIの回答 |
| LLMO | Large Language Model Optimization | 日本の支援会社がよく使う | 生成AIの回答 |
| AIO | AI Optimization など | 日本の支援会社がよく使う | 生成AIの回答。GoogleのAI Overviewsを指す会社もある |

**やることはほぼ同じで、呼び名と出どころが違うだけです。** GEOの元の論文が何を確かめたか、各語の細かい違いは[GEO対策とは](/media/geo-taisaku/)に書いています。

### SEOとの違い

Googleの立場ではAEOはSEOの一部です。違いが出るのは測るものの方で、SEOは検索結果の順位とクリックを数え、AEOは回答に自社のページが使われたか・社名が出たかを数えます。

**作業は重なっても、成果の見方は分けて持つ必要があります。** 回答で社名を知った人はリンクを押さずにあとで社名を検索して来ることがあり、アクセス解析ではAIから来たと記録されません。

## Googleが公式に書いていること

AEO対策の提案でよく引かれるのがGoogleの見解です。Googleは[生成AI機能向けの最適化ガイド](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide?hl=ja)（2026年5月15日公開、日本語版は10月9日更新）で、AEOという語を何度か出しています。中心になるのは次の2か所です。

1か所目はSEOが生成AI検索でも有効かを答える節です。

> 「AEO」は「回答エンジン最適化」、「GEO」は「生成エンジン最適化」の略です。どちらも、AI 検索エクスペリエンスでの視認性の向上に特化した作業を説明するために使用されることがある用語です。Google 検索の観点から見ると、生成 AI 検索向けに最適化することは、検索エクスペリエンス向けに最適化することであるため、SEO であることに変わりはありません。

2か所目は「する必要のないこと」を並べた節の前置きです。

> オンラインでは、回答エンジン最適化（AEO）や生成エンジン最適化（GEO）などの用語がよく使われますが、提案されている「ハック」の多くは効果がなく、Google 検索の実際の仕組みによってもサポートされていません。

<figure class="post-figure"><img src="/media/images/aeo-taisaku/aeo_04_google_ai_guide.png" alt="Google検索セントラルの生成AI機能向けの最適化ガイドの、する必要のないことの節。AEOやGEOの用語がよく使われるが、提案されているハックの多くは効果がなくGoogle検索の仕組みにも支えられていないと書かれている" loading="lazy"><figcaption>Google 検索の生成 AI 機能向けにウェブサイトを最適化する（Google 検索セントラル、2026年10月30日）</figcaption></figure>

英語版の原文も「many」（多く）です。**全部が効かないとは書いておらず、多くは効果がないという強さです。**

### する必要のないこと

同じ節が、Google検索では対応しなくてよいものとして挙げているのは次の5つです。

| 項目 | ガイドの記述の要旨 |
|---|---|
| llms.txtなど特別なファイルやマークアップ | Google検索自体が使わない。ほかのサービスのために置くのは問題ない |
| 文章のチャンク化 | 細かく分ける必要はない。理想的なページの長さも無い |
| AI向けの書き換え | AIは類義語や意味を理解する。言い回しの網羅を心配しなくてよい |
| 不自然な言及を集める | 一見役立ちそうだが、実際にはそれほど役に立たない |
| 構造化データへの過剰な取り組み | 生成AI検索に構造化データは要らない。リッチリザルトのためには引き続き使うよう勧める |

ガイドの末尾はAEO・GEOのハックより効果的なSEOの戦略を優先するよう求めています。**Googleが一番強く勧めているのは、読者が独自で役に立つと感じる内容を作ることでした。**

### 外部の助言とツールの扱い

Googleの[サードパーティのSEOに関するガイダンス](https://developers.google.com/search/docs/fundamentals/third-party-seo?hl=ja)も、AEO・GEOと呼ばれる助言やツールに触れています。Googleはサードパーティのサービスを評価しておらず、外部のツールは内部のランキングのデータにアクセスできず、成果も保証できないという内容です。Googleに認められたとほのめかすサービスには注意するよう、同じページは書いています。

### Google以外のAIの公式の記述

ここまではGoogle検索の話で、ChatGPTやPerplexityの扱いはこのガイドの範囲外です。Microsoft BingのプロダクトマネージャーはMicrosoft Advertisingのブログ（[2025年10月8日](https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers)）で、問いと答えの組はAIの回答にそのまま使われることがよくあり、スキーマで内容を商品・レビュー・FAQ・イベントなどと示せると書きました。同じ記事はAIの回答に選ばれることを保証する方法は無いとも書いています。**Googleは生成AI検索のためには構造化データは要らないとし（リッチリザルトのためには勧めています）、Bing側はAIの回答のために勧めているため、どのAIを狙うかで判断が分かれます。**

## AEO対策で勧められる手の効き目

AEO対策の記事や提案でよく並ぶ手を、公式の文書と並べます。

| 勧められる手 | よく言われること | 公式に書いてあること |
|---|---|---|
| FAQの構造化データ（FAQPage） | AIに質問と答えが伝わる | Google検索ではFAQのリッチリザルトの表示が2026年5月7日に終わった |
| FAQのページを作る | AIに引用されやすい | 専用の記述は無い。読者の役に立つ構成として扱う |
| 見出しを問いにする | AIが答えを抜き出しやすい | 読者の役に立つ見出しは勧める。AI向けの書き換えは不要 |
| 質問の直後に答えを書く | 強調スニペットやAIに選ばれる | 強調スニペットは自分で指定できない |
| 構造化データ全般 | AIの理解を助ける | 生成AI検索には不要。リッチリザルトのために勧める |
| llms.txtを置く | AIに読まれやすくなる | Google検索は使わない |

<figure class="post-figure"><img src="/media/images/aeo-taisaku/aeo_02_tactics.png" alt="AEO対策で勧められる手をGoogleの公式の記述で分けた図。読者のために続けるのは問いの見出しと先に答える書き方、FAQの本文、表示と一致した構造化データ。Google検索のために新しく足す理由が無いのはFAQPageのマークアップとllms.txt" loading="lazy"></figure>

### FAQの構造化データ

FAQPageはschema.orgの型の1つで、[schema.orgの定義](https://schema.org/FAQPage)は、1つ以上のよくある質問を載せたウェブページです。同じページには使っているドメインが100万〜1,000万あると出ています（2026年8月時点のGoogleの集計）。

Googleはこの型を使ったリッチリザルトを段階的に絞りました。2023年8月の[ブログ](https://developers.google.com/search/blog/2023/08/howto-faq-changes?hl=ja)で、表示をよく知られた信頼できる政府と医療のサイトに限ると発表しています。さらに[ドキュメントの更新履歴](https://developers.google.com/search/updates?hl=ja)では、2026年5月7日から表示されなくなると5月8日に告知し、6月15日に説明のページそのものを外しました。

**すでに入れているマークアップは外す必要がありません。** 2023年のブログは使われていない構造化データが検索で問題を起こすことは無いと書いています。新しく入れるかどうかはBingのように公式に勧めているAIを狙うかで決めます。

形は次のようなJSON-LDで、答えは画面に出ている文章と同じにします。GoogleのAI機能のページも、構造化データを表示されているテキストと一致させるよう求めています。

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "見積もりは無料ですか？",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "無料です。現地の確認が要る場合も費用はかかりません。"
    }
  }]
}
```

似た型にQ&A（QAPage）がありますが、[GoogleのQAPageの説明](https://developers.google.com/search/docs/appearance/structured-data/qapage?hl=ja)は、サイト運営者が作って利用者が回答を足せないFAQのページを使えない例に挙げています。**会社のFAQをQAPageに書き換えて表示を取り戻す手は使えません。**

### 問いの見出しと先に答える書き方

見出しを読者の質問の形にし、直後に答えを書く書き方は、AEOの記事でよく勧められる手です。Googleのガイドも、段落と見出しで整理された読みやすいページを勧めています。

一方で、AIのために文章を書き換えたり細かく分けたりする必要は無いと同じガイドは書いています。強調スニペットについても、Googleの[強調スニペットの説明](https://developers.google.com/search/docs/appearance/featured-snippets?hl=ja)は、自分のページを強調スニペットに設定することはできないと答えています。**問いの見出しは読者のための書き方として続け、AIに選ばれる手としては期待しすぎないのが公式の記述に沿った扱いです。**

FAQのページで答える質問の選び方は[AIに引用されるFAQページの作り方](/media/faq-for-ai/)、AIによる概要に出る条件は[AI Overview対策とは](/media/cited-by-ai-overviews/)にまとめました。

### 構造化データ全般

組織・商品・記事などの構造化データは、Google検索のリッチリザルトの対象になるために引き続き勧められています。生成AI検索のための特別なマークアップは無いとGoogleは書いているため、**画面とずれた古いマークアップを直す方が、新しい型を足すより先です。** 会社の情報を整える構造化データは[エンティティSEOとは](/media/entity-seo/)、llms.txtとの違いは[llms.txtとは](/media/llms-txt-structured-data/)で扱っています。

## AEO対策で会社がやること

AEOと呼んでもAIO・LLMOと呼んでも、会社が進める順番は変わりません。

<figure class="post-figure"><img src="/media/images/aeo-taisaku/aeo_03_steps.png" alt="AEO対策で会社がやる5つの順番を縦に並べた図。測る質問を決める、読まれる状態か確かめる、社内にしかない情報を載せる、外部の情報をそろえる、同じ条件で測る" loading="lazy"></figure>

1つ目は、見込み客がAIに聞きそうな質問を決めることです。社名を入れない質問（〇〇を相談できる会社はどこか）で候補に入るかどうかが、新しい顧客につながります。質問の案は商談の最初に聞かれることや比べられた相手から集めると、実際の聞かれ方に近づきます。

2つ目はページが読まれる状態かの確認です。GoogleのAI機能に出る条件はインデックスに登録され、スニペットを表示できることで、Search Consoleの生成AI設定で除外していないことも要ります。ChatGPTについてはOpenAIの[クローラーの説明](https://developers.openai.com/api/docs/bots)が、OAI-SearchBotを止めたサイトはChatGPTの検索の回答に出ない（ナビゲーション用のリンクとしては出ることがある）と書いています。

3つ目に、料金の決まり方・納期・対応できない条件・事例の数字のように、社内にしかない情報をページに載せます。4つ目はGoogleビジネスプロフィールや業界の比較サイトなど社外の情報をそろえることです。

5つ目は同じ質問を同じ条件で何回か聞き、出た割合で見ることです。**nitoが支援するSaaS企業では、会員登録のときのアンケートで26.7%がAI検索で知った・比べたと答えた一方、同じ期間のGA4でAI経由として記録された会員登録は、全体の0.007%でした。** 回答への言及の割合だけでなく、問い合わせで何で知ったかを聞く数まで目標に置きます。各段階の進め方は[AIO対策とは](/media/aio-taisaku/)に書いています。

## AEOツールの見方

AEOツールは登録した質問をAIに聞いて、自社の名前や引用の割合を記録するものです。どのAIに何問を何回聞くか、回答の数え方は製品ごとに違い、Googleの内部のデータには触れられません。料金と測れるAIの比較は[GEO対策ツール・AIO対策ツール10製品の比較](/media/geo-aio-tools/)にまとめました。

## 会社が決めること

AEO対策を外に頼むか社内で進めるかの前に、決めておくことがあります。

| 決めること | 選び方 | 主に決める人 |
|---|---|---|
| 対象のAI | Google検索だけか、ChatGPT・Gemini・Perplexity・Bingまで含めるか | マーケ責任者 |
| 測る質問 | 社名を入れない質問を中心に数十問 | マーケ担当と営業 |
| 目標 | 言及の割合だけか、問い合わせで何で知ったかまで見るか | 事業の責任者 |
| 作業の範囲 | 診断・ページの修正・記事の制作・測定のどこまでを頼むか | マーケ責任者 |
| 見直しの時期 | 何か月目にどの数字で続けるかを決めるか | 決裁者 |

AEO対策の提案を比べるときは、呼び名でなく作業の範囲で見積もりを並べます。**FAQの構造化データやllms.txtの設置だけで成果をうたう提案は、Google検索については公式の記述と合いません。** Googleに認められたと言う、上位を保証すると言う提案も、Googleのガイダンスが注意を促している言い方です。費用の幅は[LLMO対策の費用相場](/media/llmo-cost/)、社内との分け方は[内製と外注どちらがいい？](/media/llmo-inhouse-vs-outsource/)で読めます。

## よくある質問

### Q. AEO対策とSEO対策は何が違いますか？

Googleの公式ガイドは、生成AI検索向けの最適化もGoogle検索から見ればSEOだと書いています。作業は重なり、違うのは測るものです。SEOは順位とクリック、AEOは回答に自社の情報が使われたか・社名が出たかを見ます。

### Q. AEO対策でFAQPageの構造化データは今も必要ですか？

Google検索のためには新しく足す理由がありません。FAQのリッチリザルトは2026年5月7日に表示が終わり、Googleは生成AI検索に構造化データは要らないと書いています。すでに入れているものは外さなくてよく、Bingのように公式に勧めているAIを狙うなら入れる判断もあります。

### Q. AEOとGEO・LLMO・AIOは別の対策ですか？

指す取り組みはほぼ同じです。AEOは強調スニペットや音声検索の頃からの英語圏の呼び名、GEOは2023年の論文、LLMOとAIOは日本の支援会社がよく使う呼び名です。見積もりは呼び名でなく作業の範囲で比べます。

### Q. Googleの強調スニペットは自分のページで指定できますか？

できません。Googleの強調スニペットの説明は、ページの内容がふさわしいとGoogleのシステムが判断したときに表示されると書いています。表示させない設定（nosnippetなど）はできます。

### Q. AEO対策をすればChatGPTで自社が紹介されますか？

必ずではありません。ChatGPTの検索に出るには、OAI-SearchBotを止めていないことが前提です。そのうえで同じ質問を何回か聞き、社名が出た割合で確かめます。

### Q. AEO対策の効果はGoogle Search Consoleで確かめられますか？

Googleの分は確かめられます。Search Consoleの生成AIパフォーマンスレポートは、AIによる概要とAIモードでサイトへのリンクが表示された回数をページごとに出すレポートです。ChatGPTやPerplexityの分は入らないため、手で聞いた記録や問い合わせのアンケートと組み合わせます。

## 出典

- Google 検索セントラル「[Google 検索の生成 AI 機能向けにウェブサイトを最適化する](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide?hl=ja)」2026年5月15日公開、日本語版は10月9日更新（2026年10月30日取得）
- Google 検索セントラル「[AI 機能とウェブサイト](https://developers.google.com/search/docs/appearance/ai-features?hl=ja)」2025年12月31日更新（同）
- Google 検索セントラル「[サードパーティの SEO ツール、サービス、アドバイスの使用に関する Google 検索のガイダンス](https://developers.google.com/search/docs/fundamentals/third-party-seo?hl=ja)」（同）
- Google 検索セントラル「[ドキュメントの最新の更新内容](https://developers.google.com/search/updates?hl=ja)」2026年5月8日・5月15日・6月15日の項（同）
- Google 検索セントラル ブログ「[How-to とよくある質問のリッチリザルトの変更](https://developers.google.com/search/blog/2023/08/howto-faq-changes?hl=ja)」2023年8月8日（9月14日更新）（同）
- Google 検索セントラル「[Q&A（QAPage）の構造化データ](https://developers.google.com/search/docs/appearance/structured-data/qapage?hl=ja)」2026年9月12日更新（同）
- Google 検索セントラル「[強調スニペットとウェブサイト](https://developers.google.com/search/docs/appearance/featured-snippets?hl=ja)」2025年12月18日更新（同）
- schema.org「[FAQPage](https://schema.org/FAQPage)」（同）
- Microsoft Advertising ブログ「[Optimizing your content for inclusion in AI search answers](https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers)」2025年10月8日（同）
- OpenAI「[Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)」（同）
- Kalicube「[Answer Engine Optimization](https://kalicube.com/entity/answer-engine-optimization/)」（同）
- 株式会社Speee「[ChatGPTなどAIに自社を推奨されやすくするための「AEOサービス」を正式提供開始](https://prtimes.jp/main/html/rd/p/000000242.000014788.html)」PR TIMES、2025年7月30日（同）
- 株式会社Speee「[AEO対策とは？SEOとの違いから具体的な手法、成功へのロードマップを徹底解説](https://webanalytics.speee.jp/media/article/what-is-aeo/)」2025年10月30日（2026年9月30日更新）（同）
