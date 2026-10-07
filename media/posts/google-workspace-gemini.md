---
title: 【2026年10月】Google WorkspaceのGeminiとは？料金と個人版の違い｜学習・上限・設定
date: 2026-10-08
category: AI活用
description: Google WorkspaceのGeminiを公式の料金ページとヘルプで解説。プランごとの料金と使える機能、個人のGoogle AI Proとの違い、学習に使われない条件、使用量の上限、管理者がオンとオフを切り替える場所まで。
cover_tag: 法人
cover_headline: Google WorkspaceのGemini
cover_sub: 料金・個人版との違い・学習されない条件
---

Google WorkspaceのBusinessプランには、追加料金なしでGeminiが入っています。GmailやGoogleドキュメントの中で動くGeminiと、gemini.google.comで会話するGeminiアプリの2つがあり、どこまで使えるかはプランで決まります。

社内でGeminiを使うかを決めるとき、個人向けのGoogle AI Proとの違いが分かりにくいのは、**同じ画面のGeminiでも契約によってデータの扱いと上限の数え方が変わる**ためです。この記事はGoogle Workspaceの料金ページと管理者向けヘルプ、Geminiアプリ ヘルプ（いずれも2026年10月8日に取得）をもとに、料金と機能の差、学習に使われない条件、管理者が設定する場所を整理します。

<figure class="post-figure"><img src="/media/images/google-workspace-gemini/gwg_00_overview.jpg" alt="個人のGoogle AI ProとWorkspaceのBusiness Standardを比べた図。Google AI Proは月2,900円で1人分、学習は本人の設定しだい、上限は使った量で決まる、履歴は本人が消す。Business Standardは月1,600円（年契約・税別）、学習に使われない、Proは4時間に25件まで、履歴は管理者が決める" loading="lazy"><figcaption>同じGeminiでも、個人の契約と会社の契約で決まり方が違う</figcaption></figure>

:::takeaways
- Business Starter・Standard・Plusの年間プランは**1ユーザー月800円・1,600円・2,500円（税別）**。月ごとのフレキシブルプランは950円・1,900円・3,000円
- **StarterでGeminiが動くアプリはGmailとVidsだけ**。ドキュメント・スプレッドシート・Meetなどで使うにはStandard以上
- Geminiアプリの会話は、Workspaceのコアサービスなら**人のレビューも生成AIモデルの改良への利用もない**。ただしデータ保護を受けるにはドメインの所有権の確認が要る
- Standard・PlusのGeminiアプリは**Proモデルが4時間に25件まで・思考モードが1日300件まで**。個人のプランとは上限の数え方が違う
- 管理者は**管理コンソールの［生成AI］［Geminiアプリ］**でオンとオフ、使える人、会話履歴の保存期間を決める
:::

## Google WorkspaceのGeminiとは

「WorkspaceのGemini」と呼ばれるものは、管理者向けヘルプでは2つに分けて扱われています。1つはGmail・ドキュメント・スプレッドシート・スライド・Meet・ドライブの画面の中で動くGeminiで、ヘルプはこれをGemini in Workspaceと呼びます。もう1つはgemini.google.com、スマホのGeminiアプリ、Gemini in Chromeをまとめた**Geminiアプリ**です。

2つは上限も設定も別です。Geminiアプリ ヘルプには、Workspaceのアプリ内でGeminiを使う場合は**別途上限が設定される**と書かれています。管理者ヘルプも、Geminiアプリの設定で管理するのはgemini.google.com・モバイルアプリ・Gemini in Chromeへのアクセスで、WorkspaceのほかのAI機能には影響しないとしています。

