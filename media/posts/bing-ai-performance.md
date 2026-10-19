---
title: 【2026年10月】Bing Webmaster ToolsのAIパフォーマンスとは？見方と注意点
date: 2026-10-20
category: AI検索対策
description: Bing Webmaster ToolsのAIパフォーマンスで、CopilotとBingのAI回答に自社ページが引用された回数を見る方法を公式の説明で整理。指標の読み方、6月に加わった4機能、クリックが出ない点、Googleのレポートとの違いまで。
cover_tag: 計測
cover_headline: BingのAIパフォーマンス
cover_sub: Copilotで引用された回数の見方
cta: llmo
---

Microsoftは2026年2月10日、Bing Webmaster Toolsに「AI Performance（AIパフォーマンス）」を公開プレビューで加えました。CopilotやBingのAIの回答で、自社のページが出典として何回示されたかを、サイトの持ち主が無料で見られるレポートです。

AIの回答から自社サイトへの動きは、GA4ではクリックされた分しか残らないため、引用されているかどうかは社内で確かめにくいままでした。この記事は公式のブログとヘルプをもとに、見られる指標と読み方、6月に加わった4つの機能、数字を社内で報告するときの注意を整理します。

:::takeaways
- **CopilotとBingのAI要約、一部の提携先で自社ページが引用された回数**を、ページ別と語句別に無料で見られる
- 引用は**クリックでも流入でもない**。提携先の名前は公表されておらず、ChatGPTやGoogleのAIの数字が入るとは書かれていない
- 2026年6月に**意図・トピック・引用シェア・比較**の4つがプレビューで加わった。Googleも8月末に生成AIの表示回数のレポートを全サイトへ広げた
:::

<!-- SHOT: AIパフォーマンスのダッシュボード（総引用数・平均引用ページ数・推移のグラフ）。Bing Webmaster Tools にログインして撮る。サイト名・URL・アカウントのアイコンは写さない・PC・赤枠なし。撮れない場合は Bing Webmaster Blog 2月の記事の図（https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview）を PC 幅で -->

## AIパフォーマンスで分かること

