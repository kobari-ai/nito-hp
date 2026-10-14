---
title: 【2026年10月】WorkspaceでNotebookLMを有効にする方法 管理コンソール・使えない原因
date: 2026-10-15
category: AI活用
description: Google WorkspaceでNotebookLM（Gemini Notebook）を有効にする手順を管理者ヘルプで解説。設定の今の場所、部署ごとの許可、エディション別の上限、使えないときの確認、組織外との共有と監査ログまで。
cover_tag: 法人
cover_headline: WorkspaceでNotebookLMを有効に
cover_sub: 管理コンソール・使えない原因・共有
---

NotebookLMは2026年7月16日にGemini Notebookへ名前が変わり、Google Workspaceの管理コンソールでも［生成AI］の下の［Gemini Notebook］で設定する形になりました。Googleの告知「[NotebookLM is now Gemini Notebook](https://workspaceupdates.googleblog.com/2026/07/notebooklm-now-gemini-notebook.html)」によると、改名で管理者がやることはなく、共有済みのノートブックとリンクは自動で転送されます。

困るのは改名より前に書かれた解説の手順をなぞったときです。［アプリ］［その他の Google サービス］や早期アクセスのアプリとして探しても、今の管理コンソールでは見つかりません。この記事は2026年10月15日に取得した管理者ヘルプをもとに、Gemini Notebookをオンにする場所と手順・部署ごとの分け方・エディションで変わる上限・オンにしても使えないときの確かめ方・組織外との共有・監査ログを説明します。管理コンソールにはログインしていないため、手順はヘルプの記述とヘルプの画面で示します。

<figure class="post-figure"><img src="/media/images/notebooklm-workspace-admin/nwa_00_overview.jpg" alt="Gemini Notebookを使えるまでと題した図。エディション、サービスのステータス、共有設定の3つの確認が順に並び、最後に社員が使える状態になる流れ" loading="lazy"><figcaption>有効にする前後に見る3つの設定</figcaption></figure>

:::takeaways
- 設定の場所は**［生成AI］［Gemini Notebook］［サービスのステータス］**。開くにはGeminiの「設定」の管理者権限が要る
- 組織部門ごとにオンとオフを分けられ、**部署をまたぐならアクセスグループ**を使う
- 上限はエディションで6段階に分かれ、Business Starterは**ノートブック100件・1冊にソース50件・チャット1日50回**
- 組織外との共有は**オフ・許可したドメインだけ・オン**の3択で、一般公開は別のスイッチ
- 2026年9月3日から**Gemini Notebookのログイベント**を管理コンソールで検索できる。ノートブックの中身はデータリージョンの対象外
:::

## NotebookLMの設定がある場所

管理者ヘルプ「[ユーザーに対して Gemini Notebook を有効または無効にする](https://knowledge.workspace.google.com/admin/generative-ai/gemini-notebook/turn-gemini-notebook-on-or-off-for-users?hl=ja)」の冒頭には、NotebookLMはGemini Notebookに名称変更されると書かれています。**管理コンソールでNotebookLMの名前を探しても出てこないのはこのため**で、オンとオフも共有の設定も同じ［Gemini Notebook］の画面にまとまっています。

| やりたいこと | 管理コンソールの場所 | 必要な管理者権限 |
|---|---|---|
| 使える人をオンまたはオフにする | ［生成AI］［Gemini Notebook］［サービスのステータス］ | Geminiの「設定」 |
| 組織外との共有を決める | ［生成AI］［Gemini Notebook］の［組織名の外部との共有］ | Geminiの「設定」 |
| 利用の記録を見る | ［レポート］［監査と調査］［Gemini Notebookのログイベント］ | 監査と調査 |

GmailやドキュメントのGemini、gemini.google.comのGeminiアプリは別のサービスとして扱われ、設定の画面も別です。そちらを止めたり許可したりする手順は[WorkspaceのGeminiを無効化する方法](/media/google-workspace-gemini-admin/)で説明しています。

## Gemini Notebookをオンにする手順

手順には全員を一度に切り替える方法と、組織部門ごとに切り替える方法の2通りがあります。どちらも最後に［保存］を押すまで反映されません。

1. [Google管理コンソール](https://admin.google.com/)のメニューから［生成AI］［Gemini Notebook］に進む
2. ［サービスのステータス］を押す
3. 全員に使わせるなら［オン（すべてのユーザー）］、止めるなら［オフ（すべてのユーザー）］を選ぶ
4. 一部だけにするなら、左側で組織部門を選んでから［オン］か［オフ］を選ぶ
5. ［保存］を押す

<figure class="post-figure"><img src="/media/images/notebooklm-workspace-admin/nwa_01_onoff.jpg" alt="管理者ヘルプのGemini Notebookをオンまたはオフにする節。管理コンソールで生成AIからGemini Notebookに移動し、Geminiの設定の管理者権限が要ること、サービスのステータスを押してオン（すべてのユーザー）かオフ（すべてのユーザー）を選んで保存する手順が書かれ、サービスのステータスとオンとオフの行が赤枠" loading="lazy"><figcaption>管理者ヘルプの手順（2026年10月15日）。赤枠の順に押す</figcaption></figure>

オンとオフのページには、反映までの時間は書かれていません。同じ［Gemini Notebook］の共有設定のページには**変更の反映に最長24時間ほど**とあるため、保存した直後に社員が使えなくても、翌日まで待ってから確かめるほうが確実です。

### 一部の部署だけで使う

組織部門を選んで切り替えた画面で、［サービスのステータス］が［継承］になっていれば親の組織と同じ設定です。親の設定が後で変わっても今の設定を保ちたいなら［オーバーライド］を押し、親と同じに戻すなら［継承］を押します。

部署をまたいで試す人を集めたいときは、ヘルプは**アクセスグループ**を使う方法を案内しています。会社全体はオフのまま、試験導入のグループだけオンにする使い方です。組織部門とグループの分け方は、[WorkspaceのGeminiの記事の組織部門の節](/media/google-workspace-gemini-admin/)と同じ考え方で組めます。

## エディションで変わる上限と規約

**使えるかどうかと、どこまで使えるかは、Workspaceのエディションで決まります。**ヘルプはエディションを6段階に分けていて、BusinessやEnterpriseの多くはGemini Notebookがコアサービスとして含まれます。

| 段階 | 主なエディション | 規約 |
|---|---|---|
| 標準 | Business Base・Essentials Starter・Workspace Individualなど（追加サービス） | Google利用規約 |
| 標準（エンタープライズ向けの保護） | Business Starter・Enterprise Starter・Frontline・Nonprofitsなど | Google Cloud利用規約 |
| より広範 | Education Plus・Teaching and Learningアドオン | Workspace for Education利用規約 |
| 高レベル | Business Standard・Business Plus・Enterprise Standard・Enterprise Plus | Google Cloud利用規約 |
| 拡張 | AI Expanded Accessアドオン | Google Cloud利用規約 |
| 最高 | AI Ultra Accessアドオン | Google Cloud利用規約 |

<figure class="post-figure"><img src="/media/images/notebooklm-workspace-admin/nwa_02_editions.jpg" alt="管理者ヘルプのGemini Notebookの機能（Workspaceエディション別）の表。左から標準、エンタープライズグレードの保護つきの標準、より広範、高レベル、拡張、最高の6列があり、追加サービスとしてBusiness BaseやEssentials Starter、コアサービスとしてBusiness Starter、Business StandardやEnterprise Plusなどのエディション名が並ぶ" loading="lazy"><figcaption>エディション別の表（2026年10月15日）</figcaption></figure>

違いが大きいのはデータの扱いです。追加サービスとして使う段階では、フィードバックを送らない限り学習には使われないものの、Googleの利用規約が適用されます。2段目より上は**アップロードしたファイル・チャット・回答を人のレビュアーが見ることも、モデルの改善に使うこともない**と書かれています。

上限は5列の表で示されていて、標準の2段は同じ数字です。

| 項目 | 標準 | より広範 | 高レベル | 拡張 | 最高 |
|---|---|---|---|---|---|
| ノートブック | 100件 | 200件 | 500件 | 500件 | 500件 |
| 1冊のソース | 50件 | 100件 | 300件 | 400件 | 600件 |
| チャット | 1日50回 | 1日200回 | 1日500回 | 1日1,000回 | 1日5,000回 |
| 音声解説 | 1日3件 | 1日6件 | 1日20件 | 1日40件 | 1日200件 |
| Deep Research | 月10回 | 1日3件 | 1日20件 | 1日30件 | 1日200件 |

<figure class="post-figure"><img src="/media/images/notebooklm-workspace-admin/nwa_03_limits.jpg" alt="管理者ヘルプの使用量上限の内訳の表。標準アクセス、アクセス権の追加、上位レベル、Expanded Level Access、最高レベルの5列で、ノートブック、出典、チャット、音声概要、動画の概要、レポートなどの上限が並ぶ" loading="lazy"><figcaption>使用量上限の表（2026年10月15日、ヘルプの表記のまま）</figcaption></figure>

社員が自分のアカウントの段階を確かめる方法は、Gemini Notebookのヘルプ「[仕事用または学校用の Google アカウントで Gemini Notebook を使用する](https://support.google.com/gemininotebook/answer/16337734?hl=ja)」にあります。Gemini Notebookを開き、画面上部のプロフィール画像の横に**Pro・Plus・Expanded・Ultraのどれかのバッジ**があれば、上限が引き上げられた段階です。上限を上げたい社員には管理者にライセンスのアップグレードを頼むよう同じヘルプが案内しています。

<figure class="post-figure post-figure--sp"><img src="/media/images/notebooklm-workspace-admin/nwa_04_badge.jpg" alt="Gemini Notebookのヘルプのアップグレードされたアクセス権の確認方法。ブラウザでGemini Notebookを開き、仕事用または学校用のアカウントでログインしていることを確かめ、プロフィール画像の横にPro、Plus、Expanded、Ultraのバッジがあるかを見る3つの手順で、3つ目が赤枠" loading="lazy"><figcaption>社員がバッジで段階を確かめる手順（2026年10月15日、スマホ）</figcaption></figure>

## オンにしたのに使えないとき

「管理コンソールでオンにしたのに使えない」と言われたら、社員の側と管理者の側を順に切り分けます。ヘルプの記述から拾った原因を、確かめる順に並べました。

<figure class="post-figure"><img src="/media/images/notebooklm-workspace-admin/nwa_05_check.jpg" alt="オンにしたのに使えないときの確認の順番の図。ログイン中のアカウント、所属する組織部門の設定、保存からの経過時間、エディション、ドメインを登録した国の5つを上から順に確かめる" loading="lazy"></figure>

| 症状 | 確かめる所 |
|---|---|
| 上限が個人と同じで、会社の資料も見えない | 個人のGoogleアカウントでログインしていないか |
| 一部の社員だけ使えない | その人の組織部門が［オーバーライド］でオフになっていないか |
| 保存した直後から変わらない | 保存から24時間たったか |
| 管理コンソールに［Gemini Notebook］が無い | 自分にGeminiの「設定」の管理者権限があるか |
| ［オン］にできない | ドメインを最初に登録した国でサービスが制限されていないか |
| ドライブのファイルを入れられない | その社員が元のファイルを閲覧できるか |

最後の行は、Gemini Notebookがドライブのファイルに組織の共有設定をそのまま当てるためです。ヘルプには**元のファイルを閲覧以上の権限で開ける人だけがソースに使える**と書かれています。オンにできないケースは管理者ヘルプ「[サービスを有効にできない](https://knowledge.workspace.google.com/admin/support/troubleshooting/unable-to-turn-on-a-service?hl=ja)」の説明のとおり、Workspaceのドメインを最初に登録した国の設定が関わります。

学校で使う場合は年齢の設定も関わります。Workspace for Educationで18歳未満とされた人は、Gemini Notebook自体は使えますが、Deep Research・インフォグラフィック・シネマティック動画解説・Googleスライドの作成などが使えません。

## 組織外との共有の設定

取引先とノートブックを共有できない、という相談の多くはこの設定です。管理者ヘルプ「[Gemini Notebook の共有設定を管理する](https://knowledge.workspace.google.com/admin/generative-ai/gemini-notebook/manage-gemini-notebook-sharing-settings?hl=ja)」によると、［組織名の外部との共有］は次の3つから選びます。

- オフ: 組織の外の人とは共有できない
- 許可リスト登録済みドメイン: 入力したドメインの個人のアカウントとだけ共有できる。Googleグループとの共有は使えない
- オン: どの外部のメールアドレスとも共有できる

<figure class="post-figure"><img src="/media/images/notebooklm-workspace-admin/nwa_06_sharing.jpg" alt="管理者ヘルプのGemini Notebookの共有オプションを設定する節。組織名の外部との共有で、オフ、許可リスト登録済みドメイン、オンの3つの選択肢と、一般公開の共有をオンにする任意の手順が書かれ、3つの選択肢の行が赤枠" loading="lazy"><figcaption>共有の3択と一般公開（2026年10月15日）</figcaption></figure>

外部との共有を［オン］にしたときだけ、［一般公開の共有］をオンにできます。こちらを許可すると、**リンクを知っている人なら誰でもノートブックを開ける**ようになります。社外秘の資料を入れる部署では、外部共有を許可リストにとどめ、一般公開はオフのままにしておくのが無難です。

## データの扱いと監査ログ

導入の稟議でよく聞かれるのは、入れた資料がどこに置かれ、誰が何をしたかを後から追えるかです。ヘルプによるとGemini Notebookはドライブのファイルを性能のためにキャッシュしていて、**組織のデータリージョンの設定はGemini Notebookで処理・保存されるデータには適用されません**。

Googleの告知「[Introducing comprehensive audit logs for Gemini Notebook](https://workspaceupdates.googleblog.com/2026/08/introducing-comprehensive-audit-logs-for-Gemini-Notebook-in-the-Workspace-Admin-console.html)」も同じ点に触れています。ノートブック・ソース・チャット履歴はグローバルに保存され、今はデータのリージョン指定に対応していません。

利用の記録は2026年9月3日から段階的に管理コンソールで見られるようになりました。［レポート］［監査と調査］［Gemini Notebookのログイベント］を開くと、既定で過去7日間のイベントが表示されます。操作した人のメールアドレスや、ノートブックの公開設定が変わる前と後の状態を検索できます。

<figure class="post-figure"><img src="/media/images/notebooklm-workspace-admin/nwa_07_audit.jpg" alt="管理者ヘルプのGemini Notebookのログイベントのページ。管理コンソールでレポート、監査と調査、Gemini Notebookのログイベントに移動する手順と、監査と調査の管理者権限が要ること、既定で過去7日間のイベントが表示されることが書かれ、移動先の行が赤枠" loading="lazy"><figcaption>ログイベントを開く場所（2026年10月15日）</figcaption></figure>

ログはBigQueryへ書き出せますが、管理者がオンにするまで書き出しはオフです。セキュリティ調査ツールで同じログを調べられるのは、Enterprise Standard・Enterprise Plus・Frontline Standardなどに限られます。

## Gemini Notebook Enterpriseとの違い

名前の似た製品に、Google Cloudで契約するGemini Notebook Enterpriseがあります。WorkspaceのGemini Notebookとは管理する場所も契約も別です。

| 項目 | WorkspaceのGemini Notebook | Gemini Notebook Enterprise |
|---|---|---|
| 管理する場所 | Google管理コンソール | Google Cloudのプロジェクト |
| ログイン | Workspaceのアカウント | Cloud IdentityかEntra ID・Oktaなどの外部のIdP |
| ソースの形式 | PDF・ドキュメント・スライド・URLなど | 左に加えてWord・PowerPoint・Excelのファイル |
| データの置き場所 | 指定できない | Google Cloudのプロジェクトの中 |

Google Cloudのドキュメント「[Gemini Notebook Enterprise とは](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview?hl=ja)」には、Enterpriseの上限としてノートブック500個・1冊にソース300個・1日500件のクエリが載っています。Google Cloud Japanの解説動画「[NotebookLM Enterprise 管理者向けセットアップ手順](https://www.youtube.com/watch?v=orKp7G8gwtU)」では、IDプロバイダの設定・プロジェクトの作成・ライセンスの払い出し・IAMのロールの付与・ユーザーへの割り当ての順に進めています。データの置き場所まで指定したい組織でなければ、WorkspaceのGemini Notebookで足ります。

## 社内で使い始める前に決めること

オンにするのは数分で終わるので、手間がかかるのは社内での決めごとのほうです。最初に決めておくと問い合わせが減る項目は4つあります。

- 試す範囲: 全社か、組織部門かアクセスグループか
- 外部との共有: オフか許可リストか。一般公開を許すか
- 案内するアカウント: 会社のアカウントでログインすること。個人のアカウントで業務の資料を入れない
- 記録の見方: ログイベントを誰がどの頻度で見るか

社員向けの使い方の案内には、ノートブックの作り方やStudioの機能をまとめた[NotebookLM（Gemini Notebook）の使い方](/media/gemini-notebook-guide/)を渡せます。社内の資料を読ませる使い方が定着し、問い合わせ対応などの業務をAIに任せる段階に進むときの組み立て方は、[AIエージェント構築支援](/ai-agent/)のページで紹介しています。

## よくある質問

### NotebookLMはWorkspaceで使えますか？

使えます。Business StarterからEnterprise Plusまでの多くのエディションにコアサービスとして含まれ、Business Baseなどでは追加サービスの扱いです。今の名前はGemini Notebookです。

### NotebookLMを管理コンソールで有効にするには？

［生成AI］［Gemini Notebook］［サービスのステータス］で［オン（すべてのユーザー）］を選び、［保存］を押します。Geminiの「設定」の管理者権限が要ります。

### NotebookLMを一部の社員だけに使わせられますか？

できます。左側で組織部門を選んでオンにするか、部署をまたぐならアクセスグループを使います。会社全体はオフのままでも構いません。

### NotebookLMで社外と共有できないのは？

［組織名の外部との共有］がオフになっていると、組織の外の人とは共有できません。許可リストに相手のドメインを入れるか、オンに変えると共有できます。

### NotebookLMの入力は学習に使われますか？

フィードバックを送らない限り学習には使われません。Business Starter以上のコアサービスでは、人のレビュアーが内容を見ることもないとヘルプに書かれています。

### 管理者はNotebookLMの利用状況を確認できますか？

2026年9月3日から、［レポート］［監査と調査］［Gemini Notebookのログイベント］で操作の記録を検索できます。監査と調査の管理者権限が要ります。

### WorkspaceのNotebookLMの上限は？

Business Starterはノートブック100件・1冊にソース50件・チャット1日50回です。Business StandardとBusiness Plusは500件・300件・1日500回に増えます。

### NotebookLM Enterpriseとの違いは？

WorkspaceのGemini Notebookは管理コンソールで管理し、EnterpriseはGoogle Cloudのプロジェクトで管理します。Enterpriseは外部のIdPでのログインやWord・Excelのファイルのソースにも対応しています。

## 出典

ヘルプとドキュメントは2026年10月15日に取得しました。管理コンソールの項目名はヘルプの表記に合わせています。

- Google Workspace 管理者ヘルプ「[ユーザーに対して Gemini Notebook を有効または無効にする](https://knowledge.workspace.google.com/admin/generative-ai/gemini-notebook/turn-gemini-notebook-on-or-off-for-users?hl=ja)」
- Google Workspace 管理者ヘルプ「[Gemini Notebook の共有設定を管理する](https://knowledge.workspace.google.com/admin/generative-ai/gemini-notebook/manage-gemini-notebook-sharing-settings?hl=ja)」
- Google Workspace 管理者ヘルプ「[Gemini Notebook のログイベント](https://knowledge.workspace.google.com/admin/reports/gemini-notebook-log-events?hl=ja)」
- Google Workspace 管理者ヘルプ「[サービスを有効にできない](https://knowledge.workspace.google.com/admin/support/troubleshooting/unable-to-turn-on-a-service?hl=ja)」
- Google Workspace 管理者ヘルプ「[Google サービスへのアクセスを年齢別に管理する](https://knowledge.workspace.google.com/admin/getting-started/editions/control-access-to-google-services-by-age?hl=ja)」
- Google Workspace 管理者ヘルプ「[アクセス グループを使用してサービスへのアクセスをカスタマイズする](https://knowledge.workspace.google.com/admin/users/advanced/customize-service-access-using-access-groups?hl=ja)」
- Gemini Notebook ヘルプ「[仕事用または学校用の Google アカウントで Gemini Notebook を使用する](https://support.google.com/gemininotebook/answer/16337734?hl=ja)」
- Google Workspace Updates「[NotebookLM is now Gemini Notebook](https://workspaceupdates.googleblog.com/2026/07/notebooklm-now-gemini-notebook.html)」（2026年7月16日）
- Google Workspace Updates「[Introducing comprehensive audit logs for Gemini Notebook in the Workspace Admin console](https://workspaceupdates.googleblog.com/2026/08/introducing-comprehensive-audit-logs-for-Gemini-Notebook-in-the-Workspace-Admin-console.html)」（2026年9月3日）
- Google Cloud ドキュメント「[Gemini Notebook Enterprise とは何ですか？](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview?hl=ja)」
- YouTube「[NotebookLM Enterprise 管理者向けセットアップ手順](https://www.youtube.com/watch?v=orKp7G8gwtU)」（Google Cloud Japan）
