---
title: 【2026年9月】Claude MCPとは？Claude Codeへの接続方法を解説｜4つのトランスポート・3つのスコープ・認証・つまずきどころ
date: 2026-09-21
category: AI検索対策
description: Claude MCPを公式ドキュメントを一次ソースに解説。MCPの役割、claude mcp addの4つの接続方法、local・project・userのスコープ、OAuth認証、サーバー状態の読み方、設定でつまずく箇所まで。
cover_tag: 使い方
cover_headline: Claude MCPの接続方法
cover_sub: トランスポート・スコープ・認証・つまずきどころ
---

MCP（Model Context Protocol）は、AIツールと外部のデータやツールをつなぐためのオープンな規格です。Claude Codeはこの規格を通じて数百のツールに接続でき、課題管理やデータベース、デザインツールの中身を、コピーして貼り付けることなく直接読み書きできます。

接続そのものは `claude mcp add` の一行で終わります。つまずくのはその先で、どのトランスポートを選ぶか、設定をどこに保存するか、チームで共有したサーバーがなぜ承認待ちのまま動かないのか、といった部分です。以下はAnthropicの[Claude Code公式ドキュメント](https://code.claude.com/docs/ja/mcp)（2026年9月21日取得）を一次ソースにした、接続の手順と、運用でつまずく箇所です。

:::takeaways
- MCPは**AIと外部ツールをつなぐ共通規格**で、Claude Code固有の機能ではない。同じサーバーを他のMCPクライアントでも使える
- 接続方法は4つ。リモートは**HTTPが推奨**で、SSEは非推奨、ローカルのプロセスはstdio、サーバーから割り込みを受けたいときだけWebSocket
- 設定の保存先は3つ。**local（既定・自分だけ）／project（.mcp.jsonでチーム共有）／user（全プロジェクト）**。同じ名前があればlocalが勝つ
- プロジェクトスコープのサーバーは**承認を通すまで接続されない**。`⏸ Pending approval` はこれ
- 外部のコンテンツを取ってくるサーバーは**プロンプトインジェクションの経路になりうる**。信頼できるサーバーだけを入れ、データベースは読み取り専用ユーザーでつなぐ
:::

## MCPとは何か

「AIが社内のツールを触れない」という制約は、モデルの性能ではなく接続の問題です。MCPはその接続の作法をツールごとにバラバラに実装せずに済ませるための共通規格で、[modelcontextprotocol.io](https://modelcontextprotocol.io/docs/getting-started/intro) で公開されています。

公式ドキュメントには導入を検討する目安がはっきり書かれています。課題追跡ツールや監視ダッシュボードから**チャットにデータをコピーしている作業があるなら、そのシステムをつなぐ**、という基準です。貼り付けたものから作業する代わりに、Claudeがそのシステムを直接読み書きできる状態にします。

<figure class="post-figure"><img src="/media/images/claude-mcp-guide/cm_01_docs.jpg" alt="Claude Code公式ドキュメント「MCPを使用してClaude Codeをツールに接続する」。別のツールからチャットにデータをコピーしている場合はサーバーを接続してくださいと書かれている" loading="lazy"><figcaption>公式ドキュメント。つなぐ基準は「チャットにコピーしている作業があるか」</figcaption></figure>

MCPサーバーはClaude Code専用ではありません。同じサーバーをClaude Desktopや他のMCPクライアントでも使えるため、セットアップ手順が別のクライアント向けに書かれていることがよくあります。その読み替え方は後述します。

## MCPで何ができるか

公式ドキュメントが挙げている依頼の例は、どれも複数のツールをまたぐものです。

- 課題追跡ツールから機能を実装する（JIRAの課題に書かれた内容を実装し、GitHubにPRを作る）
- 監視データを分析する（SentryとStatsigで機能の使用状況を確認する）
- データベースをクエリする（PostgreSQLから条件に合うユーザーを検索する）
- デザインを統合する（Slackに投稿されたFigmaのデザインをもとにテンプレートを更新する）
- ワークフローを自動化する（対象者へのGmail下書きをまとめて作る）

このほかにMCPサーバーは**チャネル**としても動きます。サーバー側からセッションにメッセージを押し込めるため、離席中に届いたDiscordのチャットやwebhookのイベントにClaudeが反応できます。使うにはサーバーが `claude/channel` 機能を宣言し、起動時に `--channels` フラグで有効にしてください。

接続するサーバーは[Anthropic Directory](https://claude.com/directory)で探せます。DirectoryのコネクターはClaude Codeと同じMCPの仕組みを使うため、`claude mcp add` でそのまま追加できます。

## サーバーを追加する4つの方法

トランスポートはサーバーがどこで動くかで決まります。

| 方法 | どんなサーバー向きか | 追加の仕方 |
|---|---|---|
| HTTP（推奨） | クラウド上のサービス。最も広くサポートされている | `claude mcp add --transport http <name> <url>` |
| SSE（非推奨） | SSEのエンドポイントしか公開していないサービス | HTTPと同じコマンド（自動で切り替わる） |
| stdio | 自分のマシンで動かすプロセス、カスタムスクリプト | `claude mcp add <name> -- <command> [args...]` |
| WebSocket | サーバー側から予期しないイベントを押し込みたい場合 | `claude mcp add-json` で `"type":"ws"` を指定 |

<figure class="post-figure"><img src="/media/images/claude-mcp-guide/00_fig_transports.png" alt="MCPサーバーを追加する4つの方法の図。HTTPは推奨でクラウド上のサービス向けOAuth対応、SSEは非推奨でHTTPと同じコマンド、stdioはローカルのプロセスで--の後ろがサーバーのコマンド、WebSocketはサーバー側からイベントを押し込みたいときでOAuthは使えない" loading="lazy"><figcaption>4つのトランスポートの選び分け</figcaption></figure>

リモートのサービスをつなぐならHTTPを選んでください。SSEしか公開していないサーバーも、HTTPと同じコマンドで追加できます。Claude CodeがまずHTTPを試し、受け付けられなければSSEに切り替えるためです。

```
claude mcp add --transport http notion https://mcp.notion.com/mcp
```

ローカルのプロセスを動かすstdioでは、`--`（ダブルダッシュ）の位置が重要です。`--` より後ろはすべてサーバーを起動するコマンドとして渡され、前にあるものはClaude Code自身のオプションとして解釈されます。

```
claude mcp add --env AIRTABLE_API_KEY=YOUR_KEY --transport stdio airtable -- npx -y airtable-mcp-server
```

`--` を書かないと、サーバー側のフラグ（`--port` など）をClaude Codeが自分のオプションとして読もうとして失敗します。`--env` を複数渡すときは、サーバー名が `--env` の直後に来ないよう、間に別のオプションを挟みます。

WebSocketだけは `claude mcp add --transport` が受け付けないため、`claude mcp add-json` で指定します。OAuthにも対応していないので、認証はヘッダーで渡します。**サーバーがリクエストに応えるだけならHTTPを選ぶ**、というのが公式の指針です。

## 他のクライアント向けの手順を読み替える

MCPサーバーの導入手順は、Claude DesktopやCursor向けに書かれていることがあります。`claude mcp add` のコマンドが載っていなくても、手元にある情報は次の3つのどれかです。

**URLがある場合**、そのサーバーはリモートにあります。`https://` なら `--transport http` で追加し、`wss://` ならWebSocketの手順を使います。APIキーやトークンのヘッダーが指定されていれば `--header` で渡します。

**`npx -y @example/mcp-server` のような起動コマンドがある場合**は、ローカルのstdioサーバーです。コマンド全体を `--` の後ろに置きます。

```
claude mcp add example --env API_KEY=your-key -- npx -y @example/mcp-server
```

**`mcpServers` のJSONブロックがある場合**は、`mcpServers` の中身のオブジェクトだけを `claude mcp add-json` に渡します。ラッパーごと渡すのではありません。

```
claude mcp add-json example '{"command":"npx","args":["-y","@example/mcp-server"]}'
```

このとき2か所を直す必要があります。ひとつが、`url` はあるのに `type` がないエントリです。Claude Codeは `type` のないエントリをstdioサーバーとして読むため、`"type": "http"`（または `sse`、`ws`）を足さないとそのサーバーはスキップされます。もうひとつはサーバー名で、使えるのは英数字とハイフンとアンダースコアだけです。

## 3つのスコープと優先順位

`claude mcp add` は、`--scope` を付けなければローカルスコープに書き込みます。3つのスコープで違うのはこの2点です。どのプロジェクトで読み込まれるか、そしてチームと共有されるかどうか。

| スコープ | 読み込まれる範囲 | チームと共有 | 保存場所 |
|---|---|---|---|
| local（既定） | 追加したプロジェクトだけ | されない | `~/.claude.json` |
| project | そのプロジェクトだけ | される（バージョン管理経由） | プロジェクトルートの `.mcp.json` |
| user | すべてのプロジェクト | されない | `~/.claude.json` |

<figure class="post-figure"><img src="/media/images/claude-mcp-guide/00_fig_scopes.png" alt="MCPの3つのスコープの図。localは既定で~/.claude.jsonに保存され追加したプロジェクトだけ、projectはプロジェクトルートの.mcp.jsonでチームと共有し各自の承認が要る、userは~/.claude.jsonで全プロジェクト。同名はlocalからclaude.aiコネクタの順に優先しフィールドはマージされない" loading="lazy"><figcaption>スコープは保存場所と共有範囲で選ぶ</figcaption></figure>

localは個人の実験や、バージョン管理に入れたくない認証情報を持つサーバー向けです。名前が紛らわしいのですが、**MCPのローカルスコープが書き込むのはホームディレクトリの `~/.claude.json`** で、一般的なローカル設定の `.claude/settings.local.json` とは別のファイルです。

projectは `.mcp.json` に書き込まれ、これをバージョン管理に入れるとチーム全員が同じサーバーを使えます。ただし**セキュリティ上の理由から、`.mcp.json` のサーバーは対話セッションで承認するまで使われません**。承認の選択をやり直すには `claude mcp reset-project-choices` を実行します。

同じ名前のサーバーが複数の場所にある場合、Claude Codeは優先度の高いほうの定義を使って1回だけ接続します。順番はlocal、project、user、プラグイン提供、claude.aiコネクタの順で、**フィールドはスコープをまたいでマージされません**。片方の定義が丸ごと使われます。

## リモートサーバーで認証する

多くのクラウド型サーバーは認証を求めてきます。Claude CodeはOAuth 2.0に対応しており、`/mcp` を実行してブラウザでログインすれば、トークンは安全に保存され、以後の更新も自動です。

ターミナルから直接サインインすることもできます。

```
claude mcp login sentry
```

SSH越しなど、手元にブラウザがない環境では、このコマンドが認可URLを出力します。ローカルのマシンでそのURLを開き、リダイレクト先の完全なURLをプロンプトに貼り付けます。貼り付けの工程があるため、`ssh -t` で対話的な端末を確保しておきます。保存した認証情報を消すときは `claude mcp logout <name>` です。

よくつまずくのが「Incompatible auth server: does not support dynamic client registration」というエラーです。これは動的クライアント登録に対応していないサーバーで、開発者ポータルでOAuthアプリを登録し、クライアントIDとシークレットを渡す必要があります。リダイレクトURIを登録する場合は `http://localhost:PORT/callback` の形にして、追加時の `--callback-port` と同じポートを指定します。

```
claude mcp add --transport http --client-id your-client-id --client-secret --callback-port 8080 my-server https://mcp.example.com/mcp
```

`--client-secret` は値を書きません。実行するとマスクされた入力でシークレットを聞かれるため、シェルの履歴には残らない形です。保存先はmacOSのキーチェーンか認証情報ファイルで、設定ファイルには書かれません。後から変更するなら、いったん `claude mcp remove` してから同じスコープで追加し直してください。

なお、`headers.Authorization` を自分で設定したサーバーが認証に失敗した場合、Claude CodeはOAuthに切り替えず、接続失敗として報告します。トークンを直すか、ヘッダーを外してOAuthに任せるかのどちらかです。

## サーバーの状態を読む

`claude mcp add` が出す `Added ...` は、設定が書き込まれたという意味でしかありません。つながったかどうかは `claude mcp list` か、セッション内の `/mcp` で確認します。

| 表示 | 意味 | すること |
|---|---|---|
| ✔ Connected | 接続済み | なし |
| ! Needs authentication | 認証が必要 | `/mcp` か `claude mcp login <name>` でサインイン |
| ✘ Failed to connect | 接続に失敗 | 同じ行に出るHTTPステータスやエラーを読む |
| ⏸ Pending approval | `.mcp.json` のサーバーが未承認 | `claude` を対話的に起動して承認する |
| ⊘ Disabled for this project | このプロジェクトで無効 | `/mcp` のパネルから戻す |

<figure class="post-figure"><img src="/media/images/claude-mcp-guide/00_fig_status.png" alt="claude mcp listが出す5つの状態と対処の表。Connectedは接続済み、Needs authenticationは/mcpかclaude mcp loginでサインイン、Failed to connectは同じ行のHTTPステータスを読む、Pending approvalはclaudeを対話的に起動して承認、Disabledは/mcpのパネルから戻す" loading="lazy"><figcaption>状態ごとに、次にすることが決まる</figcaption></figure>

`✘ Failed to connect` はサーバーに接続できなかったという意味で、`list` コマンドが失敗したわけではありません。失敗の詳細にはサーバーが返したHTTPステータス（401など）とエラーテキストが付きます。認証情報のように見えるテキストと展開後のURLは、秘密が混ざりうるため伏せられます。

WebSocketのサーバーは `claude mcp list` の出力に表示されません。消えたわけではないので、`claude mcp get <name>` か `/mcp` のパネルで確認します。

## 設定でつまずく箇所

公式ドキュメントにはClaude Codeが警告を出す設定ミスが列挙されています。どれも原因が見えにくいものばかりです。

**隠れた空白**はトークンを貼り付けたときに起きます。末尾の改行まで一緒に入ってしまうためです。Claude Codeは `command`・`url`・`args`・`env`・`headers` の値とキー名をチェックし、`Leading or trailing whitespace in: headers.Authorization` のように場所を名指しします。**空白は自動では取り除かれない**ので、設定を直します。

**予約名**も引っかかります。`workspace`、`claude-in-chrome`、`computer-use`、`Claude Preview`、`Claude Browser` は組み込みサーバーの名前として予約されており、同じ名前のサーバーは読み込み時にスキップされます。

**環境変数の展開**で `${VAR}` が未設定でデフォルトもない場合、設定は読み込まれるものの `${VAR}` という文字列がそのまま使われます。`${VAR:-default}` を書いておくと安全です。

リモートサーバーの `url` と `headers` では、**`ANTHROPIC_API_KEY` や `AWS_BEARER_TOKEN_BEDROCK`、`NPM_TOKEN` のような認証情報の変数が、意図的に空として読み込まれます**。プロジェクトの `.mcp.json` やプラグインが、Claude Code自身の認証情報を外部のサーバーへ送ってしまうのを防ぐためです。`Bearer ${ANTHROPIC_AUTH_TOKEN}` と書くとサーバーには `Bearer ` だけが届き、たいてい401で弾かれます。渡したい場合は自分の名前の変数にコピーして、その名前を参照します。

<figure class="post-figure"><img src="/media/images/claude-mcp-guide/00_fig_pitfalls.png" alt="設定でつまずく4つの図。隠れた空白は自動では取り除かれない、予約名は同名だとスキップされる、${VAR}が未設定だと文字列のまま読み込まれる、リモートのurlとheadersでは認証情報の変数が意図的に空として読まれる" loading="lazy"><figcaption>どれも原因が見えにくい4つ</figcaption></figure>

タイムアウトまわりも押さえておくと、途中で切れたときに慌てずに済みます。

- サーバー起動のタイムアウトは `MCP_TIMEOUT`（ミリ秒）
- ツール実行のタイムアウトは `.mcp.json` の `timeout`。サーバーごとに指定でき、1000未満は無視される
- 応答も進捗通知も返さない呼び出しは、アイドルとして中断される。既定はリモートが5分、stdioが30分
- **2分を超えた呼び出しは自動でバックグラウンドのタスクに移り**、セッションは止まらない。結果は通知として届く
- MCPツールの出力が10,000トークンを超えると警告が出て、既定で25,000トークンに制限される。上げるには `MAX_MCP_OUTPUT_TOKENS`

<figure class="post-figure"><img src="/media/images/claude-mcp-guide/00_fig_timeouts.png" alt="MCPのタイムアウトと制限の表。サーバー起動はMCP_TIMEOUT、ツール実行は.mcp.jsonのtimeout、無反応での打ち切りはリモート5分stdio30分、2分でバックグラウンドへ、出力は25,000トークン制限で1万で警告" loading="lazy"><figcaption>止まったときに見る5か所</figcaption></figure>

## claude.aiのコネクターとの関係

claude.aiのアカウントでClaude Codeにログインしている場合、claude.aiに追加したMCPサーバー（コネクター）はClaude Codeでも自動的に使えます。設定は [claude.ai/customize/connectors](https://claude.ai/customize/connectors) で行います。TeamとEnterpriseのプランでは、追加できるのは管理者だけです。

Claude Desktopで設定済みのサーバーは、そのまま取り込めます。

```
claude mcp add-from-claude-desktop
```

対話的なダイアログで取り込むサーバーを選ぶ形式で、macOSとWSLでのみ動きます。ひとつ注意点があり、`claude mcp` が受け付けるサーバー名は英数字とハイフンとアンダースコアだけなので、スペースを含む名前のサーバーは取り込めません。取り込みは拒否した名前を報告し、残りは通常どおり追加します。

## 安全に使うために

公式ドキュメントには接続する前に**そのサーバーを信頼できるか確認する**よう明記されています。外部のコンテンツを取得するサーバーは、プロンプトインジェクションの経路になりうるためです。取ってきたページや課題の本文に指示のような文字列が混ざっていれば、それがAIへの入力になります。

実務で効く対策は2つあります。ひとつが、データベースをつなぐときに**読み取り専用のユーザーで接続文字列を書く**ことです。公式の例も読み取り専用ユーザーを使っています。もうひとつが、`headersHelper` のように任意のシェルコマンドを実行する設定を、信頼したフォルダでしか動かさないことです。Claude Codeはプロジェクトの `.mcp.json` にあるヘルパーを、そのディレクトリの信頼ダイアログを受け入れるまで実行しません。

リポジトリやプラグインが提供する `headersHelper` は、環境から認証情報らしき変数を取り除いた状態で実行されます。名前に `TOKEN`・`SECRET`・`PASSWORD`・`KEY`・`AUTH` を含む変数が対象なので、ヘルパー側はファイルや認証情報ストアから読む作りにします。

## AI検索での見え方は別の話

MCPで自社のデータをAIにつなぐことと、自社がAIの回答に登場することは別の問題で、後者は[AI検索対策](https://nito-0210.com/llmo/)として扱います。

## よくある質問

Claude MCPについて検索されている関連質問を中心に答えます。

**Claude MCPで何ができますか？**
課題追跡ツールの内容を読んで実装する、監視データを分析する、データベースをクエリする、デザインツールの更新を反映する、といった外部ツールをまたぐ作業ができます。サーバーがチャネルに対応していれば、外部で起きたイベントにClaudeが反応することもできます。

**MCPサーバーはどこで探せますか？**
Anthropic Directoryにレビュー済みのコネクターがまとまっています。Directoryのサーバーは `claude mcp add` でそのまま追加できます。

**HTTPとSSEとstdioはどう選びますか？**
クラウドのサービスはHTTP、自分のマシンで動かすものはstdioです。SSEは非推奨で、SSEしか公開していないサーバーもHTTPと同じコマンドで追加でき、Claude Codeが自動で切り替えます。

**チームで同じMCPサーバーを使うにはどうしますか？**
`--scope project` で追加して、プロジェクトルートの `.mcp.json` をバージョン管理に入れます。各メンバーは最初に対話セッションで承認する必要があります。

**サーバーが「Pending approval」のまま動きません。**
`.mcp.json` のプロジェクトスコープのサーバーが未承認の状態です。`claude` を対話的に起動して承認します。クローンしたリポジトリでは、ワークスペースの信頼ダイアログを受け入れるまで自分のサーバーを承認できません。

**設定を消さずにサーバーを止められますか？**
`/mcp` のパネルでオフに切り替えると、設定を残したまま接続を止められます。選択はプロジェクトごとに `~/.claude.json` に記録されます。

**MCPサーバーを入れるとセキュリティ上のリスクはありますか？**
外部のコンテンツを取得するサーバーはプロンプトインジェクションの経路になりえます。信頼できるサーバーだけを入れ、データベースは読み取り専用ユーザーでつないでください。

**ツールの呼び出しが途中で止まります。**
応答も進捗通知も返さない呼び出しは、アイドルとして中断されます。既定の待ち時間はリモートが5分、stdioが30分です。実行時間そのものが長い場合は、2分を超えた時点で自動的にバックグラウンドのタスクへ移ります。

## 出典

本文の事実関係はAnthropicの公式ドキュメントで確認しています（2026年9月21日取得）。

- [MCPを使用してClaude Codeをツールに接続する](https://code.claude.com/docs/ja/mcp)
- [Model Context Protocol 公式サイト](https://modelcontextprotocol.io/docs/getting-started/intro)
- [Anthropic Directory](https://claude.com/directory)
