---
title: 【2026年10月】Copilotが社内で使われないときの調べ方｜使用状況レポート・定着の手順
date: 2026-10-19
category: AI活用
description: Microsoft 365 Copilotが社内で使われないとき、使用状況レポートで使えない人・試していない人・離れた人を分ける方法を公式ドキュメントから解説。通知の出し方、ライセンスの配り直し、経営に出す数字まで。
cover_tag: 導入担当向け
cover_headline: Copilotが社内で使われないとき
cover_sub: 使用状況レポート・定着の手順
cta: ai_agent
---

Microsoft 365 管理センターの「Microsoft Copilot の使用状況レポート」のアクティブ ユーザーは、ウィンドウを開いただけでは数えず、プロンプトを送る・要約のボタンを押すなどの操作をして初めて数える定義です。

使われていないと感じたら、先にこの数字で止まっている人を分けると打ち手が決まります。この記事では2026年10月19日時点のMicrosoft Learnと導入サイトをもとに、レポートの読み方・定着の材料・配り直しと報告の数字を扱います。管理センターの画面は操作していません。

:::takeaways
- **アクティブ ユーザーはCopilotの機能を実際に使った人の数**。ウィンドウを開いただけでは数えない
- 使われない人は**使えない・試していない・試して離れた**の3つに分け、それぞれに別の打ち手を当てる
- 未使用の人への通知、配り直しの候補、経営向けの推定時間は**管理センターとViva インサイトに用意されている**
:::

<figure class="post-figure"><img src="/media/images/copilot-adoption/cadp_01_split.png" alt="使われない人を使えない人・試していない人・試して離れた人の3つに分け、それぞれレポートで見る所を並べた図" loading="lazy"><figcaption>Copilotを使わない人の3つの型と、レポートで見る所</figcaption></figure>

## 使われていないかを数字で確かめる

