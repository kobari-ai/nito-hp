---
title: 【2026年10月】エンティティSEOとは？Googleの公式情報と会社が整える項目・確かめ方
date: 2026-10-29
category: AI検索対策
description: エンティティSEOとは何かを、Googleのナレッジグラフ・構造化データ・ナレッジパネルの公式文書で確認。SEO会社の説明との違い、会社が整える名前の表記・会社概要・sameAs、決められないこと、効いたかの確かめ方まで。
cover_tag: 解説
cover_headline: エンティティSEOとは
cover_sub: 公式情報と会社が整える項目
cta: llmo
---

Googleは2012年5月、検索を文字列の一致から物事の理解へ移すとして、ナレッジグラフを発表しました。2020年5月の説明では50億のエンティティについて5,000億を超える事実を集めています。

SEO会社から「エンティティSEO」を勧められても、会社として何を整えればよいのかは見えにくいものです。この記事は2026年10月29日に取得したGoogleの文書をもとに、**公式に書かれていること、会社が整えること、効いたかの確かめ方**を分けて書きます。

:::takeaways
- エンティティはGoogleが1つの対象として見分ける人・組織・場所・物事です。**ナレッジパネルは自動で作られ、手動では作れないとGoogleのヘルプにあります**
- Googleが書いているのは、組織の構造化データで**検索結果で組織を明確化できる**ことまでです。エンティティを強くすると順位やE-E-A-Tが上がるという説明は、読んだ文書に見当たりません
- 会社がすぐできるのは**名前の表記をそろえる・基準の会社概要ページを決める・Organizationの構造化データとsameAsを入れる**ことです。社外の記事やナレッジパネルの表示は会社では決められません
:::

## エンティティとは

英語のentityは実在するひとまとまりの対象を指す言葉で、Googleは2020年のブログでエンティティを人・場所・物事と説明しています。その事実を集めたしくみがナレッジグラフです。**会社・商品・代表者・本社の所在地は、どれもGoogleが見分ける対象になりえます。**

<figure class="post-figure"><img src="/media/images/entity-seo/ent_01_what.png" alt="ウェブの情報からナレッジグラフができ、社名で検索するとナレッジパネルに出る流れの図。公式サイト・社外のページ・Wikidataなどのデータベースが元になる" loading="lazy"></figure>

### キーワードとの違い

Googleが2012年の発表で挙げた例は「taj mahal」という検索でした。この2語はインドの霊廟も、グラミー賞を取った音楽家も、米国のカジノも、近所のインド料理店も指します。文字列が同じでも指す対象が違うため、Googleは対象どうしの関係まで持つデータを作ったと説明しています。

キーワードは検索窓に入る文字の並びで、エンティティはその文字が指す対象です。**社名が一般名詞や他社の名前と同じ会社ほど、この見分けが問題になります。**

### ナレッジグラフとナレッジパネル