Bing Webmaster Toolsは、Bingの検索での表示やクロールの状態を確かめるMicrosoftの管理画面です。[紹介ページ](https://www.bing.com/webmasters/about)はSEOとGEOの無料のツールと案内しています。2月の発表によると、AIパフォーマンスはその対象をAIの回答に広げたもので、**Microsoft Copilot、BingのAIが作る要約、一部の提携先の3か所で、自社のページが出典として表示された回数を数えます**。どのURLが参照されたか、回数がどう変わったかも日ごとに追えます。

ただし、公式の説明には書かれていないことも残っています。読み違えやすい点を、公式の文に沿って分けました。

| 項目 | 公式に書いてあること | 書いていないこと |
|---|---|---|
| 対象 | Copilot・BingのAI要約・一部の提携先 | 提携先の会社名 |
| ChatGPT | 名前は出てこない | 含むかどうか |
| 数えるもの | 回答に出典として表示された回数 | 回答の中の位置や順番 |
| 提供の段階 | 公開プレビュー | 正式提供の時期 |
| 費用 | Bing Webmaster Toolsは無料のツール | AIパフォーマンスだけの料金の話は無い |

Microsoftは3月の広告主向けのブログで、自社のグラウンディング（AIが回答の根拠になるWebの情報を引く仕組み）が主要なAIアシスタントのほぼすべてを支えていると書いています。**これはMicrosoftの主張で、どのアシスタントの引用がレポートに入るのかは明かしていません**。Adobeの日本語の解説（2026年10月3日更新）は、ChatGPTなどほかのAIアシスタントはまだ含まれないと説明しています。

日本の企業がBingの数字を見る理由もあります。[Statcounter](https://gs.statcounter.com/search-engine-market-share/all/japan)の集計では、2026年9月の日本の検索エンジンの割合はGoogleが59.27%、Bingが31.41%でした。デスクトップに限るとBingが51.83%で、Googleの42.17%を上回ります。Statcounterはページビューの標本で数える集計で、検索の回数そのものではありません。それでも、**会社のパソコンで比較される商材ほど、BingとCopilotでの見え方を確かめる意味は大きくなります**。

## 見られる5つの指標

[2月の発表](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)が挙げる指標は5つです。画面のラベルは英語のままなので、英語名も並べました。

| 指標 | 意味 | 読むときの注意 |
|---|---|---|
| 総引用数（Total Citations） | 期間中にAIの回答で出典として表示された回数 | 回答の中の位置は分からない |
| 平均引用ページ数（Average Cited Pages） | 1日に引用された自社の異なるページの数の平均 | 順位や重要さを表さない |
| グラウンディングクエリ（Grounding queries） | 引用したページを取りに行くときにAIが使った語句 | 全体から抜き出した標本 |
| ページ別の引用 | URLごとの引用回数 | ページの重要さではない |
| 推移 | 日ごとの引用の増減 | 増減の理由は示さない |

いちばん使い道があるのはグラウンディングクエリです。Search Consoleの検索クエリに近い見え方ですが、利用者が打った質問ではなく、**AIが回答の材料を探すときに使った語句**を示します。自社のどのページが、どんな語句でAIに拾われているかが分かります。

3月には、[Microsoft Advertisingのブログ](https://about.ads.microsoft.com/en/blog/post/march-2026/the-ai-performance-dashboard-your-view-into-where-your-brand-appears-across-the-ai-web)で語句とページを対応づける表示が加わりました。語句を選ぶと引用されたページが、ページを選ぶとそのページを引いた語句が出ます。[ヘルプ](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c)によると語句とページで同時に絞ることはできないため、両方で見たいときはエクスポートしたファイルで突き合わせます。

## 6月に加わった4つの機能

Bingは2026年6月16日の[ブログ](https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare)で、4つの機能をプレビューとして世界で出し始めました。どれも分類にAIを使っていて、**専門性の高い分野では分類が大まかになることがある**と断っています。

### 意図（Intents）

グラウンディングクエリを、情報収集・購入検討・比較・地域・調査などの意図に分けて見せます。ヘルプの例では、ECで売る会社なら購入検討（Commercial）や比較（Comparison）の意図で引用されているかを確かめる使い方が挙がっています。調査の意図で引かれたいのに情報収集の語句ばかりなら、根拠や深さが足りないかを見直す手がかりになります。

### トピック（Topics）

関係する語句を大きなテーマにまとめます。ブログの例は、ソーラーパネル・発電効率・住宅への設置の3つの語句が1つのテーマに入る形です。トピックで絞って引用されたページを見るには、エクスポートしてから絞り込みます。

### 引用シェア（Citation Share）

ある語句で表示された出典のうち、自社サイトが占めた割合です。総引用数が多くても、同じ語句で多くのサイトが引かれていれば割合は低く出ます。**ほかのサイトのドメインは表示されず、順位でも流入の割合でもない**と公式は書いています。

### 比較（Compare）

前の期間を同じグラフに重ねます。今の期間は実線、比べる期間は点線で、直近30日と前の30日のような並べ方も、日付を選んだ比較もできます。ヘルプは、変わったことは見えても理由は示さないとしています。

## 使い始めるまでの手順

AIパフォーマンスに別の申し込みは要らず、Bing Webmaster Toolsでサイトの所有を確認すれば開けます。すでにGoogle Search Consoleでサイトを確認しているなら、インポートで確認の手順を省けます。

1. [Bing Webmaster Tools](https://www.bing.com/webmasters/about)にサインインするか、アカウントを作る
2. My Sitesの画面でImportを押し、Google Search Consoleのアカウントでサインインして許可する
3. 一覧から追加するサイトを選んでImportを押す
4. AI Performanceを開いて期間を選ぶ
5. 必要な表をエクスポートして、社内の資料に使う

<!-- SHOT: Bing Webmaster Tools の My Sites の Import ボタン。ログインして撮る・PC・赤枠1つ（Import）。サイト名とアカウント名は写さない -->

<!-- SHOT: AI Performance の画面で期間の選択と Compare の位置。ログインして撮る・PC・赤枠2つ（期間・Compare）。サイト名は写さない -->

[インポートの手順のブログ](https://blogs.bing.com/webmaster/september-2019/Import-sites-from-Search-Console-to-Bing-Webmaster-Tools)によると、1回に取り込めるのは100サイトまで、1つのアカウントで1,000サイトまでです。**新しく確認したサイトはデータが出るまで最大48時間かかる**と書かれています。Search Consoleへのアクセスを取り消すと所有の確認が外れるため、そのときはメタタグかDNSで確認し直します。

インポートを使わない場合は、XMLファイルのアップロード・メタタグ・DNSのレコードのどれかで確認します。ヘルプによるとデータは毎日更新され、少し遅れて反映されます。

## 数字を読むときの注意

AIパフォーマンスの数字は、Search Consoleの検索の数字と同じ感覚で読むとずれます。ヘルプのよくある質問から、報告の前に知っておきたい点を拾いました。

### 引用はクリックではない

ヘルプは、引用は回答で表示または参照されたことを示し、流入・クリック・利用者の反応は表さないとはっきり書いています。**引用が1,000回あっても、サイトに1,000人来たわけではありません**。クリックの数はこのレポートには無いため、流入はGA4などで別に見ます。

### 語句は要約されている

グラウンディングクエリはまとめた一般的な語句で、利用者の個別の質問や細かいロングテールの語句は出ません。引用が少ないサイトでは語句が出ないこともあり、ヘルプは罰や除外を意味しないとしています。

### 絞り方で数がずれる

データは標本で、語句とページでは集計の期間が少しずつ違うことがあります。そのため、語句で絞ってから見たページの引用数と、ページで絞ってから見た同じ語句の数が合わない場合があります。ヘルプはこれを想定どおりの動きとしています。

### 6月の急増は後から足されたデータ

2026年6月1日から引用数が急に増えたサイトが多く出ました。PinMeToの7月3日の記事によると、MicrosoftのKrishna Madhavan氏はX上で、通常のデータの埋め戻しで異常は無いと答えています。**この時期の伸びを施策の成果として報告しない**ほうが安全です。

### エクスポートはCSVで

2月にSearch Influenceが書いた記事では、取得できるのはダッシュボードからのCSVだけで、APIは予定に入っているとMicrosoftのFabrice Canel氏がXで答えていました。これは2026年2月の話で、その後のAPIの提供は公式の発表で確かめていません。

## Googleのレポートとの違い

Googleも2026年6月3日に、Search Consoleで生成AIの機能での表示を見るレポートを出しました。[Search Centralのブログ](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports)には、8月31日に世界のすべてのサイトへ広げたと追記されています。2つは数えているものが違います。

| 項目 | BingのAIパフォーマンス | Search Consoleの生成AIレポート |
|---|---|---|
| 対象 | Copilot・BingのAI要約・一部の提携先 | AIによる概要・AIモード・Discoverの生成AI機能 |
| 数えるもの | 出典として表示された回数 | URLが表示された回数 |
| 語句 | グラウンディングクエリ（標本） | ブログの項目に無い |
| 分けて見られる軸 | ページ・語句・意図・トピック | ページ・国・デバイス・日付 |
| クリック | 無い | ブログの項目に無い |
| 提供 | 2026年2月から公開プレビュー | 2026年8月31日から全サイト |

Googleのブログは、生成AIの表示回数は検索の全体のパフォーマンスにも含まれたままだと書いています。GoogleのAIの回答で表示されたかはSearch Console、Microsoft側で引用されたかはBing Webmaster Tools、実際に来た人はGA4と、**3つは数える対象が違うため、足し合わせずに並べて見ます**。GA4でAI経由の流入を分ける設定は[AI検索対策の効果の測り方](/media/ai-search-measurement/)で扱っています。

## 社内での使い方

AIパフォーマンスは費用がかからず、サイトの確認さえ済めば今日から数字が見られます。社内で回すときに決めておきたいのは、誰が持つかと、どう報告するかです。

### 誰が登録して誰が読むか

登録はサイトの所有を確認できる人の作業で、多くの会社ではSearch Consoleの権限を持つ制作会社かWeb担当になります。読むのはAIでの見え方に責任を持つマーケ担当です。**Search Consoleを制作会社のアカウントで持っている場合は、インポートの前に自社のアカウントで権限をもらっておく**と、担当が替わっても数字が途切れません。

### 月次報告に入れる形

報告では、今月CopilotとBingのAIの回答で何ページが合計何回引用されたかを、前の月と並べて書きます。比較の機能で前の期間を重ね、ページを更新した日をグラフに書き込んでおくと、更新のあとに引用が動いたかを見られます。ヘルプのとおり、比較は変化を見るもので、更新が効いたと言い切る根拠にはなりません。

### ありがちな失敗

よくある読み違いは3つです。1つ目は引用数を流入と書くこと、2つ目はグラウンディングクエリを顧客の質問そのものと読むこと、3つ目は6月の埋め戻しによる急増を成果として報告することです。どれもヘルプとMicrosoftの説明で否定されているため、報告の脚注に1行ずつ入れておくと社内の誤解を防げます。

## 引用されることと勧められることの違い

AIの回答で自社の名前が目に入る形は2つあります。回答の下や横の出典の欄にページが並ぶ場合と、回答の文の中で会社や商品が名前で挙がる場合です。**AIパフォーマンスが数えるのは前者で、回答の文で勧められたかどうかは分かりません**。

たとえば、メーカーの選び方の記事が出典に引かれた一方で、回答の文では他社の商品が勧められていることがあります。この場合でも引用数は増えるため、引用数だけを追うと、買い手の比較で選ばれているかを見誤ります。回答の文で挙がっているかは、買い手が打ちそうな質問をAIに聞いて、回答に名前が出るかを記録しないと分かりません。

お金を払って載せる枠とも別物です。ChatGPTの広告やショッピングの枠は申請や入札で載る場所で、回答の中で自然に挙がることとは決まり方が違います。広告の側は[ChatGPT広告の出稿方法](/media/chatgpt-ads/)、回答に出てこない原因は[ChatGPTに自社が出てこない5つの原因と対策](/media/chatgpt-not-appearing/)、ECの商品ページの整え方は[EC・通販のAI検索対策](/media/ec-ai-search/)で扱っています。

## よくある質問

### Q. Bing Webmaster ToolsのAIパフォーマンスは無料ですか？

無料です。Bing Webmaster Toolsの紹介ページは無料のSEO・GEOのツールと案内していて、AIパフォーマンスはサイトの所有を確認すれば追加の申し込みなしで開けます。

### Q. Bing Webmaster ToolsのAIパフォーマンスにChatGPTの引用は入りますか？

公式の説明に出てくるのは、Copilot・BingのAI要約・一部の提携先だけです。提携先の名前は公表されておらず、ChatGPTが入るとは書かれていません。Adobeの日本語の解説は、ChatGPTはまだ含まれないとしています。

### Q. Bing Webmaster ToolsのAIパフォーマンスでクリック数は分かりますか？

分かりません。ヘルプは、引用は流入やクリックを表さないとしています。AIの回答から来た人数は、GA4などのアクセス解析で別に見ます。

### Q. Bing Webmaster ToolsのAIパフォーマンスに語句が出ないのはなぜですか？

選んだ期間の引用が少ないと、グラウンディングクエリは出ないことがあります。ヘルプは罰や除外ではないと説明しています。新しく確認したサイトは、データが出るまで最大48時間かかります。

### Q. 日本のサイトでもBing Webmaster ToolsのAIパフォーマンスは使えますか？

2月の発表に国の制限の記述は無く、6月の4つの機能は世界で提供を始めたと書かれています。画面のラベルは英語のままです。

### Q. Copilotの回答に引用されるには何をすればいいですか？

Bingの発表とヘルプは、見出し・表・よくある質問で情報を読み取りやすくすること、例やデータと出典で裏づけること、内容を新しく保つことを挙げています。更新をすぐ伝える仕組みとしてIndexNowを、店舗のある会社にはBing Places for Businessへの登録を勧めています。robots.txtで止めたページは、その指定が尊重されます。

### Q. Google Search ConsoleでAIによる概要の表示回数は見られますか？

見られます。Search Centralのブログによると、AIによる概要とAIモードでの表示回数を見るレポートは2026年8月31日に世界のすべてのサイトへ広がりました。ブログが挙げる項目は表示回数・ページ・国・デバイス・日付です。

## 出典

- Bing Webmaster Blog「[Introducing AI Performance in Bing Webmaster Tools Public Preview](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)」2026年2月10日（2026年10月20日取得）
- Bing Search Blog「[New AI Visibility Insights in Bing Webmaster Tools: Intents, Topics, Citation Share, Compare](https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare)」2026年6月16日（同）
- Bing Webmaster Tools ヘルプ「[AI Performance](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c)」（同）
- Microsoft Advertising Blog「[The AI Performance dashboard](https://about.ads.microsoft.com/en/blog/post/march-2026/the-ai-performance-dashboard-your-view-into-where-your-brand-appears-across-the-ai-web)」2026年3月23日（同）
- Bing Webmaster Blog「[Easily Verify Your Site in Bing Webmaster Tools by Importing from Google Search Console](https://blogs.bing.com/webmaster/september-2019/Import-sites-from-Search-Console-to-Bing-Webmaster-Tools)」2025年6月更新（同）
- Bing Webmaster Tools「[About](https://www.bing.com/webmasters/about)」（同）
- Google Search Central Blog「[Introducing Search Generative AI performance reports in Search Console](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports)」2026年6月3日（同）
- Statcounter「[Search Engine Market Share Japan](https://gs.statcounter.com/search-engine-market-share/all/japan)」2026年9月（同）
- Adobe Experience League「[Bing ウェブマスターツール AI パフォーマンスレポート](https://experienceleague.adobe.com/ja/docs/brand-visibility-learn/tutorials/measurement/bing-webmaster-tools-ai-performance-report)」2026年10月3日更新（同）
- PinMeTo「[Bing's AI citation surge was backfill, not new visibility](https://www.pinmeto.com/news/bing-ai-performance-backfill-citation-share-2026/)」2026年7月3日（同）
- Search Influence「[Inside Bing's New AI Performance Report](https://www.searchinfluence.com/blog/bing-ai-performance-report-copilot-citations/)」2026年2月（同）
