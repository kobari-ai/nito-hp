---
title: 【2026年9月】「challenges.cloudflare.comのブロックを解除してください」の原因と対処を解説｜ChatGPT・Claude・障害の見分け方
date: 2026-09-27
category: AI検索対策
description: ChatGPTやClaudeで出る「続行するには、challenges.cloudflare.comのブロックを解除してください」の原因と対処。Cloudflareの障害か手元の設定かの見分け方を、公式ドキュメントと検査ツールの実測で確かめました。
cover_tag: 使い方
cover_headline: challenges.cloudflare.comのブロック解除
cover_sub: 障害か手元かの見分け方と対処
---

「続行するには、challenges.cloudflare.com のブロックを解除してください。」を出しているのはChatGPTやClaudeそのものではなく、手前にあるCloudflareの確認画面です。英語の画面では「Please unblock challenges.cloudflare.com to proceed.」と表示されます。

**2025年11月18日の夜には、Cloudflareの障害でこの表示がChatGPTやClaudeで一斉に出ました。**日本語で検索して上に出てくる記事の多くは、この日の障害について書かれたものです。ただ、障害が無い日でも、広告ブロックの拡張機能やVPN、会社のネットワークが確認を止めていると同じ表示になります。

この記事ではCloudflareの公式ドキュメントと、Cloudflareが公開している検査ツールを2026年9月27日に実際に動かした結果をもとに、障害か手元かの見分け方と、手元が原因だったときの直し方を整理します。

:::takeaways
- メッセージを出しているのは**Cloudflareの確認画面**。確認に使う challenges.cloudflare.com に届かないと出る
- 最初に**Cloudflare・OpenAI・Anthropicのステータスページ**を見る。障害なら手元では直せない
- 障害が無いなら、**シークレットモード**と**モバイル回線**で開けるかを試すと、原因を拡張機能かネットワークかに絞れる
- Cloudflareの**検査ツール**は、通信が止められているかを4項目で表示する。実測では接続を止めると「Server Connection」だけが赤になった
- Cloudflareに問い合わせても確認は外れない。外せるのは**サイトの運営者**だけ
:::

## メッセージの意味と出る仕組み

ChatGPTやClaudeは、Cloudflareという会社のネットワークを通して配信されています。Cloudflareはアクセスが人かボットかを見ていて、怪しいと判断したときだけ、サイトを開く前に確認画面をはさむ仕組みです。

確認画面は challenges.cloudflare.com から確認の仕組み（Turnstile）を読み込んで動きます。**この読み込みが途中で止まると、確認が終わらず「ブロックを解除してください」と表示されます。**Cloudflareの確認画面に組み込まれた日本語の案内文でも、インターネットやファイアウォールの設定が challenges.cloudflare.com へのアクセスを止めていないかを確かめるよう書かれています。

<figure class="post-figure"><img src="/media/images/cloudflare-challenges-unblock/00_fig_where.png" alt="メッセージが出るまでの流れの図。1、ChatGPTやClaudeを開くと、手前のCloudflareがアクセスが人かボットかを見る。2、確認が必要と判断されると確認画面が出る。3、確認の仕組みを challenges.cloudflare.com から読み込み、届かないとメッセージが出る。止まる場所は2つで、手元ではブラウザ・ネットワーク・端末のどこかが通信を止めている。Cloudflare側では障害で確認の仕組みそのものが動かず、手元では直せない" loading="lazy"><figcaption>メッセージが出るまでの流れと、止まる場所（Cloudflareのドキュメントと確認画面の案内文から作成）</figcaption></figure>

止まる場所は、手元とCloudflare側の2つに分かれます。手元なら設定を直せば開けるようになり、Cloudflare側なら復旧を待つしかありません。**どちらなのかで対処が正反対になるため、先に見分けます。**

## 障害か手元かの見分け方

見分けるときは手間の少ないものから順に試します。Cloudflareのトラブルシューティングの手順を、確かめる順に並べ替えると次のようになります。

