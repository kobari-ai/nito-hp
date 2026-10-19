---
title: 【2026年10月】Copilot Studioの料金を解説｜M365 Copilotの範囲・作れる人
date: 2026-10-20
category: AI活用
description: Microsoft Copilot Studioの料金を価格ページとライセンスガイドから解説。25,000クレジットのパック・従量課金・事前購入の違い、M365 Copilotで追加費用なく作れる範囲、作れる人の決め方まで。
cover_tag: 導入担当向け
cover_headline: Copilot Studioの料金
cover_sub: M365 Copilotで足りる範囲・作れる人
cta: ai_agent
---

Copilot Studioの課金の単位は、2025年9月1日に「メッセージ」から「Copilotクレジット」に変わりました。1パックに入る量と従量課金の単価はそのままですが、今の価格ページではハーネスという実行の仕組みによってクレジットがかかるかどうかが分かれています。

社内でエージェントを作る話が出ると、担当者はいくらかかるかとMicrosoft 365 Copilotで足りるかを聞かれます。この記事は2026年10月20日に取得した価格ページとMicrosoft Learnをもとに、払い方・追加費用なしの範囲・作れる人・作る前の決めごとを扱います。購入と管理画面の操作は試していません。

:::takeaways
- **Copilot Studioは1パック月29,985円で25,000クレジット**。ほかに後払いの従量課金と1年分の事前購入がある
- **Microsoft 365 Copilotのライセンスを持つ社員が社内で使うエージェントは追加費用なし**。社外への公開とGitHub Copilotハーネスはクレジットがかかる
- **作る人には無料のユーザーライセンスか作成者の役割が要る**。試用版で作ったエージェントは公開できない
:::

<!-- SHOT: 01_fig_pay.png｜HTML図（brain/scripts/seo/fig/cstd_pay.html）。払い方3通りを縦に3段｜幅640・DPR2｜赤枠なし -->

## Copilot Studioとエージェント ビルダー

Microsoft 365 Copilotを入れた会社には、エージェントを作る入口が2つあります。Copilotのアプリの中で開くエージェント ビルダーと、専用の画面で開くCopilot Studioです。Microsoft Learnの「[エージェント ビルダーと Copilot Studio のどちらかを選択してエージェントを構築します](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/copilot-studio-experience)」（2026年9月30日更新）は、使う相手・共有する広さ・できること・管理の細かさで選ぶよう書いています。

| | エージェント ビルダー | Copilot Studio |
|---|---|---|
| 開く場所 | Microsoft 365 Copilotのアプリ | Copilot Studio |
| 作る人 | 一般の社員 | 作成者と開発者 |
| 使う相手 | 自分か小さなチーム | 部署・組織全体・社外の顧客 |
| 向くもの | 社内の資料に答えるQ&A | 複数の手順・承認・業務システムとの連携 |
| 管理する場所 | Microsoft 365 管理センター | Power Platform 管理センター |

**料金の見積もりが要るのは主にCopilot Studioのほうで、エージェント ビルダーで作ったものは後からCopilot Studioへコピーして機能を足せます。** [エージェント ビルダーの概要](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/agent-builder)によると、エージェント ビルダーは外部のサービスを呼ぶアクションを作れません。業務システムにつなぐ段になったら、コピーしてCopilot Studioで続きを作る流れです。

<!-- SHOT: 02_learn_compare.png｜Learn「エージェント ビルダーと Copilot Studio のどちらかを選択」の機能の比較表（アクセス ポイント〜エージェントの種類の行）｜https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/copilot-studio-experience｜PC｜赤枠 1: エージェントの対象者の行 -->

## 料金の払い方は3通り

