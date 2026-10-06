---
title: 【2026年10月】Claudeの領収書はどこから発行？インボイス番号・宛名変更・日本円の表示
date: 2026-10-07
category: AI活用
description: Claudeの領収書と請求書の出し方を契約した窓口別に、Anthropicのヘルプと国税庁の公表サイトで確認。登録番号T7700150134388、消費税の円表示、会社名の宛名と納税者番号、請求書払いの条件まで。
cover_tag: 料金
cover_headline: Claudeの領収書とインボイス
cover_sub: 登録番号・宛名・日本円の表示
---

Anthropicは2026年4月1日から、日本の顧客に10%の消費税（JCT）を別に請求しています。同じ告知で適格請求書発行事業者の登録を終えたと発表し、登録番号はT7700150134388です。Claudeの請求書はウェブで申し込んだか、スマホのアプリで申し込んだか、APIのConsoleで払ったかで受け取る場所が分かれます。

この記事は2026年10月7日に確認したAnthropicのヘルプセンターと国税庁の公表サイトをもとに、請求書の開き方と宛名・納税者番号・通貨の扱いを窓口ごとに並べます。請求画面はログインが要るため撮影しておらず、手順はヘルプの記述で示します。勘定科目や仕入税額控除の可否のような税務の判断は扱わないため、顧問の税理士に確認してください。

:::takeaways
- ウェブで契約したPro・Maxの請求書は**設定の「請求」にある請求書の一覧から「表示」で開く**。件名「Your receipt from Anthropic」のメールでも届く
- iPhone・Androidのアプリで契約した分は**Anthropicが請求書を出さず、AppleかGoogle Playの領収書**になる
- Anthropicの登録番号は**T7700150134388（Anthropic, PBC）**で、国税庁の公表サイトでの登録年月日は2026年2月17日
- 請求の通貨は変わらず、**消費税の額は適格請求書に日本円で表示される**とヘルプに書かれている
- 会社名の宛名と納税者番号は**次の請求書から反映**され、発行済みの請求書は編集も再発行もできない
:::

## 契約した窓口ごとの受け取り先

