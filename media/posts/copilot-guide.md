---
title: 【2026年9月】Copilotの使い方を解説｜3つのライセンスとWork IQの違い
date: 2026-09-23
category: AI検索対策
description: Microsoft Copilotは同じ名前でもライセンスで中身が変わります。Copilot Chatとアドオンの違い、Wordなどアプリ内の機能、Work IQをオンにしたときの応答の差を公式ドキュメントで整理します。
cover_tag: 使い方
cover_headline: Copilotの使い方
cover_sub: 3つのライセンスとWork IQの違い
---

Copilotの使い方でつまずく理由の多くは、操作ではなく**自分が使っているCopilotがどれなのか分からない**ところにあります。会社で配られたCopilotと、隣の部署が使っているCopilotと、個人のアカウントで開いたCopilotは、名前が同じでも見に行けるデータが違います。

ここではMicrosoftの[公式ドキュメント](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-overview)と[サポートページ](https://support.microsoft.com/ja-jp/copilot)（2026年9月23日取得）から、3つのライセンスの違い、アプリごとにできること、社内のデータを踏まえた回答が返る条件を整理します。

:::takeaways
- ライセンスは**Copilot Chat（基本）・Microsoft 365 Copilot（基本）・Microsoft 365 Copilot（プレミアム）**の3段
- **Copilot Chat（基本）ではWord・Excel・PowerPoint・OneNoteのCopilotは使えない**
- アドオンなしの標準アクセスは**混み具合の影響を受け、1日の中でも変わる**
- 社内のメールやファイルを踏まえた回答が返るのはプレミアムで、**Work IQをオンにしたとき**
- エージェントは階層によって従量課金。個人アカウントと職場アカウントでは入口そのものが別
:::

## 自分のCopilotがどれかを先に確かめる

3つのライセンスで変わるのは、答えを作るときに何を見に行けるかです。

<figure class="post-figure"><img src="/media/images/copilot-guide/cp_03_fig_tiers.png" alt="Copilotの3つのライセンスの比較図。Copilot Chat基本はWebのデータ中心、Microsoft 365 Copilot基本はアプリ内の標準アクセス、プレミアムは優先アクセスと組織データの根拠付けが付く" loading="lazy"><figcaption>3つのライセンスで変わるもの</figcaption></figure>

どれを使っているかが分かると、できないことの理由もはっきりします。

共通しているのは土台のほうです。どの階層も、大規模言語モデルによる自然言語の理解と生成、Webや組織データによる根拠付け、そして**利用者のアクセス許可の範囲に限定されたアクセス**という3つで支えられていると公式ドキュメントに書かれています。権限のないファイルが回答に混ざることはありません。

モデルについての注記もあります。Anthropicのサブプロセッサは該当するMicrosoft 365ライセンスのエクスペリエンスでのみ使え、既定で全員が使えるわけではありません。

<figure class="post-figure"><img src="/media/images/copilot-guide/cp_01_overview.jpg" alt="Microsoft Learnの日本語ドキュメント。Copilot ChatとMicrosoft Copilotは、データの根拠付け、統合の深さ、ライセンスが異なると書かれている" loading="lazy"><figcaption>公式ドキュメントの冒頭にある説明</figcaption></figure>

導入の相談で食い違いが起きるのは、たいていこの前提の共有漏れです。

## Copilot Chatでできること

Copilot Chat（基本）は、対象のMicrosoft 365ライセンスに含まれるベースラインです。主にWebのデータを使い、組織のコンテンツの利用を制限したチャットになります。

入口は複数あります。

- m365copilot.com
- Microsoft Edgeの右上のCopilotアイコン
- OutlookとTeamsの中のCopilot Chat
- bing.com/chat と bing.com/copilotsearch
- copilot.com と copilot.ai

社内のコンテンツを使わせたい場合は、こちらから渡します。プロンプトを書くときに内容を貼り付ける、ファイルをアップロードする、ファイルを選択する、のいずれかです。TeamsやOutlookでは、対象を開いた状態でCopilot Chatを使うと、開いている内容を認識するので貼り付けは要りません。

Copilot Chatには、指示と一般公開されているWebサイトに基づいた宣言型エージェントが含まれます。それ以外のカスタムのエージェントを使う場合は従量課金です。

## アプリの中で使えるもの

Microsoft 365 Copilot（基本）は、アドオンのライセンスは無いがアプリ内のCopilot機能に標準アクセスできる状態を指します。Word、Excel、PowerPoint、OneNoteのCopilotが使えるのはこの段からです。

| アプリ | できること |
|---|---|
| Word | 文書の下書き、書き換え、要約 |
| Excel | データの分析、分析情報の生成、数式とビジュアルの作成 |
| PowerPoint | プロンプトや既存の内容からの作成、要約、編集 |
| Outlook | メールの下書き、スレッドの要約、明確さや語調の助言 |
| OneNote | 下書きの計画、アイデア、リストの作成 |
| Teams | 会議の要約と文字起こし、アクションアイテムの記録 |
| Forms | アンケートや投票の質問の下書き |

Teamsの会議の要約には期間の条件が付いていて、公式の説明では最大30日間です。

標準アクセスで注意したいのは安定性のほうです。公式ドキュメントは標準アクセスが**サービス容量の影響を受け、1日を通して変わる**ことがあると明記しています。混雑する時間に使えなかった経験があるなら、設定ではなくライセンスの問題かもしれません。

プレミアムのアドオンを足すと、ここに優先アクセスが付き、ピーク時でも応答が安定します。

## Work IQをオンにすると何が変わるか

社内のデータを踏まえた回答が返るのは、プレミアムの階層です。根拠付けに使われるのはMicrosoft Graph、Work IQ、Copilot検索、セマンティックインデックスの4つになります。

Microsoft Graphが持ち込むのは、メール、ファイル、会議、予定表、チーム、組織の関係といった文脈です。Work IQはその上で、エージェントが組織のデータやコンテンツやツールについて推論できるようにする層になります。

<figure class="post-figure"><img src="/media/images/copilot-guide/cp_04_fig_workiq.png" alt="Work IQのオンとオフの比較図。オフでは会議準備の一般論しか返らないのに対し、オンでは予定表やメールやファイルから出席者と前回の決定を拾って答える" loading="lazy"><figcaption>Work IQのオンとオフで変わる答え</figcaption></figure>

この差は、依頼の文面を工夫しても埋まりません。

**Work IQはオンとオフを切り替えられます**。オフにすると、回答はMicrosoft GraphとWork IQに基づかなくなります。答えは返ってきますが、仕事固有の文脈は乗りません。思ったより一般論しか返ってこないときに、まず見るべき設定です。

なお、Work IQ APIは別物です。カスタムのアプリやエージェントや統合のために、独立して購入して使う従量課金のサービスと位置づけられています。

## エージェントと従量課金の線

エージェントはCopilotを特定の用途に絞った形で、業務プロセスの自動化まで担当します。サポートページにはリサーチツールのエージェントや、Word・Excel・PowerPointのエージェントの案内が並びます。

<figure class="post-figure"><img src="/media/images/copilot-guide/cp_02_support.jpg" alt="Microsoft Copilotの日本語サポートページ。作業の開始、チャット、Agentsの3つのカードが並び、Agentsにはリサーチツールエージェントの案内がある" loading="lazy"><figcaption>公式サポートの入口</figcaption></figure>

課金の線は、使うデータの種類で引かれています。

Copilot Chat（基本）とMicrosoft 365 Copilot（基本）では、Webのデータを使うエージェントにアクセスでき、**作業データを使うエージェントは従量課金**です。プレミアムではWebと作業データの両方を使うエージェントへのアクセスが含まれます。

プレミアムにはMicrosoft Copilot Coworkも付きますが、こちらも使用量ベースの課金です。Coworkは利用者に代わってMicrosoft 365の環境全体でタスクを実行します。

## 個人と職場で入口が違う

同じCopilotという名前でも、サインインしているアカウントの種類で入口が分かれます。

職場や学校のアカウントでCopilot Chatを使う場合は、Microsoft Entraのアカウントでサインインしたうえで、Microsoft Copilotアプリ、copilot.cloud.microsoft、EdgeのCopilot Chat、または各アプリから入ります。

個人用アカウントの入口はMicrosoft Copilotアプリ（Web・デスクトップ・モバイル）、copilot.microsoft.com、bing.com/chat、bing.com/copilotsearch、copilot.com、copilot.aiです。

**同じブラウザで両方を使っていると、いま社内データを見られる側にいるのかどうかが分からなくなります**。管理者側では個人用アカウントでMicrosoft 365アプリにサインインできるかどうかを制御できます。

## 管理側で先に整えるもの

回答の質はテナント側の整理にも左右されます。公式ドキュメントが挙げているのは次の3つです。

1. SharePoint 高度な管理。過剰な共有を減らし、使われていないサイトを片付けることで、Copilotが見に行く先を整える
2. 制限付きコンテンツ検出。レビュー中のSharePointサイトの内容を、検索結果やCopilotの回答に出さないようにする
3. Microsoft Purview。機微度でデータを分類してラベルを付け、不正な共有や漏洩を防ぎ、プロンプトと応答を確認する

導入後の定着を見るなら、使用状況レポートで利用の様子を追い、組織のメッセージ機能で日常の業務の流れの中に案内を出す、という手順が案内されています。

## AI検索での見え方は別の話

社内でCopilotを使いこなすことと、自社の情報がAIの回答に出てくるかどうかは別の問題です。後者はAIがたどれる形で情報が置かれているかで決まります。考え方は[AI検索対策は何から始めるかの記事](https://nito-0210.com/media/ai-search-first-steps/)にまとめています。

## よくある質問

回答の内容はすべて2026年9月23日時点のMicrosoftの公式ドキュメントとサポートページの記載です。

**Copilotは無料で使えますか？**

対象のMicrosoft 365ライセンスがあれば、Copilot Chat（基本）が含まれます。個人用アカウントでもcopilot.microsoft.comなどから使えます。ただしWordやExcelの中のCopilotは、これらには含まれません。

**WordやExcelでCopilotが出てきません**

Copilot Chat（基本）だけの状態では、Word・Excel・PowerPoint・OneNoteのCopilotにはアクセスできません。アプリ内で使うには標準アクセスがある状態かアドオンのライセンスが必要です。

**Copilotが社内のファイルを見てくれません**

組織データの根拠付けが付くのはMicrosoft 365 Copilot（プレミアム）です。そのうえでWork IQがオフになっていると、回答はMicrosoft GraphとWork IQに基づかなくなります。Copilot Chatの場合は、ファイルを貼るかアップロードして渡します。

**Work IQとは何ですか？**

エージェントが組織のデータやコンテンツやツールについて推論できるようにする層です。オンにすると、メール、ファイル、会議、予定表、チーム、組織の関係を踏まえた回答になります。

**Copilotは自分に権限のない資料まで見ますか？**

見ません。どの階層も、利用者のアクセス許可の範囲に限定されたアクセスで動くと公式ドキュメントに書かれています。

**時間帯によって使えたり使えなかったりします**

アドオンなしの標準アクセスは、サービス容量の影響を受けて1日を通して変わることがあると公式が明記しています。混雑時の安定性が要るなら、優先アクセスの付くプレミアムが選択肢になります。

**エージェントは追加料金がかかりますか？**

使うデータによります。基本の階層では作業データを使うエージェントが従量課金です。プレミアムではWebと作業データの両方を使うエージェントが含まれます。Microsoft Copilot Coworkは使用量ベースの課金です。

**Teamsの会議の要約はいつまで見られますか？**

公式の説明では、会議の要約は最大30日間です。長く残したい内容は会議のあとに別の場所へ書き出しておきます。

## 出典

出典はMicrosoftの公式ページで、取得日は2026年9月23日です。

- [Microsoft Copilot の概要（Microsoft Learn）](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/microsoft-365-copilot-overview) — 3つのライセンスの違い、アプリ内の機能、Work IQの挙動、エージェントの課金、管理側の設定
- [Microsoft Copilot のヘルプとラーニング（Microsoft サポート）](https://support.microsoft.com/ja-jp/copilot) — 入口の案内、エージェントとリサーチツール、プロンプトの書き方