名前の似た「Gemini Enterprise - Businessエディション」は、AIエージェントを作って共有するための別の製品で、いまのアドオンの一覧に載っています。以前Workspaceに足していたGemini BusinessとGemini Enterpriseのアドオンはこれとは別物で、[Geminiアプリ ヘルプ](https://support.google.com/gemini/answer/14620100?hl=ja)では「以前のエディション（現在は購入不可）」の扱いです。

## プランごとの料金

[Google Workspaceの料金ページ](https://workspace.google.com/intl/ja/pricing)に載っている日本の価格は次のとおりです。**すべて1ユーザーあたりの月額で、税別と明記されています。**

| プラン | 年間プラン | フレキシブルプラン | ストレージ（1人あたり） | Geminiが動く場所 |
|---|---|---|---|---|
| Business Starter | 800円 | 950円 | 30GB | Gmail、Vids、Geminiアプリ |
| Business Standard | 1,600円 | 1,900円 | 2TB | Gmail、ドキュメント、Meetなど全般 |
| Business Plus | 2,500円 | 3,000円 | 5TB | Standardと同じ |
| Enterprise | 要問い合わせ | 要問い合わせ | 5TBから | Standardと同じ |

年間プランは1年契約で、料金ページの表示ではフレキシブルプランより16%安くなります。Businessの3プランは**1つの契約で最大300人まで**です。取得した日の料金ページには、新しく契約する人向けに最初の3か月を割り引く表示も出ていました。割引率はプランと時期で変わるので、申し込む画面で確かめてください。

<figure class="post-figure post-figure--sp"><img src="/media/images/google-workspace-gemini/gwg_01_starter_sp.jpg" alt="Google Workspaceの料金ページをスマホで開いた画面。年間プランのスイッチがオンで、Starterは3か月間20%オフの表示とともに640円と取り消し線の800円、ユーザーあたりの月額。Starterの機能に30GB、カスタムのビジネス用メールアドレス、GmailのGemini AIアシスタントが並ぶ" loading="lazy"><figcaption>Starterの機能欄にあるGeminiはGmailのアシスタントだけ（10月8日の表示。割引率は時期で変わる）</figcaption></figure>

<figure class="post-figure post-figure--sp"><img src="/media/images/google-workspace-gemini/gwg_02_standard_sp.jpg" alt="同じ料金ページのStandardのカード。3か月間50%オフの表示とともに800円と取り消し線の1,600円。Starterの全機能に加えて2TB、カスタムレイアウトとメールへの差し込み、Gmail・Googleドキュメント・Google MeetなどのGemini AIアシスタント" loading="lazy"><figcaption>Standardからドキュメントや Meet でもGeminiが使える（10月8日の表示。割引率は時期で変わる）</figcaption></figure>

個人のGoogle AIのプランと比べるときは、**税の表示がそろっていない**ことに気をつけます。Workspaceの金額は税別なので、請求では消費税が加わります。[Google AIのプランのページ](https://one.google.com/about/google-ai-plans/?hl=ja)はGoogle AI Plusを月額725円、Google AI Proを月額2,900円と表示していて、税の表記はありません。総額表示の決まりから税込の金額と考えられるため、比べるならWorkspaceの側に消費税10%を足し、Business Standardの年間プランを1,760円として見るとそろいます。

## プランで変わるGeminiの機能

いちばん大きな差は**Business Starterでは、WorkspaceのアプリのうちGeminiが動くのがGmailとVidsだけ**という点です。[Businessエディションの比較](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-business-editions?hl=ja)の表では、Gmailのサイドパネル・文書作成サポート・返信の候補・スレッドの要約・校正はStarterから使えます。ドキュメント・スプレッドシート・スライド・Meet・Chat・ドライブ・フォームのGeminiは、Standardからの列にだけチェックが入っています。

Meetの自動メモ生成や、スプレッドシートのAI関数もStandardからです。会議の議事録をGeminiに任せたい、表の集計を頼みたいという目的なら、Starterでは足りません。

Geminiアプリの差も同じ表に並んでいます。

| Geminiアプリ | Business Starter | Business Standard・Plus |
|---|---|---|
| Proモデル | 基本アクセス（上限は頻繁に変わる） | 4時間ごとに25件まで |
| 思考モード | 基本アクセス（上限は頻繁に変わる） | 1日300件まで |
| 一度に読ませられる長さ | 32,000トークン | 100万トークン |
| Deep Research | 月5件 | 1日20件 |
| Nano Banana Proでの再生成 | 1日3枚 | 1日100枚 |
| 動画の生成 | なし | 1日3本 |

<figure class="post-figure"><img src="/media/images/google-workspace-gemini/gwg_03_editions.jpg" alt="Google Workspace管理者ヘルプのBusinessエディションの比較の表のGeminiアプリの行。Business Starterはアクセスが機能とモデルへの標準権限、Proと思考は基本アクセス、コンテキストウィンドウのサイズは32,000、Deep Researchは月あたり5件。Business StandardとPlusは拡張されたアクセス、Proは4時間ごとにプロンプト25件まで、思考は1日あたり最大300件、コンテキストウィンドウは100万、Deep Researchは1日あたり20件" loading="lazy"><figcaption>Business エディションの比較の Gemini アプリの行</figcaption></figure>

長い資料を読ませる用途では、Starterの32,000トークンがすぐ壁になります。Standardの100万トークンは、個人のGoogle AI Proと同じ大きさです。動画の生成のモデル名はエディションの比較がVeo 3.1 Lite、Geminiアプリ ヘルプがOmniで、2つのページの表記が合っていません。

## 個人のGoogle AI Plus・Proとの違い

同じGeminiでも、個人のGoogleアカウントで契約するGoogle AIのプランと、会社が契約するWorkspaceでは決まりが違います。主な違いは次の表のとおりです。

| 項目 | 個人のGoogle AI Plus・Pro | WorkspaceのBusiness Standard |
|---|---|---|
| 月額 | Plus 725円・Pro 2,900円（税の表記なし） | 1,600円（年間・税別） |
| 会話の学習とレビュー | アクティビティの保存がオンなら使われることがある | 使われない（条件は次の節） |
| 履歴の設定 | 本人が決める | 管理者が決める（既定は18か月保存） |
| 上限の数え方 | 使った量で決まり5時間と週で区切る | Proは4時間に25件・思考は1日300件 |
| 一度に読ませられる長さ | Plus 128,000・Pro 100万トークン | 100万トークン |
| ストレージ | Plus 400GB・Pro 5TB | 2TB |
| 契約の単位 | 1人（家族と共有できる） | ユーザーごと（最大300人） |

[使用量上限のヘルプ](https://support.google.com/gemini/answer/16275805?hl=ja)によると、個人のプランの上限はコンピューティング量で決まり、5時間ごとと週ごとに区切られます。仕組みは[Geminiの回数制限](/media/gemini-limits/)で、プランごとの料金と機能は[Geminiの料金プラン](/media/gemini-pricing/)で詳しく扱っています。

スマホのアプリでできることにも差があり、管理者ヘルプによると仕事用のアカウントではモバイルアプリでGemとCanvasが使えません。Geminiアプリ ヘルプにも、モバイルアプリではチャットの削除や公開リンクの作成ができないと書かれています。

WorkspaceのアカウントでGoogle AI Proを買い足すことはできません。Google AIのプランのページのよくある質問は、**申し込めるのは個人のGoogleアカウントだけ**で、Workspaceの利用者には、今の契約にWorkspace側のアドオンを足すよう案内しています。

### 学習に使われない条件

「WorkspaceのGeminiは学習されない」と言い切る解説は多いものの、公式の書き方には条件があります。Geminiアプリ ヘルプのエディション別の表では、Geminiアプリが**コアサービスとして入っているエディション**について、チャットの内容やアップロードしたファイルを人間のレビュアーが見ることも、生成AIモデルの改良に使うこともないとしています。適用されるのはGoogle Workspace利用規約です。

一方でWorkspace Individual、Business Base、Essentials Starter、G Suiteなどは、Geminiアプリを**追加サービス**として使う扱いです。こちらには個人と同じGoogle利用規約とGeminiアプリのプライバシーに関するお知らせが適用され、チャットがレビューされ、Googleのサービスや機械学習技術の改良に使われる場合があります。

<figure class="post-figure"><img src="/media/images/google-workspace-gemini/gwg_04_protect.jpg" alt="チャットが学習に使われるかどうかの図。ドメインを確認済みのBusiness StarterからPlusは使われない・人のレビューもない。Workspace Individualなどの追加サービスは個人と同じ規約で改善に使われることがある。アクティビティの保存がオンの個人のGoogle AI Proは改善と学習に使われ、オフなら以降は使われない" loading="lazy"><figcaption>同じWorkspaceでも、エディションとドメインの確認で扱いが分かれる</figcaption></figure>

Businessのプランでも、もう1つ確かめる点があります。エディションの比較の注記は、Geminiアプリの**エンタープライズ級のデータ保護を利用するにはドメインの所有権を証明する必要がある**としています。会社のドメインを確認せずに使い始めた契約は、管理コンソールでドメインの確認が済んでいるかを見ておいてください。

[Geminiアプリのプライバシー ハブ](https://support.google.com/gemini/answer/13594961?hl=ja)によると、個人のGeminiでもアクティビティの保存をオフにすれば以降のチャットはAIモデルの改良に使われません。ただしオフでも会話は72時間アカウントに残り、送ったフィードバックは別に扱われます。

## 使用量の上限

Standard・PlusのGeminiアプリの上限は、[Geminiアプリ ヘルプ](https://support.google.com/gemini/answer/14620100?hl=ja)の表ではProモデルが4時間あたり25件、思考モードが1日300件です。高速モードは「一般的なアクセス」とだけ書かれ、件数はありません。

<figure class="post-figure"><img src="/media/images/google-workspace-gemini/gwg_05_limits.jpg" alt="Geminiアプリ ヘルプのGoogle Workspaceのエディション別Geminiアプリの表。追加サービスのエディション、Business Starterなどのコアサービス、Business StandardとPlusなどのコアサービス、AI Expanded Access、AI Ultra Accessの5列。Proは4時間あたり最大25件・1日200件・1日500件、思考モードは1日300件・600件・1500件、コンテキストのサイズは32,000と100万" loading="lazy"><figcaption>ヘルプの表ではアドオンを足したときの件数も並ぶ</figcaption></figure>

この件数はgemini.google.com、スマホのGeminiアプリ、Gemini in Chromeの**合計で数えられます**。パソコンで使い切ってからスマホに移っても、同じモデルなら残りは増えません。上限に達するまでの回数はプロンプトの長さ・ファイルの大きさ・会話の長さでも変わる、とヘルプは説明しています。

件数が足りなければ管理者がアドオンでライセンスを上げます。AI Expanded AccessではProが1日200件・思考モードが1日600件・Deep Researchが1日30件になり、AI Ultra Accessではそれぞれ500件・1,500件・120件になります。Deep Think 3.1が使えるのはAI Ultra Accessだけです。アドオンの価格は公式のエディションの比較にもアドオンの一覧にも載っていません。

ドキュメントやスプレッドシートの中のGeminiには、月ごとの上限が別にあります。たとえばスプレッドシートのAI関数はStandard・Plusで月5,000回、スライドの生成は月100枚で、AI Expanded Accessを足すとそれぞれ25,000回・500枚です。

## 使えるモデルの確かめ方

自分のアカウントでどこまで使えるかは、gemini.google.comを仕事用のアカウントで開くと分かります。Geminiアプリ ヘルプによると、画面の上部に**Pro・Expanded・Ultraのバッジ**が出ていれば、それぞれ拡張されたアクセス、さらに拡張されたアクセス、最上位のアクセスです。バッジが無ければ標準の機能とモデルで、Starterなどのエディションはこの扱いです。

Geminiアプリ ヘルプの表では、高速・思考・Proの3つから選びます。Proや思考モードを選べない、上限にすぐ届くという場合は、自分では変えられないので管理者にライセンスを確かめてもらいます。

## 管理者が有効・無効にする場所

Geminiアプリを組織で使えるようにするか止めるかは、[Geminiアプリをオンまたはオフにする](https://support.google.com/a/answer/14571493?hl=ja)のヘルプにある手順で切り替えます。設定に要るのはGeminiの「設定」の管理者権限です。

1. [Google管理コンソール](https://admin.google.com/)でメニューから［生成AI］［Geminiアプリ］に進む
2. ［サービスのステータス］を開く
3. ［オン（すべてのユーザー）］か［オフ（すべてのユーザー）］を選んで保存する
4. 一部の人だけ変えるときは、組織部門かグループを選んでから保存する

<figure class="post-figure"><img src="/media/images/google-workspace-gemini/gwg_06_admin_help.jpg" alt="Google Workspace管理者ヘルプのGeminiアプリをオンまたはオフにするの手順。Google管理コンソールでメニューアイコンから生成AI、Geminiアプリに移動、サービスのステータスをクリック、オン（すべてのユーザー）またはオフ（すべてのユーザー）を選んで保存、組織部門かグループを選ぶ、変更の反映には最長で24時間ほどかかる" loading="lazy"><figcaption>管理者ヘルプのオンとオフの手順</figcaption></figure>

反映には最長で24時間ほどかかります。［検索とアシスタント］のサービスがオフのままだと、Androidでは使えません。

同じ［Geminiアプリ］の画面には、ほかに2つの設定があります。［ユーザーアクセス］はWorkspaceのライセンスを持たない人にもGeminiアプリを使わせるかどうかで、［Gemini会話履歴］は会話を残すかと残す期間です。

<figure class="post-figure"><img src="/media/images/google-workspace-gemini/gwg_07_admin.jpg" alt="管理者がGeminiを設定する場所の図。管理コンソール、生成AI、Geminiアプリの順に進むと、サービスのステータスで全員または部署ごとにオンとオフ、ユーザーアクセスでライセンスの無い人にも使わせるか、Gemini会話履歴で保存するかと保存の期間を決める" loading="lazy"><figcaption>Geminiアプリの設定は1つの画面に3つ</figcaption></figure>

会話履歴は**既定でオンで、18か月で自動的に消えます**。管理者は3か月・18か月・36か月から選ぶか、履歴をオフにできます。利用者はこの設定を変えられません。履歴をオフにするとGeminiからGmailやドライブを呼び出す連携も使えなくなるので、止める前に影響を確かめておきます。

スマホのGeminiアプリは管理コンソールに専用の設定がなく、止めたいときはデバイス管理でアプリをブロックします。Gemini in Chromeは、米国でChromeにログインしていて既定の言語が英語（米国）の人だけが対象です。個人の側でGmailのGeminiを止める方法は[GmailのGeminiをオフにする方法](/media/gmail-gemini-off/)にまとめています。

## 1人で契約するときの注意

Workspaceは会社でなくても契約できます。**1人だけのアカウントならGmailのアドレスでも申し込める**と、エディションの比較に書かれています。個人のGoogle AI Proより月額が安いことから、1人でBusiness Standardを契約する使い方を紹介する解説動画もありました。

ただし前の節のとおり、Geminiアプリのエンタープライズ級のデータ保護はドメインの所有権の確認が条件です。Businessのプランでスマホのアプリを使うにも、ビジネス用のメールアドレスで登録するかドメインを確認する必要があります。学習されないことが目的なら、独自ドメインを用意してから申し込みます。

Workspaceのアカウントは今の個人アカウントとは別のアカウントになり、写真やドライブのファイルは自動では移りません。仕事用のアカウントでGeminiを使えるのは18歳以上で、年齢の条件は[Geminiの年齢制限](/media/gemini-age-limit/)で扱っています。ほかの法人向けAIと比べるなら、[ChatGPT Business](/media/chatgpt-business/)と[Claude Teamプラン](/media/claude-team/)の料金と学習の扱いも同じ形で整理しています。

## よくある質問

### WorkspaceのGeminiは無料で使えますか？
Business StarterからPlusまで、Geminiは月額の中に含まれていて追加料金はかかりません。ただしWorkspace自体は1ユーザー月800円（年間・税別）からの有料サービスです。

### Google WorkspaceでGeminiは使えますか？
BusinessとEnterpriseのほとんどのエディションで使えます。StarterではGmailとVidsの中のGeminiとGeminiアプリが使え、ドキュメントやMeetのGeminiはStandard以上です。管理者がオフにしていると使えません。

### WorkspaceのGeminiは学習に使われますか？
Geminiアプリがコアサービスとして入っているエディションでは、チャットやファイルが人にレビューされることも生成AIモデルの改良に使われることもありません。Workspace Individualなど追加サービスの扱いのエディションでは、改良に使われる場合があります。

### WorkspaceのGeminiと個人版の違いは何ですか？
大きいのはデータの扱いと上限の数え方です。Workspaceは会話が学習に使われず履歴は管理者が決め、Proモデルは4時間に25件までです。Google AI Proは本人の設定で扱いが決まり、上限は使った量で決まります。

### WorkspaceのGeminiで使えるモデルは何ですか？
Geminiアプリでは高速・思考・Proの3つから選びます。Starterは標準のアクセスで、ProモデルはStandard・Plusで4時間に25件まで使えます。Deep Think 3.1はAI Ultra Accessのアドオンが必要です。

### WorkspaceのGeminiに上限はありますか？
あります。Standard・PlusではProモデルが4時間に25件、思考モードが1日300件です。Deep Researchは1日20件、Starterは月5件です。ドキュメントなどアプリの中のGeminiには別の月ごとの上限があります。

### WorkspaceでGeminiをオフにできますか？
管理者が管理コンソールの［生成AI］［Geminiアプリ］［サービスのステータス］でオフにできます。部署やグループごとにも切り替えられ、反映までは最長で24時間ほどです。

### Workspaceを1人で契約してGeminiを使えますか？
使えます。1人のアカウントはGmailのアドレスでも申し込めます。ただしGeminiアプリのデータ保護を受けるには、ドメインの所有権の確認が必要です。

## 出典

料金と機能は2026年10月8日に取得した公式ページの表示です。料金ページの年間プランとフレキシブルプランは、ページのスイッチを切り替えて確認しました。

- Google Workspace「[料金](https://workspace.google.com/intl/ja/pricing)」
- Google Workspace 管理者ヘルプ「[Business エディションの比較](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-business-editions?hl=ja)」（Gemini の機能・Gemini の高度な機能の表）
- Gemini アプリ ヘルプ「[仕事用または学校用の Google アカウントで Gemini アプリを利用する](https://support.google.com/gemini/answer/14620100?hl=ja)」（エディション別の表・データの取り扱い・モバイルアプリ）
- Google Workspace 管理者ヘルプ「[Gemini アプリをオンまたはオフにする](https://support.google.com/a/answer/14571493?hl=ja)」
- Google Workspace 管理者ヘルプ「[Google Workspace の生成 AI に関するプライバシー ハブ](https://support.google.com/a/answer/15706919?hl=ja)」
- Google Workspace 管理者ヘルプ「[Google Workspace のアドオン](https://knowledge.workspace.google.com/admin/getting-started/editions/google-workspace-add-ons?hl=ja)」
- Gemini アプリ ヘルプ「[Gemini アプリのプライバシー ハブ](https://support.google.com/gemini/answer/13594961?hl=ja)」
- Gemini アプリ ヘルプ「[Google AI のサブスクリプション プランに応じた Gemini アプリの使用量上限とアップグレード](https://support.google.com/gemini/answer/16275805?hl=ja)」
- Google One「[Google AI のプラン](https://one.google.com/about/google-ai-plans/?hl=ja)」（日本の価格・よくある質問）
