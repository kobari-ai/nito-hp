---
title: 【2026年10月】Bing Webmaster ToolsのAIパフォーマンスとは？見方と注意点
date: 2026-10-21
category: AI検索対策
description: Bing Webmaster ToolsのAIパフォーマンスで、CopilotとBingのAI回答に自社ページが引用された回数を見る方法を公式の説明で整理。指標の読み方、6月の4機能、Googleのレポートとの違いまで。
cover_tag: 計測
cover_headline: BingのAIパフォーマンス
cover_sub: Copilotで引用された回数の見方
cta: llmo
---

Microsoftは2026年2月10日、Bing Webmaster Toolsに「AI Performance（AIパフォーマンス）」を公開プレビューで加えました。CopilotやBingのAIの回答で、自社のページが出典として何回示されたかを、サイトの管理者が無料で見られるレポートです。

AIの回答から自社サイトへの動きは、GA4ではクリックされた分しか残らないため、引用されているかどうかは社内で確かめにくいままでした。この記事は公式のブログとヘルプをもとに、見られる指標と読み方、6月に加わった4つの機能、数字を社内で報告するときの注意を整理します。

:::takeaways
- **CopilotとBingのAI要約、一部の提携先で自社ページが引用された回数**を、ページ別と語句別に無料で見られる
- 引用は**クリックでも流入でもない**。提携先の名前は公表されておらず、ChatGPTやGoogleのAIの数字が入るとは書かれていない
- 2026年6月に**意図・トピック・引用シェア・比較**の4つがプレビューで加わった。Googleも8月末に生成AIの表示回数のレポートを全サイトへ広げた
:::

<figure class="post-figure"><img src="/media/images/bing-ai-performance/bwai_01_three.png" alt="AIの数字は3か所で別々に見る。Bing Webmaster ToolsはCopilotなどで出典に引かれた回数、Google Search ConsoleはAIによる概要などでの表示回数、GA4はAIの回答から実際にサイトに来た人" loading="lazy"></figure>

## AIパフォーマンスで分かること

