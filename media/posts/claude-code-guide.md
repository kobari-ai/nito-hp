---
title: 【2026年9月】Claude Codeの使い方を初心者向けに解説｜インストール・基本コマンド・CLAUDE.md・上級編
date: 2026-09-19
category: AI検索対策
description: Claude Codeの使い方を、Anthropicの公式ドキュメント（クイックスタート・セットアップ・権限・メモリ）を一次ソースに、インストールから最初の質問、権限モードの切り替え、必須コマンドとショートカット、CLAUDE.mdの書き方、エンジニア以外の使い道、上級編3つ、つまずきやすい点まで順番に書きました。
cover_tag: 使い方
cover_headline: Claude Codeの使い方
cover_sub: インストールから最初の変更、CLAUDE.md、上級編まで
---

Claude Codeは、Anthropicが提供するコーディングエージェントです。ターミナルで `claude` と打つと、フォルダの中のファイルを読み、編集し、コマンドを実行するところまでを日本語の指示だけで進めてくれます。2026年9月時点ではターミナルのほかにVS Code、JetBrains、デスクトップアプリ、ウェブからも使え、公式ドキュメントにはコードのないフォルダで議事録や資料を扱う使い方も載っています。

この記事は[公式ドキュメントのクイックスタート](https://code.claude.com/docs/ja/quickstart)、[セットアップ](https://code.claude.com/docs/ja/setup)、[インタラクティブモード](https://code.claude.com/docs/ja/interactive-mode)、[権限](https://code.claude.com/docs/ja/permissions)、[メモリ](https://code.claude.com/docs/ja/memory)の各ページ（いずれも2026年9月19日取得）を一次ソースに、インストールから最初の変更、CLAUDE.mdの書き方、上級編までを順番に書いています。料金と使用量の上限は[Claude Codeの料金プランの記事](https://nito-0210.com/media/claude-code-pricing/)にまとめてあるので、この記事の範囲は使い方だけです。

:::takeaways
- Claude Codeは**無料プランでは使えない**。Pro（月$22）以上のプランか、APIの従量課金が必要
- インストールは**1行のコマンド**（macOS・Linux・WSLは `curl -fsSL https://claude.ai/install.sh | bash`、Windowsは PowerShell）。ターミナルを避けたい人はデスクトップアプリ
- 起動は作業フォルダで `claude`。最初は**「このプロジェクトは何をしていますか？」と聞く**だけでいい
- **Shift+Tab で権限モードが切り替わる**。慣れるまでは変更前に確認が出る既定のままか、先に手順だけ出させる計画モード
- 毎回の指示を減らすなら**CLAUDE.md**。`/init` で自動生成でき、公式の目安は**1ファイル200行以下**
:::

## Claude Codeとは何か

Claude CodeはAnthropicの[公式ドキュメント](https://code.claude.com/docs/ja/overview)で「コードベースを読み取り、ファイルを編集し、コマンドを実行し、開発ツールと統合するagentic codingツール」と説明されています。チャット画面のClaudeが「答えを返す」道具だとすると、Claude Codeは「作業を代わりにやる」道具です。指示を受けると、必要なファイルを自分で探して読み、変更を加え、テストを回し、結果を報告します。

| | チャットのClaude（claude.ai） | Claude Code |
|---|---|---|
| 主な入口 | ブラウザ・スマホアプリ | ターミナル・VS Code・デスクトップアプリ |
| ファイルの扱い | 添付したものを読む | フォルダの中を自分で探して読み書きする |
| コマンドの実行 | できない | できる（許可の上で） |
| 向いている作業 | 質問・文章作成・相談 | 複数ファイルにまたがる変更・定型作業の自動化 |
| 料金 | 無料プランあり | 有料プラン（Pro以上）かAPI |

コードを書く道具として作られていますが、公式ドキュメントの[一般的なワークフロー](https://code.claude.com/docs/ja/common-workflows)には「ノートと非コードフォルダで作業する」という節があり、Markdownのメモや資料のフォルダで動かす使い方も正式に案内されています。

## 使う前に必要なもの

必要なものは3つです。有料のアカウント、対応するOS、そしてターミナル（またはデスクトップアプリ）です。

| 必要なもの | 内容（2026年9月19日、公式ドキュメント） |
|---|---|
| アカウント | Claude Pro・Max・Team・Enterpriseのいずれか、またはClaude Console（API）のアカウント。無料プランでは使えない |
| OS | macOS 13.0以上、Windows 10 1809以上、Ubuntu 20.04以上など |
| ハードウェア | 4GB以上のRAM、x64またはARM64 |
| ネットワーク | インターネット接続 |
| 入口 | ターミナル、VS Code、JetBrains、デスクトップアプリ、ウェブのいずれか |

無料プランで `claude` を起動してもログインの段階で止まります。プランの違いと使用量の上限は[料金プランの記事](https://nito-0210.com/media/claude-code-pricing/)に書いたので、この記事で前提にするのは「Pro（月$22）以上に入っている」状態です。

## Claude Codeを使える5つの場所

公式ドキュメントはClaude Codeを使える場所としてターミナル、VS Code、デスクトップアプリ、ウェブ、JetBrainsの5つを並べています。どれを選んでも中身は同じClaude Codeで、違いは画面の操作感と、ファイルの変更をどこで確認するかです。

<figure class="post-figure"><img src="/media/images/claude-code-guide/00_fig_surfaces.png" alt="Claude Codeを使える5つの場所（ターミナル・VS Code・デスクトップアプリ・ウェブ・JetBrains）と、それぞれが向いている人を並べた図" loading="lazy"><figcaption>使える場所は5つ。エンジニア以外はデスクトップアプリかVS Codeから入ると迷いにくい</figcaption></figure>

| 場所 | 向いている人 | 特徴 |
|---|---|---|
| ターミナル（CLI） | コマンド操作に抵抗がない人 | 一番自由度が高い。この記事の手順はここが基準 |
| VS Code拡張 | エディタで差分を見ながら進めたい人 | 変更箇所がエディタ内に差分で出る。@メンションでファイルを指定できる |
| デスクトップアプリ | ターミナルを避けたい人 | Chat・Cowork・Codeの3タブ。macOS・Windows・Linux（ベータ） |
| ウェブ（claude.ai） | 手元のPCに入れたくない人 | GitHubのリポジトリをクラウドで動かす |
| JetBrains | IntelliJ・PyCharmなどを使う人 | プラグインとして入れる |

エンジニアではない人が最初に触るなら、[デスクトップアプリ](https://code.claude.com/docs/ja/desktop)が入りやすいです。解説動画（キノコード「Claude Codeの使い方」）でも、生成されたファイルをその場で開いて確認できるVS Code版かデスクトップアプリ版が非エンジニア向けだと案内されています。以下はターミナル版を基準に書きますが、コマンドはどの入口でも同じです。

## インストールの3つの方法

公式が推奨するのはネイティブインストールで、macOS・Linux・WSLなら1行です。Homebrew、WinGetでも入ります。

<figure class="post-figure"><img src="/media/images/claude-code-guide/00_fig_install.png" alt="OS別のインストール方法。macOS・Linux・WSLはcurl、WindowsはPowerShell、HomebrewとWinGetは自動更新されない注意つき" loading="lazy"><figcaption>インストールは3経路。公式推奨のネイティブインストールだけが自動で更新される</figcaption></figure>

### macOS・Linux・WSL

ターミナルを開いて、次の1行を貼り付けます。

```
curl -fsSL https://claude.ai/install.sh | bash
```

Homebrewを使っている人は `brew install --cask claude-code` でも入ります。ただし公式ドキュメントには、Homebrew版は自動更新されないので `brew upgrade claude-code` を定期的に実行するように書かれています。バックグラウンドで自動更新されるのはネイティブインストール版だけです。

### Windows

PowerShellを開いて、次を実行します。

```
irm https://claude.ai/install.ps1 | iex
```

`winget install Anthropic.ClaudeCode` でも入りますが、こちらも自動更新はされません。コマンドプロンプト（CMD）で `The token '&&' is not a valid statement separator` と出た場合は、CMDではなくPowerShellを使っている状態なので、公式のCMD用コマンドに切り替えます。

### 入ったかどうかの確認

```
claude --version
```

バージョン番号のあとに `(Claude Code)` と表示されれば完了です。以前はNode.jsのインストールが前提でしたが、2026年9月時点のネイティブインストールではNode.jsは不要です。

<figure class="post-figure"><img src="/media/images/claude-code-guide/ccg_01_docs_quickstart.jpg" alt="Claude Code公式ドキュメントのクイックスタート。ステップ1のインストールにネイティブインストール・Homebrew・WinGetの3つのタブ" loading="lazy"><figcaption>公式クイックスタートのインストール手順（2026年9月19日）</figcaption></figure>

## ログインと最初の起動

作業したいフォルダに移動して `claude` と打ちます。

```
cd 作業フォルダのパス
claude
```

初回はログインを求められるので、案内に従ってブラウザで認証します。Pro・Max・Team・Enterpriseのアカウントでログインするのが公式の推奨で、一度ログインすれば認証情報が保存され、次回からは不要です。ログインし直したいときはセッション内で `/login` と打ちます。

ここで1つ注意があります。環境変数 `ANTHROPIC_API_KEY` が設定されていると、Claude Codeはログイン画面を出さずにAPIキーで認証し、従量課金になります。ProやMaxに加入していてもこの環境変数があるとAPIキーが優先される、と公式ヘルプに明記されているので、Proに入ったのにコンソールの残高が減るときは、最初に疑う場所がここです。

起動すると画面上部に出るのはバージョン、使っているモデル、作業ディレクトリの3つです。`/help` で使えるコマンドの一覧が出ます。

## 最初の質問と最初の変更

公式クイックスタートが最初にすすめるのは、コードを書かせることではなく、フォルダの中身を説明させることです。

```
このプロジェクトは何をしていますか？
```

Claude Codeは必要なファイルを自分で読んで概要を返します。ファイルを添付したり、パスを指定したりする必要はありません。「フォルダ構成を説明して」「入口になるファイルはどれ？」と続けると、慣れていないプロジェクトの全体像がつかめます。

次に、小さな変更を頼みます。

```
メインファイルに hello world 関数を追加してください
```

Claude Codeは対象のファイルを見つけ、変更内容を表示し、既定の設定では**書き込む前に確認**を求めます。`Yes` を選ぶまでファイルは変わりません。公式ドキュメントはこの流れを「有能な同僚と話すように」と表現しており、指示が具体的なほど結果は安定するというのが公式の助言です。「バグを直して」ではなく「ログインで間違ったパスワードを入れたあと画面が真っ白になるバグを直して」のように、状況と期待する結果を書くのがコツです。

<figure class="post-figure"><img src="/media/images/claude-code-guide/00_fig_terminal.png" alt="Claude Codeの操作の流れを示した画面イメージ。指示を打つと、ファイルを読み、変更内容を表示し、Yesで書き込む" loading="lazy"><figcaption>操作の流れ（画面イメージ）。指示→ファイルを読む→変更を提示→承認して書き込み</figcaption></figure>

Gitも会話で扱えます。「どのファイルを変更しましたか？」「分かりやすいメッセージでコミットしてください」「feature/quickstart という名前のブランチを作ってください」と頼めば、コマンドを覚えていなくても進みます。

## 権限モードを切り替える

初心者が一番戸惑うのが「許可しますか？」の確認です。Claude Codeはファイルの書き込みやコマンドの実行のたびに確認を出しますが、これは権限モードで変えられます。セッション中に**Shift+Tab**を押すと、モードが順番に切り替わります。

<figure class="post-figure"><img src="/media/images/claude-code-guide/00_fig_modes.png" alt="Claude Codeの権限モード4つ。default（毎回確認）、acceptEdits（編集は自動）、plan（読むだけで計画を出す）、auto（分類器が判断）を並べた図" loading="lazy"><figcaption>Shift+Tabで循環する権限モード。迷ったら既定か計画モード</figcaption></figure>

| モード | 動き | 向いている場面 |
|---|---|---|
| default（Manual） | ツールを初めて使うたびに確認する | 最初の数日。何をしているか把握したいとき |
| acceptEdits | 作業フォルダ内のファイル編集は自動で受け入れる | 編集は任せてよいが、コマンド実行は確認したいとき |
| plan | ファイルを読んで計画を出すだけで、編集しない | 大きめの変更の前。手順を先に見たいとき |
| auto | 分類器が安全性を確認しながら自動で承認する | Pro・Max・Teamのターミナルで使える。慣れてから |

2026年9月時点で、Pro・Max・Teamのターミナルセッションでは**autoモードが既定の開始モード**になっています。分類器がClaudeの行動をリクエストと照らして確認し、ほとんどの作業を確認なしで進めます。動画では「初心者は安全性を判断できないので自動モードか計画モードにするのが安全」と案内されていましたが、何が起きているかを覚える段階では、あえて既定（Manual）に切り替えて確認を1つずつ読むのも悪くありません。`bypassPermissions` という確認をすべて省くモードもありますが、公式ドキュメントも注意書きを付けており、初心者向けではありません。

## 覚えておく基本コマンドとショートカット

公式クイックスタートが「必須コマンド」として挙げているのは、ターミナルから打つシェルコマンド5つと、Claude Codeの中で打つスラッシュコマンド3つです。それに `/compact` `/init` `/model` を足した11個を表にします。

| 種類 | コマンド | 動き |
|---|---|---|
| シェル | `claude` | 対話モードを開始 |
| シェル | `claude "指示"` | 指示つきで開始 |
| シェル | `claude -p "質問"` | 1回だけ答えて終了（スクリプトに組み込める） |
| シェル | `claude -c` | このフォルダの直前の会話を続ける |
| シェル | `claude -r` | 過去の会話を選んで再開 |
| セッション | `/help` | コマンド一覧 |
| セッション | `/clear` | 会話履歴を消して新しい話題へ |
| セッション | `/compact` | 会話を要約して文脈を軽くする |
| セッション | `/init` | CLAUDE.mdを自動生成 |
| セッション | `/model` | モデルを切り替える |
| セッション | `/exit` | 終了（Ctrl+Dを2回でも可） |

ショートカットの一覧は公式の[インタラクティブモード](https://code.claude.com/docs/ja/interactive-mode)のページに一覧があります。その中から、この記事で触れたものを6つ抜き出します。

| キー | 動き |
|---|---|
| Shift+Tab | 権限モードを切り替える |
| Esc | 実行中の応答を止める |
| Esc Esc | 入力を消す、または直前の状態に巻き戻す |
| Ctrl+V（macOSのiTerm2はCmd+V） | クリップボードの画像を貼り付ける |
| Ctrl+O | 詳細な実行ログ（トランスクリプト）を開く |
| Option+P / Alt+P | 入力を消さずにモデルを切り替える |

`/` を打つとコマンドとスキルの一覧が出て、Tabで補完が効きます。↑キーで呼び出せるのは過去の入力です。

<figure class="post-figure"><img src="/media/images/claude-code-guide/ccg_02_docs_shortcuts.jpg" alt="Claude Code公式ドキュメントのキーボードショートカット一覧。Ctrl+C、Ctrl+D、Ctrl+O、Ctrl+Rなどの説明" loading="lazy"><figcaption>公式ドキュメントのショートカット一覧（2026年9月19日）</figcaption></figure>

## CLAUDE.mdでルールを覚えさせる

「日本語で答えて」「コミット前にテストを回して」を毎回書くのは面倒です。そのためにあるのが**CLAUDE.md**で、セッションの開始時に必ず読み込まれる指示書です。

<figure class="post-figure"><img src="/media/images/claude-code-guide/00_fig_claudemd.png" alt="CLAUDE.mdの配置場所4つ。~/.claude/CLAUDE.md（全プロジェクト）、./CLAUDE.md（このプロジェクト、共有）、CLAUDE.local.md（このプロジェクト、自分だけ）、.claude/rules/（ファイル種別ごと）" loading="lazy"><figcaption>CLAUDE.mdの置き場所と届く範囲。まずはプロジェクト直下の1枚から</figcaption></figure>

| 置き場所 | 届く範囲 | 用途 |
|---|---|---|
| `~/.claude/CLAUDE.md` | 自分の全プロジェクト | 「日本語で答える」など個人の好み |
| `./CLAUDE.md` | このプロジェクト（Gitで共有） | ビルド・テストのコマンド、命名規則 |
| `./CLAUDE.local.md` | このプロジェクト（自分だけ） | 手元だけの設定。`.gitignore` に入れる |
| `./.claude/rules/*.md` | このプロジェクトの特定のファイル | 「`*.tsx` を触るときはこの規約」のように範囲を絞る |

一番早い作り方は、プロジェクトのフォルダで `/init` を打つことです。Claude Codeがフォルダを分析して、ビルドコマンドやテストの手順、規約を含む下書きを作ります。全プロジェクト共通の設定は `~/.claude/` という隠しフォルダに置きますが、Finderで見えなくて迷う人が多いところです（macOSは Shift+Cmd+. で表示）。動画で紹介されていたとおり、「すべてのプロジェクトで日本語で答えるように設定して」とClaude Code自身に頼めば、場所を探さなくても作ってくれます。

公式ドキュメントの[メモリ](https://code.claude.com/docs/ja/memory)のページには、書き方の目安が3つ挙げられています。

- **長さ**: 1ファイル200行以下。長いほど文脈を消費し、守られにくくなる
- **具体性**: 「きれいに整形する」ではなく「インデントは2スペース」。「変更をテストする」ではなく「コミット前に `npm test` を実行する」
- **一貫性**: 矛盾する2つのルールがあると、どちらかが無視される

解説動画では指示を100個並べると精度がかえって落ちるので、最初は役割・目標・制約の3点を10行以内で書く、と説明されていました。CLAUDE.mdは毎回の会話の開始時に全文が読み込まれるため、長く書くほど毎回トークンを使うという点も同じ動画で触れられています。`@README` のように書けば別ファイルを取り込めるので、長くなったら分割します。

2026年9月時点のClaude Codeには、CLAUDE.mdとは別に「自動メモリ」もあります。こちらはClaude自身が会話の中で受けた修正や学びを書き留めるもので、リポジトリごとに保存され、次のセッションでも読み込まれます。公式の比較表では「誰が書くか」がCLAUDE.mdは「あなた」、自動メモリは「Claude」と分けられています。

<figure class="post-figure"><img src="/media/images/claude-code-guide/ccg_03_docs_memory.jpg" alt="Claude Code公式ドキュメントの「指示とメモリを保存する」ページ。CLAUDE.mdファイルと自動メモリの比較表" loading="lazy"><figcaption>公式ドキュメントのCLAUDE.mdと自動メモリの比較（2026年9月19日）</figcaption></figure>

## エンジニア以外の使い道

Claude Codeは「どのディレクトリでも動く」と公式が明記しており、コードのないフォルダでも使えます。解説動画（キノコード「Claude Codeの使い方」、Y0a0zqSPtssの回）で紹介されていた非エンジニア向けの使い道は次のようなものでした。

- **議事録とタスクの抽出**: 会議の文字起こしを入力フォルダに置き、「要約して見出しを付け、ToDoを抜き出して出力フォルダにMarkdownで保存して」と頼む
- **フォルダの整理**: ダウンロードフォルダのファイルを種類ごとに分ける、重複を見つける
- **画像の読み取り**: エラー画面や図のスクリーンショットをCtrl+Vで貼り、「この画面のエラーの原因は？」と聞く
- **外部サービスとの連携**: [MCP](https://code.claude.com/docs/ja/mcp)でGoogleカレンダーやSlackをつなぎ、「今日の予定から議事録のテンプレートを作って」と頼む

このうちフォルダの整理と議事録は、デスクトップアプリのCoworkタブのほうが向いています。Coworkはローカルのファイルの読み書きに絞られていて、コマンドの実行が要らない作業なら制限が少ないぶん挫折しにくい、というのが動画の整理でした。

## 上級編

基本を覚えたあとで効いてくる使い方を3つに絞ります。

### ① 計画モードで手順を先に出させる

大きめの変更を頼む前に、Shift+Tabで**plan**に切り替えます。Claude Codeはファイルを読んで探索しますが、ソースファイルは編集しません。代わりに「何をどの順番で変えるか」を計画として出すので、それを読んでから承認します。公式ドキュメントの「編集前に計画する」の節にある通り、ステータスバーに `⏸ plan mode on` と出ていれば計画モードです。動画では「計画はOpus、実装はSonnet」のようにモデルを分ける例も紹介されていました。

### ② /compact とモデルの切り替えで文脈を軽くする

会話が長くなると応答が遅くなり、トークンの消費も増えます。話題が変わるときは `/clear`、続けたいが履歴が重いときは `/compact` で要約します。`/model` でモデルを切り替えることもでき、Option+P（Alt+P）なら入力中の文章を消さずに切り替わります。動画では計画はOpus、ファイルの生成や実装は速くてトークン消費の少ないSonnet、という分け方が紹介されていました。

### ③ 定型作業をスキルにする

同じ手順を何度も頼むなら、[スキル](https://code.claude.com/docs/ja/skills)にします。`.claude/skills/<スキル名>/SKILL.md` に手順を書くと、フォルダ名がそのまま `/スキル名` というコマンドになります。「週次レポートの作り方」「議事録の整形」のような定型作業に向いています。動画で紹介されていた通り、ファイルを自分で組まなくても「この作業をスキルにして」と頼めば構成ごと作ってくれます。

スキルがCLAUDE.mdと違うのは、最初は名前と説明文だけが読み込まれ、必要と判断されたときにだけ本文が読まれる点です。CLAUDE.mdに手順を全部書くより文脈を圧迫しません。

## つまずきやすい点

公式ドキュメントと解説動画に共通して出てきた、初心者が止まりやすい点をまとめます。

| つまずき | 原因 | 対処 |
|---|---|---|
| ログインで止まる | 無料プランで使おうとしている | Pro以上に入るか、ConsoleでAPIクレジットを買う |
| Proなのに残高が減る | 環境変数 `ANTHROPIC_API_KEY` がある | 環境変数を外して `/login` でログインし直す |
| Windowsでコマンドがエラー | CMDでPowerShell用のコマンドを打っている | PowerShellを使う |
| アプリを作ろうとしてNode.jsを要求される | 作りたいものに実行環境が要る | Claude Codeにインストール手順を聞く。またはHTML単体で動くものとして頼む |
| 上限に達した | 5時間枠を使い切った | 待つか、上位プランか、使用クレジット。詳細は料金の記事 |
| 隠しフォルダが見つからない | `~/.claude` は非表示 | Shift+Cmd+.（macOS）で表示。またはClaude Codeに作らせる |

上限の仕組みと、上限に当たったときの3つの選択肢は[料金プランの記事](https://nito-0210.com/media/claude-code-pricing/)に詳しく書いています。インストールやログインのエラーは公式の[トラブルシューティング](https://code.claude.com/docs/ja/troubleshooting)に対処法がまとまっています。

## よくある質問

Googleの「他の人はこちらも質問」に出ている質問が中心です。

### Claude Codeはどう使いますか？

作業したいフォルダでターミナルを開き、`claude` と打って起動します。あとは日本語で「このプロジェクトは何をしていますか？」「〇〇の関数を追加して」と話しかけるだけです。ファイルの読み書きやコマンドの実行はClaude Codeが自分で行い、既定の設定では書き込む前に確認が出ます。

### Claude Codeはどこから使えますか？

ターミナル、VS Code、JetBrains、デスクトップアプリ、ウェブ（claude.ai）の5つです。公式ドキュメントはターミナルを基準に書かれていますが、ターミナルを避けたい人はデスクトップアプリ、エディタで差分を見たい人はVS Code拡張が向いています。

### Claude Codeは無料で使えますか？

使えません。Claude Pro（月$22、年払いなら月$18）以上のプランに加入するか、Claude ConsoleでAPIのクレジットを買う必要があります。2026年9月19日時点の日本向け料金ページの表示です。

### Claude Codeは何ができますか？

フォルダの中のファイルを読んで説明する、複数ファイルにまたがる変更を加える、テストやビルドを実行する、Gitのコミットやブランチを操作する、画像を読み取る、MCPで外部サービスとつなぐ、といったことができます。コードのないフォルダで議事録や資料の整理に使うことも公式に案内されています。

### Claude CodeはWindowsで使えますか？

使えます。Windows 10 1809以上またはWindows Server 2019以上が対象で、PowerShellから `irm https://claude.ai/install.ps1 | iex` でインストールします。WSLでもmacOSと同じ手順で入ります。

### Claude Codeは日本語で使えますか？

使えます。指示も応答も日本語で問題ありません。常に日本語で答えてほしい場合は、`~/.claude/CLAUDE.md` に「日本語で答える」と書いておくと、すべてのプロジェクトで有効になります。

### Claude Codeで勝手にファイルを消されませんか？

既定の権限モードではファイルの書き込みやコマンドの実行の前に確認が出ます。変更の内容を見てから承認する運用なら、意図しない削除は防げます。不安な作業は計画モード（Shift+Tabで切り替え）で手順だけ先に出させると安全です。Gitで管理しているフォルダなら、変更を戻すこともできます。

### Claude Codeの上限に達したらどうなりますか？

5時間ごとの枠と1週間の枠があり、使い切ると枠がリセットされるまで待つか、上位プランに変えるか、使用クレジットを買って続けるかの3択です。勝手に課金されることはありません。仕組みは[料金プランの記事](https://nito-0210.com/media/claude-code-pricing/)に書いています。

## 出典

- [Claude Code クイックスタート](https://code.claude.com/docs/ja/quickstart)（Anthropic、2026年9月19日取得）
- [Claude Code セットアップ（システム要件・インストール）](https://code.claude.com/docs/ja/setup)（同上）
- [Claude Code インタラクティブモード（ショートカット）](https://code.claude.com/docs/ja/interactive-mode)（同上）
- [Claude Code 権限（権限モード）](https://code.claude.com/docs/ja/permissions)（同上）
- [Claude Code 指示とメモリを保存する（CLAUDE.md）](https://code.claude.com/docs/ja/memory)（同上）
- [Claude Code 一般的なワークフロー](https://code.claude.com/docs/ja/common-workflows)（同上）
- [Claude Code スキル](https://code.claude.com/docs/ja/skills)、[デスクトップ版](https://code.claude.com/docs/ja/desktop)（同上）
- [Anthropic 料金ページ（日本向け）](https://claude.com/ja/pricing)（2026年9月18日取得）
- 解説動画: キノコード「Claude Codeの使い方」（YouTube、EpUWXT0Fcic・Y0a0zqSPtss。使用感と数値は投稿者の実測で第三者検証なし）