<figure class="post-figure"><img src="/media/images/cloudflare-challenges-unblock/01_fig_check.png" alt="障害か手元かを見分ける4つの順番。1、ステータスページでCloudflare・OpenAI・Anthropicに障害が出ていれば、原因はそちらなので復旧を待つ。2、シークレットモードで開けるなら原因は拡張機能。3、Wi-Fiを切ってスマホの回線で開けるなら原因はネットワーク。4、Cloudflareの検査ツールで止まっている場所を4項目で確かめ、赤の項目から直す" loading="lazy"><figcaption>障害か手元かを見分ける順番（Cloudflareのトラブルシューティングから作成）</figcaption></figure>

### ステータスページで障害を確かめる

最初に見るのは、[Cloudflareのステータスページ](https://www.cloudflarestatus.com/)です。「Active incidents」に進行中の障害が並び、ネットワーク全体の障害ならここに出ます。

<figure class="post-figure post-figure--sp"><img src="/media/images/cloudflare-challenges-unblock/ccu_01_sp_cfstatus.jpg" alt="スマホで開いたCloudflare System Statusのページ。Active incidentsに、アジア太平洋のネットワーク性能の低下、Cloudflare One Clientsが一部のサイトで誤って確認を求められる件、一部のWARP利用者の位置情報の誤りの3件が、Identifiedの表示で並んでいる" loading="lazy"><figcaption>Cloudflareのステータスページ（2026年9月27日、スマホ）</figcaption></figure>

**2026年9月27日に開いたときは、「Cloudflare One Clients are incorrectly challenged on some sites」が対応中でした。**会社などで入れるCloudflareの接続アプリ（Cloudflare One Client）を使っている人が、一部のサイトで誤って確認を求められる不具合で、9月23日から「原因を特定し修正中」の表示が続いています。会社のパソコンでだけ確認画面が出るなら、この種類の不具合も疑えます。

ChatGPTなら[OpenAIのステータスページ](https://status.openai.com/)、Claudeなら[Claudeのステータスページ](https://status.claude.com/)も合わせて見てください。サービス側の障害でも画面が開かない症状は似ています。

<figure class="post-figure"><img src="/media/images/cloudflare-challenges-unblock/ccu_02_status_ai.jpg" alt="左はOpenAIのステータスページで、We're fully operationalと表示され、APIs、ChatGPT、Codexなどに緑のチェックが付いている。右はClaude Statusのページで、All Systems Operationalと表示され、claude.aiなどの過去30日の稼働率が棒グラフで並んでいる" loading="lazy"><figcaption>OpenAIとClaudeのステータスページ（2026年9月27日、スマホ）</figcaption></figure>

### シークレットモードとモバイル回線で試す

どのステータスページにも障害が出ていなければ、原因は手元にあると考えて進めます。Cloudflareのドキュメントが勧めるのは、シークレットモード（プライベートモード）で開き直すことです。**シークレットモードでは多くの拡張機能が止まるため、そこで開けるなら拡張機能が原因**だと絞れます。

次に、スマホならWi-Fiを切ってモバイル回線で開いてみます。パソコンなら、スマホのテザリングにつなぎ替えても同じ確認ができます。**回線を変えて開けるなら、原因はネットワーク側です。**会社や学校のWi-Fi、家のルーターの広告ブロック機能、VPNなどが候補になります。

## Cloudflareの検査ツールで確かめる

Cloudflareは確認がうまく動くかを調べる[検査ツール（Turnstile Troubleshooter）](https://debug.challenges.cloudflare.com/)を公開しています。開くだけで診断が始まり、30秒ほどで結果が出ました。

2026年9月27日に、スマホ表示のChromeでこのツールを2回動かしました。1回目は何も変えずに開き、4項目すべてが緑になりました。

<figure class="post-figure post-figure--sp"><img src="/media/images/cloudflare-challenges-unblock/ccu_03_sp_debug_ok.jpg" alt="スマホで開いたCloudflareのTurnstile Troubleshooter。SECURITY CHECKに私はロボットではありませんのチェック欄が表示され、DIAGNOSTICSは4分の4でDiagnostics complete。Diagnostic resultsではAutomation Check、System Clock、Privacy Tools、Server Connectionの4項目がすべて緑" loading="lazy"><figcaption>通常の状態で開いた検査ツール。4項目すべて緑（2026年9月27日、スマホ）</figcaption></figure>

2回目は、ブラウザから challenges.cloudflare.com に届かない状態を作ってから開きました。拡張機能やネットワークが通信を止めたときと同じ状態を、ブラウザの設定で再現したものです。**確認欄は「Loading security check...」のまま進まず、「Cannot Connect to Security Servers」という警告が出ました。**

<figure class="post-figure post-figure--sp"><img src="/media/images/cloudflare-challenges-unblock/ccu_04_sp_debug_block.jpg" alt="challenges.cloudflare.comに届かない状態で開いた検査ツール。SECURITY CHECKはLoading security checkのまま。ISSUE FOUNDの枠にCannot Connect to Security Serversと出て、ファイアウォール、VPN、プロキシ、広告ブロックで止められていると説明し、接続の確認、VPNやプロキシの停止、別のネットワーク、ファイアウォールの設定、広告ブロックの停止の5つの手順が並ぶ。Diagnostic resultsではServer Connectionだけが赤でCannot reach servers" loading="lazy"><figcaption>challenges.cloudflare.com に届かない状態で開いた検査ツール。Server Connectionだけが赤（2026年9月27日、スマホ）</figcaption></figure>

4項目の意味は次のとおりです。赤になった項目が直す場所を指しています。

| 項目 | 見ているもの | 赤のときの対処 |
|---|---|---|
| Automation Check | 自動操作のブラウザではないか | 自動操作のツールや開発者ツールの設定を切る |
| System Clock | 端末の時計が合っているか | 日付と時刻を自動設定にする |
| Privacy Tools | プライバシー系の機能が邪魔していないか | 追跡防止や広告ブロックの拡張機能を止める |
| Server Connection | Cloudflareのサーバーに届くか | VPN・広告ブロック・ファイアウォールを外す、回線を変える |

画面の下にある「Technical details」には、IPアドレスとブラウザの情報が出ます。サイトの運営者やサポートに聞かれたときに渡すための欄なので、SNSなどに画面をそのまま貼らないでください。

## 手元の原因と対処

Cloudflareのドキュメントと確認画面の案内文を合わせると、手元の原因は次の6つに分かれます。

| 原因 | 当てはまりやすい人 | 対処 |
|---|---|---|
| 広告ブロックなどの拡張機能 | 追跡防止・スクリプト停止の拡張機能を入れている | 拡張機能を止めて再読み込み |
| VPN・プロキシ | VPNアプリやプロキシを使っている | いったん切って試す |
| 会社や学校のネットワーク | 職場のWi-Fiや社用パソコンで使っている | 別の回線で試し、IT部門に challenges.cloudflare.com の許可を頼む |
| セキュリティソフト・ファイアウォール | 通信を監視するソフトを入れている | 許可リストに challenges.cloudflare.com を加える |
| JavaScriptやCookieがオフ | ブラウザの設定を変えている | 両方をオンにする |
| 古いブラウザ・アプリ内ブラウザ | LINEやXのリンクから開いた、ブラウザを更新していない | 標準のブラウザで開く、最新版に更新する |

<figure class="post-figure"><img src="/media/images/cloudflare-challenges-unblock/ccu_05_docs_troubleshoot.jpg" alt="CloudflareのドキュメントのTroubleshootingの節。ブラウザの対応の確認と互換性チェックツール、拡張機能を止める、JavaScriptを有効にする、シークレットモードやプライベートモードで試す、別のブラウザや端末で試す、VPNやプロキシを避ける、モバイルのホットスポットなど別のネットワークに切り替える、の7つの手順が並ぶ" loading="lazy"><figcaption>Cloudflareのドキュメントのトラブルシューティング（2026年9月8日更新、2026年9月27日取得）</figcaption></figure>

### 拡張機能と広告ブロック

Cloudflareの対応ブラウザのページは、広告ブロックやコンテンツブロッカーが確認のスクリプトを止めたり、Cloudflareとの通信を遮ったりすることがあると書いています。スクリプトを止める拡張機能や、端末の特徴を読まれないようにする拡張機能も同じです。**全部をいったん止めて再読み込みし、開けたら1つずつ戻して原因の拡張機能を探します。**

原因が分かったら、その拡張機能の設定で chatgpt.com や claude.ai、challenges.cloudflare.com を対象外にすれば、ほかのサイトでは広告ブロックを使い続けられます。ブラウザに最初から入っている広告ブロックも、同じように止めて試してください。

### VPN・プロキシと会社のネットワーク

VPNやプロキシを通すと、確認が増えたり、Cloudflareから見たIPアドレスが途中で変わったりすることがあります。いったん切って開けるなら、VPNの接続先を変えるか、ChatGPTやClaudeを使うときだけ切ります。

会社や学校のネットワークは、自分では設定を変えられません。**IT部門には「challenges.cloudflare.com への通信を許可してほしい」と、ドメイン名をそのまま伝えると話が早くなります。**セキュリティソフトの場合も、ソフトを丸ごと止めるのではなく、許可リストにこのドメインを足すのが安全です。

### ブラウザの設定と端末の時刻

Cloudflareのドキュメントでは、どの確認もJavaScriptとCookieが有効でないと通れないとされています。確認画面の案内文には端末の日付や時刻がずれていると確認が終わらないという項目もあります。時刻は手で合わせるより、自動設定にするほうが確実です。

スマホで見落としやすいのが、LINEやXの中でリンクを開いたときです。Cloudflareの対応ブラウザのページは、アプリの中で開くブラウザ（アプリ内ブラウザ）は機能が制限されていて、確認の動きが変わることがあると書いています。**右上のメニューから「ブラウザで開く」を選び、SafariやChromeで開き直してください。**

## やってはいけない対処

検索で見つかる対処の中には効き目が無いものや危ないものも混ざっています。

- **セキュリティソフトのリアルタイム保護を切ったままにする。**試すなら短時間で戻し、原因と分かったら許可リストで対応する
- **知らない会社のDNSに切り替える。**通信の行き先を預けることになる。DNSを変えて試すなら、Google（8.8.8.8）やCloudflare（1.1.1.1）のような大手に限る
- **障害中に設定をいじり続ける。**Cloudflare側の障害なら手元では直らず、変えた設定を戻し忘れる
- **Cloudflareに確認を外してもらおうとする。**Cloudflareのドキュメントには、Cloudflareの社員は確認を外せず、外せるのはサイトの運営者だけと書かれている

手元をすべて試しても開けないときは、OpenAIやAnthropicのサポートに連絡します。**Cloudflareのドキュメントは、エラーコードとRay ID（確認画面の下に出る英数字）をサイトの運営者に伝えるよう案内しています。**画面を撮っておくと伝えやすくなります。

## 2025年11月18日の障害

日本語の検索で上位に並ぶ記事の多くは、この日の障害について書かれています。[Cloudflareの公式ブログ](https://blog.cloudflare.com/ja-jp/18-november-2025-outage/)には、障害の時間の流れと原因が日本語で公開されています。日本時間に直すと、夜から翌日の未明まで続いた障害でした。

<figure class="post-figure"><img src="/media/images/cloudflare-challenges-unblock/02_fig_1118.png" alt="2025年11月18日のCloudflare障害の時間の流れ。日本時間20時20分に障害が始まり、Turnstileも読み込めなくなった。23時30分に正しい設定ファイルに戻して主な影響が解消。翌日2時6分に残りのサービスの再起動が終わってすべて復旧" loading="lazy"><figcaption>2025年11月18日のCloudflare障害の時間の流れ（日本時間。Cloudflare公式ブログから作成）</figcaption></figure>

原因は攻撃ではありません。ボット管理に使う設定ファイルが想定の2倍の大きさになり、それを読み込むソフトが処理できなくなったと説明されています。**影響を受けたサービスの一覧には「Turnstileが読み込めなかった」とあり、確認の仕組みそのものが止まっていました。**この日にメッセージが出た人は、手元の設定を変えても直らなかったことになります。

Cloudflareは2025年12月5日にも、日本時間17時47分から18時12分まで、約25分の障害を[公式ブログ](https://blog.cloudflare.com/5-december-2025-outage/)で報告しています。**同じメッセージが大勢に同時に出ているときは、まずステータスページを見るのが一番の近道です。**

## よくある質問

### Cloudflareでブロックされた原因は何ですか？

Cloudflareの確認画面が、確認に使う challenges.cloudflare.com に届かなかったためです。手元の拡張機能・VPN・会社のネットワーク・セキュリティソフトが通信を止めているか、Cloudflare側で障害が起きているかのどちらかです。

### Cloudflareの確認用ドメインは安全ですか？

challenges.cloudflare.com は、Cloudflareが確認画面のために使う公式のドメインで、Cloudflareのドキュメントにも名前が出てきます。このドメインへの通信を許可しても、ウイルスを招くことにはなりません。

### Cloudflareの確認画面がループするのはなぜですか？

Cloudflareのドキュメントは、不安定な回線、拡張機能やブラウザの設定、対応していないブラウザ、JavaScriptがオフ、ボットと疑われる動きの5つを挙げています。シークレットモードや別の回線で試し、それでも続くなら別の端末で試します。

### iPhoneでだけこのメッセージが出るのはなぜですか？

候補はSafariに入れた広告ブロックの機能拡張、VPNアプリ、LINEやXのアプリ内ブラウザの3つです。機能拡張とVPNを止め、Safariで直接開き直してください。

### ChatGPTだけで出てほかのサイトは開けるのはなぜですか？

確認画面を出すかどうかはサイトごとの設定とアクセスの様子で決まります。ChatGPTで確認が求められ、そのときだけ通信が止められていると、ほかのサイトは開けるのにChatGPTだけ止まります。

### Cloudflareに解除を頼めますか？

解除してもらえません。Cloudflareのドキュメントによると、確認を外せるのはサイトの運営者だけです。手元の対処で直らなければ、OpenAIやAnthropicのサポートにRay IDを添えて連絡します。

### Cloudflare Challengesとは何ですか？

Cloudflareが、アクセスが人かボットかを確かめる仕組みの総称です。サイトの前に出る確認画面、サイトの中に置く確認欄のTurnstile、裏で動く判定のJavaScript Detectionsが含まれます。

### Cloudflareの障害はどこで確認できますか？

[Cloudflareのステータスページ](https://www.cloudflarestatus.com/)で、進行中の障害と過去の障害を見られます。ChatGPTは[OpenAIのステータスページ](https://status.openai.com/)、Claudeは[Claudeのステータスページ](https://status.claude.com/)も合わせて確認してください。

## 出典

- Cloudflare Docs「[Challenge solve issues](https://developers.cloudflare.com/cloudflare-challenges/troubleshooting/challenge-solve-issues/)」（2026年9月8日更新、2026年9月27日取得）
- Cloudflare Docs「[Supported browsers](https://developers.cloudflare.com/cloudflare-challenges/reference/supported-browsers/)」（2026年8月18日更新、2026年9月27日取得）
- Cloudflare Docs「[Resolve a Challenge](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/resolve-challenge/)」（2026年4月15日更新、2026年9月27日取得）
- Cloudflare ブログ「[2025年11月18日のCloudflareの障害](https://blog.cloudflare.com/ja-jp/18-november-2025-outage/)」
- Cloudflare ブログ「[Cloudflare outage on December 5, 2025](https://blog.cloudflare.com/5-december-2025-outage/)」
- [Cloudflareのステータスページ](https://www.cloudflarestatus.com/)、[OpenAIのステータスページ](https://status.openai.com/)、[Claudeのステータスページ](https://status.claude.com/)
- [Turnstile Troubleshooter](https://debug.challenges.cloudflare.com/)（2026年9月27日にスマホ表示のChromeで実行）
- 確認画面の日本語の案内文は、Cloudflareの確認画面のスクリプトに含まれる文言を2026年9月27日に取得
