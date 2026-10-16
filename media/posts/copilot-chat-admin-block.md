---
title: 【2026年10月】Copilot Chatを社内で止める方法｜ブロック・Web検索・エージェント
date: 2026-10-17
category: AI活用
description: 無料のCopilot Chatを管理者が止める・絞る方法を公式ドキュメントから解説。ピン留めを外すだけでは止まらない理由、統合アプリでのブロック、Web検索やエージェントだけ止める設定、私用アカウントへの抜け道まで。
cover_tag: 管理者向け
cover_headline: Copilot Chatを社内で止める
cover_sub: ブロック・ピン留め・Web検索・エージェント
---

Microsoft 365 Business StandardやE3などの対象プランを契約している会社では、職場のアカウント（Microsoft Entra ID）でサインインした社員が、追加料金なしでCopilot Chatを使えます。TeamsとOutlookのナビゲーションには既定でピン留めされているため、導入を決める前から社員の画面に出ていることがあります。名前は「Microsoft 365 Copilot Chat」から「Microsoft Copilot Chat」に変わりました。

社内のルールが決まるまで止めたい、一部の部署だけ使わせたい、Web検索だけ切りたい、という相談は管理者に集まります。Microsoft Learnの「[Microsoft Copilot Chatの管理](https://learn.microsoft.com/ja-jp/copilot/manage)」（2026年10月12日更新）は、アクセスを絞る方法としてピン留めを外す・特定のユーザーやグループに限る・ブロックする、の3つを挙げています。この記事は2026年10月17日に取得したMicrosoft LearnとMicrosoftの日本のサポートブログをもとに、どの設定で何が止まるかを整理したものです。管理センターの操作はこちらでは試していないので、手順と画面の動きは公式の説明に沿って書いています。

:::takeaways
- **ピン留めを外しても、Copilot Chatは使えるまま**。Copilotアプリやブラウザからたどり着ける
- **使えなくするのは統合アプリでのブロック**。対象となるCopilotライセンスを持つ人も止まる
- 一部の人だけ使わせるなら、統合アプリの［ユーザー］タブで**特定のユーザーやグループ**を選ぶ
- **Web検索だけ**は「Copilot での Web 検索を許可する」ポリシーで切れる。オプションの接続エクスペリエンスを切ると他の機能まで止まる
- 社内データを読むエージェントは**従量課金で既定オフ**。課金の設定をしなければ費用は出ない
:::

<figure class="post-figure"><img src="/media/images/copilot-chat-admin-block/01_fig_scope.png" alt="Copilot Chatを止める3段階の図。ピン留めを外すのは見えなくするだけ、特定の人・Web検索・エージェントは一部だけ止める、統合アプリでブロックすると使えなくなる。止まる範囲はこの順に広がる" loading="lazy"><figcaption>止まる範囲は3段階</figcaption></figure>

## 止めたい範囲を先に決める

画面から消したいのか使えなくしたいのかで、選ぶ設定は変わります。Copilot Chatの入口はCopilotアプリ（Web・デスクトップ・モバイル）、Edge、Outlook、Teams、WordやExcelのエージェントと複数あり、**どこか1つを閉じても別の入口から開ける**ように作られています。

| やりたいこと | 使う設定 | 止まる範囲 |
|---|---|---|
| TeamsとOutlookから見えなくする | Copilot＞設定のピン留め | ナビゲーションの表示だけ |
| 全員が使えないようにする | 統合アプリでCopilotをブロック | Copilotアプリ・Outlook・Teams・Web版のChat |
| 一部の人だけに使わせる | 統合アプリの［ユーザー］タブ | 選ばなかった人（ライセンスなし） |
| Web検索だけ止める | Copilot での Web 検索を許可する | Bingへの検索クエリ |
| 有料のエージェントを止める | 従量課金を設定しない・エージェントのブロック | 社内データを読むエージェント |
| Edgeのボタンを消す | Microsoft365CopilotChatIconEnabled | Edgeのツールバーの表示 |

迷ったら、**表示を消す設定と利用を止める設定を分けて考える**と整理しやすくなります。前者はピン留めとEdgeのボタン、後者は統合アプリでのブロックと各機能のポリシーです。

## ピン留めを外しても使える

TeamsのアイコンからCopilotが消えれば止まった、と考えたくなります。しかしLearnの管理のページは、ピン留めを外してもCopilot Chatへのアクセスは削除されず、Copilotアプリなどから引き続き使える可能性がある、と注意書きを置いています。**ピン留めは表示の設定で、利用の可否は決めません。**

<figure class="post-figure"><img src="/media/images/copilot-chat-admin-block/02_pin_options.jpg" alt="Microsoft Learnのピン留めオプションの節。推奨のピン留めする設定と、ピン留めしない設定の説明が並び、ピン留めしない場合も利用者はアプリストアからCopilotを自分で追加できると書かれている（赤枠1）。赤枠2は設定の変更が反映されるまでの時間" loading="lazy"><figcaption>Microsoft Learn「Microsoft 365 アプリでMicrosoft Copilot Chatをピン留めする」のピン留めオプション</figcaption></figure>

### ピン留めの設定の場所

設定にはAI 管理者のロールが要ります。[Microsoft 365 管理センター](https://admin.microsoft.com/)にサインインし、［Copilot］＞［設定］から［Microsoft Copilot Chatをピン留めする］を開くと、ピン留めする（推奨・既定）と、ピン留めしない、の2つから選べます。変更が有効になるまで最大48時間かかる場合がある、とLearnに書かれています。

### 2026年1月からCopilotアプリには効かない

Microsoft Copilotアプリ（旧Microsoft 365 Copilotアプリ）のナビゲーションには、ピン留めの設定が効かなくなりました。Learnの管理のページによると、欧州経済領域とスイスのテナントは2025年7月25日から、それ以外のテナントは2026年1月28日からです。**ピン留めしない設定にしても、Copilotアプリを開けばChatは並んでいます。**

ピン留めしない設定でも、利用者はTeamsやOutlookのアプリストアからCopilotを自分で追加できます。ピン留めを外す手は社員を急に戸惑わせずに入口を目立たなくしたいとき向けで、利用を止める手ではありません。

## 統合アプリでCopilotをブロックする

社員がCopilot Chatを使えない状態にしたいときは、ブロックを使います。Learnの管理のページには、すべてのユーザー、または特定のユーザーとグループのCopilot Chatへのアクセスをブロックでき、そこには対象となるMicrosoft Copilotライセンスを持つ人も含まれる、と書かれています。

<figure class="post-figure"><img src="/media/images/copilot-chat-admin-block/03_learn_block.jpg" alt="Microsoft LearnのMicrosoft Copilot Chatへのアクセスを制限する節。ピン留めを外す、特定のユーザーまたはグループに制限する、アクセスのブロックの3つが並ぶ（赤枠1）。ブロックの項には対象となるライセンスを持つユーザーも含めてブロックでき、ブロックされるとCopilotアプリ・Outlook・Teams・Web版などで使えなくなると書かれている（赤枠2）" loading="lazy"><figcaption>Microsoft Learn「Microsoft Copilot Chatの管理」のアクセスを制限する節</figcaption></figure>

### ブロックの手順

Learnの管理のページは、ブロックできることと利用者の画面は説明していますが、ブロックの設定画面の手順は載せていません（2026年10月17日に確認）。手順はMicrosoftの日本のサポートチームのブログ「[Microsoft 365 Copilot Chat のピン留めの制御方法](https://jpmessaging.github.io/blog/Outlook-microsoft365-copilot-chat-pin-admin-control/)」（2025年12月23日）に載っています。統合アプリでCopilotをブロックするとライセンスの有無にかかわらずOutlookなどでCopilot Chatが使えなくなったことも、ブログが説明しています。

1. Microsoft 365 管理センターで［設定］＞［統合アプリ］を開く
2. ［利用可能なアプリ］で［Copilot］を選ぶ
3. ［アプリをブロックする］を選ぶ

<figure class="post-figure"><img src="/media/images/copilot-chat-admin-block/09_blog_block.jpg" alt="Microsoftの日本のサポートブログに載っている、Microsoft 365 管理センターの統合アプリの画面。設定の下の統合アプリ（赤枠1）、利用可能なアプリのタブ（赤枠2）、Copilotの詳細パネルの処理にあるアプリをブロックする（赤枠3）" loading="lazy"><figcaption>サポートブログの統合アプリの画面。赤枠の番号は手順の番号と同じ</figcaption></figure>

表記が見つからないときは、統合アプリの一覧で「Copilot」を検索してください。

### ライセンスを持つ人も止まる

統合アプリの3つの設定でCopilotライセンスの有無によって動きが変わることも、同じブログが表で示しています。違いが出るのは**［アプリをブロックする］以外の2つ**で、ライセンスを持つ人のCopilot Chatは使えるままです。

| 統合アプリの設定 | ライセンスなしの人 | ライセンスありの人 |
|---|---|---|
| 展開対象から外す | 使えない・追加もできない | 使える |
| 組織のユーザーはインストールできません | 使えない・追加もできない | 使える |
| アプリをブロックする | 使えない | 使えない |

<figure class="post-figure"><img src="/media/images/copilot-chat-admin-block/04_fig_block_matrix.png" alt="統合アプリの3つの設定でCopilot Chatを使えるかの図。展開対象から外すと、組織のユーザーはインストールできませんの2つは、ライセンスなしの人は使えず、ライセンスありの人は使える。アプリをブロックするはどちらも使えない" loading="lazy"><figcaption>ライセンスを持つ人まで止まるのはブロックだけ</figcaption></figure>

有料のCopilotを入れた部署は残し、それ以外を止めたいなら、［展開対象から外す］か［組織のユーザーはインストールできません］が合います。全員を止めるならブロックです。ブロックしたあとのアイコンの見え方はOutlookの種類によってそろわない場合がある、とブログは書いています。

### ブロックされた社員の画面

ブロックされた社員がCopilotアプリでChatを選ぶと、組織のポリシーでアクセスが無効になっている、という説明が出ます。ナビゲーションからChatの項目がすぐ消えるとは限らないため、社員から壊れているのでは、と問い合わせが来るかもしれません。

その画面には社内のルールのページへのリンクを出せます。Learnの手順では管理センターの［Copilot］＞［設定］で［すべて表示］を選び、ブロックされた Microsoft Copilot アプリの［カスタム リンク］に社内のページのURLを入れます。**社員の画面に出るのは「View info from your organization」というリンクです。**リンク先に止めている理由・代わりに使ってよいツール・問い合わせ先を書いておくと、情報システムへの問い合わせが減ります。

## 一部の人だけに使わせる

試験導入の部署だけに使わせるときも、使うのは統合アプリの設定です。組織の構成に応じて、Microsoft 365 管理センターのアプリ管理の設定で選んだユーザーだけがCopilotを使えるようにできる、とLearnは説明しています。

具体的には統合アプリの［Copilot］の［ユーザー］タブで［特定のユーザー/グループがインストールできる］を選び、対象のグループを指定します。先ほどのブログの表のとおり、**対象から外れた人のうちライセンスを持たない人は使えず、自分で追加もできません。**ライセンスを持つ人は対象に入れなくても使えます。

社員が自分で有料のCopilotを買ってしまうのを防ぐ設定も、同じ［Copilot］＞［設定］にあります。［Microsoft Copilot セルフサービス購入］の選択肢は、許可・試用版のみを許可・許可しない、の3つです。有料ライセンスを外す手順は[Copilotのライセンスを割り当てる方法](/media/copilot-license-assign/)の「外すときと付け替えるとき」に書いています。

## Web検索だけを止める

Copilot Chatは、答えを作るときにBingへ検索クエリを送り、Webの新しい情報を使います。社外に検索の語が出ることを避けたい会社では、Chatは残してWeb検索だけ切る選択肢があります。

<figure class="post-figure"><img src="/media/images/copilot-chat-admin-block/05_web_search_policy.jpg" alt="Microsoft LearnのIT 管理者の制御の節。管理者が選ぶ設定はMicrosoft CopilotとCopilot Chatの両方に効く。有効、無効、作業モードだけ無効の3つの選択肢が赤枠で囲まれている" loading="lazy"><figcaption>Microsoft Learn「Web 検索のデータ、プライバシー、セキュリティ」のIT 管理者の制御</figcaption></figure>

使うのは「Copilot での Web 検索を許可する」ポリシーです。Microsoft 365 のクラウドポリシー サービスで設定し、グループやユーザーごとに変えられます。管理センターでの置き場所は［Copilot］＞［設定］＞［データ アクセス］＞［Web 検索］だと、Learnの設定管理のページは書いています。Web検索のページは「クラウド ポリシー サービスでのみ」としていて、Learnの中でも説明がそろっていません。選択肢は次の3つです。

- Microsoft Copilot および Microsoft Copilot Chat で有効
- Microsoft Copilot と Microsoft Copilot Chat で無効にする
- Microsoft Copilot 作業モードで無効になっています。Microsoft Copilot Web モードと Microsoft Copilot Chat で有効

無効にすると、社員の画面の［Web コンテンツ］の切り替えがオフになって淡色になり、社員がオンに戻すことはできません。Learnによると、このときCopilot Chatは基になる大規模言語モデルだけで答えを作ります。最新のニュースや料金のような質問には弱くなります。

### 接続エクスペリエンスを切る副作用

ポリシーを何も構成していなければ、Web検索は既定でオンです。Officeのポリシーで［追加のオプションの接続エクスペリエンスの使用を許可する］を無効にしても止まりますが、Learnは、これはMicrosoft 365全体で複数の機能を制限すると書いています。**Web検索だけを止めたいなら、使うのは専用のポリシーです。**

## エージェントと従量課金を止める

無料のCopilot Chatでもエージェントは使えるものの、費用が出るかどうかはエージェントが何を読むかで分かれます。

Learnの「[Copilot Chatでのエージェントの使用](https://learn.microsoft.com/ja-jp/copilot/agents)」によると、指示と公開Webサイトだけで動く宣言型のエージェントは追加料金なしで、既定で使えます。**SharePointやGraph コネクタの社内データを読むエージェントは従量課金で、既定でオフ**です。オンにするには管理者がCopilot Studioのサブスクリプションか従量課金の課金ポリシーを用意する必要があります。

<figure class="post-figure"><img src="/media/images/copilot-chat-admin-block/06_agents_billing.jpg" alt="Microsoft Learnのエージェントを有効にする節。指示と公開Webサイトだけで動く宣言型エージェントは追加料金なし。赤枠はSharePointやGraph コネクタの共有データを読むエージェントが従量課金で、Copilot Chatのユーザーには既定でオフという記述" loading="lazy"><figcaption>Microsoft Learn「Copilot Chatでのエージェントの使用」</figcaption></figure>

つまり、課金の設定をしていなければ社内データを読むエージェントで費用は出ません。用意する場合は容量パックと従量課金の組み合わせを選べます。容量パックは1パックあたり月25,000 Copilot クレジットの前払いです。クレジットのポリシーだけにすると、使い切った時点で補充まで対象の社員はCopilot Chatを使えなくなり、従量課金の請求は出ません。

## EdgeとWindowsと個人アカウントの入口

ブロックで止まる場所としてLearnが挙げているのは、Copilotアプリ・Outlook・Teams・Web版のCopilot Chatです。それ以外の入口は別の設定です。

### Edgeのボタン

Edgeのツールバーに出るCopilotのボタンは、Edgeのポリシー「[Microsoft365CopilotChatIconEnabled](https://learn.microsoft.com/ja-jp/deployedge/microsoft-edge-browser-policies/microsoft365copilotchaticonenabled)」で消せます。対象はWindowsとmacOSのEdge 139以降で、職場のアカウント（Entra ID）のプロファイルに効きます。開いているページの内容・閲覧履歴・動画の文字起こしをCopilot Chatに渡すかどうかは、EdgeEntraCopilotPageContext（Edge 130以降）で決めます。どちらもボタンや渡す情報の設定で、Copilot Chat自体の利用を止める設定ではありません。

<figure class="post-figure"><img src="/media/images/copilot-chat-admin-block/07_edge_policy.jpg" alt="Edgeのポリシーの説明。有効ならツールバーにCopilotが表示され、無効なら表示されない。構成しない場合は表示され、ユーザーが設定で切り替えられる（赤枠）" loading="lazy"><figcaption>Microsoft Learn「Microsoft365CopilotChatIconEnabled」の説明</figcaption></figure>

### WindowsのCopilotアプリ

Windowsに入っている個人向けのCopilotアプリは、Copilot Chatとは別のアプリです。インストールの防止にはAppLockerを使うよう、Learnは案内しています。社員側から見た消し方と管理者に頼むときの設定名は、[Copilotを消す方法](/media/copilot-remove/)の記事が扱う範囲です。

### 個人アカウントへの抜け道

Copilotアプリには職場のアカウントと個人のMicrosoftアカウントのどちらでもサインインできます。社員が会社のPCで個人のアカウントに切り替えれば、職場のブロックは関係なくなります。

個人アカウントを止める目的で copilot.cloud.microsoft のURLをブロックしないよう、Learnは書いています。代わりに使うのが、Microsoft Entraの「[テナント制限 v2](https://learn.microsoft.com/ja-jp/entra/external-id/tenant-restrictions-v2)」です。会社のネットワークや端末から、外部のアカウントでサインインできる範囲を絞れます。**URLやIPアドレスでの遮断は、Microsoft 365のアプリまで止まる恐れがあるとしてMicrosoftは勧めていません。**

## 止める前と止めたあとに見るもの

止める前に、誰がどれだけ使っているかを数えておくと、社内の説明がしやすくなります。管理センターの［レポート］＞［使用状況］で［Microsoft Copilot］＞［Copilot Chat］を開くと、アクティブなユーザーの数やプロンプトの数を7日・28日・90日・180日の範囲で見られます。

<figure class="post-figure"><img src="/media/images/copilot-chat-admin-block/08_usage_report.jpg" alt="Microsoft Learnの使用状況レポートを表示する手順。管理センターに戻り、レポート、使用状況を選び、レポートでMicrosoft CopilotとCopilot Chatを順に選ぶ4つの手順が赤枠で囲まれている" loading="lazy"><figcaption>Microsoft Learn「Microsoft Copilot Chat使用状況レポート」の表示手順</figcaption></figure>

このレポートが数えるのは、今のところCopilotライセンスを持たない社員の利用だけです。

ブロックやWeb検索の停止を始めるときは、社員に先に知らせます。止める範囲・理由・代わりに使ってよいツール・いつ見直すかの4つを書き、同じ内容をカスタムリンクの先に置いておくと、問い合わせへの答えが1か所にまとまるのも利点です。

止めて社内のルールが決まったら、次はどの業務でAIを使うかです。業務を決めてAIを仕組みとして組む段階の相談先は、[AIエージェント構築支援](/ai-agent/)のページです。

## よくある質問

### Copilot Chatは管理者が無効にできますか？
できます。Learnによると、ブロックした社員はCopilotアプリ・Outlook・Teams・Web版でCopilot Chatを使えなくなります。全員にも、特定のユーザーやグループにもかけられ、日本のサポートブログは統合アプリでCopilotをブロックする手順を載せています。

### Copilot Chatはピン留めを外せば止まりますか？
止まりません。ピン留めはTeamsやOutlookのナビゲーションに出すかどうかの設定です。2026年1月28日からはCopilotアプリにも効かず、社員はCopilotアプリやブラウザから使えます。

### Copilot Chatのブロックは有料の人も止まりますか？
止まります。統合アプリで［アプリをブロックする］を選ぶと、ライセンスの有無にかかわらずCopilot Chatを使えません。ライセンスを持つ人を残したいなら［展開対象から外す］か［組織のユーザーはインストールできません］を選びます。

### Copilot ChatのWeb検索だけを止められますか？
止められます。「Copilot での Web 検索を許可する」ポリシーで無効を選ぶと、社員の［Web コンテンツ］の切り替えが淡色になり、オンにできなくなります。

### Copilot Chatのエージェントに費用はかかりますか？
指示と公開Webサイトだけで動くエージェントは追加料金なしです。社内データを読むエージェントは従量課金で既定でオフのため、管理者が課金を設定しない限り費用は出ません。

### Copilot Chatの設定はいつ反映されますか？
ピン留めの変更は最大48時間かかる場合がある、とLearnに書かれています。ブロックなど他の設定の反映時間は、Learnには書かれていません。

### Copilot Chatは個人アカウントでも止まりますか？
止まりません。個人のMicrosoftアカウントでCopilotアプリにサインインすれば、職場のブロックとは関係なく使えます。会社の端末やネットワークから外部のアカウントで入れないようにするには、Microsoft Entraのテナント制限 v2を使います。

### Copilot Chatの利用者数はどこで分かりますか？
管理センターの［レポート］＞［使用状況］＞［Microsoft Copilot］＞［Copilot Chat］です。今のところCopilotライセンスを持たない社員の利用だけが数えられます。

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