「入れたのに誰も使っていない」と感じても、それだけでは誰が止まっているのか分かりません。Microsoft Learnの「[Microsoft Copilot の使用状況レポート](https://learn.microsoft.com/ja-jp/microsoft-365/admin/activity-reports/microsoft-365-copilot-usage)」によると、レポートは管理センターの［レポート］＞［使用状況］で［Microsoft Copilot］＞［Copilot］を選び、［使用状況］タブで開きます。期間は過去7日・28日・90日・180日から選べ、ある日の利用は通常その日の終わり（UTC）から48時間以内に反映されます。

<figure class="post-figure"><img src="/media/images/copilot-adoption/cadp_03_usage.png" alt="Microsoft Learn の使用状況レポートの表示手順。管理センターのレポートから使用状況を選び、Microsoft Copilot の使用状況タブを開く" loading="lazy"><figcaption>使用状況レポートを開く手順（Microsoft Learn）</figcaption></figure>

上の段に並ぶ数字のうち、まず見るのは次の3つです。

| 数字 | 中身 |
|---|---|
| 有効なユーザー | 期間中にCopilotのライセンスを持っていた人の数 |
| アクティブ ユーザー | 有効なユーザーのうち、どれか1つのアプリでCopilotの機能を試した人の数 |
| アクティブ ユーザー率 | アクティブ ユーザーを有効なユーザーで割った値 |

数え方で注意したいのはアクティブの定義です。**AIの機能に意図的な操作をしたときだけアクティブと数えるため、Wordのリボンでアイコンを押してウィンドウを開いただけの人は入りません。**率が低いときは開いてはみたものの何も頼まずに閉じた人が含まれている、という読み方もできます。

ユーザー名や表示名は既定ではどのレポートでも隠れており、出すときは［設定］＞［組織の設定］＞［サービス］タブの［レポート］で「すべてのレポートでユーザー、グループ、サイト名を非表示にする」のチェックを外します（Microsoft Learn「[Microsoft 365 管理センターのアクティビティ レポート](https://learn.microsoft.com/ja-jp/microsoft-365/admin/activity-reports/activity-reports)」）。**社内のプライバシーの方針で名前を出してよいかを先に確かめておかないと、誰に案内を送るかを決める段階で作業が止まります。**

Purviewの監査ログから自前でプロンプト数を集計する会社もありますが、Microsoftは監査ログを使用状況レポートの土台として使う想定ではないとしています。集計した数が公式のレポートと一致しない場合があるため、社内で報告する数字は管理センターのレポートかViva インサイトのCopilot ダッシュボードにそろえるのが無難です。

## 使われない人を3つに分ける

アクティブ ユーザー率が低いと分かっても、全員に同じ研修を案内するだけでは止まっている理由は解消しません。レポートの表を書き出して、使われない人を次の3つに分けると打ち手を当てやすくなります。

| 分け方 | レポートで見る所 | 打ち手 |
|---|---|---|
| 使えない人 | 準備状況レポートの更新チャネルの列・推奨カード | 端末とアプリの設定を直す |
| 試していない人 | 最終アクティビティ日が空欄 | 組織のメッセージで通知する |
| 試して離れた人 | アプリ別の最終アクティビティ日が古い | 部署の使い道を渡す・声を聞く |

ユーザー別の表には過去180日の間に一度でもライセンスを持った人が全員出ます。途中でライセンスを外した人や、一度も使っていない人も含まれるので、［エクスポート］でCSVに落としてから並べ替えると分けやすくなります。

### 使えない人

本人に使う気があっても、画面にCopilotが出ていなければ使いようがありません。同じ［Microsoft Copilot］のレポートの最初のタブが「[Microsoft Copilot 準備状況レポート](https://learn.microsoft.com/ja-jp/microsoft-365/admin/activity-reports/microsoft-365-copilot-readiness)」で、ユーザーごとの「対象となる更新プログラム チャネルを使用する」の列で、端末が対象のチャネルかどうかが分かります。**Copilot ダッシュボードの説明では、デスクトップ版のアプリでCopilotを使うには最新チャネルか月次エンタープライズ チャネルに入っている必要があるとされています。**

<figure class="post-figure"><img src="/media/images/copilot-adoption/cadp_04_readiness.png" alt="Microsoft Learn の準備状況レポートのユーザー アクティビティ テーブル。対象となる更新プログラム チャネルを使用するの行を赤枠で囲んでいる" loading="lazy"><figcaption>準備状況レポートのユーザー アクティビティ テーブル（Microsoft Learn）</figcaption></figure>

Viva インサイトのCopilot ダッシュボードの準備ページには、OutlookやCopilotアプリでの利用がブロックされている、Microsoft 365 アプリにCopilot Chatがピン留めされていない、といった推奨カードが出ます。割り当てた直後で表示を待っている人もいるため、反映の時間と出ないときの順番は「[Copilotのライセンスを割り当てる方法](/media/copilot-license-assign/)」で確かめてください。

### 一度も試していない人

ライセンスがあるのに最終アクティビティ日が空欄の人は、まだ一度もCopilotの機能を使っていない可能性が高い人です。ただしレポートの説明には、割り当てから24時間以内に使った人が、まれに空欄になる場合があると書かれています。

この層に向いているのはレポートに組み込まれた組織のメッセージです。Microsoft Learnの「[Microsoft Copilot を使用して導入を促進する 使用状況レポート 組織のメッセージング](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/track-copilot-adoption)」（2026年9月25日更新）によると、あらかじめ用意された推奨カードは次の2枚です。

| 推奨カード | 届く相手 | 出る場所 |
|---|---|---|
| Microsoft Copilot の使用をユーザーに奨励する | ライセンスを持つWindows 11の利用者で、30日間使っていない人 | Windowsの通知（画面の右下） |
| Teams の Copilot を使用してユーザーが時間を節約できるようにする | Copilotのライセンスを持つTeamsの新しい利用者で、30日以内にTeamsのCopilotを使っていない人 | TeamsのCopilotチャットの横 |

カードの［アクションの実行］からメッセージの種類を選び、受信者をMicrosoft 365 グループで絞り、開始日と終了日、頻度（毎週・毎月・隔月）を決めればスケジュールが組まれます。**部署のグループで絞れるため、利用率の低い部署にだけ通知を出す使い方ができます。**送ったあとは［レポート］＞［組織のメッセージ］で、メッセージの総数・クリック数・クリック率を追えます。

<figure class="post-figure"><img src="/media/images/copilot-adoption/cadp_05_orgmsg.png" alt="Microsoft Learn の組織メッセージの推奨カードの節。Copilot の使用を促すカードと Teams で使うよう促すカードの2枚が用意されている" loading="lazy"><figcaption>あらかじめ用意された推奨カード（Microsoft Learn）</figcaption></figure>

用意された文面は「Copilot をお試しください」のような一般的なものです。用意された推奨カードより細かく決めたいときは、管理センターの組織のメッセージのページから出します。

### 試して離れた人

一度は使ったのに、最終アクティビティ日が1か月以上前で止まっている人もいます。ユーザー別の表にはTeams・Word・Excel・PowerPoint・Outlook・OneNote・Loop・Copilot Chatのアプリ別に最後の日付が並ぶので、**どのアプリで止まったかを見ると、案内する使い方が絞れます。**Teamsの会議の要約だけ続いていてWordが止まっている人には、Wordでの文書の下書きの例を案内する、といった具合です。

Word・Excel・PowerPointなどの最終日は、送信の遅れで実際より新しく出たり空欄になったりする既知の制限があります。1人の数字で判断せず、部署の傾向として読むほうが安全です。

使い道の材料はMicrosoftの導入サイトの[シナリオ ライブラリ](https://adoption.microsoft.com/ja-jp/scenario-library/)にあります。財務・人事・営業・法務などの機能別と、製造・小売・金融などの業種別に、Copilotでやる作業の例を集めたページです。Copilot ダッシュボードの満足度（回答へのサムアップの割合）を見ると、どのグループで手応えが無いかも分かります。

## Microsoftが用意している定着の材料

Microsoft Learnの「[IT 管理者向け Microsoft Copilot 導入ガイドと概要](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/microsoft-365-copilot-enablement-resources)」（2026年10月15日更新）は、導入を5つの手順で示しています。5つ目に置かれているのが、ライセンスを割り当てたあとのウェルカム メールと、利用者がMicrosoftにフィードバックを送れる設定です。**割り当てで終わらせず、使い始めの案内までを導入の範囲に入れています。**

社内の推進で使える材料は次のとおりです。

| 材料 | 中身 | 使う場面 |
|---|---|---|
| [Copilot Success Kit](https://adoption.microsoft.com/ja-jp/copilot/success-kit/) | 実装の概要・利用者向けガイド・技術準備ガイド・導入計画チェックリスト・ライセンス配分ガイドなど | 推進の計画を作り直すとき |
| [シナリオ ライブラリ](https://adoption.microsoft.com/ja-jp/scenario-library/) | 機能別・業種別の使い方の例 | 部署ごとの使い道を決めるとき |
| 組織のメッセージ | Windows・Teamsへの通知 | 試していない人に届けるとき |
| [Copilot オンボード](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/manage-copilot-onboarding) | 製品の中で使い方を案内する機能 | 使い始めの案内をそろえるとき |
| [チャンピオン プログラム](https://adoption.microsoft.com/ja-jp/become-a-champion/) | 推進役が会社をまたいで情報を交換するMicrosoftのコミュニティ（英語）と、社内のコミュニティの作り方のガイド | 部署ごとに相談役を置くとき |

<figure class="post-figure"><img src="/media/images/copilot-adoption/cadp_06_kit.png" alt="Microsoft の Copilot サクセス キットのページ。実装の概要・ユーザー有効化ガイド・技術準備ガイドなどの資料が並ぶ" loading="lazy"><figcaption>Copilot サクセス キットの資料（Microsoft）</figcaption></figure>

Copilot オンボードは、管理センターで社内のAI 使用ポリシーのURLを入れておくと、利用者が使い始めにそのポリシーを読む流れを作れます。Viva Learningを有効にすれば、誰が最後まで終えたかも追えます。ただし今はFrontier プログラムに参加したテナントだけが対象です。

## ライセンスを配り直す判断

使っていない人のライセンスにも、1人ごとの月額がかかり続けます。ライセンスの割り当てを外しても契約の数は減らないため（[Copilotのライセンスを割り当てる方法](/media/copilot-license-assign/)の最後の節）、配り直すのか、契約を減らすのかを分けて決めます（料金は[Microsoft 365 Copilotの公式ページ](https://www.microsoft.com/ja-jp/microsoft-365/copilot)で確かめてください）。

配り直す先の候補は準備状況レポートの「Copilot のおすすめユーザー」の列に出ます。**ライセンスを持っていない人のうち、過去28日のOutlook・Teams・Wordなどの使い方が多い上位25%に、毎週印が付きます。**25%の中での順位は付かず、Copilotのライセンスを買った会社だけが使える機能です。Microsoftはこのデータを社員の評価に使うものではないと明記しています。

<figure class="post-figure"><img src="/media/images/copilot-adoption/cadp_07_candidates.png" alt="Microsoft Learn の Copilot の候補者列の追加情報。ライセンスの無い利用者のうち使い方が多い上位25%に印が付く" loading="lazy"><figcaption>Copilot の候補者列の説明（Microsoft Learn）</figcaption></figure>

Copilot ダッシュボードの準備ページにも、無料のCopilot Chatをよく使っている人をライセンスの候補と考える、という推奨カードがあります。Microsoftの説明では、Copilot Chatをよく使う人ほどライセンスを持ったときにCopilotから価値を引き出せるとされています。

数字を出すのは管理者でも、誰から外して誰に回すかは部署の業務を知る人でないと決められません。**管理者は止まっている人の一覧と候補の一覧を出し、配り直しは推進の担当と部門の責任者で決める、と役割を分けておくと話が早く進みます。**レポートを見るだけなら、グローバル管理者でなくレポート閲覧者のロールで足ります。名前を出す設定を変えられるのは全体管理者です。

## 経営に報告する数字

利用率だけを出しても、投資に見合ったかの議論にはなりません。Viva インサイトの「[Microsoft Copilot ダッシュボード](https://learn.microsoft.com/ja-jp/viva/insights/org-team-insights/copilot-dashboard)」は、準備・導入・影響・センチメントの4つの切り口で数字を出します。**見る人に有料のViva インサイトのライセンスやCopilotのライセンスは要りません。**ただしデータの処理には、テナントにCopilotのライセンスが1つ以上か、Viva インサイトのライセンスが50以上要ります。データは過去28日分で、最大6日の遅れがあり、ライセンスを割り当ててから処理が始まるまでは最大7日です。

| 指標 | 中身 | 報告で気をつけること |
|---|---|---|
| アクティブなCopilot ユーザー | 28日間にどれかのアプリで1回以上使った人 | 管理センターの数とは対象の人と期間が違う |
| Copilot アシスト時間 | Copilotの操作の数に、Microsoftの調査に基づく係数を掛けた時間 | 実測ではなく推定 |
| Copilot アシストバリュー | アシスト時間に時給を掛けた額 | 時給の既定は72ドル。自社の数字に替える |
| 満足度 | 回答へのサムアップの割合 | 押した人の反応だけを数える |

<figure class="post-figure"><img src="/media/images/copilot-adoption/cadp_08_dashboard.png" alt="Microsoft Learn の Copilot ダッシュボードのアシストバリューの説明。時給の既定は72ドルで設定から変えられる文を赤枠で囲んでいる" loading="lazy"><figcaption>アシストバリューの時給の既定（Microsoft Learn）</figcaption></figure>

アシスト時間を漏れなく出すには、オプションの診断データを有効にしておく必要があります。**時給の既定は米国労働統計局のデータに基づく72ドルで、自社の人件費とは合わないため、報告の前に設定で自社の時給と円に替えてください。**

自動で見られるのは一部の人だけです。Entra IDの利用者が2,500人以上で、大半の人が1つのレポートライン（同じ経営者の下の系統）に入っている会社では、上位3階層にいて部下の多い人に、自動でダッシュボードが表示されます。部門の管理者は自分のチームの導入と影響を見られるため、部署ごとの振り返りに使えるのが利点です。

<figure class="post-figure"><img src="/media/images/copilot-adoption/cadp_02_report.png" alt="管理センターの使用状況レポートは担当が毎週見る数字、Copilot ダッシュボードは経営に出す数字、という使い分けの図" loading="lazy"><figcaption>使用状況レポートと Copilot ダッシュボードの使い分け</figcaption></figure>

## 社内で先に決めておくこと

レポートもダッシュボードも、見る人と見方が決まっていないと開かれなくなります。推進を始める前か立て直す前に、次の5つを社内で決めておくと迷いが減ります。

- 数字を見る人と、その人に付けるロール
- 使用状況レポートに名前を出すかどうか
- 見る期間（28日など）と見る間隔
- 組織のメッセージを出す相手と頻度
- AI 使用ポリシーの置き場と、オンボードに入れるかどうか

ライセンスの種類ごとの違いは「[Copilotの使い方を解説](/media/copilot-guide/)」、無料のCopilot Chatを止める・絞る設定は「[Copilot Chatを社内で止める方法](/media/copilot-chat-admin-block/)」の記事で扱いました。

## よくある質問

### Copilotの使用状況はどこで確認できますか？
Microsoft 365 管理センターの［レポート］＞［使用状況］で［Microsoft Copilot］＞［Copilot］を選び、［使用状況］タブを開きます。期間の選択肢は7日・28日・90日・180日の4つです。

### Copilotのアクティブ ユーザーは何を数えていますか？
Copilotのライセンスを持つ人のうち、期間中にどれかのアプリでCopilotの機能に意図的な操作をした人です。ウィンドウを開いただけでは数えず、プロンプトを送ると数えます。

### Copilotのレポートで名前が出ないのはなぜ？
既定ではすべてのレポートでユーザー名や表示名が隠れているためです。［設定］＞［組織の設定］＞［サービス］＞［レポート］で、非表示にするチェックを外すと出ます。

### Copilotを使っていない人に通知を送れますか？
送れます。使用状況レポートの推奨カードから組織のメッセージを出すと、30日間使っていない人にWindowsの通知で、Copilotのライセンスを持つTeamsの新しい利用者で30日以内にTeamsのCopilotを使っていない人にはTeamsの中の表示で届きます。受信者の絞り込みはMicrosoft 365 グループ単位です。

### Copilotのライセンスを誰に回すかはどう決めますか？
手がかりは準備状況レポートの「Copilot のおすすめユーザー」の列です。ライセンスの無い人のうち、Microsoft 365 アプリをよく使う上位25%に毎週印が付きます。最終的な判断は部署の業務を知る人と一緒に行うのが確実です。

### Copilot ダッシュボードは有料ですか？
見る人に有料のViva インサイトのライセンスやCopilotのライセンスは要りません。ただしデータの処理には、テナントにCopilotのライセンスが1つ以上か、Viva インサイトのライセンスが50以上要ります。ベンチマークやエージェントの分析など一部の機能は、Copilotのライセンス数や有料のViva インサイトの有無で使えるかが変わります。

### Copilotの2つのレポートで数が違うのはなぜ？
アクティブの定義は同じでも、対象に含める人と期間が違うためです。ダッシュボードは28日分で最大6日遅れるため、管理センターの同じ日の数字とはずれます。

### Copilotの利用は監査ログから集計できますか？
集計はできますが、Microsoftは監査ログを使用状況レポートの土台として使う想定ではないとしています。公式のレポートと数が一致しない場合があるため、社内の報告は管理センターかダッシュボードの数字にそろえます。

## 出典

- Microsoft Learn「[Microsoft Copilot の使用状況レポート](https://learn.microsoft.com/ja-jp/microsoft-365/admin/activity-reports/microsoft-365-copilot-usage)」（2026年10月19日取得）
- Microsoft Learn「[Microsoft Copilot 準備状況レポート](https://learn.microsoft.com/ja-jp/microsoft-365/admin/activity-reports/microsoft-365-copilot-readiness)」（同）
- Microsoft Learn「[Microsoft 365 管理センターのアクティビティ レポート](https://learn.microsoft.com/ja-jp/microsoft-365/admin/activity-reports/activity-reports)」（同）
- Microsoft Learn「[Microsoft Copilot を使用して導入を促進する 使用状況レポート 組織のメッセージング](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/track-copilot-adoption)」（同）
- Microsoft Learn「[Microsoft 365 の顧客向けの Microsoft Copilot ダッシュボードに接続する](https://learn.microsoft.com/ja-jp/viva/insights/org-team-insights/copilot-dashboard)」（同）
- Microsoft Learn「[IT 管理者向け Microsoft Copilot 導入ガイドと概要](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/microsoft-365-copilot-enablement-resources)」（同）
- Microsoft Learn「[Microsoft Copilot オンボードを管理する (Frontier)](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/manage-copilot-onboarding)」（同）
- Microsoft 導入サイト「[Copilot Success Kit](https://adoption.microsoft.com/ja-jp/copilot/success-kit/)」（同）
- Microsoft 導入サイト「[シナリオ ライブラリ](https://adoption.microsoft.com/ja-jp/scenario-library/)」（同）
- Microsoft 導入サイト「[チャンピオン プログラム](https://adoption.microsoft.com/ja-jp/become-a-champion/)」（同）
