---
title: 【2026年10月】GoogleビジネスプロフィールのAI対策とは？AIモード・口コミ要約・Gemini連携
date: 2026-10-19
category: AI検索対策
description: GoogleビジネスプロフィールのAI対策を公式ヘルプで整理。AIモードやマップの口コミ要約で店舗情報が使われる場面、Googleが書いていないこと、Gemini連携の条件、社内で決めることと失敗例まで。
cover_tag: 店舗の対策
cover_headline: ビジネスプロフィールとAI
cover_sub: AIモード・口コミ要約・Gemini連携
---

Googleは2026年8月7日、Googleマップで条件を話して店を探す「マップに相談」を日本で始めました。検索のAIモードやマップのクチコミの要約も、来店や問い合わせの前に読まれる場所になっています。

店舗や事務所を持つ会社には、MEO業者から「AI対策」の提案が届く一方で、Googleビジネスプロフィール（以下 GBP）の何を直せばよいのかは見えにくいままです。この記事は2026年10月19日に取得したGoogleのヘルプをもとに、**AIがGBPの情報を使う場面と、会社として決めること**を整理します。

:::takeaways
- Googleの検索セントラルはAIによる概要とAIモードに**特別な最適化は要らない**としたうえで、GBPの情報を最新に保つことを基本のひとつに挙げている
- マップのクチコミの要約やプレイス トピックは**クチコミから作られ、店舗側は書き換えられない**。できるのは情報を埋めること・返信すること・誤りを報告すること
- GeminiからGBPを管理する機能は、**オーナー確認済みのプロフィールを1つだけ持つ個人のGoogleアカウント**が条件。複数店舗の管理や仕事用のアカウントでは使えない
:::

## AIが店舗情報を使う4つの場面

「駅の近くで個室のある居酒屋」「土曜に診てもらえる歯医者」のような相談は、検索窓にもマップにも入力されます。Googleのヘルプとブログを並べると、日本でGBPの情報がAIの答えに入りうる場面は次の4つです。

<figure class="post-figure"><img src="/media/images/gbp-ai-search/01_fig_where.png" alt="AIが店舗情報を使う4つの場面の図。検索のAIモード、マップの場所のヒント、クチコミの要約、マップに相談" loading="lazy"></figure>