Bing Webmaster Toolsは、Bingの検索での表示やクロールの状態を確かめるMicrosoftの管理画面です。[紹介ページ](https://www.bing.com/webmasters/about)はSEOとGEOの無料のツールと案内しています。2月の発表によると、AIパフォーマンスはその対象をAIの回答に広げたもので、**Microsoft Copilot、BingのAIが作る要約、一部の提携先の3か所で、自社のページが出典として表示された回数を数えます**。どのURLが参照されたか、回数がどう変わったかも日ごとに追えます。

公式の説明には書かれていないことも残っているため、読み違えやすい点を公式の文に沿って分けました。

| 項目 | 公式に書いてあること | 書いていないこと |
|---|---|---|
| 対象 | Copilot・BingのAI要約・一部の提携先 | 提携先の会社名 |
| ChatGPT | 名前は出てこない | 含むかどうか |
| 数えるもの | 回答に出典として表示された回数 | 回答の中の位置や順番 |
| 提供の段階 | 公開プレビュー | 正式提供の時期 |
| 費用 | Bing Webmaster Toolsは無料のツール | AIパフォーマンス単体の料金の記載 |

Microsoftは3月の広告主向けのブログで、自社のグラウンディング（AIが回答の根拠になるWebの情報を引く仕組み）が主要なAIアシスタントのほぼすべてを支えていると書いています。**これはMicrosoftの主張で、どのアシスタントの引用がレポートに入るのかは明かしていません**。Adobeの日本語の解説（2026年10月3日更新）も、対象はCopilotの引用とAIの要約だけで、ChatGPTなどほかのAIアシスタントはまだ含まれないと説明しています。

日本の企業がBingの数字を見る理由もあります。[Statcounter](https://gs.statcounter.com/search-engine-market-share/all/japan)の検索結果から来た閲覧の標本による集計（2026年10月21日時点）では、2026年9月の日本の検索エンジンの割合はGoogleが59.27%、Bingが31.41%でした。デスクトップに限るとBingが51.83%で、Googleの42.17%を上回ります。検索の回数そのものではありませんが、**会社のパソコンで比較される商材ほど、BingとCopilotでの見え方を確かめる意味は大きくなります**。

## 見られる5つの指標

[2月の発表](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)が挙げる指標は5つです。画面で探しやすいよう英語名も並べました。

| 指標 | 意味 | 読むときの注意 |
|---|---|---|
| 総引用数（Total Citations） | 期間中にAIの回答で出典として表示された回数 | 回答の中の位置は分からない |
| 平均引用ページ数（Average Cited Pages） | 1日に引用された自社の異なるページの数の平均 | 順位や重要度を表さない |
| グラウンディングクエリ（Grounding queries） | 引用したページを取りに行くときにAIが使った語句 | 全体から抜き出した標本 |
| ページ別の引用 | URLごとの引用回数 | ページの重要度ではない |
| 推移 | 日ごとの引用の増減 | 増減の理由は示さない |

<figure class="post-figure"><img src="/media/images/bing-ai-performance/bwai_02_dashboard.png" alt="Bing Webmaster ToolsのAI Performanceの画面の例。期間の切り替え、総引用数と平均引用ページ数、日ごとの推移のグラフ、データは全体の標本という注記が並ぶ" loading="lazy"><figcaption>Bing Webmaster Blog（2026年2月10日）に載ったAI Performanceの画面の例</figcaption></figure>

いちばん使い道があるのはグラウンディングクエリです。Search Consoleの検索クエリに近い見え方ですが、利用者が入力した質問ではなく、**AIが回答の根拠を探すときに使った語句**を示します。自社のどのページが、どんな語句でAIに拾われているかが分かります。

[Microsoft Advertisingのブログ](https://about.ads.microsoft.com/en/blog/post/march-2026/the-ai-performance-dashboard-your-view-into-where-your-brand-appears-across-the-ai-web)によると、3月には語句とページを対応づける表示が加わりました。語句を選ぶと引用されたページが、ページを選ぶとそのページを引いた語句が出ます。[ヘルプ](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c)によると語句とページで同時に絞ることはできないため、両方で見たいときはエクスポートしたファイルで突き合わせます。

## 6月に加わった4つの機能

Bingは2026年6月16日の[ブログ](https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare)で、4つの機能をプレビューとして世界で出し始めました。**意図とトピックはAIの分類で、プレビューの間は専門性の高い分野でラベルが大まかになることがある**と断っています。

### 意図（Intents）

グラウンディングクエリを情報収集・購入検討・比較・地域・調査などの意図に分けて見せる機能です。ECで売るサイトなら購入検討（Commercial）や比較（Comparison）の意図で引用されているかを確かめる使い方を、ヘルプは例に挙げています。調査の意図で引かれたいのに情報収集の語句ばかりなら、根拠や深さが足りないかを見直す手がかりになります。

### トピック（Topics）

関係する語句を大きなテーマにまとめる機能です。ブログではソーラーパネル・発電効率・住宅への設置の3つの語句を、1つのテーマにまとめる例が挙がっています。トピックで絞って引用されたページを見るには、エクスポートしてから絞り込みます。

### 引用シェア（Citation Share）

ある語句で表示された出典のうち、自社サイトが占めた割合です。総引用数が多くても、同じ語句で多くのサイトが引かれていれば割合は低く出ます。**ほかのサイトのドメインは表示されず、順位でも流入の割合でもない**と公式は書いています。

### 比較（Compare）

前の期間を同じグラフに重ねる機能です。今の期間は実線、比べる期間は破線で、直近30日と前の30日のような並べ方も、日付を選んだ比較もできます。ただし変化の理由までは示さないと、ヘルプは注記しています。

## 使い始めるまでの手順

AIパフォーマンスはBing Webmaster Toolsでサイトの所有を確認したサイトで開ける機能です。すでにGoogle Search Consoleでサイトを確認しているなら、インポートで確認の手順を省けます。

1. [Bing Webmaster Tools](https://www.bing.com/webmasters/about)にサインインするか、アカウントを作る
2. My Sitesの画面でImportを押し、Google Search Consoleのアカウントでサインインして許可する
3. 一覧から追加するサイトを選んでImportを押す
4. AI Performanceを開き、期間を選ぶ
5. 必要な表を書き出して、社内の資料に使う





[インポートの手順のブログ](https://blogs.bing.com/webmaster/september-2019/Import-sites-from-Search-Console-to-Bing-Webmaster-Tools)によると、1回に取り込めるのは100サイトまで、1つのアカウントで1,000サイトまでです。新しく確認したサイトの検索のデータは、出るまで最大48時間かかると書かれています。Search Consoleへのアクセスを取り消すと所有の確認が外れるため、そのときは再接続するか、メタタグかDNSで確認し直します。

インポートを使わない場合は、XMLファイルのアップロード・メタタグ・DNSのレコードのどれかで確認します。ヘルプによればAIパフォーマンスのデータは毎日の更新で、反映には少しの遅れがあるとのことです。

## 数字を読むときの注意

AIパフォーマンスの数字は、Search Consoleの検索の数字と同じ感覚で読むとずれます。報告の前に知っておきたい点を、ヘルプのよくある質問から拾いました。

### 引用はクリックではない

引用は回答で表示または参照されたことを示すだけで、流入・クリック・利用者の反応は表さない、とヘルプははっきり書いています。**引用が1,000回あっても、サイトに1,000人来たわけではありません**。クリックの数はこのレポートに無いため、流入はGA4などで別に見ます。

### 語句は要約されている

グラウンディングクエリはまとめた一般的な語句で、利用者の個別の質問や細かいロングテールの語句は出ません。引用が少ないサイトでは語句が出ないこともありますが、ペナルティや除外を意味するものではないとヘルプは説明しています。

### 絞り方で数がずれる

データは標本で、語句とページでは集計の期間が少しずつ違うことがあります。語句で絞ってから見たページの引用数と、ページで絞ってから見た同じ語句の数が合わない場合もあり、ヘルプはこれを想定どおりの動きとしています。

### 6月の急増は後から足されたデータ

PinMeToの7月3日の記事によると、2026年6月1日から引用数が急に増えたという報告が多くのアカウントで出ました。MicrosoftのKrishna Madhavan氏はX上で、これを過去分のデータを後から反映する通常のバックフィルと説明しています。**この時期の伸びを施策の成果として報告しない**ほうが安全です。

### APIはまだ公式の記述が無い

画面の表は書き出せて、絞り込んだ条件がそのまま反映されます。2月にSearch Influenceが書いた記事では、APIは対応を検討する一覧に入っているが時期は示していない、とMicrosoftのFabrice Canel氏がXで答えていました。2026年10月21日に見たヘルプにAPIの記述は無く、定期の報告は画面からの書き出しで回すことになります。

## Googleのレポートとの違い

Googleも2026年6月3日に、Search Consoleで生成AIの機能での表示を見るレポートを一部のサイトから出しました。[Search Centralのブログ](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports)には、8月31日に世界のすべてのサイトへ広げたと追記されています。2つは数えているものが違うため、表で並べました。

| 項目 | BingのAIパフォーマンス | Search Consoleの生成AIレポート |
|---|---|---|
| 対象 | Copilot・BingのAI要約・一部の提携先 | AIによる概要・AIモード・Discoverの生成AI機能 |
| 数えるもの | 出典として表示された回数 | URLが表示された回数 |
| 語句 | グラウンディングクエリ（標本） | ブログの項目に無い |
| 分けて見られる軸 | ページ・語句・意図・トピック | ページ・国・デバイス・日付 |
| クリック | 無い | ブログの項目に無い |
| 提供 | 2026年2月から公開プレビュー | 2026年8月31日から全サイト |

生成AIの表示回数は検索の全体のパフォーマンスにも含まれたままだと、Googleのブログは書いています。GoogleのAIの回答で表示されたかはSearch Console、Microsoft側で引用されたかはBing Webmaster Tools、実際に来た人はGA4と、**3つは数える対象が違うため、足し合わせずに並べて見ます**。GA4でAI経由の流入を分ける設定は[AI検索対策の効果の測り方](/media/ai-search-measurement/)、GoogleのAIによる概要に引かれるための実務は[AI Overviewsに引用されるには](/media/cited-by-ai-overviews/)で扱っています。

## 社内での使い方

AIパフォーマンスは費用がかからず、サイトの確認が済めば数字を見始められます。社内で回すときに決めておきたいのは、誰が担当するかと、どう報告するかです。

### 誰が登録して誰が読むか

登録はサイトの所有を確認できる人の作業で、多くの会社ではSearch Consoleの権限を持つ制作会社かWeb担当になります。読むのはAIでの見え方に責任を持つマーケ担当です。**Search Consoleを制作会社のアカウントで持っている場合は、インポートの前に自社のアカウントで権限をもらっておく**と、担当が替わっても数字が途切れません。

### 月次報告に入れる形

月次報告には今月CopilotとBingのAIの回答で何ページが合計何回引用されたかを、前の月と並べて書きます。比較の機能で前の期間を重ね、ページを更新した日をグラフに書き込んでおくと、更新のあとに引用が動いたかを見られます。ただし比較は変化を見るもので、更新が効いたと言い切る根拠にはならないとヘルプは書いています。

### ありがちな失敗

よくある読み違いは3つです。1つ目は引用数を流入と書くこと、2つ目はグラウンディングクエリを顧客の質問そのものと読むこと、3つ目は6月のバックフィルによる急増を成果として報告することです。1つ目と2つ目はヘルプが、3つ目はMicrosoftの担当者がX上で否定しているため、報告の脚注に1行ずつ入れておくと社内の誤解を防げます。

## 引用数と回答で名前が挙がることの違い

AIの回答で自社が目に入る形は2つあります。回答の下や横の出典の欄にページが並ぶ場合と、回答の文の中で会社や商品が名前で挙がる場合です。**AIパフォーマンスが数えるのは前者だけで、回答の文で勧められたかどうかは分かりません**。

たとえば、選び方を解説した自社の記事が出典に引かれた一方で、回答の文では他社の名前が勧められていることがあります。それでも引用数は増えますし、引用シェアは他社のドメインを出さないため、レポートから誰が勧められたかは読めません。数字を見たあとの次の判断は、状況で分かれます。

| 状況 | レポートで分かること | 次に確かめること |
|---|---|---|
| 引用が増えたのに問い合わせが変わらない | 出典に引かれた回数 | 買い手が打ちそうな質問をAIに聞き、回答の文に社名が出るか |
| 引用がほとんど出ない | 引用が少ない事実だけ | Bingのインデックスとrobots.txtの設定 |
| ChatGPTやGeminiでの出方を知りたい | 入るとは書かれていない | 同じ質問を各AIに定期的に聞いて記録する |

表の2行目でrobots.txtを見るのは、Bingは引用でもrobots.txtの設定に従うと2月の発表が書いているためです。回答の文で自然に挙がること（AIO）は出典に引かれることとは別の結果で、このレポートの数字だけでは測れません。回答に社名が出てこない原因は[ChatGPTに自社が出てこない5つの原因と対策](/media/chatgpt-not-appearing/)、お金を払って載せる枠は[ChatGPT広告の出稿方法](/media/chatgpt-ads/)で扱っています。

## よくある質問

### Q. Bing Webmaster ToolsのAIパフォーマンスは無料ですか？

無料です。Bing Webmaster Toolsの紹介ページは無料のSEO・GEOのツールと案内していて、AIパフォーマンスはサイトの所有を確認すると開けます。

### Q. Bing Webmaster ToolsのAIパフォーマンスにChatGPTの引用は入りますか？

公式の説明に出てくるのはCopilot・BingのAI要約・一部の提携先だけで、提携先の名前は公表されていません。ChatGPTが入るとは書かれておらず、Adobeの日本語の解説もChatGPTはまだ含まれないとしています。

### Q. Bing Webmaster ToolsのAIパフォーマンスでクリック数は分かりますか？

分かりません。引用は流入やクリックを表さない、というのがヘルプの説明です。AIの回答から来た人数はGA4などのアクセス解析で別に見ます。

### Q. Bing Webmaster ToolsのAIパフォーマンスに語句が出ないのはなぜですか？

選んだ期間の引用が少ないと、グラウンディングクエリは出ない場合があるためです。ペナルティや除外を意味するものではないと、ヘルプは説明しています。

### Q. 日本のサイトでもBing Webmaster ToolsのAIパフォーマンスは使えますか？

使えます。2月の発表に国の制限の記述は無く、6月の4つの機能も世界での提供でした。

### Q. Copilotの回答に引用されるには何をすればいいですか？

Bingのヘルプが、検討してよい一般的な目安として挙げるのは6つです。利用者の意図に合わせる、見出し・表・よくある質問で読み取りやすくする、深さと専門性を出す、例やデータと出典で裏づける、内容を新しく保つ、形式をまたいで表記をそろえる、です。2月の発表が勧めるのは更新をすぐ伝える仕組みのIndexNowと、店舗のある会社のBing Places for Businessへの登録です。robots.txtで止めたページは、その設定に従って扱われます。

### Q. Google Search ConsoleでAIによる概要の表示回数は見られますか？

見られます。Search Centralのブログによると、AIによる概要とAIモードでの表示回数を見るレポートは2026年8月31日に世界のすべてのサイトへ広がりました。ブログが挙げる項目は表示回数・ページ・国・デバイス・日付です。

## 出典

- Bing Webmaster Blog「[Introducing AI Performance in Bing Webmaster Tools Public Preview](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)」2026年2月10日（2026年10月21日取得）
- Bing Search Blog「[New AI Visibility Insights in Bing Webmaster Tools: Intents, Topics, Citation Share, Compare](https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare)」2026年6月16日（同）
- Bing Webmaster Tools ヘルプ「[AI Performance in Bing Webmaster Tools](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c)」（同）
- Microsoft Advertising Blog「[The AI Performance dashboard](https://about.ads.microsoft.com/en/blog/post/march-2026/the-ai-performance-dashboard-your-view-into-where-your-brand-appears-across-the-ai-web)」2026年3月23日（同）
- Bing Webmaster Blog「[Easily Verify Your Site in Bing Webmaster Tools by Importing from Google Search Console](https://blogs.bing.com/webmaster/september-2019/Import-sites-from-Search-Console-to-Bing-Webmaster-Tools)」2025年6月更新（同）
- Bing Webmaster Tools「[About](https://www.bing.com/webmasters/about)」（同）
- Google Search Central Blog「[Introducing Search Generative AI performance reports in Search Console](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports)」2026年6月3日（同）
- Statcounter「[Search Engine Market Share Japan](https://gs.statcounter.com/search-engine-market-share/all/japan)」2026年9月（同）
- Adobe Experience League「[Bing ウェブマスターツール AI パフォーマンスレポート](https://experienceleague.adobe.com/ja/docs/brand-visibility-learn/tutorials/measurement/bing-webmaster-tools-ai-performance-report)」2026年10月3日更新（同）
- PinMeTo「[Bing's AI citation surge was backfill, not new visibility](https://www.pinmeto.com/news/bing-ai-performance-backfill-citation-share-2026/)」2026年7月3日（同）
- Search Influence「[Inside Bing's New AI Performance Report](https://www.searchinfluence.com/blog/bing-ai-performance-report-copilot-citations/)」2026年2月12日（同）
