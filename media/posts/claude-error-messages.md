---
title: 【2026年9月】Claudeのエラーの原因と対処を解説｜容量制約・529 Overloaded・500・障害の見分け方
date: 2026-09-27
category: AI検索対策
description: Claudeで出るエラーを文言ごとに整理。「予期しない容量制約」と障害の違い、Claude Codeの529 Overloadedと500と429の見分け方、モデルを切り替えて続けられる場合を公式ヘルプとドキュメントで確かめました。
cover_tag: 使い方
cover_headline: Claudeのエラーの見分け方
cover_sub: 容量制約・529・500・障害
---

Anthropicのヘルプ「[Claudeのエラーメッセージのトラブルシューティング](https://support.claude.com/ja/articles/12466728)」には、使用制限・長さ制限・ログインエラー・容量制約・サービスインシデントの5つが並んでいます。このうち「予期しない容量制約により、Claudeはメッセージに応答できません」は障害ではなく、[ステータスページ](https://status.claude.com/)にも載らないとされています。ステータスページがすべて緑でもエラーが出ることがあるのは、このためです。

Claude Codeや開発者向けのAPIでは、529 Overloaded・500・429といった番号つきのエラーが出るのが、アプリとの違いです。**529は使用量に数えられず、容量はモデルごとに管理されているので、別のモデルに切り替えれば続けられることがあります。**この記事では公式ヘルプとClaude Code・APIのドキュメント（2026年9月27日取得）をもとに、表示される文言から原因と対処を見分ける方法を整理します。

:::takeaways
- 「予期しない容量制約」は**障害ではなく全体の混雑**。ステータスページには出ない。ヘルプの対処は数分おいて送り直すこと
- ステータスページのインシデントは技術的な問題。**2026年9月は27日までに14件**が載り、うち6件は特定のモデルのエラーの増加だった
- Claude Codeの**529は使用量に数えられない**。容量はモデルごとなので、/model で別のモデルに切り替えれば続けられることがある
- 5時間と週間の制限は**すべてのモデルで共有**。こちらはモデルを変えても戻らず、表示された時刻まで待つ
- 「Server is temporarily limiting requests (not your usage limit)」は、プランの枠とは別の一時的な流量制限
:::

## 表示される文言で見分ける

原因は画面に出た文言でおおむね分かれます。Claudeのアプリ（claude.aiとスマホ・デスクトップのアプリ）の文言はヘルプから、Claude Codeの文言は[Claude Codeのエラーリファレンス](https://code.claude.com/docs/ja/errors)から拾いました。

| 表示される文言 | 出る場所 | 原因 | 対処 |
|---|---|---|---|
| 予期しない容量制約により、Claudeはメッセージに応答できません | アプリ | Claude全体の混雑 | 数分おいて送り直す |
| 5時間の制限に達しました - [時間]にリセットされます | アプリ | 自分の使用量の枠 | 表示された時刻まで待つ |
| メッセージがこのチャットの長さ制限を超えます | アプリ | 1つの会話に入る量 | ファイルを減らすか新しい会話にする |
| ログインエラーが発生しました | アプリ | VPN・拡張機能・キャッシュなど | 手元の環境を確かめる |
| API Error: Repeated 529 Overloaded errors | Claude Code | 全体の混雑（使用量に数えない） | 数分待つか /model で切り替える |
| API Error: 500 Internal server error | Claude Code | Anthropic側の予期しない障害 | 送り直し、続けばステータスを見る |
| API Error: Server is temporarily limiting requests | Claude Code | プランの枠とは別の一時的な流量制限 | 少し待って送り直す |
| You've hit your session limit | Claude Code | 自分の使用量の枠 | 表示された時刻まで待つ |

使用量の枠の見方とリセットの時刻は「[Claudeの使用制限とリセット時間](/media/claude-usage-limits/)」、ログインで止まる場合は「[Claudeにログインできない原因と対処](/media/claude-login-error/)」で詳しく扱っています。

返答の途中で「Claudeはこのターンのツール使用制限に達しました」と出た場合は使用量の枠とは別の仕組みで、続け方は「[Claudeのこのターンのツール使用制限](/media/claude-tool-use-limit/)」で扱っています。

文言で見当がつかないときは、次の順で確かめます。

<figure class="post-figure"><img src="/media/images/claude-error-messages/01_fig_check.png" alt="Claudeでエラーが出たときに確かめる4つの順番の図。1、制限やリセットの文字があれば自分の使用量の枠で、表示された時刻まで待つ。2、容量制約や529 Overloadedなら全体の混雑で、ステータスページには出ないので数分おいて送り直す。3、ステータスページに障害が出ていれば復旧を待つ。4、どれにも当たらずログインや読み込みで止まるなら、VPNや拡張機能やキャッシュを確かめる" loading="lazy"><figcaption>エラーが出たときに確かめる順番（Anthropicのヘルプとドキュメントから作成）</figcaption></figure>

## 容量制約と障害の違い

ヘルプは、容量制約とサービスインシデントを別の項目として説明しています。容量制約はClaudeのインフラ全体に高い需要がかかっているときに起きるものです。**ヘルプには「容量制約は停止ではありません」とあり、システムは正常に動いたまま、すべての利用者の需要を調整している状態とされています。**

<figure class="post-figure"><img src="/media/images/claude-error-messages/cem_01_help_capacity.jpg" alt="Anthropicのヘルプの容量制約の節。予期しない容量制約により、Claudeはメッセージに応答できません。しばらくしてからもう一度お試しくださいという表示の例と、重要として容量制約は停止ではなく一時的なもので、数分後にもう一度試すよう書かれた囲み。容量の問題はステータスページには表示されないという1文と、その下のサービスインシデントと停止の節" loading="lazy"><figcaption>Anthropicのヘルプの容量制約の節（2026年9月27日取得）</figcaption></figure>

容量の問題は通常の負荷の管理なので、ステータスページには出ません。一時的なもので、1日のうちに需要の波が変わるにつれて解消するのが普通です。ヘルプの勧める対処は数分後にもう一度送ることです。

サービスインシデントのほうは、Claudeがすべてかほとんどの利用者にとって使えない、または大きく落ちている状態を指します。こちらはシステムの実際の技術的な問題で、[status.claude.com](https://status.claude.com/)に範囲と影響、復旧の経過が載ります。

**ステータスページが緑でもエラーが続くなら、容量制約か手元の原因を先に疑ってください。**容量制約なら、ヘルプの勧めどおり数分おいてから送り直します。

## ステータスページで障害を確かめる

ステータスページにはclaude.ai・Claude Console・Claude API・Claude Code・Claude Coworkが別々の行で並びます。過去30日の棒グラフの色で、どの日にどのサービスで問題があったかが分かります。

<figure class="post-figure post-figure--sp"><img src="/media/images/claude-error-messages/cem_02_sp_status.jpg" alt="スマホで開いたClaude Statusのページ。All Systems Operationalの緑の帯の下に、claude.ai、Claude Console、Claude API、Claude Codeの過去30日の稼働率の棒グラフが並ぶ。claude.aiとClaude APIとClaude Codeの棒の一部が黄色やオレンジや赤になっている" loading="lazy"><figcaption>Claudeのステータスページ（2026年9月27日、スマホ）</figcaption></figure>

2026年9月1日から27日までに、このページには14件のインシデントが載りました（日本時間で数えた件数）。**そのうち6件は「Elevated errors for Claude Sonnet 5」のように、特定のモデルか複数のモデルでエラーが増えたという件名でした。**障害が出ても、すべてのモデルが同時に止まるとは限りません。

9月22日の「Elevated errors for multiple models」では、最初にMythos 5.1・Fable 5.1・Opus 5のエラーの増加が報告されました。途中の更新でFableとMythosが先に戻り、Opus 5のエラーが残っていると書かれています。影響が出ていたのは日本時間の9時50分から11時10分までです。

<figure class="post-figure post-figure--sp"><img src="/media/images/claude-error-messages/cem_03_sp_incident.jpg" alt="スマホで開いたClaudeのステータスページのインシデント詳細。件名はElevated errors for multiple models。ResolvedはUTCの0時50分から2時10分まで影響があったこと、Monitoringは成功率が戻ったこと、UpdateはClaude Fable 5と5.1、Mythos 5と5.1が戻りClaude Opus 5のエラーの解消を進めていることを伝えている" loading="lazy"><figcaption>9月22日のインシデントの経過（2026年9月27日、スマホ）</figcaption></figure>

ページ上部の「SUBSCRIBE」から、メールなどで障害の通知を受け取ることもできます。

## Claude Codeの529 Overloaded

Claude Codeで「API Error: Repeated 529 Overloaded errors」と出たら、APIがすべての利用者の分で一時的に容量に達しているという意味です。エラーリファレンスによると、Claude Codeはこの表示を出す前にすでに何度か再試行しています。

<figure class="post-figure"><img src="/media/images/claude-error-messages/cem_04_code529.jpg" alt="Claude Codeのエラーリファレンスの529の節。APIは全ユーザー間で一時的に容量に達していて、Claude Codeは表示の前に数回再試行していること、529は使用制限ではなくクォータに数えられないこと、対応方法としてステータスページの確認、数分後の再試行、容量はモデルごとなので/modelで別のモデルに切り替えることが書かれている" loading="lazy"><figcaption>Claude Codeのエラーリファレンスの529の節（2026年9月27日取得）</figcaption></figure>

**529は利用者の使用制限ではなく、使用量にも数えられません。**エラーが続いても、そのぶん5時間の枠が減ることはありません。

ドキュメントの対処は3つです。ステータスページで容量の通知を確かめる、数分後に試す、そして /model で別のモデルに切り替えて作業を続けることです。**容量はモデルごとに管理されているため、Opusが混んでいてもSonnetなら通ることがあります。**1つのモデルに負荷が集中しているときは、Claude Codeのほうから「Opus is experiencing high load, please use /model to switch to Sonnet」のように切り替えを勧める表示も出ます。

CIのように人が見ていない場所で動かしているなら、環境変数 CLAUDE_CODE_RETRY_WATCHDOG を1にすると、429と529の容量のエラーを回数の上限なしで再試行させられます。

## モデルを切り替えて続けられる場合

モデルを変えれば済むのはそのモデルだけが混んでいるか止まっているときです。どのエラーがそれに当たるかは、次のように分かれます。

<figure class="post-figure"><img src="/media/images/claude-error-messages/02_fig_model.png" alt="モデルの切り替えで続けられるかの図。続けられるのは容量がモデルごとに管理されている529 Overloaded、そのモデルの系統だけにかかるOpusの制限とSonnetの制限、特定のモデルだけエラーが増えている障害。続けられないのはすべてのモデルで共有される5時間の制限と週間の制限、1つの会話に入る量の長さ制限、手元の環境やアカウントが原因のログインエラー" loading="lazy"><figcaption>モデルの切り替えで続けられるエラー（Claude Codeのドキュメントとヘルプから作成）</figcaption></figure>

Claude Codeの「You've hit your Opus limit」「You've hit your Sonnet limit」は、それぞれのモデルの系統にだけかかる制限です。**制限がかかったモデルの系統以外に切り替えれば、同じ時間帯でも作業を続けられます。**ただしモデルごとに会話の読み込みのキャッシュが別なので、切り替えた直後の1回は会話全体を読み直すぶん重くなります。

一方の「You've hit your session limit」と「You've hit your weekly limit」は、表示されたリセットの時刻まで待つか、ProとMaxなら使用クレジットで続けます。

## 500と429の見分け方

Claude Codeの「API Error: 500 Internal server error」は、API内部の予期しない障害です。エラーリファレンスには**利用者のプロンプト・設定・アカウントが原因ではない**と書かれています。表示にも「usually temporary」とあり、まず送り直して、続くならステータスページを見てください。インシデントが出ていないのに続く場合は、/feedback で報告するようドキュメントは勧めています。

Claude Codeには、プランの枠とは別の理由で止まる表示が2つあります。

| 表示 | 何が起きているか | 対処 |
|---|---|---|
| Server is temporarily limiting requests (not your usage limit) | サーバー側の一時的な流量制限。プランの枠とは関係ない | 少し待って送り直す |
| Request rejected (429) | APIキーやAmazon Bedrock、Google Cloudのプロジェクトに設定されたレート制限に達した | 使っている認証を /status で確かめ、同時に動かす数を減らす |

「not your usage limit」と括弧で書かれているとおり、1つ目はプランの使用量とは無関係です。2つ目はAPIキーなどで使っている人向けの表示です。エラーリファレンスが最初に /status を勧めているのは、環境に残ったAPIキーがあると、サブスクリプションではなくそのキーを通して送られることがあるためです。

## APIで出るエラーの番号

Claude APIを自分のプログラムから呼んでいる場合は、HTTPの番号とエラーの種類で原因が分かれます。[Claude APIのエラーのドキュメント](https://platform.claude.com/docs/en/api/errors)に一覧があります。

<figure class="post-figure"><img src="/media/images/claude-error-messages/cem_05_api_errors.jpg" alt="Claude APIのエラーのドキュメントのHTTP errorsの節。400のinvalid_request_error、401のauthentication_error、402のbilling_error、403のpermission_error、404のnot_found_error、409のconflict_error、413のrequest_too_large、429のrate_limit_error、500のapi_error、504のtimeout_error、529のoverloaded_errorが並び、529は全利用者の高い負荷で起こりうるという注意書きが付いている" loading="lazy"><figcaption>Claude APIのエラーの一覧（2026年9月27日取得）</figcaption></figure>

| 番号 | 種類 | 意味 |
|---|---|---|
| 400 | invalid_request_error | リクエストの形式か中身の問題 |
| 401 | authentication_error | APIキーの形式の誤り・失効・期限切れ |
| 402 | billing_error | 支払い情報の問題 |
| 429 | rate_limit_error | レート制限か、利用ティア（Tier）ごとの月の上限に達した |
| 500 | api_error | Anthropicのシステム内部の予期しないエラー |
| 504 | timeout_error | 処理中にタイムアウトした |
| 529 | overloaded_error | APIが一時的に過負荷 |

529の原因は、APIに全利用者の高い負荷がかかっていることです。ドキュメントには自分の組織の使用量が急に増えたときに429が出るまれなケースもあると注記されています。避ける方法として、送る量を少しずつ増やし、一定のペースで送るよう勧めています。公式のSDKは接続エラー・レート制限・500番台のエラーを既定で2回まで間隔を空けながら自動で再試行する仕組みです。

## 手元が原因のエラー

アプリで「ログインエラーが発生しました」と出た場合、ヘルプはVPNを使っていないかを確かめ、ブラウザの拡張機能を止め、キャッシュとCookieを消すよう勧めています。それでも出るなら、ステータスページで障害を確かめてください。

画面に「challenges.cloudflare.com のブロックを解除してください」と出る場合は、Cloudflareの確認が拡張機能やネットワークで止められています。見分け方と対処は「[challenges.cloudflare.com のブロック解除の原因と対処](/media/cloudflare-challenges-unblock/)」にまとめています。

長さ制限のエラーは待っても戻りません。**ヘルプによると、コード実行を有効にした有料プランでは、会話が長くなると前のメッセージが自動で要約されるため、ふだんの使い方でこのエラーに当たることはめったにありません。**それでも出るのは、最初のメッセージがとても大きい場合などです。内容を小さく分ける、要点だけを抜き出してから送る、新しい会話を始める、のどれかで対処します。

## よくある質問

### Claudeで容量制約のエラーが出たらいつ直りますか？

ヘルプでは一時的なもので、1日のうちに需要の波が変わるにつれて解消するとされています。数分おいてから送り直してください。

### Claudeのステータスが正常でもエラーが出ますか？

容量制約は障害ではなく通常の負荷の管理なので、ステータスページには載りません。ログインや読み込みで止まるなら、VPN・拡張機能・キャッシュなど手元の原因も考えられます。

### Claude Codeの529は使用量に数えますか？

数えません。Claude Codeのエラーリファレンスに、529は使用制限ではなくクォータに数えないと書かれています。

### Claude Codeで529が続くときは？

数分待つか、/model で別のモデルに切り替えます。容量はモデルごとに管理されているので、混んでいないモデルなら続けられます。

### Claudeでモデルを切り替えれば使用制限は戻りますか？

5時間と週間の制限はすべてのモデルで共有されるので戻りません。Claude CodeのOpusの制限とSonnetの制限は系統ごとなので、もう一方のモデルに切り替えれば続けられます。

### Claude Codeの一時的な制限は使用制限ですか？

使用制限ではありません。「Server is temporarily limiting requests (not your usage limit)」の表示にあるとおり、プランの枠とは別のサーバー側の一時的な流量制限です。少し待って送り直してください。

### ClaudeのAPIで429が出たときはどうしますか？

組織のレート制限か、利用ティア（Tier）ごとの月の上限に達しています。月の上限による429は時間をおいても戻らないので、Claude Consoleで上限を確かめてください。

### Claudeの長さ制限のエラーは待てば直りますか？

直りません。添付するファイルを減らすか小さくする、内容を分けて送る、新しい会話を始める、のどれかで対処します。

## 出典

- Anthropic ヘルプセンター「[Claudeのエラーメッセージのトラブルシューティング](https://support.claude.com/ja/articles/12466728)」（日本語版は2026年3月13日更新、2026年9月27日取得）
- Claude Code ドキュメント「[エラーリファレンス](https://code.claude.com/docs/ja/errors)」（2026年9月27日取得）
- Claude Platform Docs「[Claude API errors](https://platform.claude.com/docs/en/api/errors)」（2026年9月27日取得）
- [Claudeのステータスページ](https://status.claude.com/)（インシデントの件数は2026年9月1日〜27日の日本時間で集計、2026年9月27日取得）
