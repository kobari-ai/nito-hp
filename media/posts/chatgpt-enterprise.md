---
title: 【2026年10月】ChatGPT Enterpriseとは？Businessとの違い・料金・何人から
date: 2026-10-10
category: AI活用
description: ChatGPT EnterpriseとBusinessの違いを公式の比較表で整理。料金が非公開であること、何人から契約できるか、SCIM・監査ログ・データ保持など管理機能の差、営業への申し込み手順まで。
cover_tag: 法人
cover_headline: ChatGPT Enterpriseとは
cover_sub: Businessとの違い・料金・申し込み
---

ChatGPT Enterpriseは、OpenAIの[料金ページ](https://chatgpt.com/ja-JP/pricing)で「カスタム価格設定」と書かれた法人向けのプランです。Businessのように画面から申し込むことはできず、営業チームへの問い合わせから始まります。2026年10月10日時点で、1人あたりの金額はどの公式ページにも載っていません。

検討する側が迷うのは日本語の解説記事に出回っている「1人月60ドル」「150席から」という数字です。**この2つはOpenAIの料金ページにもヘルプにも見当たらず、公式に書かれているのは「Businessは1契約200席まで」と「企業向けプランは2名から」の2点です。**この記事は2026年10月10日に取得した料金ページの比較表とヘルプセンターをもとに、Businessとの違い・人数の考え方・申し込みの手順を整理します。

:::takeaways
- **Enterpriseの料金は公開されていない**。料金ページは「カスタム価格設定」で、クレジット制とトークン制の2つの体系がある
- 1契約で**有料の席が200を超えるならEnterprise**。Businessの上限は200席で、サポートに頼んでも増やせない
- SAML SSOとドメイン認証はBusinessにもある。**SCIM・ロールベースのアクセス制御・Compliance API・IP許可リスト・データレジデンシーはEnterpriseだけ**
- 申し込みは**営業への問い合わせフォームで製品に「ChatGPT Enterprise」を選ぶ**。日本ではNTTデータも販売代理店になっている
- Businessのワークスペースは、**データを残したままEnterpriseに上げられる**（営業経由）
:::

<figure class="post-figure"><img src="/media/images/chatgpt-enterprise/01_fig_overview.jpg" alt="ChatGPT BusinessからEnterpriseへの違いを示した概要図。左の箱にBusinessと200席まで、右の箱にEnterpriseとSCIMと監査ログと料金は個別見積もりが書かれ、左から右へ矢印でつながっている" loading="lazy"><figcaption>BusinessとEnterpriseの関係（OpenAIの料金ページとヘルプから作成）</figcaption></figure>

## ChatGPT Enterpriseとは

OpenAIのヘルプ「[ChatGPT Enterprise とは何ですか？](https://help.openai.com/ja-jp/articles/8265053)」は、Enterpriseを組織向けに管理されたプランと説明しています。**組織単位で購入するプランなので、個人がEnterpriseに直接サインアップすることはできません。**社員はワークスペースの所有者か管理者から招待されるか、会社のIDシステムから自動で登録されて使い始めます。

ワークスペースは個人のChatGPTとは分かれていて、会社が統合を求めない限り個人のチャットは移りません。統合を求められると個人のチャットやファイルが会社の管理下に入り、元には戻せません。個人で払っていた有料プランは、Enterpriseに移ると自動で解約され、使っていない期間の分が一部返金されます。

ChatGPTの契約とAPIの契約は別物です。**Enterpriseのワークスペースに入っても、APIプラットフォームの組織には自動で入りません。**開発でAPIを使うなら、API側の管理者に別に追加してもらう必要があります。

## 料金は公開されていない

料金ページのビジネス・エンタープライズ向けタブでは、Businessの標準シートが1人月3,050円（年額課金、月額課金なら3,850円）と円で出ています。Enterpriseの欄は「カスタム価格設定」で、金額の代わりに置かれているのは営業への問い合わせボタンです。

<figure class="post-figure post-figure--sp"><img src="/media/images/chatgpt-enterprise/02_pricing_sp.jpg" alt="ChatGPT公式の料金ページのビジネス・エンタープライズ向けタブをスマホで開いた画面。Enterpriseの欄にカスタム価格設定とエンタープライズ向け料金については営業チームにお問い合わせくださいという注記、含まれる内容の最後に請求書発行と請求管理とボリューム割引が書かれ、2か所を赤枠で囲んでいる" loading="lazy"><figcaption>ChatGPTの料金ページ（2026年10月10日、スマホ表示）</figcaption></figure>

欄の注記には、Enterpriseでは**クレジットベースとトークンベースの2つの料金体系を選べる**と書かれています。ヘルプによると、クレジットベースの契約では席に基本の利用枠が含まれ、それを超える分はワークスペースのクレジットを買って使います。2026年4月にはCodexだけを使う「Codexシート」も加わりました。こちらは1人あたりの月額の固定費がない、利用量に応じた席です。

料金ページの説明にはほかに、請求書の発行とボリューム割引があります。同じページのFAQによると、非営利団体はBusinessとEnterpriseを最大75%割引で使えます。

### 出回っている60ドルと150席

**「1人月60ドル・最低150席・年間契約」は、2026年10月10日時点の公式ページには載っていない数字です。**検索上位の日本語の解説記事を7本読むと、そのうち3本がこの数字を目安や条件として載せていました。海外の解説記事でも、購入した企業の報告をもとにした値だと断ったうえでの紹介でした。

見積もりの金額は席の数や契約期間で変わるので、予算を組むならこの数字を前提にせず、営業から見積もりを取るのが確実です。

## 何人から契約できるか

公式に書かれている人数の条件は2つだけです。料金ページのFAQは「企業向けプランは、ユーザー2名からご利用いただけます」とし、BusinessとEnterpriseをまとめて企業向けプランと呼んでいます。Enterpriseだけの最低席数は料金ページにもヘルプにも書かれていないため、見積もりの段階で営業に確かめる項目です。

もう1つは上限で、ヘルプの「[ChatGPT Business：一般FAQ](https://help.openai.com/ja-jp/articles/8542115-chatgpt-business-general-faq)」に、2026年8月24日以降は1つのBusinessの契約で有料の席が合計200席までとあります。**サポートチームは席数の上限を変えられないため、200席を超えて使うならEnterpriseを検討する**ことになります。

200席を超える会社だけがEnterpriseの対象というわけでもありません。Businessの概要のヘルプには、請求書払い・銀行振込・ゼロデータ保持・BAAなどが要るなら、セルフサービスのBusinessではなく契約ベースのサービスを使うよう書かれています。人数が少なくても、こうした条件があれば営業に相談する形です。Businessの料金と席の仕組みは[ChatGPT Businessの記事](/media/chatgpt-business/)にまとめています。

## Businessとの違い

料金ページの「各プランの機能を比較」は、BusinessとEnterpriseの2列で、チェックの有無がアイコンで示されています。2列で違う行だけを抜き出すと、次の表のようになります。

<figure class="post-figure"><img src="/media/images/chatgpt-enterprise/03_compare.jpg" alt="ChatGPT公式の料金ページの機能比較表のセキュリティと管理の部分。ISO認証、SCIM、エンタープライズキー管理、きめ細かなGPTコントロールとグループ権限、ロールベースのアクセス制御の行と、Compliance APIログプラットフォーム、IP許可リスト、10地域のデータレジデンシーの行で、Businessの列がダッシュ、Enterpriseの列がチェックになっている部分を赤枠で囲んでいる" loading="lazy"><figcaption>料金ページの機能比較表（2026年10月10日）</figcaption></figure>

| 項目 | Business | Enterprise |
|---|---|---|
| SAML SSO・ドメイン認証・管理コンソール | あり | あり |
| SOC 2 Type 2 | あり | あり |
| ISO 27001・27017・27018・27701 | なし | あり |
| SCIM・ロールベースのアクセス制御 | なし | あり |
| エンタープライズキー管理（EKM） | なし | あり |
| Compliance APIのログ・IP許可リスト | なし | あり |
| 10地域のデータレジデンシー | なし | あり |
| グローバル管理コンソール・コネクターレジストリ | なし | あり |
| 専任サポートによる導入支援・カスタムのセキュリティレビュー | なし | あり |
| GPT Instantで一度に読ませられる量 | 約40ページ分 | 約250ページ分 |

GPT Instantの文脈の上限はBusinessが54K、Enterpriseが128Kです。推論モデルのほうはどちらも256K（約320ページ分）で差がありません。このほか、iOS用のIntune・ブランド付きワークスペースもEnterpriseの列だけにチェックがあります。

### SSOはBusinessにもある

SSOの有無でプランを分けたくなりますが、**比較表ではSAML SSOとドメイン認証はBusinessにもチェックが付いています。**Businessに無いのはSCIMのほうです。SCIMのヘルプ（[SCIM プロビジョニングと管理](https://help.openai.com/ja-jp/articles/10011769)）は、単体のBusinessにはSCIMが含まれないとしています。

ログインの方法を受け持つのがSSOで、社員の追加と削除をIDプロバイダーから同期するのがSCIMです。入社や退職のたびに管理画面で手で追加・削除するのを避けたいなら、Enterpriseが必要です。ヘルプが対応先として挙げているのは、Okta・Microsoft Entra ID・Google Workspace・PingFederate・OneLogin・Ripplingです。

### データ保持と監査ログ

[エンタープライズプライバシー](https://openai.com/ja-JP/enterprise-privacy/)のページは、Enterpriseのデータの保持期間はワークスペースの管理者が決められるとしています。削除した会話は、法律で保持が求められない限り30日以内にOpenAIのシステムから消えます。BusinessのFAQにも管理者が保持期間を設定できるとあり、料金ページでは「カスタムのデータ保持ポリシー」がEnterpriseの欄に並んでいます。

監査ログはEnterpriseの差が大きいところです。**Enterpriseの管理者はCompliance APIを通じて、会話やGPTの監査ログを取り出し、eディスカバリー・DLP・SIEMのツールに渡せます。**ヘルプ「[Enterprise および Edu のお客様向け OpenAI コンプライアンスプラットフォーム](https://help.openai.com/ja-jp/articles/9261474-compliance-apis-for-enterprise-customers)」によると、ログが残るのは30日間です。それより長く残すなら、自社のシステムで続けてダウンロードして保管する必要があります。

### データを日本に保存できる

会話・ファイル・メモリ・カスタムGPTなどを決めた地域に保存する機能がデータレジデンシーです。ヘルプ「[ChatGPT のデータレジデンシーと推論レジデンシー](https://help.openai.com/ja-jp/articles/9903489-data-residency-and-inference-residency-for-chatgpt)」の対応地域には日本が入っています。

**対象は新しく導入するEnterpriseとEduの顧客と書かれているため、日本に置きたいなら契約の段階で営業に伝えておく**必要があります。ワークスペース設定の［一般］に出る地域は確認用の表示で、そこから変えることはできません。外部のアプリやウェブ検索を通じたデータは、選んだ地域の外で扱われることがあるとも書かれています。

## Enterpriseにするかの目安

<figure class="post-figure"><img src="/media/images/chatgpt-enterprise/05_fig_when.jpg" alt="BusinessとEnterpriseの選び方を2列で示した図。Businessは自分で申し込む、有料の席が200まで、SAML SSOとドメイン認証で足りる、カードで払える、今日から使い始めたい。Enterpriseは営業に問い合わせる、200席を超える、SCIMで社内の名簿と同期、監査ログをSIEMやDLPへ、データを日本に保存、請求書払いやBAA。下にBusinessからはデータを残したまま移れる（営業経由）と書かれている" loading="lazy"><figcaption>どちらを選ぶかの目安（料金ページとヘルプの記載から作成）</figcaption></figure>

Enterpriseの列に並べた条件のうち、1つでも外せないものがあればEnterpriseの見積もりを取る価値があります。どれも当てはまらなければ、Businessで始めて困った時点で上げる順番でも遅くありません。

ヘルプのBusinessのFAQには、**既存のBusinessのワークスペースとデータを維持したままEnterpriseにアップグレードできる**とあります。手続きは営業経由で、別のEnterpriseのワークスペースに移す場合の方法も営業に相談する形です。Businessでの社員の招待と席の管理は[Businessのメンバー招待と管理](/media/chatgpt-business-admin/)の記事で手順を追っています。

## 申し込みの流れ

申し込みはOpenAIの営業チームへの問い合わせから始まります。Enterpriseのページか料金ページの［営業へのお問い合わせ］から、フォームに進みます。

<figure class="post-figure post-figure--sp"><img src="/media/images/chatgpt-enterprise/04_enterprise_sp.jpg" alt="ChatGPT Enterpriseの公式ページをスマホで開いた画面。企業向けに設計されたフロンティアAIという見出しの下にある営業へのお問い合わせボタンを赤枠と番号1で示している" loading="lazy"><figcaption>ChatGPT Enterpriseのページ（2026年10月10日、スマホ表示）</figcaption></figure>

1. [ChatGPT Enterpriseのページ](https://chatgpt.com/ja-JP/business/enterprise/)を開き、［営業へのお問い合わせ］を押す
2. [問い合わせフォーム](https://chatgpt.com/ja-JP/contact-sales/)で会社の規模を選び、会社名・氏名・勤務先のメールアドレス・電話番号を入れる
3. 「当社のどの製品またはサービスに興味をお持ちですか？」で**ChatGPT Enterpriseを選ぶ**
4. ニーズと課題を書いて［送信する］を押す

<figure class="post-figure post-figure--sp"><img src="/media/images/chatgpt-enterprise/06_contact_sp.jpg" alt="ChatGPTの営業チームへのお問い合わせフォームをスマホで開いた画面。番号1が会社の規模の選択欄、番号2が当社のどの製品またはサービスに興味をお持ちですかの選択欄、番号3が送信するボタンで、それぞれ赤枠で囲んでいる" loading="lazy"><figcaption>営業への問い合わせフォーム（2026年10月10日、スマホ表示）</figcaption></figure>

会社の規模の選択肢は「1～50」から「20,001+」までの8段階です。送ったあとはOpenAIの担当者から連絡があり、要件を聞いたうえで提案が出てくる流れだとヘルプは説明しています。

日本の会社なら販売代理店を通す道もあります。NTTデータグループは2025年4月24日の[発表](https://www.nttdata.com/global/ja/news/release/2025/042400/)で、OpenAIの日本初の販売代理店としてChatGPT Enterpriseの提供を始めるとしました。社内の調達の決まりで国内の取引先を通したい場合の選択肢になります。

### 申し込む前に決めておくこと

ヘルプの「[ChatGPT Enterprise 管理者クイックスタート](https://help.openai.com/ja-jp/articles/20001264-chatgpt-enterprise-admin-quickstart)」は、社員を広く招待する前に決めておくことを並べています。

- ワークスペースの所有者と管理者を誰にするか
- 使っているIDプロバイダーと、確認するメールのドメイン
- 社員をどのグループに分け、どの機能を許可するか
- 監査ログ・データの保持・ネットワークの制御で必要なもの
- ChatGPTだけか、Codexも使う人がいるか

**SSOとSCIMは社員を広く招待する前に設定する**よう書かれています。先に社員を招待してからグループを作ると、あとで1人ずつ権限を直す手間が出るためです。社員向けにはOpenAI Japanが基本の操作を説明する[スタートガイドの動画](https://www.youtube.com/watch?v=Niumppe23d4)を公開しています。

導入したあとに、請求書の照合や問い合わせの一次対応のような決まった業務を任せるなら、ChatGPTの画面で使う段階の先にAIエージェントを組む方法があります。進め方は[AIエージェント構築支援](/ai-agent/)のページで説明しています。

## よくある質問

### Q. ChatGPT Enterpriseの料金はいくらですか？

公開されていません。料金ページは「カスタム価格設定」で、金額は営業との相談で決まります。日本語の記事に出てくる1人月60ドルは、2026年10月10日時点の公式ページには載っていない数字です。

### Q. ChatGPT Enterpriseは何人から契約できますか？

Enterpriseだけの最低席数は公式に書かれていません。料金ページのFAQに書かれた企業向けプラン（BusinessとEnterpriseの両方）の条件は2名からです。Businessの上限は1契約200席なので、それを超えるならEnterpriseが前提になります。

### Q. ChatGPT EnterpriseとBusinessの違いは何ですか？

申し込み方と管理機能が違います。Businessは画面から申し込めて200席まで、Enterpriseは営業経由でSCIM・ロールベースのアクセス制御・Compliance API・IP許可リスト・データレジデンシーなどが加わります。

### Q. ChatGPT Enterpriseは個人で申し込めますか？

申し込めません。Enterpriseは組織単位で購入するプランで、個人が直接サインアップすることはできないとヘルプに書かれています。個人やチームで始めるならBusinessかPlusが候補です。

### Q. ChatGPT BusinessでもSSOは使えますか？

使えます。料金ページの比較表で、SAML SSOとドメイン認証はBusinessとEnterpriseの両方にチェックが付いています。Businessで使えないのは、社員の追加と削除を同期するSCIMです。

### Q. ChatGPT BusinessからEnterpriseに移るとデータはどうなりますか？

BusinessのFAQには、既存のワークスペースとそのデータを維持したままEnterpriseにアップグレードできるとあります。手続きは営業に問い合わせて進めます。

### Q. ChatGPT EnterpriseでAPIは使えますか？

別の契約です。Enterpriseのワークスペースに入っても、APIプラットフォームの組織には自動で入りません。APIはAPIの組織の管理者に追加してもらい、料金も別にかかります。

### Q. ChatGPT Enterpriseのデータは日本に保存できますか？

保存先の地域に日本があります。ヘルプでは新しく導入するEnterpriseとEduの顧客が対象とされているため、契約の段階で営業に伝えておく必要があります。

## 出典

- ChatGPT「[料金](https://chatgpt.com/ja-JP/pricing)」ビジネス・エンタープライズ向けタブと機能比較表（2026年10月10日取得）
- ChatGPT「[ChatGPT Enterprise](https://chatgpt.com/ja-JP/business/enterprise/)」（同）
- ChatGPT「[営業チームへのお問い合わせ](https://chatgpt.com/ja-JP/contact-sales/)」（同）
- OpenAI「[エンタープライズプライバシー](https://openai.com/ja-JP/enterprise-privacy/)」（同）
- OpenAI「[ビジネスデータのプライバシー、セキュリティ、コンプライアンス](https://openai.com/ja-JP/business-data/)」（同）
- OpenAI ヘルプセンター「[ChatGPT Enterprise とは何ですか？](https://help.openai.com/ja-jp/articles/8265053)」（同）
- OpenAI ヘルプセンター「[ChatGPT Business：一般FAQ](https://help.openai.com/ja-jp/articles/8542115-chatgpt-business-general-faq)」（同）
- OpenAI ヘルプセンター「[ChatGPT Business - 概要](https://help.openai.com/ja-jp/articles/8792828-chatgpt-business-overview)」（同）
- OpenAI ヘルプセンター「[SCIM プロビジョニングと管理](https://help.openai.com/ja-jp/articles/10011769)」（同）
- OpenAI ヘルプセンター「[Enterprise および Edu のお客様向け OpenAI コンプライアンスプラットフォーム](https://help.openai.com/ja-jp/articles/9261474-compliance-apis-for-enterprise-customers)」（同）
- OpenAI ヘルプセンター「[ChatGPT のデータレジデンシーと推論レジデンシー](https://help.openai.com/ja-jp/articles/9903489-data-residency-and-inference-residency-for-chatgpt)」（同）
- OpenAI ヘルプセンター「[ChatGPT Enterprise 管理者クイックスタート](https://help.openai.com/ja-jp/articles/20001264-chatgpt-enterprise-admin-quickstart)」（同）
- NTTデータグループ「[OpenAIとのグローバルでの戦略的提携を開始](https://www.nttdata.com/global/ja/news/release/2025/042400/)」（2025年4月24日）