| 場面 | AIが使う情報 | 日本での提供 |
|---|---|---|
| 検索のAIモードとAIによる概要 | インデックスされたページ。検索セントラルはGBPを最新に保つことを基本に挙げる | AIモードは[2025年9月に日本語で提供開始](https://blog.google/intl/ja-jp/products/explore-get-answers/ai-mode-search/) |
| マップの場所のヒントと質問 | ヒントはクチコミとオンライン上の情報、質問は場所に関する情報 | 2026年2月13日の発表で日本のAndroidとiOSに |
| マップのクチコミの要約 | ユーザーのクチコミ | 同じ発表で日本のAndroidとiOSに |
| マップに相談 | Googleマップの最新情報 | 2026年8月7日から数週間かけて順に |

マップの場所のヒントは、Google Japan Blogの[2026年2月13日の記事](https://blog.google/intl/ja-jp/products/explore-get-answers/maps-gemini-tips/)が紹介した機能です。レストランやホテルのページを下にスクロールすると、クチコミやオンラインの情報をGeminiが分析した予約方法や駐車のコツが出ます。同じ記事はお店のページで「無料駐車場はありますか？」と尋ねる使い方と、Geminiによるクチコミの要約も日本で使えるとしています。

<figure class="post-figure"><img src="/media/images/gbp-ai-search/02_blog_maps_tips.png" alt="Google Japan Blog の Gemini で Google マップの場所の詳細を確認する節" loading="lazy"><figcaption>GeminiでGoogleマップの場所の詳細を確認する（Google Japan Blog）</figcaption></figure>

GMO TECHが[2026年8月6日に公表した調査](https://prtimes.jp/main/html/rd/p/000005478.000000136.html)（第三者の実測）は、日本語のローカル検索約10万9,500クエリ・延べ約44万回答のうち約7割で、Google上の店舗カードを参照したとみられる回答があったとしています。店舗カードにはGBPのほか、公式サイトなどの情報も入ります。業種の差は大きく、7月4日時点で引用に占める店舗情報の割合は居酒屋が87.5％、フィットネスが9.8％でした。Googleが公表した数字ではありませんが、**店を探す相談では、AIモードの答えにGoogle上の店舗情報が使われている**ことを示す結果です。

利用者の側から見たマップのGeminiの入口と設定は、[GoogleマップのGeminiの記事](/media/google-maps-gemini/)にまとめています。

## Googleが書いていることと書いていないこと

業者の提案資料にはAIが重視する項目を言い切るものもあります。Googleの公式ページで確かめられる範囲を、書いてあることと書いていないことに分けました。

| 論点 | 公式に書いてあること | 書いていないこと |
|---|---|---|
| AI機能に出る条件 | 追加の要件も特別な最適化も不要。インデックス登録とスニペットの表示が前提 | AIモードがどの店を選ぶかの基準 |
| GBPの役割 | SEOの基本のひとつとして、GBPとMerchant Centerの情報を最新に保つ | GBPのどの項目をAIが重く見るか |
| ローカル検索の順位 | 主に関連性・距離・知名度を組み合わせて決める | AIモードの店の並びが同じ仕組みか |
| クチコミの要約 | ユーザーのクチコミだけをもとにAIが作る（開発者向けドキュメント） | 要約に入るクチコミの選び方 |
| 測り方 | AI機能での表示はSearch Consoleの「ウェブ」に含まれる | GBPの閲覧数のうちAI経由の内訳 |

1・2行目はGoogle 検索セントラルの「[AI 機能とウェブサイト](https://developers.google.com/search/docs/appearance/ai-features?hl=ja)」、3行目はGBPヘルプの「[Google のローカル検索結果のランキングを改善するヒント](https://support.google.com/business/answer/7091?hl=ja)」、4行目はGoogle Maps Platform の開発者向けドキュメント「[AI によるクチコミの要約](https://developers.google.com/maps/documentation/places/web-service/review-summaries?hl=ja)」によります。検索セントラルはAI向けの新しいファイルや特別な schema.org の構造化データも不要としています。

<figure class="post-figure"><img src="/media/images/gbp-ai-search/03_help_ai_features.png" alt="Google 検索セントラルの AI 機能とウェブサイトのページ。AI 機能に表示されるための追加の要件は無いと書かれている" loading="lazy"><figcaption>AI 機能とウェブサイト（Google 検索セントラル）</figcaption></figure>

右の列を埋める説明は、業者の経験則か推測です。**社内で予算を通すときに根拠を示せるのは、ヘルプが挙げる基本の項目のほう**でしょう。ウェブサイト側の手入れは[AIによる概要の記事](/media/ai-overviews-guide/)の企業の対策の節で扱っています。

## GBPで整える5つの項目

GBPヘルプは情報が充実して正確なほどローカル検索結果に出やすいと説明しています。AIに読まれるかをGoogleは項目ごとに書いていないため、ローカル検索のヘルプが勧める項目から埋めていきます。

### ① ビジネスの種類とサービス

ヘルプの説明によると関連性とは、検索語とプロフィールが合う度合いのことです。ヘルプが関連性の例に挙げるのはビジネスの種類（カテゴリ）です。工務店なら注文住宅やリフォーム、クリニックなら診療の内容のように、**サービスの項目もあわせて埋めておくと、検索語とプロフィールを照らし合わせる手がかりが増えます**。

### ② 営業時間と特別営業時間

[マップに相談を紹介したブログ](https://blog.google/intl/ja-jp/products/connect-communicate/japanese-ask-maps/)の質問の例には「今夜使える」のような時刻の条件が入っています。ヘルプも特別営業時間を含めた入力を勧めており、祝日や年末年始の時間まで入れておけば、時間の条件がついた相談にも答えられる情報がそろいます。

### ③ 属性とメニュー

駐車場やWi-Fiの有無などの属性は、ヘルプが入力を勧める項目です。マップの場所への質問の例も「テラス席はありますか？」「無料駐車場はありますか？」でした。**来店前に聞かれそうな条件は属性の項目でも入れておきます**。飲食店はメニューの項目も使えます。

### ④ 説明文

説明文はAIに候補を書かせることもできます。GBPヘルプの「[ビジネス プロフィールの説明を管理する](https://support.google.com/business/answer/13682007?hl=ja)」では、プロフィールやウェブサイトの情報をもとに候補が出る手順を次のように案内しています。

1. ビジネス プロフィールに移動する
2. ［プロフィールを編集］を押す
3. ［説明］の横の編集アイコンを押す
4. ［説明の候補を見る］を押す
5. 候補を確かめて［使用］を押し、直してから［保存］を押す

<figure class="post-figure post-figure--sp"><img src="/media/images/gbp-ai-search/04_help_description_sp.png" alt="ビジネス プロフィールのヘルプの AI を活用してビジネスの説明を生成する手順" loading="lazy"><figcaption>AI を活用してビジネスの説明を生成する手順（ビジネス プロフィール ヘルプ）</figcaption></figure>

この手順はヘルプの記載によるもので、nitoは実際の画面では試していません。ヘルプは一部の地域と言語だけの機能とし、生成された文が正確か確認するよう求めています。変更の反映は通常10分ほどですが、30営業日ほどかかる場合もあるとのことです。書く中身は別のヘルプ「[Google マップに表示されるビジネスの概要について](https://support.google.com/business/answer/6088158?hl=ja)」の案内どおり、価格やセールではなく商品やサービスと他にない特長にします。

### ⑤ 写真と動画

ランキングのヘルプは写真や動画で商品やサービスを紹介するよう勧めています。後で触れるGeminiのビジネス ノートブックも、店の外観などの写真を足すことを提案の例に挙げています。

## クチコミとAIの要約

マップで店を短く紹介する文は、店舗側が書いたものとは限りません。GBPヘルプの「Google マップに表示されるビジネスの概要について」は、マップの概要を説明・編集者による概要・クチコミ抜粋の3種類に分けています。

**編集者による概要は店舗側で編集できず、プレイス トピックやクチコミ抜粋はクチコミから作られます**。Geminiによるクチコミの要約も、Google Maps Platform の開発者向けドキュメントではユーザーのクチコミだけをもとにした要約で、「Gemini で要約」と表示されます。概要が無関係な場所に結びついている場合や、提供していないサービスに触れている場合は、マップアプリの［概要を報告］から報告できます。

<figure class="post-figure"><img src="/media/images/gbp-ai-search/05_help_overview.png" alt="ビジネス プロフィールのヘルプのビジネスの概要のページ。ビジネスの説明と編集者による概要の説明" loading="lazy"><figcaption>ビジネスの概要の種類（ビジネス プロフィール ヘルプ）</figcaption></figure>

### 返信と依頼の仕方

ランキングのヘルプによると、好意的なクチコミや有用な返信があるとビジネスが目に留まりやすくなります。要約を変えられるのはクチコミの中身だけなので、**来店した人に具体的な体験を書いてもらう依頼と、全件への返信**が店舗側の打てる手です。クチコミを頼むリンクやQRコードの作り方は、GBPヘルプの「[リンクまたは QR コードを作成してクチコミをリクエストする](https://support.google.com/business/answer/16816815?hl=ja)」にあります。

### やってはいけない依頼

Googleマップの「[禁止または制限されているコンテンツ](https://support.google.com/contributionpolicy/answer/7400114?hl=ja)」は、割引や無料の商品と引き換えにクチコミを頼む行為を禁じています。否定的なクチコミの投稿を妨げることや、肯定的なクチコミだけを選んで募ることも禁止です。一方、特典をつけずに実体験の投稿を促すことは認められています。

<figure class="post-figure"><img src="/media/images/gbp-ai-search/06_policy_reviews.png" alt="マップのユーザー投稿コンテンツのポリシーの虚偽のエンゲージメントの節" loading="lazy"><figcaption>虚偽のエンゲージメントの禁止（マップのユーザー投稿コンテンツのポリシー）</figcaption></figure>

## Gemini連携で変わる運用

2026年6月10日、GoogleはGeminiアプリにGBPを接続する機能を[公式ブログ](https://blog.google/innovation-and-ai/products/gemini-app/gemini-features-for-businesses/)で発表しました。GBPヘルプの「[Google ビジネス プロフィールを Gemini ウェブアプリで管理する](https://support.google.com/business/answer/17142585?hl=ja&co=GENIE.Platform%3DDesktop)」によると、接続するとGeminiで次の作業ができます。

- 営業時間・連絡先・予約などのリンク・属性の更新
- クチコミへの返信の下書きと投稿の作成
- クチコミの要約とフィードバックのテーマの整理
- インプレッション数・ウェブサイトへの誘導数・検索キーワードの確認

接続するとビジネス ノートブックも作れ、不足している情報の更新や写真の追加をGeminiが提案します。どちらも段階的な提供で、すぐには使えない場合もあります。

### 接続の条件と会社への影響

会社でGBPを持つときの運用に、条件の多くが直接かかわります。

| ヘルプの条件 | 会社で起きること |
|---|---|
| オーナー確認済みのGBPを1つだけ所有・管理している | 複数の店舗を持つアカウントでは使えない。複数社を受け持つ代理店の担当者も同じ |
| GBPにつながった個人のGoogleアカウントでログインする | 仕事用・学校用のアカウントは不可。会社のプロフィールを社員個人のアカウントで扱うことになる |
| ［アクティビティの保存］がオン | Geminiの会話が保存される設定が前提 |
| 欧州経済領域と英国を除く。日本語に対応 | 日本の店舗は対象 |
| gemini.google.com だけで使える | スマホのGeminiアプリでは使えない。スマホでもブラウザで gemini.google.com を開けば使える |

<figure class="post-figure"><img src="/media/images/gbp-ai-search/07_help_gemini_req.png" alt="ビジネス プロフィールのヘルプの Gemini ウェブアプリで管理するための必要なもの。プロフィールを1つのみ所有または管理していることなど" loading="lazy"><figcaption>Gemini でビジネス プロフィールを管理するのに必要なもの（ビジネス プロフィール ヘルプ）</figcaption></figure>

**最初の判断は、会社のプロフィールを社員個人のGoogleアカウントに結びつけてよいか**です。GBPヘルプの「[ビジネス プロフィールのオーナーと管理者を管理する](https://support.google.com/business/answer/3403100?hl=ja)」では、オーナーはユーザーの追加と削除やプロフィールの削除までできます。管理者はそれ以外の編集はほぼ同じようにできるため、Geminiを使う担当者を管理者にとどめ、オーナーは経営者が持つ分け方もあります。担当者が辞めるときに権限を外す手順は、接続の前に決めておきましょう。

## AIモードの自動通話と詳細設定

Google 検索ヘルプの「[AI モードを使用してローカルの在庫状況と価格を確認する](https://support.google.com/websearch/answer/17104441?hl=ja&co=GENIE.Platform%3DDesktop)」によると、店のウェブサイトに予約枠や在庫が載っていない場合、AIモードは利用者の代わりに店へ電話して確かめます。GBPヘルプの「[Google からビジネスへの自動通話またはテキスト メッセージについて](https://support.google.com/business/answer/7690269?hl=ja)」はこの通話を一部の地域と言語に限った提供とし、英語で動いており、2026年10月19日時点で日本で使えるとの記載はありません。

自動通話を受けるかどうかは、GBPの詳細設定で決められます。GBPヘルプの「[プロフィールの詳細設定を管理する](https://support.google.com/business/answer/10737668?hl=ja)」では、その他アイコンから［ビジネス プロフィールの設定］の［詳細設定］に進むと、自動通話とテキスト メッセージの許可・拒否と、ほかのGoogleのサービスとのデータ共有を切り替えられます。

<figure class="post-figure"><img src="/media/images/gbp-ai-search/08_help_settings.png" alt="ビジネス プロフィールのヘルプの詳細設定の使用可能な設定。Google からの自動通話とテキスト メッセージなど" loading="lazy"><figcaption>使用可能な詳細設定（ビジネス プロフィール ヘルプ）</figcaption></figure>

## 社内で決めること

GBPそのものは無料ですが、GBPヘルプの「[サードパーティと連携してビジネス プロフィールを管理するためのヒント](https://support.google.com/business/answer/7163406?hl=ja)」によると、管理を外部に頼む場合は多くが有料です。費用をかける前に、次の6つを社内で決めておくと、業者の提案を比べやすくなります。

<figure class="post-figure"><img src="/media/images/gbp-ai-search/09_fig_decide.png" alt="社内で決める6つのことの図。誰のアカウントで持つか、Geminiに接続するか、誰が情報を直すか、クチコミの頼み方、自動通話を受けるか、何で測るか" loading="lazy"></figure>

| 決めること | 決める人の例 | 根拠になる公式ページ |
|---|---|---|
| メインのオーナーを誰のアカウントにするか | 経営者 | オーナーと管理者の役割 |
| Geminiに接続するか | 経営者とマーケ担当 | Gemini ウェブアプリで管理する |
| 営業時間・属性・写真を誰が直すか | 店舗の責任者 | ランキングのヒント |
| クチコミの頼み方と返信の決まり | マーケ担当 | 投稿のポリシー |
| 自動通話を許可するか | 店舗の責任者 | 詳細設定 |
| 何で効果を測るか | マーケ担当 | パフォーマンス・Search Console |

### 効果の測り方

GBPヘルプの「[ビジネス プロフィールのパフォーマンスとインサイトを確認する](https://support.google.com/business/answer/9918094?hl=ja)」では、検索とマップでのプロフィールの閲覧数・クリック数などが見られます。[Googleアナリティクスにつなぐ](https://support.google.com/analytics/answer/16930347?hl=ja)こともできますが、どちらのヘルプにもAIモードから見られた分を分ける項目の説明はありません。

ウェブサイト側はAI機能での表示もSearch Consoleの検索タイプ「ウェブ」に含まれると検索セントラルが説明しています。**AI経由の数字が取れない部分は、自社の条件でAIモードとマップに相談に質問し、名前が挙がるかを毎月記録する**のが現実的な測り方です。

業種ごとの考え方は[飲食店](/media/restaurant-ai-search/)・[クリニック](/media/clinic-ai-search/)・[建設・リフォーム](/media/construction-ai-search/)・[不動産](/media/real-estate-ai-search/)の記事にあります。

## 失敗しやすい例

AI対策のつもりで、GBPのガイドラインやポリシーに触れてしまう例を3つ挙げました。

### ビジネス名に地域名やサービス名を足す

「[Google に掲載するビジネス情報のガイドライン](https://support.google.com/business/answer/3038177?hl=ja)」は、ビジネス名に看板や書類で使っている実際の名称を使うよう求めています。不要な情報を名前に入れると、プロフィールが停止される場合もあるため注意が必要です。業種を突然大きく変えるのも避けたい操作です。Googleは[2025年5月27日の発表](https://blog.google/intl/ja-jp/products/explore-get-answers/google-business-profiles-ai-fake-reviews/)で、カテゴリが突然カフェから配管工に変わるような不審な編集をGeminiで見分けているとしました。

### 業者を同時に何社も入れる

業者と組むなら一度に1社ずつ試すのが、GBPヘルプの勧める進め方です。同じヘルプはGoogleでの上位表示を保証する業者や、Googleの社員を名乗る業者を注意すべき兆候に挙げています。ヘルプはAIモードに触れていませんが、AIモードで必ず上位に出すという約束も根拠を示せない点は同じです。

### サイトとGBPで情報が食い違う

GBPヘルプの「[Google がビジネス プロフィールとローカル検索結果の情報を入手する方法と、それらの用途](https://support.google.com/business/answer/2721884?hl=ja)」は、GBPの情報源に公式サイトなどの公開情報も挙げています。営業時間や料金がサイトとGBPで違うと、どちらが正しいか利用者には判断できません。片方を直したら、もう片方も同じ日に直します。

## よくある質問

### GoogleビジネスプロフィールにAI対策は必要ですか？

AI専用の設定はありません。検索セントラルはAIによる概要とAIモードに特別な最適化は要らないとし、GBPの情報を最新に保つことを基本に挙げています。業種・営業時間・属性・説明文・写真を正確に埋めることが、Googleが挙げる基本です。

### ビジネスプロフィールはAIモードで使われますか？

GoogleはAIモードがGBPのどの項目をどう使うかを公表していません。第三者のGMO TECHの調査は、日本語のローカル検索の延べ約44万回答のうち約7割で、Google上の店舗カードを参照したとみられる回答があったとしています。店舗カードにはGBPのほか、公式サイトなどの情報も入ります。

### Googleマップのクチコミの要約は直せますか？

店舗側で書き換える方法はヘルプに載っていません。編集者による概要も編集できず、要約やプレイス トピックの元はクチコミです。無関係な内容が出ている場合は、マップアプリの［概要を報告］から報告できます。

### ビジネスプロフィールの説明文はAIで作れますか？

作れます。編集画面の［説明の候補を見る］で候補が出ますが、一部の地域と言語だけの機能で、ヘルプは正確さを確かめてから使うよう求めています。

### ビジネスプロフィールはGeminiで管理できますか？

条件つきで可能です。gemini.google.com でGBPを接続すると、営業時間の更新やクチコミへの返信の下書きを頼めます。提供は段階的で、まだ出ないアカウントもある点に注意が必要です。

### 複数店舗のプロフィールもGeminiにつなげますか？

2026年10月19日時点のヘルプでは、つなげません。条件はオーナー確認済みのGBPを1つだけ所有または管理していることです。仕事用のGoogleアカウントも対象外です。

### ビジネスプロフィールでAI経由の数は分かりますか？

パフォーマンスの画面のヘルプに、AIモードから見られた分を分ける説明はありません。閲覧数・通話・ルートの全体の動きを見ながら、AIモードとマップに相談に自社の条件で質問して、名前が挙がるかを記録します。

### ビジネスプロフィールの管理を業者に頼めますか？

頼めます。GBPヘルプは経験のある業者を選ぶこと、一度に1社と組むこと、パフォーマンスの数字を共有してもらうことを勧めています。上位表示を保証する業者は注意すべき兆候のひとつです。

## 出典

いずれも2026年10月19日に取得しました。

- Google 検索セントラル「[AI 機能とウェブサイト](https://developers.google.com/search/docs/appearance/ai-features?hl=ja)」
- Google ビジネス プロフィール ヘルプ
  - 「[Google のローカル検索結果のランキングを改善するヒント](https://support.google.com/business/answer/7091?hl=ja)」
  - 「[Google マップに表示されるビジネスの概要について](https://support.google.com/business/answer/6088158?hl=ja)」
  - 「[ビジネス プロフィールの説明を管理する](https://support.google.com/business/answer/13682007?hl=ja)」
  - 「[Google ビジネス プロフィールを Gemini ウェブアプリで管理する](https://support.google.com/business/answer/17142585?hl=ja&co=GENIE.Platform%3DDesktop)」
  - 「[ビジネス プロフィールのオーナーと管理者を管理する](https://support.google.com/business/answer/3403100?hl=ja)」
  - 「[プロフィールの詳細設定を管理する](https://support.google.com/business/answer/10737668?hl=ja)」
  - 「[Google からビジネスへの自動通話またはテキスト メッセージについて](https://support.google.com/business/answer/7690269?hl=ja)」
  - 「[リンクまたは QR コードを作成してクチコミをリクエストする](https://support.google.com/business/answer/16816815?hl=ja)」
  - 「[ビジネス プロフィールのパフォーマンスとインサイトを確認する](https://support.google.com/business/answer/9918094?hl=ja)」
  - 「[サードパーティと連携してビジネス プロフィールを管理するためのヒント](https://support.google.com/business/answer/7163406?hl=ja)」
  - 「[Google に掲載するビジネス情報のガイドライン](https://support.google.com/business/answer/3038177?hl=ja)」
  - 「[Google がビジネス プロフィールとローカル検索結果の情報を入手する方法と、それらの用途](https://support.google.com/business/answer/2721884?hl=ja)」
- マップユーザーの投稿コンテンツに関するポリシー「[禁止または制限されているコンテンツ](https://support.google.com/contributionpolicy/answer/7400114?hl=ja)」
- Google Japan Blog「[Google 検索における「AI モード」を日本語で提供開始](https://blog.google/intl/ja-jp/products/explore-get-answers/ai-mode-search/)」（2025年9月9日）
- Google 検索ヘルプ「[AI モードを使用してローカルの在庫状況と価格を確認する](https://support.google.com/websearch/answer/17104441?hl=ja&co=GENIE.Platform%3DDesktop)」
- アナリティクス ヘルプ「[Google ビジネス プロフィール（GBP）を Google アナリティクスに接続する](https://support.google.com/analytics/answer/16930347?hl=ja)」
- Google Maps Platform「[AI によるクチコミの要約](https://developers.google.com/maps/documentation/places/web-service/review-summaries?hl=ja)」
- Google Japan Blog「[Google マップの新機能で、お出かけをもっとスムーズに](https://blog.google/intl/ja-jp/products/explore-get-answers/maps-gemini-tips/)」（2026年2月13日）
- Google Japan Blog「[Google マップの新機能「マップに相談」を日本で提供開始](https://blog.google/intl/ja-jp/products/connect-communicate/japanese-ask-maps/)」（2026年8月7日）
- Google Japan Blog「[AI を活用した Google マップのクチコミなどの信頼維持に向けた取り組み](https://blog.google/intl/ja-jp/products/explore-get-answers/google-business-profiles-ai-fake-reviews/)」（2025年5月27日）
- Google Blog「[Save time and grow your business with new Gemini tools](https://blog.google/innovation-and-ai/products/gemini-app/gemini-features-for-businesses/)」（2026年6月10日）
- GMO TECH「[AIがお店を探すとき、頼りにしている情報は何か](https://prtimes.jp/main/html/rd/p/000005478.000000136.html)」（PR TIMES、2026年8月6日）