[ナレッジパネルのヘルプ](https://support.google.com/knowledgepanel/answer/9163198?hl=ja)は、ナレッジパネルを「ナレッジグラフに存在する対象（人、場所、組織、物事など）を検索したときに Google に表示される情報ボックス」と説明しています。中身は自動で作られ、元はウェブ上のさまざまな情報です。

2020年のブログによれば情報源はウェブの資料とオープンなデータベース、ライセンスを受けたデータベースで、Wikipediaは数百ある情報源の1つとされています。**会社の情報は公式サイトだけでなく社外のページからも集まる前提で整えます。**

## Googleが公式に書いていること

SEO会社の記事ではエンティティを強くすると評価が上がるという説明をよく見かけます。ここではGoogleが自社の文書で何をどの強さで書いているかだけを並べました。

### 組織の構造化データの文書

[組織（Organization）の構造化データ](https://developers.google.com/search/docs/appearance/structured-data/organization?hl=ja)のページ（2026年9月12日更新）は、ホームページに組織の構造化データを足すと「Google は組織の管理情報の詳細を把握して、検索結果で組織を明確化できるようになります」と書いています。必須のプロパティは無く、当てはまるものをできるだけ多く足すよう勧めています。

置き場所はホームページか企業情報ページのような単一のページで、全ページに入れる必要はありません。urlは「Google が組織を一意に識別するのに役立ちます」、logoは検索結果やナレッジパネルに出すロゴの把握に役立つ、という書き方です。**Googleが約束しているのは把握や識別に役立つところまでで、順位が上がるとは書いていません。**

<figure class="post-figure"><img src="/media/images/entity-seo/ent_org_doc.png" alt="Google検索セントラルの組織の構造化データのページ冒頭。組織の構造化データを追加すると検索結果で組織を明確化できると書かれている" loading="lazy"><figcaption>組織（Organization）の構造化データ（Google検索セントラル、2026年10月29日）</figcaption></figure>

### ナレッジパネルのヘルプ

[自分に関する情報についてフィードバックを送信する](https://support.google.com/knowledgepanel/answer/7534842?hl=ja)のヘルプには、パネルの表示と非表示は検索語句との関連性にもとづいてGoogleの自動システムが決めると書かれています。続けて「現在のポリシーではナレッジパネルを手動で作成または削除することはできません」とあります。

申請できるのは、すでに出ているパネルの認証です。[Google の認証を受ける](https://support.google.com/knowledgepanel/answer/7534902?hl=ja)の手順はパネル下部の［ナレッジパネルの認証を受ける］から始まります。本人の確認にはYouTube・Search Console・Twitter・Facebookのどれかへのログインを使います。すべてのパネルが認証を受けられるわけではない、という注意も添えられています。

<figure class="post-figure"><img src="/media/images/entity-seo/ent_kp_manual.png" alt="ナレッジパネルのヘルプ。表示と非表示は自動システムが決め、手動で作成または削除はできないと書かれている" loading="lazy"><figcaption>自分に関する情報についてフィードバックを送信する（ナレッジパネル ヘルプ、2026年10月29日）</figcaption></figure>

### AI機能のページ

[AI 機能とウェブサイト](https://developers.google.com/search/docs/appearance/ai-features?hl=ja)のページは、AIによる概要とAIモードに出るための追加の要件や特別な最適化は無いとしています。そのうえで、SEOの基本に「構造化データをページに表示されるテキストと一致させます」とビジネス プロフィールの情報を最新に保つことを挙げました。

同じ箇所によれば、特別なschema.orgの構造化データを足す必要もありません。**GoogleのAI機能（AIによる概要・AIモード）のための専用マークアップは無く、画面の表記と構造化データを食い違わせないことが公式の求めです。**

<figure class="post-figure"><img src="/media/images/entity-seo/ent_ai_features.png" alt="AI機能とウェブサイトのページ。構造化データを表示されるテキストと一致させ、特別なschema.orgの構造化データを追加する必要は無いと書かれている" loading="lazy"><figcaption>AI 機能とウェブサイト（Google検索セントラル、2026年10月29日）</figcaption></figure>

### SEO会社の説明との違い

よく見る説明と、Googleの文書の書き方を並べました。「見当たらない」は出典に挙げたGoogleの文書を読んだ範囲での判断です。

| よく見る説明 | Googleの文書 |
|---|---|
| 構造化データで組織を伝える | 書いてある。組織を明確化できる |
| sameAsでSNSなどを結ぶ | 書いてある。追加情報があれば必要に応じて |
| ナレッジパネルは申請で出せる | 出せないと書いてある。手動では作れない |
| エンティティを強くするとE-E-A-Tが上がる | 見当たらない |
| エンティティが強いと順位が上がる | 見当たらない |
| GoogleのAI機能には専用のマークアップが要る | 要らないと書いてある |

E-E-A-Tそのものは[E-E-A-Tとは](/media/eeat-for-ai-search/)、構造化データ全般の扱いは[llms.txtとは](/media/llms-txt-structured-data/)の構造化データの節に書いています。

<figure class="post-figure"><img src="/media/images/entity-seo/ent_02_official.png" alt="Googleの文書に書いてあることと見当たらないことの図。書いてあるのは組織の明確化・ロゴとサイト名・ナレッジパネルは手動で作れない・GoogleのAI機能に専用の記述は要らない。見当たらないのは順位やE-E-A-Tが上がるという説明" loading="lazy"></figure>

## 会社が整えること

整える項目は6つあり、自社で完結するものと相手しだいのものが混ざっています。先に分けておくと、社内の誰に頼むかが決めやすくなります。

| 項目 | 主な担当 | 会社で決められるか |
|---|---|---|
| 名前の表記をそろえる | 広報・総務 | 決められる |
| 基準の会社概要ページ | Web担当 | 決められる |
| OrganizationとsameAs | Web担当・制作会社 | 入れるのは決められる。使うかはGoogleが決める |
| サイト名の指定 | Web担当 | 指定はできる。表示はGoogleが決める |
| Googleビジネスプロフィール | 拠点の担当 | 拠点で客に応対する会社なら決められる |
| 社外のページ | 広報・営業 | 決められない。載せるのは相手 |

<figure class="post-figure"><img src="/media/images/entity-seo/ent_03_tasks.png" alt="会社が整える6項目を、自社で決められるもの・Googleが決めるもの・相手が決めるものに分けた図" loading="lazy"></figure>

### ① 名前の表記をそろえる

最初に作るのは、自社の名前の書き方の一覧です。登記上の正式名、通称、英字表記、略称、代表者名、本社の住所を1枚の表にします。「株式会社」が前か後ろか、代表者名の髙と高のような字体まで決めておくと、各所の担当者が迷いません。

一覧ができたら、自社サイト・SNSのプロフィール・求人媒体・業界団体の会員名簿と照らし合わせます。[ビジネス プロフィールのガイドライン](https://support.google.com/business/answer/3038177?hl=ja)も、名前は店舗・ウェブサイト・ビジネスレターなどで「一貫して使用し、顧客に認知されている、実際のビジネスの名称」にするよう求めています。**旧社名や移転前の住所が残るページは、見つけた順に直すか相手に依頼します。**

### ② 基準の会社概要ページを決める

構造化データの文書は組織の情報を1つのページにまとめて置くよう勧めています。会社概要ページを基準と決め、正式名・通称・設立年・所在地・代表者・事業内容をここに書きます。

このページが古いままだと、ほかを直しても基準がぶれてしまうのが難点です。**社名変更・移転・代表の交代のときに最初に直すページとして、社内で決めておきます。**

### ③ OrganizationとsameAsを入れる

会社概要ページかホームページに、次のようなJSON-LDを入れます。値は架空の会社の例で、Googleの組織のページにあるプロパティから、会社概要に載る項目を選びました。

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "サンプル",
  "alternateName": ["Sample", "サンプル社"],
  "legalName": "株式会社サンプル",
  "url": "https://www.example.co.jp/",
  "logo": "https://www.example.co.jp/images/logo.png",
  "description": "業務用の計測機器を開発・販売する会社です。",
  "foundingDate": "2015-04-01",
  "address": {
    "@type": "PostalAddress",
    "postalCode": "100-0001",
    "addressRegion": "東京都",
    "addressLocality": "千代田区",
    "streetAddress": "千代田1-1",
    "addressCountry": "JP"
  },
  "telephone": "+81-3-0000-0000",
  "sameAs": [
    "https://x.com/example",
    "https://www.youtube.com/@example",
    "https://www.linkedin.com/company/example"
  ]
}
```

nameにはサイト名と同じ名前を入れ、登記の正式名が違う場合はlegalNameに分けます。代表者名はGoogleの推奨プロパティに無いため、会社概要の本文に書けば足ります。

sameAsについて、schema.orgの定義は「その対象が何者かを曖昧さなく示す参照先のページのURL」です。例にはWikipediaのページ、Wikidataの項目、公式サイトが並びます。Googleの文書の例はSNSやレビューサイトにある組織のプロフィールでした。**入れるのは自社が管理して更新しているアカウントと、自社の項目が実在するデータベースだけにします。**

入れたら[リッチリザルト テスト](https://search.google.com/test/rich-results?hl=ja)か[スキーマ マークアップ検証ツール](https://validator.schema.org/)で読み取れるかを確かめます。公開後にクロールされるまで数日かかる場合がある、とGoogleの文書にあります。

<figure class="post-figure"><img src="/media/images/entity-seo/ent_sameas.png" alt="schema.orgのsameAsのページ。対象が何者かを曖昧さなく示す参照先のURLと定義し、Wikipedia・Wikidata・公式サイトを例に挙げている" loading="lazy"><figcaption>sameAs（schema.org、2026年10月29日）</figcaption></figure>

### ④ サイト名を指定する

[サイト名のページ](https://developers.google.com/search/docs/appearance/site-names?hl=ja)によると、検索結果のサイト名はホームページとウェブ上の参照元のページから自動で作られます。希望を伝えるにはホームページのWebSiteの構造化データが最も重要です。

世界規模の2つの別のサイトに同じサイト名を通常は使わない、というのも同じページの記述でした。社名が他社と重なるなら、略称や英字表記をalternateNameに入れておくと第1希望が使えないときの候補になります。**サイト名は指定できても、最後に決めるのはGoogleです。**

### ⑤ Googleビジネスプロフィール

ナレッジパネルのヘルプは特定の場所やサービス提供地域で客に応対する会社に、ビジネス プロフィールでの管理を案内しています。本社で来客を受ける会社や店舗を持つ会社は、名前と住所を①の一覧どおりに登録します。実際にサービスを提供していない借りた住所では登録できません。AIモードとの関係は[GoogleビジネスプロフィールのAI対策](/media/gbp-ai-search/)に書きました。

### ⑥ 社外のページ

ナレッジグラフは社外のページからも情報を集めるため、自社サイトの外に正しい情報が載っているかも効きます。業界団体の会員名簿、取引先の導入事例、登壇したイベントのページ、業界紙の記事が代表例です。**社外のページに載る名前と住所が①の一覧と同じかを、掲載のたびに確かめます。**社外での言及の増やし方は[サイテーションとは](/media/citation-for-ai/)にまとめました。

## 会社では決められないこと

ナレッジパネルの表示は前の節のとおりGoogleの自動システムが決めます。出ていないパネルは申請では作れず、出てから認証を受け、誤りを公開ページのURLつきで報告する流れです。

Wikipediaの記事も会社では決められません。[特筆性（組織）](https://ja.wikipedia.org/wiki/Wikipedia:%E7%89%B9%E7%AD%86%E6%80%A7_(%E7%B5%84%E7%B9%94))の目安では、企業に記事が立つのは、対象から独立した信頼できる二次情報源で報道されている場合です。[自分自身の記事](https://ja.wikipedia.org/wiki/Wikipedia:%E8%87%AA%E5%88%86%E8%87%AA%E8%BA%AB%E3%81%AE%E8%A8%98%E4%BA%8B)のページは「あなたの会社」も対象とし、自分についての記事を新しく作ることは基本的に推奨されないと書いています。**Wikipediaの記事を報酬を受けて書く人は、依頼主を開示する義務があります。作成を請け負う提案を受けたら、開示の有無と特筆性の目安を先に確かめてください。**

Wikidataの[自伝のガイドライン](https://www.wikidata.org/wiki/Wikidata:Autobiography)は自分の項目の編集を認めつつ、基準を満たすと確信できない限り新しく作るべきではないとしています。AIの答えも、会社が直接書き換える場所はありません。

<figure class="post-figure"><img src="/media/images/entity-seo/ent_wp_self.png" alt="Wikipediaの「自分自身の記事」のページ。自分自身についての記事を新しく作ることは基本的に推奨されないと書かれている" loading="lazy"><figcaption>Wikipedia:自分自身の記事（ウィキペディア、2026年10月29日）</figcaption></figure>

## AI検索との関係

Googleは2024年5月、AIによる概要の誤りについて[ブログで説明](https://blog.google/products/search/ai-overviews-update-may-2024/)しました。AIによる概要は上位のウェブ結果に裏付けのある情報だけを出す設計です。誤りの主な原因として挙げたのは、質問の読み違い・ウェブ上の言葉のニュアンスの読み違い・良い情報が少ないことの3つです。

会社名に当てはめると、社名が他社と同じうえに自社について書かれたページが少ない会社ほど、読み違いが起きやすいと考えられます。これはnitoの読みで、Googleが会社名について書いているわけではありません。ChatGPT・Gemini・Perplexityが会社をどう見分けるかも、調べた範囲では公式の説明が見つかりませんでした。

nitoはこの記事のために、AIに同名の会社を取り違えさせる試験をしていません。**AIによる概要は上位のウェブ結果を土台にするため、自社サイトと社外のページの表記がそろっているほど読み違いの材料が減る、とまでは言えます。**引用されるための書き方は[AI Overviewsに引用されるには](/media/cited-by-ai-overviews/)で扱っています。

## 効いたかの確かめ方

整えたあとの確認はGoogleの画面で見るものとAIに聞くものに分かれます。記録の頻度は月に1回、手順は毎回同じが目安です。

<figure class="post-figure"><img src="/media/images/entity-seo/ent_04_check.png" alt="効いたかを確かめる4つの手順の図。社名で検索・構造化データのテスト・Googleトレンド・AIに社名を聞く" loading="lazy"></figure>

### 社名で検索する

正式名と通称の両方で検索し、ナレッジパネルが出るか、中身が会社概要と合っているかを見ます。誤りがあれば、パネルの［フィードバック］から公開ページのURLを添えて報告します。ヘルプによれば、認証を受けたアカウントからの報告の審査は数日以内です（これより長くかかる場合もある、という但し書きつき）。

### 構造化データを確かめる

リッチリザルト テストで会社概要ページのURLを読み、Organizationが検出されるかを見ます。Googleが最新の版を読んだかどうかは、Search ConsoleのURL検査で分かります。

### Googleトレンドで社名を入れる

[Google トレンドのヘルプ](https://support.google.com/trends/answer/4359550?hl=ja)は、トピックを「すべての言語で共通の概念を持つキーワードのグループ」と説明しています。社名を入れたとき、候補に「会社」などのトピックが出れば、Googleがその名前を1つの対象としてまとめている目安です。トピックがナレッジグラフの項目だとは、ヘルプには書かれていません。

<figure class="post-figure"><img src="/media/images/entity-seo/ent_trends_topic.png" alt="Googleトレンドのヘルプのトピックの節。トピックはすべての言語で共通の概念を持つキーワードのグループと説明している" loading="lazy"><figcaption>Google トレンドでの検索キーワードの比較（Google トレンド ヘルプ、2026年10月29日）</figcaption></figure>

### AIに社名を聞く

ChatGPT・Gemini・Perplexity・AIモードに同じ質問を入れて、答えを記録します。「株式会社サンプルはどんな会社ですか」「サンプル社の代表者は誰ですか」のように、会社概要と答え合わせできる質問にするのがコツです。

答えはAIの種類・時期・会話の流れで変わるため、1回で判断しないことが大切です。**所在地・事業・代表者のどれが違うかを項目ごとに数えると、直す場所が見えます。**社名で検索する人の増減は[指名検索の記事](/media/branded-search-signal/)の方法で追えます。

## 会社が決めること

エンティティの整備はWeb担当だけでは終わりません。社名の書き方は広報、拠点の情報は総務、構造化データは制作会社と、持ち主が分かれているためです。

- **正式表記の決め手**: 表記の一覧を誰が持ち、変えるときに誰が承認するか
- **直す順番**: 社名変更・移転・代表の交代のとき、会社概要・構造化データ・ビジネス プロフィール・SNS・社外の掲載先をどの順に直すか
- **sameAsの範囲**: 更新を続けるアカウントだけを入れるか
- **ナレッジパネルの認証**: 誰のGoogleアカウントで受けるか。認証のあとは別のGoogleアカウントを正式な代表者として足せ、権限はオーナー・管理者・投稿者に分かれる
- **Wikipediaの方針**: 自社で書かない・頼まないと決めるか
- **測り方**: 4つのAIに聞く質問と記録の頻度

<figure class="post-figure"><img src="/media/images/entity-seo/ent_05_decide.png" alt="会社が決める6つのことの図。正式表記・直す順番・sameAsの範囲・ナレッジパネルの認証・Wikipediaの方針・測り方" loading="lazy"></figure>

### 失敗しやすい例

起きやすいのは、会社概要を直したのに求人媒体や業界団体の名簿に旧社名が残るケースです。構造化データのnameと画面の社名が違う、sameAsに更新の止まったSNSが入っている、という食い違いもあります。

ナレッジパネルの認証を担当者個人のアカウントで受け、退職後に誰も報告できなくなる例もあります。**担当が変わっても回るように、権限と手順を会社の持ち物にしておきます。**

## よくある質問

### エンティティSEOはGoogleの公式用語ですか？

この記事で読んだGoogleの文書には、エンティティSEOという語は出てきません。エンティティという語はナレッジパネルのヘルプで使われています。エンティティSEOはSEO会社が使う呼び名です。

### ナレッジパネルは申請すれば表示されますか？

表示されません。ヘルプは表示と非表示を自動システムが決め、手動で作ることも消すこともできないと書いています。申請できるのは出ているパネルの認証と修正の提案です。

### sameAsにはどのURLを入れればよいですか？

自社が管理するSNSやレビューサイトのプロフィール、自社の項目があるWikipedia・Wikidataのページです。schema.orgは対象が何者かを曖昧さなく示すページと定義しています。

### AIによる概要のために特別な構造化データは要りますか？

要りません。Googleの検索セントラルは、AI機能のために特別なschema.orgの構造化データを足す必要は無いと書いています。求めているのは構造化データと画面の表記をそろえることです。

### エンティティSEOの効果はどのくらいで出ますか？

Googleは期間を公表していません。構造化データは公開後のクロールまで数日かかる場合があるとされ、社外のページやナレッジパネルは相手とGoogleの判断しだいです。

### 社名が他社と同じ場合はどうすればよいですか？

会社概要とOrganizationに、正式名・所在地・事業内容をそろえて書きます。WebSiteの構造化データのalternateNameに略称や英字表記を入れ、社外のページでも同じ表記を使ってもらいます。

## 出典

いずれも2026年10月29日に取得しました。

- Google 検索セントラル
  - 「[組織（Organization）の構造化データ](https://developers.google.com/search/docs/appearance/structured-data/organization?hl=ja)」（2026年9月12日更新）
  - 「[Google 検索に対してサイト名を指定する](https://developers.google.com/search/docs/appearance/site-names?hl=ja)」（2026年2月20日更新）
  - 「[AI 機能とウェブサイト](https://developers.google.com/search/docs/appearance/ai-features?hl=ja)」（2025年12月31日更新）
- ナレッジパネル ヘルプ
  - 「[ナレッジパネルについて](https://support.google.com/knowledgepanel/answer/9163198?hl=ja)」
  - 「[自分に関する情報についてフィードバックを送信する](https://support.google.com/knowledgepanel/answer/7534842?hl=ja)」
  - 「[Google の認証を受ける](https://support.google.com/knowledgepanel/answer/7534902?hl=ja)」
- Google ビジネス プロフィール ヘルプ「[ビジネス プロフィールに関するガイドライン](https://support.google.com/business/answer/3038177?hl=ja)」
- Google トレンド ヘルプ「[Google トレンドでの検索キーワードの比較](https://support.google.com/trends/answer/4359550?hl=ja)」
- Google ブログ
  - 「[Introducing the Knowledge Graph: things, not strings](https://blog.google/products/search/introducing-knowledge-graph-things-not/)」（2012年5月16日）
  - 「[A reintroduction to our Knowledge Graph and knowledge panels](https://blog.google/products/search/about-knowledge-graph-and-knowledge-panels/)」（2020年5月20日）
  - 「[AI Overviews: About last week](https://blog.google/products/search/ai-overviews-update-may-2024/)」（2024年5月30日）
- schema.org「[sameAs](https://schema.org/sameAs)」「[Organization](https://schema.org/Organization)」
- Wikidata「[Wikidata:Autobiography](https://www.wikidata.org/wiki/Wikidata:Autobiography)」
- ウィキペディア「[Wikipedia:特筆性 (組織)](https://ja.wikipedia.org/wiki/Wikipedia:%E7%89%B9%E7%AD%86%E6%80%A7_(%E7%B5%84%E7%B9%94))」「[Wikipedia:自分自身の記事](https://ja.wikipedia.org/wiki/Wikipedia:%E8%87%AA%E5%88%86%E8%87%AA%E8%BA%AB%E3%81%AE%E8%A8%98%E4%BA%8B)」「[Wikipedia:有償の寄稿の開示](https://ja.wikipedia.org/wiki/Wikipedia:%E6%9C%89%E5%84%9F%E3%81%AE%E5%AF%84%E7%A8%BF%E3%81%AE%E9%96%8B%E7%A4%BA)」（方針。報酬を受けて寄稿する人は雇用主・依頼主を開示しなければならない）
