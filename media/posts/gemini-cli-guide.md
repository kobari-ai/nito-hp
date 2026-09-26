---
title: 【2026年9月】Gemini CLIはAntigravity CLIへ｜使えない理由と今の選択肢
date: 2026-09-22
category: AI検索対策
description: Gemini CLIは2026年6月18日に無料枠とAI Pro・Ultraへの提供を終えてAntigravity CLIに移りました。止まった対象、いまもGemini CLIを使える条件、移行先の中身を公式の発表から整理します。
cover_tag: 解説
cover_headline: Gemini CLIの今
cover_sub: Antigravity CLIへの移行と、使い続けられる条件
---

Gemini CLIの解説記事どおりに`gemini`を入れてGoogleアカウントでログインしても、無料では動きません。**2026年6月18日に、無料枠とGoogle AI Pro・Ultraに対する提供が終わっている**ためです。移行先はAntigravity CLIになります。

一方で、Gemini CLIそのものが消えたわけではありません。ここではGoogleの[発表](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli)と[公式ドキュメント](https://www.geminicli.com/docs/get-started/authentication)（2026年9月22日取得）から、誰が止まって誰が続くのか、いま何を選べばいいのかを整理します。

:::takeaways
- **2026年6月18日**に、Gemini CLIとGemini Code AssistのIDE拡張が、無料利用とGoogle AI Pro・Ultraへのリクエスト提供を停止
- 移行先は**Antigravity CLI**。Go言語で書き直され、複数のエージェントを背後で並行して動かせる
- **Gemini Code AssistのStandard・Enterpriseライセンスと、有料のAPIキーは対象外**。Gemini CLIをそのまま使える
- Agent Skills・Hooks・Subagents・Extensionsは引き継がれたが、公式は**すべての機能がそのまま揃うわけではない**と書いている
- GitHubのREADMEには今も旧来の無料枠（毎分60・1日1,000リクエスト）が載っている
:::

## 何が起きたのか

Googleは2026年5月19日に、Gemini CLIをAntigravity CLIへ移す方針を発表しました。理由として挙げられているのは、複数のエージェントが連携して作業を分担する使い方が増え、ターミナルのツールもワークフロー全体と同じ土台を共有する必要が出てきたことです。

<figure class="post-figure"><img src="/media/images/gemini-cli-guide/gc_01_banner.jpg" alt="Gemini CLI公式ドキュメントの認証ページ。上部に、無料枠とGoogle Oneのユーザー向けのGemini CLIは2026年6月18日にAntigravity CLIに置き換わったという告知が表示されている" loading="lazy"><figcaption>公式ドキュメントの上部に出ている告知</figcaption></figure>

個人の利用者に関する日付は、発表の中で明確に区切られています。

<figure class="post-figure"><img src="/media/images/gemini-cli-guide/gc_02_blog.jpg" alt="Google Developers Blogの記事。Important timeline for Consumersの節で、2026年6月18日にGemini CLIとGemini Code AssistのIDE拡張がGoogle AI ProとUltra、およびGemini Code Assist for individualsのリクエスト提供を停止すると書かれている" loading="lazy"><figcaption>発表に書かれた個人向けの日程</figcaption></figure>

Gemini Code Assist for GitHubにも同じ変更が及びます。6月18日以降はGitHubの組織への新規インストールができなくなり、その後の数週間でリクエストの処理も止まると書かれています。

## 自分は止まる側なのか

<figure class="post-figure"><img src="/media/images/gemini-cli-guide/00_fig_who.png" alt="2026年6月18日に提供が止まった対象と引き続き使える対象の図。止まったのはGemini Code Assist for individualsの無料利用、Google AI ProとUltraの個人サブスクリプション、Gemini Code Assist for GitHub。続くのはCode AssistのStandardとEnterpriseライセンス、Google Cloud経由のGitHub連携、有料のAPIキー" loading="lazy"><figcaption>対象は契約しているライセンスで分かれる</figcaption></figure>

分かれ目はアカウントの種類ではなく、**どの契約でリクエストを通しているか**です。個人で無料で使っていた場合と、Google AI ProやUltraのサブスクリプションで使っていた場合が、提供の止まった側にあたります。

会社のGemini Code AssistのStandardまたはEnterpriseライセンスを使っている場合、発表には「アクセスは変わらない」と書かれています。最新のGeminiモデルの提供も従来どおりです。Google Cloud経由でGemini Code Assist for GitHubを使っている組織も同じ扱いで、変わりません。有料のGeminiおよびGemini Enterprise Agent PlatformのAPIキー経由でも、Gemini CLIは引き続き使えます。

## 移行先のAntigravity CLIはどう違うのか

<figure class="post-figure"><img src="/media/images/gemini-cli-guide/01_fig_move.png" alt="Antigravity CLIに引き継がれた機能と新しくなった点の図。Agent Skills、Hooks、Subagents、ExtensionsはAntigravityのプラグインとして残り、Goで書き直されて動きが速く、複数のエージェントを背後で並行して動かせて、デスクトップのAntigravity 2.0と同じ土台を共有する" loading="lazy"><figcaption>残ったものと作り直されたところ</figcaption></figure>

Antigravity CLIは2026年5月19日から誰でも使えます。Goで書かれていて動作が速く、大規模なリファクタリングや複数テーマの調査をターミナルを占有せずに走らせられます。デスクトップアプリのAntigravity 2.0と同じエージェントの土台を共有しているので、土台側の改善は自動的に両方へ届く形です。

ただし公式は、すべての機能が最初から揃うわけではないと断っています。調べもの、プロジェクトの立ち上げ、クラウド環境の構築といった用途は移せる、という書き方です。使っていた機能が個別に残っているかどうかは、移す前にドキュメントで確認してください。

## 公式のREADMEがまだ古い

<figure class="post-figure"><img src="/media/images/gemini-cli-guide/gc_03_readme.jpg" alt="GitHubのgoogle-gemini/gemini-cliリポジトリのREADME。Why Gemini CLI?の節に、個人のGoogleアカウントで毎分60リクエスト、1日1,000リクエストの無料枠という記載が残っている" loading="lazy"><figcaption>リポジトリのREADMEに残る旧来の無料枠の記載</figcaption></figure>

混乱のもとがここにあります。認証の選択肢の1番目も、Googleアカウントでのサインインのままです。

2025年に書かれた解説は、この記載を前提にしています。手順どおりに進めても無料では通らないのは、記事が間違っていたからではなく、その後に前提が変わったためです。判断の基準にするなら、READMEではなく[公式ドキュメント](https://www.geminicli.com/docs/get-started/authentication)と発表のほうを見てください。

## 開発自体は止まっていない

Gemini CLIのリポジトリは動き続けています。安定版は毎週火曜のUTC 20:00（日本時間の水曜5:00）、プレビュー版は毎週火曜のUTC 23:59（同じく水曜8:59）、ナイトリー版は毎日UTC 0:00（日本時間の9:00）に公開される形です。直近のリリースはv0.60.0で、2026年9月15日に出ています。

企業のライセンスとAPIキーの利用が続く以上、当面はこのまま更新されると読めます。対象外の契約で使っているなら、置き換えを急ぐ理由はありません。

## いま取れる3つの道

<figure class="post-figure"><img src="/media/images/gemini-cli-guide/02_fig_choice.png" alt="ターミナルでGeminiを使う3つの選択肢の図。無料枠やAI Pro・Ultraで使っていた個人はAntigravity CLI、有料のAPIキーを持つ人はGemini CLIに従量課金、Code AssistのStandardやEnterpriseライセンスを持つ組織はGemini CLIをそのまま" loading="lazy"><figcaption>契約の形で選ぶ道が決まる</figcaption></figure>

どれになるかは契約の形で決まるので、選ぶ余地はあまりありません。迷うとすればこの一点です。これまで無料で使っていた人が、Antigravity CLIへ移るか、APIキーを取って従量課金でGemini CLIを続けるか。手元の設定やスクリプトを作り込んでいるなら後者、そうでなければ前者が軽く済みます。

Google Cloudのプロジェクトを指定する必要がある場合は、`GOOGLE_CLOUD_PROJECT`に自分のプロジェクトIDを入れてから起動します。

## AI検索での見え方は別の話

AI検索に古い答えが残り続ける例としても、この移行は分かりやすいものです。2025年に書かれた解説が大量にあり、検索でもAIの回答でも上位に出続けている状態です。自社の情報が同じ形で古いまま引用されていないかは、順位とは別に確かめる必要があります。実際に4つのサービスへ同じ質問を投げた結果は[AI検索エンジンの比較記事](https://nito-0210.com/media/ai-search-engine-comparison/)に載せました。

## よくある質問

内容はすべて2026年9月22日時点の公式の発表とドキュメントの記載です。

### Gemini CLIが使えなくなったのはなぜですか？

2026年6月18日に、無料のGemini Code Assist for individualsと、Google AI Pro・Ultraのサブスクリプションに対するリクエストの提供が終わったためです。移行先としてAntigravity CLIが案内されています。

### Gemini CLIは無料で使えますか？

Gemini CLIの側に無料で使う道は案内されていません。無料で使いたい場合の移行先はAntigravity CLIです。

### Gemini CLIはもう使えないのですか？

契約によります。Gemini Code AssistのStandardまたはEnterpriseライセンス、Google Cloud経由のGemini Code Assist for GitHub、有料のGeminiおよびGemini Enterprise Agent PlatformのAPIキーであれば、そのまま使えます。

### Antigravity CLIとは何ですか？

Google Antigravityというエージェント中心の開発プラットフォームに含まれる、新しいターミナル向けのツールです。Goで書かれていて、複数のエージェントを背後で動かす非同期の作業に対応しています。デスクトップアプリのAntigravity 2.0と同じ土台を共有します。

### 以前の機能はAntigravity CLIに残りますか？

Agent Skills、Hooks、Subagents、Extensionsは引き継がれました。Extensionsの扱いはAntigravityのプラグインという形になります。すべての機能がそのまま揃うわけではないと公式が書いているため、個別の機能はドキュメントで確認してください。

### 1日1,000リクエストの無料枠は使えますか？

2026年9月22日の時点でREADMEに記載は残っていますが、公式ドキュメントの告知と発表の内容が優先されます。無料枠での提供は6月18日に終わっています。

### Gemini CLIの開発は終わったのですか？

続いています。安定版が毎週火曜、ナイトリー版が毎日公開される体制で、直近のリリースは2026年9月15日のv0.60.0です。

### GitHubでの自動レビューはどうなりますか？

Gemini Code Assist for GitHubは、2026年6月18日からGitHubの組織への新規インストールができなくなり、その後数週間でリクエストの処理も止まると発表されています。Google Cloud経由で使っている組織は対象外です。

## 出典

出典は公式のページで、取得日は2026年9月22日です。

- [An important update: Transitioning Gemini CLI to Antigravity CLI（Google Developers Blog、2026年5月19日）](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli) — 移行の理由、消費者向けの日程、企業向けの扱い、引き継がれる機能
- [Gemini CLI authentication setup（公式ドキュメント）](https://www.geminicli.com/docs/get-started/authentication) — 告知のバナー、認証方法の選び方、Google Cloudプロジェクトの指定
- [google-gemini/gemini-cli（GitHub）](https://github.com/google-gemini/gemini-cli) — READMEの記載、リリースチャンネルの公開時刻、v0.60.0
