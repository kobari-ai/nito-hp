---
title: 【2026年10月】ChatGPTショッピングに自社商品を載せる方法・商品フィードの申請と日本の状況
date: 2026-10-20
category: AI検索対策
description: ChatGPTの商品の検索結果に自社商品を載せる方法をOpenAIとShopifyの公式資料で整理。商品フィードの申請、Shopify・Etsyの連携、日本の事業者の今、手数料、載せられない商品、AIの回答で挙がることとの違いまで。
cover_tag: ショッピング
cover_headline: ChatGPTショッピングに商品を載せる
cover_sub: 商品フィードの申請と日本の状況
cta: llmo
---

OpenAIの事業者向けページ「[Power product discovery in ChatGPT](https://chatgpt.com/merchants/)」には、2026年10月20日に確認した時点でChatGPTのショッピングは米国の利用者向けに提供中と書かれています。同じページはチャットの中で決済まで済ませるInstant Checkoutから離れ、購入は販売者のサイトで行う形に移ると説明しています。

日本語の解説には2025年秋のチャット内決済の説明のまま残っているものがあります。この記事は商品を載せる3つの経路と日本の事業者の今、費用、載せられない商品を、公式に書いてあることと無いことに分けて整理します。

:::takeaways
- 商品が載る経路は**Shopify・Etsyの連携、商品フィードの申請、Webの情報からの掲載**の3つ。Shopify と Etsy で売っている商品は申請しなくても連携済み
- 商品フィードの申請は承認制で、今申し込むとウェイトリストに入る。**フィードの仕様では標準の送り先が米国で、日本を選ぶ設定は載っていない**
- 自社サイトで買われた分に手数料はかからない。**酒類やサプリメントは商品の検索結果に出ない**
:::

<!-- SHOT: HTML図 cshp_routes.html（商品が載る3つの経路を縦に3段）・幅640 DPR2・赤枠なし -->

## ChatGPTショッピングの今の形

「1万円以内の手土産を探して」のように買い物の意図がある質問をすると、ChatGPTは画像と価格と購入先へのリンクを付けた商品の一覧を回答に出します。ヘルプ「[Shopping with ChatGPT Search](https://help.openai.com/en/articles/11128490)」は、**この商品の検索結果をChatGPTが独自に選んでいて、広告でもOpenAIの提携の影響を受けたものでもない**と書いています。広告は別の枠として扱われます。

### 商品の選ばれ方

ヘルプが挙げる材料は3つです。1つ目は価格や商品説明などの構造化されたデータとその他の第三者のコンテンツで、提供元には事業者自身と第三者の両方が入ります。2つ目は新しい検索結果を見る前のモデルの回答、3つ目はOpenAIの安全基準と商品のポリシーです。質問の文に加えて、メモリーやカスタム指示に書かれた好みも考慮されます。

商品を押したあとに並ぶ販売者の順番について、ヘルプは**在庫・価格・品質・その商品の製造元か主な販売者か**で決めると説明しています。価格は第三者の提供元から受け取っていて、事業者が値段を変えてから画面に反映されるまで時間がかかることがあるとも書かれています。「Budget-friendly」のようなラベルやレビューの要約はモデルが作ったもので、レビューの出どころは公開されたWebサイトです。

<!-- SHOT: OpenAI ヘルプ「Shopping with ChatGPT Search」の How Merchants Are Selected の節・https://help.openai.com/en/articles/11128490 ・PC・赤枠1: 販売者の並びの基準の文（availability, price, quality...）／赤枠2: Shopify Catalog の文 -->

事業者の側から見ると、**価格と在庫の情報が新しいことと、公開されたサイトにレビューがあること**が並び順の材料です。どちらも自社サイトの外の情報を含むため、自社のページを直すだけでは揃いません。

### Instant Checkoutの終了

2025年9月に始まったInstant Checkoutは、ChatGPTの画面で注文と支払いまで済ませる仕組みでした。今は事業者向けページに、**単独のInstant Checkoutの体験から離れ、利用者は販売者のサイトやアプリで購入する**と書かれています。主な出来事を時系列で並べました。

| 時期 | 出来事 | 出どころ |
|---|---|---|
| 2025年9月29日 | Instant Checkoutと決済の仕様ACPを発表。米国の利用者が米国のEtsy出品者から購入できる形で開始 | OpenAIのお知らせ |
| 2025年11月20日 | Shopifyの販売者に広がる（Spanx・Skims・Glossierから） | リリースノート |
| 2025年11月24日 | 商品を深く調べて比べるショッピングリサーチを開始 | リリースノート |
| 2026年3月 | チャット内の決済から離れ、商品の発見に力を移すと報じられる | 報道 |
| 2026年3月24日 | 商品の表示と比較を改善し、ACPで事業者の商品情報を取り込む | リリースノート |

ACP（Agentic Commerce Protocol）はOpenAIがStripeと作った、AIと販売者が商品情報や注文をやり取りするための仕様です。今の事業者向けページの説明では、**ACPの役目は商品の発見と推薦のための商品データの共有**です。

なお、ヘルプ「Shopping with ChatGPT Search」の冒頭には、一部の対象の商品と販売者でInstant Checkoutを出すことがあるという文がまだ残っています。事業者向けページと食い違うため、この記事は事業者向けページの説明に合わせて書いています。Shopifyのヘルプ「[ChatGPTでの販売](https://help.shopify.com/ja/manual/online-sales-channels/agentic-storefronts/chatgpt)」も、ChatGPTを商品を見つけるための参照元として扱い、購入はオンラインストアのチェックアウトで完了する仕組みです。

## 商品が載る3つの経路

自社の商品をChatGPTの商品の検索結果に出す道はどのECの仕組みで売っているかで変わり、公式資料にある経路は3つです。

| 経路 | 手続き | 費用 | 向いている会社 |
|---|---|---|---|
| Shopify・Etsyの連携 | 申請は不要。Shopifyは要件を満たすストアで既定で有効 | ChatGPTでの販売の手数料は無い | Shopify・Etsyで売っている会社 |
| 商品フィードの申請 | 事業者向けページから申し込む。承認制で今はウェイトリスト | 申請の費用は記載なし。フィードを作る工数がかかる | 自社ECで商品数が多い会社 |
| Webの情報から載る | 手続きは無い | 掲載の費用は無い | すべての会社 |

### ① Shopify・Etsyの連携

事業者向けページには**ShopifyかEtsyで売っている場合はカタログがすでに連携されていて、追加の設定も申請も要らない**とあります。Shopifyのヘルプ「[Shopifyエージェントストアフロント](https://help.shopify.com/ja/manual/online-sales-channels/agentic-storefronts)」によると、商品はShopify Catalogを通じてChatGPTに渡り、要件を満たすストアでは最初から有効です。

ただし要件を満たさないストアの商品はShopify Catalogに入りません。[Shopify Catalogの要件](https://help.shopify.com/ja/manual/shopify-catalog/requirements)のうち、事業者が引っかかりやすいものを抜き出しました。

- Starterプラン以上で、ストアがパスワードで保護されていない
- 商品にタイトルと画像が1枚以上あり、価格が0円より高い
- 商品が非掲載や検索エンジンから非表示の設定になっていない
- アカウントのメールの認証と2段階認証が済んでいて、正規の販売実績がある

要件を満たしているかは管理画面の［販売チャネル］＞［Agentic］で確かめられ、満たしていなければ理由が表示されます。ChatGPTでの販売のヘルプには、**B2B専用の商品は対象外で、法的な表示は商品説明の先頭6,000字以内に入れる**という注意もあります。Etsy側の条件はOpenAIとEtsyのどちらの資料でも確認できませんでした。

<!-- SHOT: Shopify ヘルプ「ChatGPTでの販売」の考慮事項の箇条書き・https://help.shopify.com/ja/manual/online-sales-channels/agentic-storefronts/chatgpt ・PC・赤枠1: B2B 専用商品はサポートされていない／赤枠2: ChatGPTでの販売に関連する手数料は発生しません -->

### ② 商品フィードの申請

ShopifyやEtsyを使っていない自社ECの道は、商品フィードをOpenAIに直接送る申請です。開発者向けの「[Get Started](https://developers.openai.com/commerce/guides/get-started)」は、**フィードの受け付けは今のところ承認されたパートナーに限られる**と書いています。申し込みは事業者向けページのフォームからで、申し込み済みならウェイトリストに入っています。事業者が自分でデータをつなげる仕組みは、同じページで年内に用意する予定とされています。

送り方はファイルのアップロード（SFTP）とAPIの2つです。OpenAIが勧める組み合わせは、1日1回ファイルで全件を送って日中の変更をAPIで送る形です。セールの情報はAPIでしか送れません。[商品フィードの仕様](https://developers.openai.com/commerce/specs/file-upload/products)で必須になっている項目は9つです。

| 項目 | 中身 |
|---|---|
| item_id | 商品や色・サイズ違いごとの固定のID |
| title | 商品名（色・サイズ違いは選んだものを含める） |
| description | 事実を書いた商品説明 |
| url | 商品ページのURL |
| brand | 商品ページに出しているブランド名 |
| seller_name | 売っている事業者の名前 |
| image_url | その商品のメインの画像のURL |
| availability | 在庫あり・在庫切れ・予約などの状態 |
| price | 通常の価格と通貨のコード |

仕様にはGoogle互換のフィードの扱いも書かれているため、Google Merchant Center向けに商品データを整えている会社は、その形を土台にできるか申請のときに確かめる価値があります。フィードは広告にも使われ、広告で使う商品には別の項目を付けます。広告の出し方は[ChatGPT広告の出稿方法](/media/chatgpt-ads/)で扱っています。

### ③ Webの情報から載る

ヘルプは商品を選ぶ材料に、事業者と第三者の構造化データに加えて「その他の第三者のコンテンツ」を挙げていて、自社のフィードに限っていません。Shopifyのヘルプも、ChatGPTへのカタログの提供を止めたあとでも**Webのクロールなど別の経路で商品が表示されることがある**と書いています。

この経路で手を付けられるのは、ChatGPTの検索用のクローラーを拒否しないことです。OpenAIの「[Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)」は、**OAI-SearchBotを拒否したサイトはChatGPTの検索の回答に表示されない**と説明しています。robots.txtでOAI-SearchBotを止めていないか、商品ページの価格と在庫が読める形で出ているかを先に確かめます。フィードを出していない日本の自社ECの商品が、日本のアカウントの商品一覧に出るかどうかは試していません。

## 日本の事業者が使えるか

日本で売っている会社にとっての問題は、申し込めるかどうかより、載せた商品を日本の利用者が見られるかどうかです。公式資料を並べると、書いてあることと書いていないことがはっきり分かれます。

| 公式に書いてあること | 公式に書いていないこと |
|---|---|
| 事業者向けページ: ショッピングは米国の利用者向けに提供中。事業者と地域は順に広げる予定 | 日本の利用者に提供する時期 |
| リリースノート（2026年3月24日）: 商品の表示の改善を全利用者に順次届ける | その改善が日本のアカウントに届いたか |
| フィードの仕様: 標準のアップロードの送り先は米国。表せる国は米国・カナダ・メキシコ | 日本向けのフィードの受け付けの開始 |
| フィードの仕様: ほかの市場はOpenAIが連携と国・通貨を確認してから使う | 円の価格の扱いと審査の基準・期間 |

<!-- SHOT: OpenAI 開発者ドキュメント「Products」の Geo tagging の節・https://developers.openai.com/commerce/specs/file-upload/products ・PC・赤枠1: The standard OpenAI-format upload currently targets the US／赤枠2: target_countries の行（US, CA, and MX） -->

**フィードの仕様が今想定している送り先は米国で、日本は国の一覧にも入っていません。**リリースノートの「全利用者」と事業者向けページの「米国の利用者向け」は食い違って見えますが、両者の関係はどちらの資料にも書かれていません。日本のアカウントで商品の一覧が出るかどうかも、この記事では試していません。

<!-- SHOT: ChatGPT リリースノートの 2026年3月24日「Shopping updates in ChatGPT」・https://help.openai.com/en/articles/6825453-chatgpt-release-notes ・PC・赤枠1: rolling out to all ChatGPT users this week／赤枠2: using the Agentic Commerce Protocol (ACP) -->

ここから言えるのは、日本国内向けに売っている会社がフィードを申請しても、今はウェイトリストに入る段階だということです。Shopify Catalogの要件には国の条件が書かれていないため、日本のShopifyのストアがCatalogに入っていても、ChatGPTで誰に表示されるかは別に確かめる必要があります。**国内向けの会社が今すぐ動かせるのは③のWebの情報で、①と②は申請と要件の確認までになります。**

## 費用と手数料

ChatGPTショッピングの費用を分けるのは、どの仕組みで買われるかです。事業者向けページは**自社のサイトやアプリで買われた分には手数料がかからない**と書いています。

| 場面 | 費用 | 出どころ |
|---|---|---|
| 自社サイト・アプリでの購入 | 手数料なし | 事業者向けページ |
| Shopifyのストアへの送客 | ChatGPTでの販売の手数料なし。通常の決済手数料だけ | Shopifyのヘルプ |
| 商品フィードの申請 | 記載なし | 開発者ドキュメント |
| Instant Checkout（終了） | 販売者が完了した購入ごとに少額の手数料 | OpenAIのお知らせ（2025年9月） |
| ChatGPT広告 | 表示かクリックごと | ChatGPT広告のヘルプ |

Instant Checkoutの手数料は、2026年1月に[Shopifreaks](https://www.shopifreaks.com/shopify-confirms-a-4-fee-on-sales-made-through-chatgpt-but-whats-the-real-cost/)などがShopifyの販売者で4%と報じていました。終わった仕組みの数字なので、これから載せる判断には使いません。

お金より重くなりやすいのは社内の工数です。Shopify・Etsyは追加の作業がない一方で、自社ECのフィードには商品データの書き出しと毎日の更新、価格と在庫の変更を送るAPIの開発が要ります。

## 商品の検索結果に出ない商品

OpenAIの「[Commerce policies](https://openai.com/policies/commerce-policies)」は、ショッピングで扱わない商品とサービスを決めています。対象は商品の掲載と事業者の参加で、**OpenAIは理由を問わず掲載を外したり参加を制限したりできる**とも書かれています。日本の会社で当たりやすい区分を抜き出しました。

| 区分 | ポリシーの中身 | 当たりやすい商品 |
|---|---|---|
| 酒類 | アルコール度数0.5%を超える飲料と蒸留の道具 | 日本酒・ワイン・クラフトビール |
| サプリメント | 減量・性的な効果・筋肉づくり・デトックスなどの健康効果をうたう摂取物 | 健康食品・ダイエット食品 |
| たばこ・ニコチン | たばこ・電子たばこ・ニコチン製品と吸うための道具 | 加熱式たばこの関連品 |
| 医薬品 | 処方が要る医薬品と医療用品 | 処方薬 |
| 護身用品 | 催涙スプレー・スタンガンなど | 防犯グッズ |

<!-- SHOT: OpenAI「Commerce policies」の Drugs, medications, and supplements と Tobacco, nicotine, and alcohol の節・https://openai.com/policies/commerce-policies ・PC・赤枠1: Supplements の行／赤枠2: Alcoholic beverages (over 0.5% ABV) の行 -->

酒蔵や健康食品のメーカーは、フィードを整えても商品の検索結果には出ません。ポリシーが決めているのは商品の掲載で、回答の文の中で銘柄や会社名が挙がるかどうかには触れていません。Shopifyのヘルプも、OpenAIの禁止商品に当たる商品はChatGPTの商品の検索結果に表示されないと書いています。

## 社内で決めておくこと

ShopifyのストアならChatGPTへの連携は最初から有効なため、何も決めないまま商品が出ていることがあります。申し込みの前に、社内で次の4つを決めておくと手戻りが減ります。

<!-- SHOT: HTML図 cshp_decide.html（社内で決めておく4つのことを縦に4段）・幅640 DPR2・赤枠なし -->

### ① 商品データの持ち主

価格と在庫の新しさが販売者の並び順の材料になるため、誰がデータを更新するのかを最初に決めておくのが近道です。自社ECでフィードを送るなら、EC担当とシステムの担当のどちらが毎日の送信を持つのかが最初の論点です。Shopifyなら管理画面の商品データがそのまま渡るので、商品の登録の手順がそのままChatGPTでの見え方です。

### ② 載せたくない商品の扱い

Shopifyでは［販売チャネル］＞［Agentic］で［Shopifyによる管理を許可する］を外し、［ChatGPT］の［Shopify Catalogへのアクセス］を無効にすると、ChatGPTへのカタログの提供を止められます。それでもクロールなど別の経路で表示されることはあるとヘルプに書かれているため、**完全に出したくない商品はクロールの側の設定まで確かめます**。

### ③ 法務と表示の確認

商取引のポリシーに当たる商品が無いかを、商品の一覧と照らし合わせます。Shopifyでは法的な表示を商品説明の先頭6,000字に入れる決まりがあるため、説明が長い商品は表示の位置を見直します。

### ④ 成果の見方

Shopifyのヘルプによると、AIのチャネルからの注文は発生元が分かる形で管理画面に出ます。自社ECではGA4でChatGPTからの流入を分けて見ます。設定の手順は[GA4でAI経由の流入を見る方法](/media/ai-search-measurement/)で扱っています。

## 商品枠とAIの回答で挙がることの違い

ChatGPTの中で自社の商品や会社名が目に入る場所は、商品の検索結果だけではありません。回答の文の中で名前が挙がる場合と、回答の下の広告枠があります。

<!-- SHOT: HTML図 cshp_where.html（商品や社名が出る3つの場所を縦に3段）・幅640 DPR2・赤枠なし -->

| 項目 | 商品の検索結果 | 回答の文の中 | 広告 |
|---|---|---|---|
| 出る場所 | 回答の中の商品の一覧 | 回答の文章 | 回答の下のスポンサー枠 |
| 載せ方 | 連携・フィード・Webの情報 | 手続きは無い | 広告マネージャーで出稿 |
| 日本の利用者 | 事業者向けページは米国向けと記載 | 見られる | 日本で出稿できる |
| お金 | 掲載の費用の記載なし | 掲載料は無い | 表示かクリックごと |
| 何で決まるか | 商品データ・価格・在庫・レビュー | AIが参照するWebの情報 | 会話の内容と入札 |

商品の検索結果は型番や価格で比べられる商品に向いた枠で、申請しても日本の利用者に届く時期は書かれていません。一方で、比べて選ぶ前の「どの会社に頼むか」「どのメーカーが信頼できるか」という質問には、回答の文で答えが返ります。**高額で比べられる商材ほど、回答の文の中で名前が挙がるかどうかが買い手との最初の接点になります。**

回答の文で自社が挙がらない原因は[ChatGPTに自社が出てこない5つの原因と対策](/media/chatgpt-not-appearing/)で、EC全体の進め方は[EC・通販のAI検索対策](/media/ec-ai-search/)で扱っています。

## よくある質問

### Q. ChatGPTショッピングに商品を載せるのに費用はかかりますか？

自社のサイトやアプリで買われた分に手数料はかかりません。ShopifyのストアもChatGPTでの販売の手数料は無く、通常の決済手数料だけです。フィードの申請の費用は公式資料に書かれていません。

### Q. ChatGPTショッピングは日本でも使えますか？

事業者向けページにはショッピングは米国の利用者向けに提供中とあります。商品フィードの仕様も標準の送り先は米国で、日本を選ぶ設定はありません。日本で始まる時期は公式に書かれていません。

### Q. ChatGPTの商品フィードは日本の会社でも申請できますか？

申し込みのフォームに国の制限は書かれていませんが、受け付けは承認されたパートナーに限られ、申し込むとウェイトリストに入ります。日本向けの市場の設定はOpenAIが連携を確認してからです。

### Q. ShopifyのストアはChatGPTに自動で載りますか？

Shopify Catalogの要件を満たすストアは、最初から連携が有効です。パスワードで保護したストアや、価格が0円の商品、B2B専用の商品は対象外です。

### Q. ChatGPTのInstant Checkoutは今も使えますか？

事業者向けページの説明では、単独のInstant Checkoutから離れて購入は販売者のサイトやアプリで行います。

### Q. ChatGPT広告を出すと商品の検索結果で上位に出ますか？

出ません。ヘルプは商品の検索結果が広告でなく、OpenAIの提携の影響も受けないと書いています。広告は回答の下の別の枠に出ます。

### Q. ChatGPTショッピングにお酒や健康食品は載せられますか？

載せられません。アルコール度数0.5%を超える飲料と健康効果をうたうサプリメントは、商取引のポリシーで扱わない商品に入っています。

### Q. ChatGPTに自社の商品を載せたくない場合はどうしますか？

Shopifyなら管理画面の［販売チャネル］＞［Agentic］でChatGPTのShopify Catalogへのアクセスを無効にします。クロールで表示されることはあるため、検索用のクローラーの設定も合わせて確かめます。

## 出典

- OpenAI「[Power product discovery in ChatGPT](https://chatgpt.com/merchants/)」（2026年10月20日取得）
- OpenAI ヘルプセンター「[Shopping with ChatGPT Search](https://help.openai.com/en/articles/11128490)」（同）
- OpenAI ヘルプセンター「[ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)」2025年9月29日・11月20日・11月24日・2026年3月24日の項（同）
- OpenAI「[Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol](https://openai.com/index/buy-it-in-chatgpt/)」2025年9月29日（同）
- OpenAI Developers「[Get Started](https://developers.openai.com/commerce/guides/get-started)」「[Key concepts](https://developers.openai.com/commerce/guides/key-concepts)」（同）
- OpenAI Developers「[Products](https://developers.openai.com/commerce/specs/file-upload/products)」（同）
- OpenAI「[Commerce policies](https://openai.com/policies/commerce-policies)」（同）
- OpenAI「[Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)」（同）
- Shopify ヘルプセンター「[Shopifyエージェントストアフロント](https://help.shopify.com/ja/manual/online-sales-channels/agentic-storefronts)」「[ChatGPTでの販売](https://help.shopify.com/ja/manual/online-sales-channels/agentic-storefronts/chatgpt)」「[Shopify Catalogの要件](https://help.shopify.com/ja/manual/shopify-catalog/requirements)」（同）
- Shopifreaks「[Shopify confirms a 4% fee on sales made through ChatGPT, but what's the real cost?](https://www.shopifreaks.com/shopify-confirms-a-4-fee-on-sales-made-through-chatgpt-but-whats-the-real-cost/)」2026年1月
