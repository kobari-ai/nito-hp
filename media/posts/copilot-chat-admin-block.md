---
title: 【2026年10月】Copilot Chatを社内で止める方法｜ブロック・Web検索・エージェント
date: 2026-10-17
category: AI活用
description: 無料のCopilot Chatを管理者が止める・絞る方法を公式ドキュメントから解説。ピン留めを外すだけでは止まらない理由、統合アプリでのブロック、Web検索やエージェントだけ止める設定、私用アカウントへの抜け道まで。
cover_tag: 管理者向け
cover_headline: Copilot Chatを社内で止める
cover_sub: ブロック・ピン留め・Web検索・エージェント
---

Microsoft 365 Business StandardやE3などの対象プランを契約している会社では、職場のアカウント（Microsoft Entra ID）でサインインした社員が、追加料金なしでCopilot Chatを使えます。TeamsとOutlookのナビゲーションには既定でピン留めされているため、導入を決める前から社員の画面に出ていることがあります。名前は2026年に「Microsoft 365 Copilot Chat」から「Microsoft Copilot Chat」に変わりました。

社内のルールが決まるまで止めたい、一部の部署だけ使わせたい、Web検索だけ切りたい、という相談は管理者に集まります。Microsoft Learnの「[Microsoft Copilot Chatの管理](https://learn.microsoft.com/ja-jp/copilot/manage)」（2026年10月12日更新）は、アクセスを絞る方法としてピン留めを外す・特定のユーザーやグループに限る・ブロックする、の3つを挙げています。この記事は2026年10月17日に取得したMicrosoft LearnとMicrosoftの日本のサポートブログをもとに、どの設定で何が止まるかを整理したものです。管理センターの操作はこちらでは試していないので、手順と画面の動きは公式の説明に沿って書いています。

:::takeaways
- **ピン留めを外しても、Copilot Chatは使えるまま**。Copilotアプリやブラウザからたどり着ける
- **使えなくするのは統合アプリでのブロック**。有料のCopilotライセンスを持つ人も止まる
- 一部の人だけ使わせるなら、統合アプリの［ユーザー］タブで**特定のユーザーやグループ**を選ぶ
- **Web検索だけ**は「Copilot での Web 検索を許可」ポリシーで切れる。オプションの接続エクスペリエンスを切ると他の機能まで止まる
- 社内データを読むエージェントは**従量課金で既定オフ**。課金の設定をしなければ費用は出ない
:::

<!-- SHOT: 01_fig_scope 概要図（HTML図）。止まる範囲を3段で: 見えなくする（ピン留めを外す）／一部だけ止める（特定のユーザー・Web検索・エージェント）／使えなくする（統合アプリでブロック）。PC 幅800・DPR2、文字は5か所まで -->

## 止めたい範囲を先に決める

よく混ざるのが、画面から消したいのか、使えなくしたいのか、という2つの目的です。Copilot Chatの入口はCopilotアプリ（Web・デスクトップ・モバイル）、Edge、Outlook、Teams、WordやExcelのエージェントと複数あり、**どこか1つを閉じても別の入口から開ける**ように作られています。そのため、設定は止めたい範囲から選びます。

| やりたいこと | 使う設定 | 止まる範囲 |
|---|---|---|
| TeamsとOutlookから見えなくする | Copilot＞設定のピン留め | ナビゲーションの表示だけ |
| 全員が使えないようにする | 統合アプリでCopilotをブロック | Copilotアプリ・Outlook・Teams・Web版のChat |
| 一部の人だけに使わせる | 統合アプリの［ユーザー］タブ | 選ばなかった人（ライセンスなし） |
| Web検索だけ止める | Copilot での Web 検索を許可 | Bingへの検索クエリ |
| 有料のエージェントを止める | 従量課金を設定しない・エージェントのブロック | 社内データを読むエージェント |
| Edgeのボタンを消す | Microsoft365CopilotChatIconEnabled | Edgeのツールバーの表示 |

迷ったら、**表示を消す設定と利用を止める設定を分けて考える**と整理しやすくなります。前者はピン留めとEdgeのボタン、後者は統合アプリでのブロックと各機能のポリシーです。

## ピン留めを外しても使える

TeamsのアイコンからCopilotが消えれば止まった、と考えたくなります。しかしLearnの管理のページは、ピン留めを外してもCopilot Chatへのアクセスは削除されず、Copilotアプリなどから引き続き使える可能性がある、と注意書きを置いています。**ピン留めは表示の設定で、利用の可否は決めません。**

<!-- SHOT: 02_pin_options Learn「Microsoft 365 アプリでMicrosoft Copilot Chatをピン留めする」の「ピン留めオプション」の節（https://learn.microsoft.com/ja-jp/microsoft-365/copilot/pin-copilot-chat-navbar#pinning-options）。PC幅。赤枠1: 2つの選択肢の箇条書き、赤枠2: 「最大 48 時間」の文 -->

### ピン留めの設定の場所

設定にはAI 管理者のロールが要ります。[Microsoft 365 管理センター](https://admin.microsoft.com/)にサインインし、［Copilot］＞［設定］から［Microsoft Copilot Chatをピン留めする］を開くと、ピン留めする（推奨・既定）と、ピン留めしない、の2つから選べます。変更が有効になるまで最大48時間かかる場合がある、とLearnに書かれているので、翌日にまだ出ていても慌てなくて大丈夫です。

### 2026年1月からCopilotアプリには効かない

Microsoft Copilotアプリ（旧Microsoft 365 Copilotアプリ）のナビゲーションには、ピン留めの設定が効かなくなりました。Learnによると、欧州経済領域とスイスのテナントは2025年7月25日から、それ以外のテナントは2026年1月28日からです。**ピン留めしない設定にしても、Copilotアプリを開けばChatは並んでいます。**

ピン留めしない設定でも、利用者はTeamsやOutlookのアプリストアからCopilotを自分で追加できます。Windowsの管理のページには、ピン留めせず利用者にも確認しない設定にした場合でも、IT 管理者がブロックしていなければ m365.cloud.microsoft/chat から使える、とあります。ピン留めを外す手は社員を急に戸惑わせずに入口を目立たなくしたいとき向けで、利用を止める手ではありません。

## 統合アプリでCopilotをブロックする

社員がCopilot Chatを使えない状態にしたいときは、ブロックを使います。Learnの管理のページには、すべてのユーザー、または特定のユーザーとグループのCopilot Chatへのアクセスをブロックでき、そこには有料のMicrosoft Copilotライセンスを持つ人も含まれる、と書かれています。

<!-- SHOT: 03_learn_block Learn「Microsoft Copilot Chatの管理」の「Microsoft Copilot Chatへのアクセスを制限する」の節（https://learn.microsoft.com/ja-jp/copilot/manage）。PC幅。赤枠1: 3つの箇条書き（ピン留め・ユーザーまたはグループ・ブロック）、赤枠2: 「Copilot Chat へのアクセスをブロックする」の本文 -->

### ブロックの手順

Learnの管理のページは、ブロックできることと利用者の画面は説明していますが、ブロックの設定画面の手順は載せていません（2026年10月17日に確認）。手順はMicrosoftの日本のサポートチームのブログ「[Microsoft 365 Copilot Chat のピン留めの制御方法](https://jpmessaging.github.io/blog/Outlook-microsoft365-copilot-chat-pin-admin-control/)」（2025年12月23日）に載っています。

1. Microsoft 365 管理センターで［設定］＞［統合アプリ］を開く
2. ［利用可能なアプリ］で［Copilot］を選ぶ
3. ［アプリをブロックする］を選ぶ

表記が見つからないときは、統合アプリの一覧で「Copilot」を検索してください。

### ライセンスを持つ人も止まる

統合アプリの3つの設定でCopilotライセンスの有無によって動きが変わることも、同じブログが表で示しています。違いが出るのは**［組織のユーザーはインストールできません］を選んだとき**で、ライセンスを持つ人のCopilot Chatは使えるままです。

| 統合アプリの設定 | ライセンスなしの人 | ライセンスありの人 |
|---|---|---|
| 展開対象から外す | 使えない・追加もできない | 使える |
| 組織のユーザーはインストールできません | 使えない・追加もできない | 使える |
| アプリをブロックする | 使えない | 使えない |

<!-- SHOT: 04_fig_block_matrix 比較図（HTML図）。上の表と同じ3行×2列で使える=緑・使えない=灰に塗る。PC 幅800・DPR2、図の中に見出しを入れるならキャプションは付けない -->

有料のCopilotを入れた部署は残し、それ以外を止めたいなら、［組織のユーザーはインストールできません］のほうが合います。全員を止めるならブロックです。ブロックしたあとのアイコンの見え方はOutlookの種類によってそろわない場合がある、とブログは書いています。

### ブロックされた社員の画面

ブロックされた社員がCopilotアプリでChatを選ぶと、組織のポリシーでアクセスが無効になっている、という説明が出ます。ナビゲーションからChatの項目がすぐ消えるとは限らないため、社員から壊れているのでは、と問い合わせが来るかもしれません。

その画面には社内のルールのページへのリンクを出せます。Learnの手順では管理センターの［Copilot］＞［設定］で［すべて表示］を選び、［ブロックされた Microsoft Copilot アプリのカスタム リンク］に社内のページのURLを入れます。**社員の画面に出るのは「View info from your organization」というリンクです。**リンク先に止めている理由・代わりに使ってよいツール・問い合わせ先を書いておくと、情報システムへの問い合わせが減ります。

## 一部の人だけに使わせる

試験導入の部署だけに使わせる使い方も可能です。Microsoft 365 管理センターのアプリ管理の設定で選んだユーザーだけがCopilotを使えるようにできる、とLearnは説明しています。

具体的には統合アプリの［Copilot］の［ユーザー］タブで［特定のユーザー/グループがインストールできる］を選び、対象のグループを指定します。先ほどのブログの表のとおり、**対象から外れた人のうちライセンスを持たない人は使えず、自分で追加もできません。**ライセンスを持つ人は対象に入れなくても使えます。

社員が自分で有料のCopilotを買ってしまうのを防ぐ設定も、同じ［Copilot］＞［設定］にあります。［Microsoft Copilot セルフサービス購入］の選択肢は、許可・試用版のみを許可・許可しない、の3つです。有料ライセンスを外す手順は[Copilotのライセンスを割り当てる方法](/media/copilot-license-assign/)の「外すときと付け替えるとき」に書いています。

## Web検索だけを止める

Copilot Chatは、答えを作るときにBingへ検索クエリを送り、Webの新しい情報を使います。社外に検索の語が出ることを避けたい会社では、Chatは残してWeb検索だけ切る選択肢があります。

<!-- SHOT: 05_web_search_policy Learn「Microsoft Copilot と Microsoft Copilot Chat での Web 検索のデータ、プライバシー、セキュリティ」の「IT 管理者の制御」の節（https://learn.microsoft.com/ja-jp/microsoft-365/copilot/manage-public-web-access）。PC幅。赤枠: 3つの選択肢の箇条書き -->

使うのは「Copilot での Web 検索を許可」ポリシーです。Microsoft 365 のクラウドポリシー サービスのほか、管理センターの［Copilot］＞［設定］にもあり、グループやユーザーごとに変えられます。選択肢は次の3つです。

- Microsoft Copilot と Microsoft Copilot Chat で有効
- Microsoft Copilot と Microsoft Copilot Chat で無効
- Microsoft Copilot の作業モードでだけ無効（Webモードと Copilot Chat では有効）

無効にすると、社員の画面の［Web コンテンツ］の切り替えがオフになって淡色になり、社員がオンに戻すことはできません。Learnによると、このときCopilot Chatは基になる大規模言語モデルだけで答えを作ります。最新のニュースや料金のような質問には弱くなります。

### 接続エクスペリエンスを切る副作用

ポリシーを何も構成していなければ、Web検索は既定でオンです。Officeのポリシーで［追加のオプションの接続エクスペリエンスの使用を許可する］を無効にしても止まりますが、Learnは、これはMicrosoft 365全体で複数の機能を制限すると書いています。**Web検索だけを止めたいなら、使うのは専用のポリシーです。**

## エージェントと従量課金を止める

無料のCopilot Chatでもエージェントは使えるものの、費用が出るかどうかはエージェントが何を読むかで分かれます。

Learnの「[Copilot Chatでのエージェントの使用](https://learn.microsoft.com/ja-jp/copilot/agents)」によると、指示と公開Webサイトだけで動く宣言型のエージェントは追加料金なしで、既定で使えます。**SharePointやGraph コネクタの社内データを読むエージェントは従量課金で、既定でオフ**です。オンにするには管理者がCopilot Studioのサブスクリプションか従量課金の課金ポリシーを用意する必要があります。

<!-- SHOT: 06_agents_billing Learn「Microsoft 365 Copilot Chatでのエージェントの使用」の「エージェントを有効にする」の節（https://learn.microsoft.com/ja-jp/copilot/agents）。PC幅。赤枠: 「従量制課金を利用するエージェントは、Copilot Chatのユーザーに対して既定でオフ」の文 -->

つまり、課金の設定をしていなければ社内データを読むエージェントで費用は出ません。用意する場合は容量パック（1か月あたり25,000 Copilot クレジットの前払い）と従量課金の組み合わせを選べます。容量パックだけにすると、クレジットを使い切った時点で補充まで使えなくなり、従量課金の請求は出ません。

エージェントそのものを見せたくないときは、管理センターの［設定］＞［統合アプリ］で、エージェントの展開やブロックを決めます。有料のCopilotライセンスを持つ人は、課金の設定なしでエージェントを使えます。

## EdgeとWindowsと個人アカウントの入口

統合アプリのブロックで止まるのは、Copilotアプリ・Outlook・Teams・Web版のCopilot Chatです。それ以外の入口は別の設定です。

### Edgeのボタン

Edgeのツールバーに出るCopilotのボタンは、Edgeのポリシー「[Microsoft365CopilotChatIconEnabled](https://learn.microsoft.com/ja-jp/deployedge/microsoft-edge-browser-policies/microsoft365copilotchaticonenabled)」で消せます。対象はWindowsとmacOSのEdge 139以降で、職場のアカウント（Entra ID）のプロファイルに効きます。開いているページの内容をCopilot Chatに渡すかどうかは、EdgeEntraCopilotPageContextで決めます。どちらもボタンや渡す情報の設定で、Copilot Chat自体の利用を止める設定ではありません。

<!-- SHOT: 07_edge_policy Learn「Microsoft365CopilotChatIconEnabled」のポリシーの説明（https://learn.microsoft.com/ja-jp/deployedge/microsoft-edge-browser-policies/microsoft365copilotchaticonenabled）。PC幅。赤枠: 有効・無効・未構成の3行 -->

### WindowsのCopilotアプリ

Windowsに入っている個人向けのCopilotアプリは、Copilot Chatとは別のアプリです。インストールの防止にはAppLockerを使うよう、Learnは案内しています。社員側から見た消し方と管理者に頼むときの設定名は、[Copilotを消す方法](/media/copilot-remove/)の記事が扱う範囲です。

### 個人アカウントへの抜け道

Copilotアプリには職場のアカウントと個人のMicrosoftアカウントのどちらでもサインインできます。社員が会社のPCで個人のアカウントに切り替えれば、職場のブロックは関係なくなります。

ここで copilot.cloud.microsoft のURLをブロックしたくなりますが、Learnは、個人アカウントを止める目的でこのURLをブロックしないよう書いています。代わりに使うのが、Microsoft Entraの「[テナント制限 v2](https://learn.microsoft.com/ja-jp/entra/external-id/tenant-restrictions-v2)」です。会社のネットワークや端末から、外部のアカウントでサインインできる範囲を絞れます。**URLやIPアドレスでの遮断は、Microsoft 365のアプリまで止まる恐れがあるとしてMicrosoftは勧めていません。**

## 止める前と止めたあとに見るもの

止める前に、誰がどれだけ使っているかを数えておくと、社内の説明がしやすくなります。管理センターの［レポート］＞［使用状況］で［Microsoft Copilot］＞［Copilot Chat］を開くと、アクティブなユーザーの数やプロンプトの数を7日・28日・90日・180日の範囲で見られます。

<!-- SHOT: 08_usage_report Learn「Microsoft Copilot Chat使用状況レポート」の表示手順の節（https://learn.microsoft.com/ja-jp/microsoft-365/admin/activity-reports/microsoft-copilot-usage）。PC幅。赤枠: 4つの手順の番号付きリスト -->

このレポートが数えるのは、Copilotライセンスを持たない社員の利用だけです。

ブロックやWeb検索の停止を始めるときは、社員に先に知らせます。止める範囲・理由・代わりに使ってよいツール・いつ見直すかの4つを書き、同じ内容をカスタムリンクの先に置いておくと、問い合わせへの答えが1か所にまとまるのも利点です。

止めている間に、社内のどの業務ならAIに任せられるかを整理しておくと、解禁するときの判断が早くなります。業務の一部をAIエージェントに任せる仕組みづくりの相談先は、[AIエージェント構築支援](/ai-agent/)のページです。

## よくある質問

### Copilot Chatは管理者が無効にできますか？
できます。Microsoft 365 管理センターの［設定］＞［統合アプリ］でCopilotをブロックすると、Copilotアプリ・Outlook・Teams・Web版でCopilot Chatを使えなくなります。全員にも、特定のユーザーやグループにもかけられます。

### Copilot Chatはピン留めを外せば止まりますか？
止まりません。ピン留めはTeamsやOutlookのナビゲーションに出すかどうかの設定です。2026年1月28日からはCopilotアプリにも効かず、社員はCopilotアプリやブラウザから使えます。

### Copilot Chatのブロックは有料の人も止まりますか？
止まります。統合アプリで［アプリをブロックする］を選ぶと、ライセンスの有無にかかわらずCopilot Chatを使えません。ライセンスを持つ人を残したいなら［組織のユーザーはインストールできません］を選びます。

### Copilot ChatのWeb検索だけを止められますか？
止められます。「Copilot での Web 検索を許可」ポリシーで無効を選ぶと、社員の［Web コンテンツ］の切り替えが淡色になり、オンにできなくなります。

### Copilot Chatのエージェントに費用はかかりますか？
指示と公開Webサイトだけで動くエージェントは追加料金なしです。社内データを読むエージェントは従量課金で既定でオフのため、管理者が課金を設定しない限り費用は出ません。

### Copilot Chatの設定はいつ反映されますか？
ピン留めの変更は最大48時間かかる場合がある、とLearnに書かれています。ブロックなど他の設定の反映時間は、Learnには書かれていません。

### Copilot Chatは個人アカウントでも止まりますか？
止まりません。個人のMicrosoftアカウントでCopilotアプリにサインインすれば、職場のブロックとは関係なく使えます。会社の端末やネットワークから外部のアカウントで入れないようにするには、Microsoft Entraのテナント制限 v2を使います。

### Copilot Chatの利用者数はどこで分かりますか？
管理センターの［レポート］＞［使用状況］＞［Microsoft Copilot］＞［Copilot Chat］です。Copilotライセンスを持たない社員の利用だけが数えられます。

## 出典

- Microsoft Learn「[Microsoft Copilot Chatの管理](https://learn.microsoft.com/ja-jp/copilot/manage)」（2026年10月17日取得）
- Microsoft Learn「[Microsoft 365 アプリでMicrosoft Copilot Chatをピン留めする](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/pin-copilot-chat-navbar)」（同）
- Microsoft Learn「[Microsoft 365 管理センターで Microsoft Copilot 設定を管理する](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/microsoft-365-copilot-page)」（同）
- Microsoft Learn「[管理者が制御できる Microsoft Copilot アプリの機能](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/microsoft-365-copilot-app-admin-settings)」（同）
- Microsoft Learn「[Microsoft Copilot と Microsoft Copilot Chat での Web 検索のデータ、プライバシー、セキュリティ](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/manage-public-web-access)」（同）
- Microsoft Learn「[Microsoft 365 Copilot Chatでのエージェントの使用](https://learn.microsoft.com/ja-jp/copilot/agents)」（同）
- Microsoft Learn「[Microsoft Copilot Chat エージェントと SharePoint エージェントに Copilot Studio 容量パックを使用する](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/pay-as-you-go/copilot-capacity-packs)」（同）
- Microsoft Learn「[更新された Windows および Microsoft Copilot Chat エクスペリエンス](https://learn.microsoft.com/ja-jp/windows/client-management/manage-windows-copilot)」（同）
- Microsoft Learn「[Microsoft Copilot Chat使用状況レポート](https://learn.microsoft.com/ja-jp/microsoft-365/admin/activity-reports/microsoft-copilot-usage)」（同）
- Microsoft Learn「[Microsoft365CopilotChatIconEnabled](https://learn.microsoft.com/ja-jp/deployedge/microsoft-edge-browser-policies/microsoft365copilotchaticonenabled)」（同）
- Microsoft Learn「[テナント制限 v2 を設定する](https://learn.microsoft.com/ja-jp/entra/external-id/tenant-restrictions-v2)」（同）
- Japan Exchange & Outlook Support Blog「[Microsoft 365 Copilot Chat のピン留めの制御方法](https://jpmessaging.github.io/blog/Outlook-microsoft365-copilot-chat-pin-admin-control/)」（2025年12月23日公開、2026年10月17日取得）