[Microsoft Copilot Studio プランと価格](https://www.microsoft.com/ja-jp/microsoft-365-copilot/pricing/copilot-studio)のページは、払い方を3つ並べています。**Copilot Studioはテナント（会社の契約）全体で買うもので、1人ごとの月額はありません。**

| 払い方 | 中身 | 向く場面 |
|---|---|---|
| 容量パック | 1パック月29,985円で25,000クレジット。余りは翌月に繰り越さない | 毎月の量がだいたい読める |
| 従量課金 | 使った分を月末に後払い。Azureのサブスクリプションが要る | 始めたばかり・月ごとの差が大きい |
| 事前購入プラン | 1年分を前払い。最大20%安く、余りは1年の終わりに失効 | 年間の量が大きい |

従量課金の単価は、英語の[Microsoft Copilot Studio licensing guidance](https://www.microsoft.com/licensing/guidance/Microsoft-Copilot-Studio)で1クレジット0.01ドルです。円の単価はMicrosoftが公開している[Azure Retail Prices API](https://learn.microsoft.com/ja-jp/rest/api/cost-management/retail-prices/azure-retail-prices)で1.5755円と出ました。容量パックを1クレジットあたりに直すと約1.2円になるので、**同じ量を使うなら従量課金は容量パックより3割ほど高くつきます**（ドル建てでは25%）。

<!-- SHOT: 03_pricing_plans.png｜価格ページの「ニーズに適した Copilot Studio プランを見つける」の3枚のカード｜https://www.microsoft.com/ja-jp/microsoft-365-copilot/pricing/copilot-studio｜PC｜赤枠 1: ¥4,497 ／ 2: 事前購入プランの「最大 20% 削減」 -->

事前購入プランは、1 CCCU（Copilotクレジット コミット ユニット）が1ドル・100クレジットに当たります。ライセンスガイドの表は3,000 CCCUで2,850ドル（5%引き）から3,000,000 CCCUで2,400,000ドル（20%引き）までの9段で、いちばん下の段が容量パック1つの12か月分です。容量パックで足りない分を従量課金で受ける組み合わせもでき、その場合はパックを使い切るまで従量課金の請求は出ません。

無料で試すなら、Copilot Studioの試用版かAzureの無料アカウントを使います。試用版は社員が個人でサインアップでき、期間の終わりに30日延長できます。Azureの無料アカウントに付く29,985円分のクレジットも、エージェントの作成に使えると価格ページにありました。

## クレジットの減り方

**クレジットはエージェントの動きごとに減り方が違い、社内データを引いて答えると1回で12クレジットを使います。** Learnの「[請求レートと管理](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/requirements-messages-management)」（2026年8月3日更新）の主な単価は次のとおりです。

| 動き | 減るクレジット | M365 Copilotのライセンスを持つ人 |
|---|---|---|
| 従来型の回答（作成者が書いた決まった返事） | 1 | 無料 |
| 生成回答 | 2 | 無料 |
| エージェントのアクション | 5 | 無料 |
| テナントグラフでの根拠付け | 10 | 無料 |
| エージェントフロー（100アクションあたり） | 13 | 無料 |
| AIツールのプレミアム（10回答ごと） | 100 | 無料 |

社内データ（Microsoft Graph）を引いて答えると、テナントグラフの10と生成回答の2を足して1回12クレジットです。推論モデルを使う場合はこの単価に1,000トークンあたり10クレジットが上乗せされます。

<!-- SHOT: 04_learn_rates.png｜Learn「請求レートと管理」の Copilot クレジットの課金レートの表｜https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/requirements-messages-management｜PC｜赤枠 1: 生成回答 2 Copilot クレジット ／ 2: テナント グラフの基盤設定 10 Copilot クレジット -->

Learnには課金の例が3つ載っています。そのうちWebサイトの顧客サポートのエージェントは、1回の会話で従来型の回答4つと生成回答2つを使い、1日900人で7,200クレジットという見積もりです。**これを30日続けると216,000クレジットになり、容量パック8つに従量課金を足す組み合わせで月26万5千円ほどです**（こちらの試算。パック9つなら269,865円、全部を従量課金にすると約34万円）。

もう1つの例の社内の営業データに答えるエージェントでは、使う150人のうちM365 Copilotのライセンスを持つ50人の分は数えず、残りの100人の分だけで1日4,800クレジットと見積もっています。**同じエージェントでも、使う人がライセンスを持つかどうかで費用が変わります。**

消費量はMicrosoftの[Copilot Studio Agent Usage Estimator](https://microsoft.github.io/copilot-studio-estimator/)で見積もれます。エージェントの種類・使う人の数・ナレッジ・ツールを選ぶと、月のクレジットの目安が出ます（こちらでは操作していません）。

## M365 Copilotで足りる範囲

Microsoft 365 Copilotは、価格ページで1ユーザー月4,497円相当（年払い・税抜）です。価格ページのFAQによると、**このライセンスを持つ人はMicrosoft 365の中で使う社内のエージェントを、追加費用なしで作って使えます**。英語の[Copilot Credits licensing guidance](https://www.microsoft.com/licensing/guidance/Copilot-Credits)では、この無料の扱いに公正利用の上限（fair usage limits）が付いています。

| 場面 | 費用 |
|---|---|
| ライセンスを持つ社員がTeams・SharePoint・Copilot Chatでエージェントを使う | 追加なし（公正利用の上限あり） |
| ライセンスを持たない社員が社内データを読むエージェントを使う | クレジットが減る |
| Webサイト・アプリ・SNSなど社外に公開する | Copilot Studioの契約が要る |
| GitHub Copilotハーネスで作ったエージェントとワークフロー | クレジットが減る |
| 画面を操作するエージェント（CUA） | M365 Copilotに含まれない |

エージェントフローが無料になるのは、エージェントがフローを呼ぶトリガーで動く場合だけです。スケジュールなど別のトリガーで動くフローには通常の単価がかかります。

<!-- SHOT: 05_fig_included.png｜HTML図（brain/scripts/seo/fig/cstd_included.html）。追加費用なしの範囲とクレジットが減る場面を縦に2段｜幅640・DPR2｜赤枠なし -->

### ハーネスで変わる課金

Copilot Studioで作るものは、どれもハーネスと呼ぶ実行の仕組みの上で動きます。Learnの「[Copilot Studio のハーネス](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/harnesses-overview)」（2026年10月1日更新）は3種類を挙げ、使うハーネスで請求の内容が変わると書いています。

| ハーネス | 向くもの | M365 Copilotのライセンスとの関係 |
|---|---|---|
| 標準ハーネス | 決めたトピックとルールに沿って答えるエージェントとフロー | Microsoftのチャネルでの実行は含まれる |
| Copilot Chatハーネス | 社内の知識をCopilot Chatにつなぐ | 含まれる |
| GitHub Copilotハーネス | 目標を手順に分けて進める長い作業。Word・Excel・PDFも作る | クレジットが要る |

GitHub Copilotハーネスは名前にGitHubと付きますが、Copilot Studioの中の仕組みです。Learnによると、Copilot Studioでエージェントが動くときに顧客のデータはGitHub Copilotのサービスに送られません。**社内のQ&Aや決まった手順の受付なら標準ハーネスで足り、書類を作る長い作業を任せる段からクレジットの見積もりが要ります。**

<!-- SHOT: 06_learn_harness.png｜Learn「Copilot Studio のハーネス」のハーネスの比較の表｜https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/harnesses-overview｜PC｜赤枠 1: 最適な用途の行 ／ 2: 請求書の行 -->

## 作れる人の決め方

**Copilot Studioのエージェントを使う人にライセンスは要りませんが、作る人には権限が要ります。** Learnの「[ユーザー ライセンスの割り当ておよびアクセスの管理](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/requirements-licensing)」によると、容量パックで買った会社は、テナントのライセンスとは別に作る人ごとにCopilot Studio ユーザー ライセンスを割り当てます。このユーザーライセンスは無料で、ライセンスガイドの価格も0ドルです。

従量課金か事前購入プランで買った場合は、Power Platform 管理センターの設定でCopilot Studioの作成者にセキュリティグループを割り当て、そのグループの人だけが作れるようにします。M365 Copilotのライセンスを持つ人は、そのライセンスのままMicrosoft 365向けのエージェントを作れます。

| 作る人の条件 | 公開 |
|---|---|
| Copilot Studio ユーザー ライセンス | できる |
| 作成者の役割（セキュリティグループ） | できる |
| Microsoft 365 Copilotのライセンス | Microsoft 365の中ならできる |
| 試用版 | できない（テストのチャットまで） |

試用版は社員が自分でサインアップできるため、管理者が知らないうちに作り始めている場合があります。管理者は組織の設定（AllowAdHocSubscriptions）で自分でのサインアップを止められます。テナントのゲストユーザーはCopilot Studioに入れません。M365 Copilotのライセンスそのものの配り方は[Copilotのライセンスを割り当てる方法](/media/copilot-license-assign/)にまとめています。

<!-- SHOT: 07_learn_trial.png｜Learn「ユーザー ライセンスの割り当ておよびアクセスの管理」の試用版プランの節｜https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/requirements-licensing｜PC｜赤枠 1: AllowAdHocSubscriptions の文 ／ 2:「エージェントを公開することはできません」 -->

## 作る前に社内で決めること

料金の表を読んでも、使う相手とデータが決まらないと金額は出ません。

### 社員だけか社外にも出すか

**社員がM365 Copilotのライセンスで使う範囲に収まるなら、Copilot Studioを追加で買わずに始められます。** Webサイトの問い合わせ窓口のように社外の人が使うなら、Copilot Studioの契約とクレジットの見積もりが先になります。

### どのデータを読ませるか

エージェント ビルダーで作ったエージェントは使う人のアクセス権の範囲で答えるため、その人が開けないSharePointのファイルは答えに出ません。逆に、権限が広すぎるフォルダーをナレッジに入れると、そこを開ける人の答えには中身がそのまま出ます。エージェント ビルダーで組織の全員に共有しても、ナレッジのファイルの権限は自動では広がらず、特定のセキュリティグループに共有するときだけ自動で付きます。

### 上限をどこで止めるか

前払いの容量を使い切っても、その場では止まりません。**テナントの消費が前払い分の125%に達するとカスタムのエージェントが止まり、使う人には「このエージェントは現在使用できません。使用制限に達しました。」と返ります。** 指定した管理者にはメールが届き、Power Platform 管理センターにも通知が出ます。

止めたくない環境に従量課金をつないでおけば、超過分はAzureの請求に回るため止まりません。Power Platform 管理センターではエージェントごとに月の上限を決められるため、試しに作ったエージェントが本番の枠を使い切る事態を防げます。

<!-- SHOT: 08_learn_enforcement.png｜Learn「請求レートと管理」の超過分への対応（125%）と強制施行された後のエージェントの動作の節｜https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/requirements-messages-management｜PC｜赤枠 1:「前払いキャパシティの 125% に達すると」 ／ 2:「使用制限に達しました」 -->

## 自社で作るか外に頼むか

**社内のQ&Aや申請の受付を標準ハーネスで作るなら、自社の担当者で回せる範囲です。** エージェント ビルダーから始め、足りなくなったらCopilot Studioへコピーする順で進めれば、作り直しも出ません。

外の手を借りるかを考えるのは、社外向けに公開するとき、Microsoft 365の外の業務システムにプレミアムやカスタムのコネクタでつなぐとき、GitHub Copilotハーネスで複数の手順を任せるときです。この3つはクレジットの見積もりと、環境やデータ損失防止（DLP）のポリシーの設計が毎月の費用に響きます。ライセンスガイドも、業種向けや独自の作り込みが要る場合の買い方として、Microsoftのパートナーに設計から運用まで任せる経路を挙げています。作り方の選び方そのものは[AIエージェントの作り方](/media/ai-agent-build/)で比べています。

<!-- SHOT: 09_fig_decide.png｜HTML図（brain/scripts/seo/fig/cstd_decide.html）。作る前に決める3つと自社か外部かの線を縦に4段｜幅640・DPR2｜赤枠なし -->

## よくある質問

### Copilot Studioは無料で使えますか？

試用版とAzureの無料アカウントのクレジットで試せます。試用版で作ったエージェントは公開できません。M365 Copilotのライセンスを持つ社員がMicrosoft 365の中で使うエージェントは、追加費用なしで作れます。

### Copilot Studioの料金は1ユーザーいくらですか？

1人ごとの月額はありません。テナント全体で容量パック（月29,985円で25,000クレジット）・従量課金・事前購入プランのどれかを買い、作る人には無料のユーザーライセンスか作成者の役割を割り当てます。

### Copilot Studioのクレジットは繰り越せますか？

容量パックの余りは翌月に繰り越せません。事前購入プランは1年のうちならいつ使ってもよく、1年の終わりに残りが失効します。

### Copilot Studioはクレジット切れで止まりますか？

前払い分の125%に達するとカスタムのエージェントが止まります。進行中の会話は最後まで続き、容量を足すか翌月に戻るまで新しい会話は受け付けません。従量課金をつないだ環境は止まらず、超過分がAzureの請求に回ります。

### Copilot Studioの利用にライセンスは要りますか？

使う人に特別なライセンスは要りません。ただしM365 Copilotのライセンスを持たない人が社内データを読むエージェントを使うと、その分のクレジットが減ります。

### Copilot Studioのメッセージとは何ですか？

2025年9月1日に、単位の名前がメッセージからCopilotクレジットに変わりました。Learnによると、1パックに入る量と従量課金の単価は変わっていません。古い記事にあるメッセージの数は、クレジットの数として読み替えられます。

### Copilot Studioのエージェント ビルダーとは？

エージェント ビルダーはMicrosoft 365 Copilotのアプリの中で、自分や小さなチーム向けのQ&Aを作る入口です。部署全体や社外に出すときや業務システムにつなぐときにCopilot Studioを使い、作ったものはCopilot Studioへコピーできます。

### Copilot StudioはTeamsだけで使えますか？

一部のMicrosoft 365のプランに付くTeams向けのCopilot Studioでは、従来型のオーケストレーションでTeamsに公開するエージェントを作れます。生成オーケストレーションやプレミアムのコネクタは使えないため、使うにはCopilot Studioの契約に上げます。

## 出典

いずれも2026年10月20日に取得。

- [Microsoft Copilot Studio プランと価格](https://www.microsoft.com/ja-jp/microsoft-365-copilot/pricing/copilot-studio)（Microsoft。容量パック・従量課金・事前購入プラン・M365 Copilotの価格・FAQ）
- [Microsoft Copilot Studio licensing guidance](https://www.microsoft.com/licensing/guidance/Microsoft-Copilot-Studio)（Microsoft、英語。従量課金の単価・事前購入プランの9段・ユーザーライセンス・作成者の役割）
- [Copilot Credits licensing guidance](https://www.microsoft.com/licensing/guidance/Copilot-Credits)（Microsoft、英語。ハーネスごとの扱いと公正利用の上限）
- [標準ハーネスライセンス](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/billing-licensing)（Microsoft Learn。単位の変更・試用版は公開できない・M365 Copilotに含まれる機能）
- [請求レートと管理](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/requirements-messages-management)（Microsoft Learn。課金レート・課金の例・125%での停止）
- [Copilot Studio のハーネス](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/harnesses-overview)（Microsoft Learn。3種類のハーネスの違い）
- [ユーザー ライセンスの割り当ておよびアクセスの管理](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/requirements-licensing)（Microsoft Learn。テナントとユーザーのライセンス・試用版・ゲスト）
- [Copilot Studio Standard ハーネスにアクセスする](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/requirements-licensing-subscriptions)（Microsoft Learn。試用版の延長・Teams向けのプラン）
- [エージェント ビルダーと Copilot Studio のどちらかを選択してエージェントを構築します](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/copilot-studio-experience)（Microsoft Learn。2つの比較とコピー）
- [エージェント ビルダーの概要](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/agent-builder)（Microsoft Learn。アクションの制限・SharePointの共有）
- [Azure Retail Prices API](https://learn.microsoft.com/ja-jp/rest/api/cost-management/retail-prices/azure-retail-prices)（Microsoft Learn。従量課金の円の単価を引いたAPI）
- [Copilot Studio Agent Usage Estimator](https://microsoft.github.io/copilot-studio-estimator/)（Microsoft。消費の見積もり）