同じProプランでも、ブラウザから申し込んだ人とiPhoneのアプリから申し込んだ人では領収書の発行元が違います。[ProプランまたはMaxプランの請求書を理解する](https://support.claude.com/ja/articles/16607638)によると、Claude for iOSやClaude for Androidで申し込んだ場合はApple App StoreかGoogle Playが直接請求し、Anthropicは請求書を発行しません。**請求書を探し始める前に、どの窓口で申し込んだかを確かめてください。**

<figure class="post-figure"><img src="/media/images/claude-invoice/01_fig_where.jpg" alt="Claudeの請求書の受け取り先を契約した窓口別に並べた図。ウェブで購入した分は設定の請求、アプリで購入した分はAppleとGoogle、APIはConsoleで請求書を受け取る" loading="lazy"><figcaption>Anthropicヘルプセンターの記述から作成</figcaption></figure>

請求書を開ける人も窓口で違います。

| 契約した窓口 | 請求書の場所 | 開ける人 |
|---|---|---|
| ウェブのPro・Max | 設定 > 請求の「請求書」 | 契約した本人 |
| iPhoneのアプリ | Appleの[購入履歴](https://support.apple.com/ja-jp/118212) | 契約した本人 |
| Androidのアプリ | Google Playの[注文履歴](https://support.google.com/googleplay/answer/2850369?hl=ja) | 契約した本人 |
| Team（ウェブで購入） | 組織設定 > 請求の「請求書」 | 組織のオーナー |
| API（Claude Console） | Settings > Billing の Invoice history | AdminかBillingのロールを持つ人 |
| 営業経由のEnterprise | 毎月の請求書（質問はアカウントマネージャーへ） | 契約で決まる |

どの窓口で申し込んだか覚えていない場合の見分け方は、[Claudeの解約方法の記事](/media/claude-cancel/)で説明しています。

## Pro・Maxの請求書を開く手順

個人で契約したPro・Maxの請求書は、[Claudeの請求設定](https://claude.ai/settings/billing)から開きます。[有料プラン請求に関するよくある質問](https://support.claude.com/ja/articles/8325618)の手順は次の4つです。

1. 左下のイニシャルか名前を押し、メニューから「設定」を選ぶ
2. 「請求」に移る
3. 「請求書」の欄を探す
4. 開きたい請求書の横の「表示」を押す

<figure class="post-figure post-figure--sp"><img src="/media/images/claude-invoice/04_invoice_find_sp.jpg" alt="Anthropicヘルプの請求書を見つけるの節。設定の請求に移り、請求書の欄で開きたい請求書の表示を押す3つの手順に赤枠" loading="lazy"><figcaption>Anthropicヘルプセンター「ProプランまたはMaxプランの請求書を理解する」</figcaption></figure>

請求のたびに、同じ請求書が登録した請求メールアドレスにも届きます。**受信トレイを件名「Your receipt from Anthropic」で検索すれば、過去の分もまとめて見つかります。**

### 同じ月に請求書が2通あるとき

使用クレジットを有効にしていると、クレジットの購入はプランの料金とは別に請求され、領収書も別に発行されます。オートリロードで自動的に買われた分も、使用量バンドルを買った分も同じ扱いです。月の途中でProからMaxに上げた場合も、次の更新を待たずにその場で請求書が出ます。このときはMaxの1か月分から、Proの残り期間の未使用分が差し引かれます。

### 請求書が見当たらないとき

[有料プラン請求のFAQ](https://support.claude.com/ja/articles/8325618)は、払ったのに無料プランと表示される場合の確認点を2つ挙げています。別のメールアドレスでログインしている場合と、支払いが失敗してダウングレードされた場合です。**請求書の一覧が空なら、まず契約に使ったメールアドレスでログインし直してください。**アプリで申し込んだ分はここに出てこないので、AppleかGoogle Playの履歴を見ます。

## TeamとEnterpriseの請求書

Teamプランの請求書を開けるのは組織のオーナーです。[チームプラン請求に関するよくある質問](https://support.claude.com/ja/articles/12997503)によると、組織設定 > 請求の「請求書」で「表示」を押すとStripeの新しいタブが開き、「請求書をダウンロード」でPDFを保存できます。請求書は組織の請求メールアドレスにも同じ件名で届きます。

請求メールアドレスを経理の共有アドレスに変えたいときや受取人を増やしたいときは、サポートに依頼するようヘルプが案内しています。変更には組織のオーナーの承認が要り、受取人を足す依頼ではオーナーを依頼のメールのCCに入れることが条件です。

[チームプランの請求書を理解する](https://support.claude.com/ja/articles/16607668)によると、**組織設定 > 請求に出る予想合計には税金が入っていないため、実際の請求書の合計より低く見えます。**稟議で予算を組むときは、画面の予想合計に消費税を足して見積もってください。席の追加やアップグレードは日割りでその場で請求され、メンバーを外しても請求書は減りません。

[Enterpriseプランの請求方法について](https://support.claude.com/ja/articles/11526368)によると、Enterpriseの請求はセルフサービスか営業経由かで分かれます。セルフサービスはクレジットを前払いで買い、営業経由は使った量を月ごとに後払いする仕組みです。営業経由の請求書について聞く相手はアカウントマネージャーです。Teamの料金と席の種類は[Claude Teamプランの記事](/media/claude-team/)で比べました。

## APIとClaude Codeの請求書

APIの請求はClaudeのチャットとは別のClaude Consoleで受け取ります。[Claude APIの請求書を理解する](https://support.claude.com/ja/articles/16608069)によると、Console Settings > Billing の Invoice history から「Download」で保存するか、「View」でStripeのタブを開きます。経理の担当者が自分で請求書を取るには、AdminかBillingのロールが要ります。

Consoleの請求書は2種類です。前払いでクレジットを買う組織には購入のたびに領収書が出て、営業を通じて請求契約を結んだ組織には月末にStripeから使用量の請求書が届きます。

- **0.50ドル未満の請求書は単独では請求されず、次の請求書に繰り越される**
- 銀行振込で払う場合は**請求書の金額とぴったり同じ額**を送る。数セント足りないと期限切れのまま残り、支払い済みになるまで約5営業日かかることがある
- 期限が切れたクレジットもInvoice historyに出るが、請求ではない

Claude Codeの請求は、どの窓口で使っているかで決まります。Pro・Maxのアカウントで使うならPro・Maxの請求書に含まれ、Consoleで使うなら[Claude APIの使用料金の支払い](https://support.claude.com/ja/articles/8977456)のとおり前払いのクレジットから引かれます。有料のClaudeプランとAPIの請求は別なので、両方を使う会社では請求書が2系統になります。Claude Codeの料金の比べ方は[Claude Codeの料金の記事](/media/claude-code-pricing/)を見てください。

## 消費税10%と適格請求書の登録番号

[日本の顧客向け消費税（JCT）に関するお知らせ](https://support.claude.com/ja/articles/14051822)によると、Anthropicは2026年4月1日から日本の顧客に提供するサービスに10%の消費税を別に徴収し、その日以降のすべての請求書に適用しています。すべてのプランの価格に10%が加わり、適格請求書発行事業者の登録も終えたと書かれています。

<figure class="post-figure post-figure--sp"><img src="/media/images/claude-invoice/02_jct_number_sp.jpg" alt="AnthropicヘルプのJCTのお知らせのよくある質問。登録番号はT7700150134388で国税庁の適格請求書発行事業者公表サイトで確認できる、請求通貨は変わらずJCT額は適格請求書に日本円で表示される、の2つに赤枠" loading="lazy"><figcaption>Anthropicヘルプセンター「日本の顧客向け消費税（JCT）に関するお知らせ」</figcaption></figure>

同じお知らせは、消費税の対象となる法人顧客はAnthropicの適格請求書で仕入税額控除を受けられるとし、個人顧客は控除を受けられないと書いています。個人事業主として使っている場合の扱いや、控除の要件を満たすかどうかは、このお知らせだけでは判断できません。お知らせの問い合わせ先の表でも、消費税の取り扱いは自社の税務担当者か会計士に聞くよう書かれています。

### 国税庁の公表サイトでの照合

ヘルプが示す番号を[国税庁の適格請求書発行事業者公表サイト](https://www.invoice-kohyo.nta.go.jp/regno-search/detail?selRegNo=7700150134388)で引くと、名称はAnthropic, PBC（カナはアンソロピック ピービーシー）で、所在地は英語の住所でウィルミントン（Wilmington）と載っています。**登録年月日は令和8年2月17日（2026年2月17日）で、消費税を取り始めた4月1日より前に登録されています。**

<figure class="post-figure post-figure--sp"><img src="/media/images/claude-invoice/03_nta_anthropic_sp.jpg" alt="国税庁の適格請求書発行事業者公表サイトのAnthropic, PBCの情報。登録番号T7700150134388と登録年月日 令和8年2月17日に赤枠" loading="lazy"><figcaption>国税庁「適格請求書発行事業者公表サイト」</figcaption></figure>

2026年3月31日以前の請求書は、お知らせの適用日より前のものです。その時期のClaudeの利用料をどう処理するかは、請求書の記載を税理士に見せて確かめてください。プランごとの税込の表示額は[Claudeの料金プランの記事](/media/claude-pricing/)で扱っています。

## 請求書の通貨と日本円の表示

JCTのお知らせは「請求通貨は変わりますか？」という問いに、変わらないと答えています。そのうえで、**JCTの額は適格請求書に日本円（JPY）で表示される**と書いています。

[Pro・Maxの請求書のヘルプ](https://support.claude.com/ja/articles/16607638)には、通貨を変える手順も載っていました。地域の新しい契約者に出す通貨と違う通貨で払っている人は、今の期間の終わりで解約する設定にし、期間が終わってから買い直すと、その地域の新規の契約者と同じ通貨で払えます。ただし日本の新規の契約でどの通貨が選べるかはヘルプに書かれておらず、この記事でも確かめていません。セルフサービスのEnterpriseは[ヘルプ](https://support.claude.com/ja/articles/11526368)でドル（USD）だけの請求とされ、別の通貨で払う必要があるなら営業担当の付く契約を選ぶよう案内されています。

日本の料金ページの金額はドル表示です（[Claudeの料金の記事](/media/claude-pricing/)）。ドルで請求された分をクレジットカードで払うと、カードの明細に出る円の額はカード会社が換算した金額です。請求書のドルの額と明細の円の額を突き合わせるときは、換算の日付で差が出ることを前提にしてください。

## 会社名の宛名と納税者番号

請求書に載る名前と住所は発行された時点の支払い方法から取られます。個人のカードで払えば、宛名はカードの名義のままです。

会社名を宛名にするときは設定 > 請求で支払い方法を追加するか「更新」を押し、「請求書に別の名前を使用する」にチェックを入れます。[有料Claudeアカウントの税務IDの追加](https://support.claude.com/ja/articles/9889408)によると、そのあと「請求先」の欄に会社名を入れれば請求書に反映されます。[チームプランの税務IDの追加](https://support.claude.com/ja/articles/9927624)によると、Teamでこの操作ができるのは組織のオーナーで、場所は組織設定 > 請求です。

<figure class="post-figure post-figure--sp"><img src="/media/images/claude-invoice/05_invoice_name_sp.jpg" alt="Anthropicヘルプの請求書の請求詳細の節。会社名などの異なる名前を表示するには、設定の請求で支払い方法を追加または更新するときに請求書に別の名前を使用するをチェックする、に赤枠" loading="lazy"><figcaption>Anthropicヘルプセンター「ProプランまたはMaxプランの請求書を理解する」</figcaption></figure>

[請求先住所と税金計算について理解する](https://support.claude.com/ja/articles/12997130)によると、請求先住所は税額の計算を決める住所です。Pro・Max・セルフサービスのTeamでは、支払い方法の住所がそのまま請求先住所になります。**カードの登録住所を変えると請求先住所も変わる**ため、会社の住所を請求書に載せたいならカード側の住所を確かめてください。支払い方法を変えても同じ住所にしたいときは、営業所を確かめる書類を添えてサポートに頼めば固定できると同じヘルプにあります。

納税者番号（ヘルプの表記は税務IDまたはVAT ID）の欄は、住所が税務上の対象になる場合に表示されます。入れる場所は支払い方法の「更新」のフォームで、Consoleでは設定 > 組織です。ここは自社の番号を入れる欄で、Anthropicの登録番号を写す欄ではありません。日本の会社が法人番号と自社の登録番号のどちらを入れるかはヘルプに書かれていないので、税理士に確かめてから入れてください。

**変更が効くのは次の請求書からです。**[有料プラン請求のFAQ](https://support.claude.com/ja/articles/8325618)は、支払い済みの請求書を編集する方法はなく、Anthropicの社内チームも再発行や過去の請求書の変更はできないと書いています。発行済みの分もサポートに相談できる[ChatGPTの請求書](/media/chatgpt-invoice/)とはここが違います。

<figure class="post-figure"><img src="/media/images/claude-invoice/06_fig_name.jpg" alt="Claudeの宛名と納税者番号の図。支払い方法の更新で入力すると次の請求書から反映され、発行済みの請求書は直せない" loading="lazy"><figcaption>Anthropicヘルプセンターの記述から作成</figcaption></figure>

経費精算で会社名入りの請求書が要るなら、最初の支払いの前に宛名と住所を整えておくのが確実です。

## 請求書払いと銀行振込の条件

自分で申し込むプランはどれもカード払いが前提です。ヘルプに書かれた支払い方法を窓口ごとに並べました。

| 窓口 | 払い方 | 銀行振込 |
|---|---|---|
| ウェブのPro・Max | クレジットカード・デビットカード | 不可 |
| アプリのPro・Max | AppleかGoogle Playの支払い方法 | AppleとGoogleの決まりによる |
| Team | クレジットカード・デビットカード・プリペイドカード | 不可（ACHなども受け付けていない） |
| セルフサービスのEnterprise | クレジットカード・デビットカード・ACH銀行振込 | ACHのみ |
| 営業経由のEnterprise | 銀行振込（ACHか送金）。少額ならカードも可 | 可。5万ドル以上は振込のみ |
| API（前払い） | カードでクレジットを購入 | ヘルプに記載なし |
| API（請求契約） | 月末にStripeから請求書 | 可（振込の注意がヘルプにある） |

出典は[有料プラン請求のFAQ](https://support.claude.com/ja/articles/8325618)・[チームプラン請求FAQ](https://support.claude.com/ja/articles/12997503)・[Enterpriseの請求方法](https://support.claude.com/ja/articles/11526368)・[APIの使用料金の支払い](https://support.claude.com/ja/articles/8977456)です。ACHは米国の銀行間で使われる振込の仕組みです。**日本の会社が請求書払いと振込を使いたい場合は、営業経由のEnterpriseかAPIの請求契約を営業チームに相談する流れになります。**

## 請求書の行と月の締め

Pro・Maxの請求日は変えられません。有料プラン請求のFAQには、日付を変える方法として今のプランをやめて希望の日に申し込み直す手順だけが書かれています。月末締めに合わせるなら、一度解約して月末に申し込み直すことになります。

請求書にはプランの料金以外の行が出ることがあります。[Pro・Maxの請求書のヘルプ](https://support.claude.com/ja/articles/16607638)をもとに、行の意味を整理しました。

| 請求書の行 | 意味 |
|---|---|
| 按分の請求 | 期間の途中でプランを上げたときの請求。古いプランの残りの価値が差し引かれる |
| クレジット | プラン変更で古いプランの残りが新しいプランより多かったときに残る額。次の請求に自動で使われる |
| 税金 | 請求先住所から計算した税額 |
| 適用残高 | アカウントにあったクレジットを使った分。新しい請求でも値引きでもない |
| 支払い額 | 請求書の合計から適用残高を引いた額。カードに請求された金額 |

プランの価格と請求書の額が合わないときは、ヘルプによると按分かクレジットか適用残高のどれかが理由のことが多く、どれも独立した行として載ります。

## よくある質問

### Claudeの領収書はどこから発行できますか？

ウェブで契約したPro・Maxは、設定 > 請求の「請求書」で「表示」を押して開きます。件名「Your receipt from Anthropic」のメールでも届きます。Teamは組織のオーナーが組織設定 > 請求から、APIはAdminかBillingのロールを持つ人がConsoleのInvoice historyからダウンロードします。アプリで契約した分の発行元はAppleかGoogle Playです。

### Claudeの領収書は日本円で発行できますか？

請求書の全体を円にできるかは、ヘルプに書かれていません。JCTのお知らせによると請求の通貨はJCTの開始で変わらず、消費税の額が適格請求書に日本円で表示されます。地域の新規の契約者向けの通貨に切り替える手順もヘルプにありますが、日本でどの通貨が選べるかは書かれていません。セルフサービスのEnterpriseはドルだけの請求で、別の通貨が要るなら営業担当の付く契約を選ぶようヘルプは案内しています。

### Claudeのインボイス登録番号は何ですか？

T7700150134388です。国税庁の公表サイトでは名称がAnthropic, PBC、登録年月日が2026年2月17日と表示されます。

### Anthropicの領収書はインボイスとして使えますか？

Anthropicのお知らせは、消費税の対象となる法人顧客は適格請求書で仕入税額控除を受けられると書いています。消費税が載るのは2026年4月1日以降の請求書です。自社が控除の要件を満たすかは税理士に確認してください。

### Claudeの領収書の宛名は変更できますか？

できますが、反映されるのは次の請求書からです。設定 > 請求で支払い方法を更新し、「請求書に別の名前を使用する」にチェックを入れて請求先に会社名を入れます。発行済みの請求書は編集も再発行もできないとヘルプに書かれています。

### Claudeは請求書払いできますか？

Pro・MaxとTeamはカード払いだけで、請求書払いや銀行振込はできません。営業経由のEnterpriseは銀行振込で払え、5万ドル以上の請求書は振込だけです。APIは営業を通じた請求契約で月ごとの請求書になります。

### Claude Codeは請求書払いに対応していますか？

使う窓口しだいです。Pro・Maxで使うならカード払いのプランの請求書に含まれます。Consoleで使うなら前払いのクレジットから引かれ、営業を通じて請求契約を結んだ組織だけが月末の請求書で払います。

### Claudeの消費税はいつからかかりますか？

2026年4月1日からです。Anthropicはこの日から日本の顧客に10%の消費税を別に徴収し、それ以降のすべての請求書に適用しています。

## 出典

- Anthropicヘルプセンター「[日本の顧客向け消費税（JCT）に関するお知らせ](https://support.claude.com/ja/articles/14051822)」（2026年10月7日取得）
- Anthropicヘルプセンター「[有料プラン請求に関するよくある質問](https://support.claude.com/ja/articles/8325618)」（同）
- Anthropicヘルプセンター「[ProプランまたはMaxプランの請求書を理解する](https://support.claude.com/ja/articles/16607638)」（同）
- Anthropicヘルプセンター「[チームプランの請求書を理解する](https://support.claude.com/ja/articles/16607668)」（同）
- Anthropicヘルプセンター「[チームプラン請求に関するよくある質問](https://support.claude.com/ja/articles/12997503)」（同）
- Anthropicヘルプセンター「[Claude APIの請求書を理解する](https://support.claude.com/ja/articles/16608069)」（同）
- Anthropicヘルプセンター「[Claude APIの使用料金をどのように支払いますか？](https://support.claude.com/ja/articles/8977456)」（同）
- Anthropicヘルプセンター「[Enterpriseプランの請求方法について](https://support.claude.com/ja/articles/11526368)」（同）
- Anthropicヘルプセンター「[請求先住所と税金計算について理解する](https://support.claude.com/ja/articles/12997130)」（同）
- Anthropicヘルプセンター「[有料Claudeアカウントの税務IDまたはVAT IDを追加または更新する](https://support.claude.com/ja/articles/9889408)」・「[チームプランの税務IDまたはVAT IDを追加または更新する](https://support.claude.com/ja/articles/9927624)」・「[Claude Consoleの組織の税務IDまたはVAT IDを追加または更新する](https://support.claude.com/ja/articles/9889428)」（同）
- 国税庁「[適格請求書発行事業者公表サイト](https://www.invoice-kohyo.nta.go.jp/)」[T7700150134388](https://www.invoice-kohyo.nta.go.jp/regno-search/detail?selRegNo=7700150134388)（同）
