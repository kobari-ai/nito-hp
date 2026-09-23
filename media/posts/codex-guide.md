---
title: 【2026年9月】Codexの使い方を解説｜4つの入口とプラン別にできること
date: 2026-09-23
category: AI検索対策
description: OpenAIのCodexは、デスクトップアプリ・CLI・IDE拡張・クラウドの4つの入口があります。公式ドキュメントから入口ごとの違い、プラン別に使える範囲、権限モードの選び方を整理します。
cover_tag: 使い方
cover_headline: Codexの使い方
cover_sub: 4つの入口とプラン別にできること
---

Codexを調べると「ターミナルにインストールして使うツール」という説明と「ChatGPTのサイドバーから開く機能」という説明が両方出てきます。どちらも間違いではありません。いまのCodexには**入口が4つ**あり、どこから入るかでプランの条件も使える機能も変わります。

ここではOpenAIの[Codexドキュメント](https://developers.openai.com/codex/)と[ヘルプセンター](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)（2026年9月23日取得）から、入口ごとの違いと最初の設定を整理します。ChatGPT本体の使い方は[ChatGPTの使い方の記事](https://nito-0210.com/media/chatgpt-guide/)にまとめています。

:::takeaways
- 入口は**デスクトップアプリ・CLI・IDE拡張・クラウド**の4つ
- **無料プランとGoで使えるのはデスクトップアプリだけ**。CLIとIDE拡張とクラウドはPlus以上
- CLIの導入は`curl`1行。最初に`/init`でAGENTS.mdを作り、`/permissions`で権限を決める
- 権限は**触れる範囲と、止まるタイミング**の2つで決まる。承認役を変えても範囲は広がらない
- **GPT-5.5は2026年10月14日にChatGPT側から引退**する。設定に書いてある人は入れ替えが要る
:::

## Codexは4つの入口を持つ

まず全体像です。同じCodexでも、入る場所によって扱えるものが変わります。

<figure class="post-figure"><img src="/media/images/codex-guide/cx_04_fig_entry.png" alt="Codexの4つの入口の比較図。デスクトップアプリは全プラン、CLIとIDE拡張とクラウドはPlus以上。APIキーで入るとクラウド側の機能は使えずAPI課金になる" loading="lazy"><figcaption>4つの入口と、それぞれが使えるプラン</figcaption></figure>

はじめて触るなら、手元のコードを読ませて説明させるところから入るのが早道です。

デスクトップアプリのCodexは、ChatGPTのアプリの中にある別の画面です。左上のメニューでChatGPTとCodexを切り替えます。ChatGPT側にはChatとWorkの2つがあり、Codexはそれらと履歴が分かれています。ウェブとモバイルのアプリからCodexを選ぶことはできません。モバイルアプリのRemoteタブから、デスクトップで動いているCodexのチャットに触れる形になります。

## プラン別に何ができるか

公式の料金ページは無料からEnterpriseまでCodexが含まれると書いたうえで、プランごとに使える入口を分けています。

| プラン | 月額 | Codexで使えるもの |
|---|---|---|
| 無料 | $0 | デスクトップアプリでGPT-6 Lunaを標準速度で |
| Go | $8 | デスクトップアプリでGPT-6 Lunaを標準速度で |
| Plus | $20 | ウェブ・CLI・IDE拡張・iOS、クラウド連携、GPT-6 SolとGPT-6 Luna |
| Pro | $100から | Plusの5倍または20倍の利用量 |
| Business | 1人$20（年額課金） | デスクトップとモバイル、大きい仮想マシン、管理機能 |

<figure class="post-figure"><img src="/media/images/codex-guide/cx_02_pricing.jpg" alt="OpenAIのCodex料金ページ。無料が0ドル、Goが8ドル、Plusが20ドル、Proが100ドルからで、各プランに含まれる内容が並んでいる" loading="lazy"><figcaption>公式の料金ページに並ぶ個人向けプラン</figcaption></figure>

境目はPlusです。ターミナルやエディタから使いたいなら、無料やGoでは届きません。

Businessは2人以上で年額課金のときの金額で、月額課金なら1人$25になります。APIキーで使う道もあり、この場合はCLIとSDKとIDE拡張が対象です。GitHubの自動コードレビューやSlack連携といったクラウド側の機能は付かず、料金はAPIの従量課金になります。

ChatGPT WorkとCodexは利用量を共有します。料金ページの説明はコーディングの作業を前提にしているので、Workで文書や資料を作る場合の消費は作業ごとに変わります。

## ターミナルから使う手順

CLIの導入は1行です。macOSとLinuxでは次のコマンドを実行します。

```
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

同じコマンドが更新にも使えます。npmやHomebrew、Windows向けの手順も公式に載っています。

インストールが終わったら、対象のプロジェクトのディレクトリで`codex`と打つだけです。初回はChatGPTでのサインインか、別のサインイン方法かを選びます。ChatGPTでサインインすると、契約しているプランの利用量と請求の扱いになります。APIキーを使う場合はAPIの料金です。

起動直後に案内されるコマンドが、そのまま最初にやることの並びです。

<figure class="post-figure"><img src="/media/images/codex-guide/cx_01_docs.png" alt="Codex CLIの公式ドキュメント。ターミナルの画面にmodel gpt-6-sol mediumと表示され、slash initやslash permissionsなどのコマンドが並んでいる" loading="lazy"><figcaption>公式ドキュメントに載っているCLIの起動画面</figcaption></figure>

`/init`はAGENTS.mdを作るコマンドです。プロジェクトの約束ごとをここに書いておくと、毎回同じ説明をしなくて済みます。

- `/init` プロジェクトの指示を書くAGENTS.mdを作る
- `/status` いまのセッションの設定を表示する
- `/permissions` できることの範囲を選ぶ
- `/model` モデルと推論の深さを選ぶ
- `/review` 変更を確認して問題を探す

公式は作業の前後でGitのチェックポイントを作って、いつでも戻せるようにすることを勧めています。

## 権限は範囲と止まり方で決める

Codexにローカルの操作を任せる以上、最初に決めるのは権限です。公式は3つのモードを用意しています。

<figure class="post-figure"><img src="/media/images/codex-guide/cx_05_fig_perm.png" alt="Codexの権限モード3種の比較図。Ask for approvalは作業フォルダ内で動き範囲を越えるときに確認する、Approve for meは自動で判定する、Full accessはどのファイルも承認なしで編集できる" loading="lazy"><figcaption>3つの権限モードと、それぞれの境目</figcaption></figure>

自分のマシンで動かす以上、右へ寄せるほど事故の代償が大きくなります。試す段階では既定のまま触らないのが無難です。

仕組みとしては2つの制御が組み合わさっています。サンドボックスが触れるファイルとネットワークの範囲を決め、承認の設定がどこで止まるかを決めます。**Approve for meを選んでも、触れる範囲そのものは広がりません**。範囲を越える要求を人が見るか自動で見るかが変わるだけです。

デスクトップアプリではApprove for me（設定の表記はAuto-review）とFull accessは初期状態ではメニューに出ません。設定のGeneralから有効にして初めて選べるようになります。Full accessについては、データの消失や流出、想定外の動作の危険が大きく上がると公式が明記しています。

## モデルはSolとLunaから選ぶ

Work とCodexで使うモデルは、通常のChatGPTのチャットとは別系統です。**GPT-6 SolとGPT-6 Lunaは、WorkとCodexでのみ使えます**。複雑なコーディングやエージェント的な作業にはSol、決まった形の反復作業にはLunaを公式が勧めています。

CLIでは`/model`で切り替えるか、起動時に指定します。

```
codex --model gpt-6-sol
codex exec -m gpt-6-sol "Review the current changes"
```

推論の深さはLow・Medium・High・Extra high・Max・Ultraの6段階です。既定はMediumで、Ultraはサブエージェントに作業を分けて走らせる段階です。深くするほど結果が良くなる可能性はありますが、時間もトークンも増えます。

デスクトップアプリとウェブでは、入力欄の下のコントロールでモデルと推論の深さを選びます。CLIにスライダーはありません。Codexは手動で選んだモデルを保持します。

## 10月14日にGPT-5.5が引退する

**2026年10月14日に、GPT-5.5がChatGPTとChatGPT WorkとCodexの全プランから引退します**。OpenAI APIは対象外です。

<figure class="post-figure"><img src="/media/images/codex-guide/cx_03_models.jpg" alt="Codex公式ドキュメントのModelsページ。2026年10月14日にGPT-5.5がChatGPTとChatGPT WorkとCodexから引退すること、代わりにgpt-6-solまたはgpt-6-lunaを選ぶことが書かれている" loading="lazy"><figcaption>公式ドキュメントに出ているGPT-5.5の引退の告知</figcaption></figure>

手を動かす必要があるのは、設定ファイルや自動化にモデル名を書き込んでいる場合です。

置き換え先はPlus・Pro・Business・Enterprise・Eduなら`gpt-6-sol`、無料とGoならデスクトップアプリの`gpt-6-luna`です。公式が確認を求めているのは、ワークスペースの既定値、保存したモデル設定、管理された構成、カスタムのエージェント、スケジュールしたタスク、モデルを指定しているスクリプトです。CIに組み込んでいる場合は、そこに`gpt-5.5`が残っていないかを見ます。

なお、Astraを使うにはCodex CLIのバージョン0.153.0以降が必要です。GPT-5.6をCodexで使う場合の最低バージョンは、デスクトップアプリのCodexモードが26.707.30751、Codex CLIが0.144.0と公式に書かれています。

## クラウドで並行して走らせる

手元のマシンを占有したくない作業は、クラウド側に投げられます。隔離した環境が割り当てられ、複数の作業を並行して進められる形です。

設定はCodexにサインインして、GitHubかGitLabをつなぐところから始めます。GitHubではCodexが触れるリポジトリを選び、GitLabは環境を作るときにプロジェクトを選ぶ形です。GitHub・GitLab・Linear・Slackから作業を開始することもできます。

終わったら、要約と差分を確認して、追加の依頼を出すか、そのままプルリクエストを開きます。リポジトリごとに必要な依存関係やツール、環境変数、セットアップの手順を環境として定義できます。

## AI検索での見え方は別の話

開発にCodexを使うことと、自社のサービスがAIの回答に出てくるかどうかは別の問題です。後者はAIが参照できる形で情報が置かれているかで決まります。仕組みと対策は[AI検索対策は何から始めるかの記事](https://nito-0210.com/media/ai-search-first-steps/)にまとめています。

## よくある質問

回答の内容はすべて2026年9月23日時点の公式ドキュメントとヘルプセンターの記載です。

**Codexは無料で使えますか？**

無料プランでも使えますが、入口はデスクトップアプリに限られ、モデルはGPT-6 Lunaの標準速度です。ターミナルのCLI、IDE拡張、クラウドはPlus以上が対象になります。

**Codex CLIはどうやってインストールしますか？**

macOSとLinuxでは`curl -fsSL https://chatgpt.com/codex/install.sh | sh`を実行します。npmとHomebrew、Windows向けの手順も公式にあります。更新も同じコマンドです。

**Codexで使えるモデルはどれですか？**

GPT-6 SolとGPT-6 Lunaです。この2つは通常のチャットでは選べず、ChatGPT WorkとCodexの中だけで使えます。GPT-6 Astraを使う場合はCodex CLIの0.153.0以降が必要です。

**GPT-5.5はいつまで使えますか？**

2026年10月14日にChatGPTとChatGPT WorkとCodexから引退します。OpenAI APIは対象外です。設定やスクリプトにモデル名を書いている場合は、その前に入れ替えます。

**Codexはどこまで勝手に実行しますか？**

選んだ権限モードによります。既定のAsk for approvalでは作業中のフォルダの中で動き、インターネットに出るときと範囲の外に出るときに確認を取ります。Full accessではどのファイルも承認なしで編集できます。

**Codex CLIとIDE拡張はどちらがいいですか？**

作業の形で選びます。CLIはターミナルの中で完結させたい場合や、`codex exec`でCIや繰り返しの処理に組み込む場合に向きます。IDE拡張は開いているファイルと選択範囲をそのまま渡し、差分をその場で確認したい場合に向きます。

**APIキーで使うと何が変わりますか？**

CLIとSDKとIDE拡張は使えますが、GitHubの自動コードレビューやSlack連携といったクラウド側の機能は付きません。料金はAPIの従量課金で、使えるモデルはそのキーで利用できるものに従います。

**ChatGPT WorkとCodexはどう違いますか？**

Workは調査や分析、文書や表計算や資料の作成を担当し、Codexはソフトウェア開発と技術的な作業を担当します。利用量と請求の仕組みは共通で、デスクトップアプリでは左上のメニューで切り替えます。

## 出典

出典はOpenAIの公式ページで、取得日は2026年9月23日です。

- [Codex Quickstart（公式）](https://developers.openai.com/codex/quickstart) — デスクトップアプリとウェブの始め方、ChatGPTとCodexの切り替え
- [Codex Pricing（公式）](https://developers.openai.com/codex/pricing) — プラン別の金額と使える入口、APIキーで使う場合の違い
- [Codex Models（公式）](https://developers.openai.com/codex/models) — GPT-5.5の引退日と置き換え先、推論の深さ、モデルの選び方
- [Codex CLI（公式）](https://developers.openai.com/codex/cli) — インストールとサインイン、起動直後のコマンド
- [Codex IDE extension（公式）](https://developers.openai.com/codex/ide) — エディタ内での使い方
- [Codex cloud（公式）](https://developers.openai.com/codex/cloud) — クラウド環境の設定、GitHubとGitLabの接続
- [Permissions（公式）](https://developers.openai.com/codex/permission-modes) — 3つの権限モード、サンドボックスと承認の関係
- [ChatGPT Work and Codex（公式ヘルプ）](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) — 3つの体験の使い分け、モデルの提供範囲、Astraの必要バージョン
