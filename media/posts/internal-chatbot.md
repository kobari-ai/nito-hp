---
title: 【2026年10月】社内チャットボットの選び方｜製品を買うか自社で作るか・費用・RAG
date: 2026-10-29
category: AI活用
description: 社内チャットボットを製品で買うか、Microsoft 365・Google Workspace・ChatGPT・Difyで自社で組むかを公式の情報で比較。2つの型、費用の決まり方、RAGの仕組み、失敗しやすい所、会社が決めることまで。
cover_tag: 導入担当向け
cover_headline: 社内チャットボットの選び方
cover_sub: 製品を買うか自社で作るか
cta: ai_agent
---

Microsoft 365・Google Workspace・ChatGPT Businessはどれも、契約の中で社内の文書に答えるボットを作り、社員に配れるようになりました。社内問い合わせ向けの製品を新しく買う以外の道が、すでに手元にある会社は少なくありません。

人事・総務・情シスに同じ質問が届き続ける会社で、製品を買うか自社の契約で組むかを決める担当者に向けて、型の違い・費用の決まり方・RAGの仕組み・失敗しやすい所を比べます。製品の契約と各社の画面での作成は試していません。

:::takeaways
- **社内チャットボットは、登録した答えを返すシナリオ型と、社内文書を探して答える生成AIの型（RAG）に分かれる**
- **自社で組むなら、すでに契約している基盤から選ぶ**。Microsoft 365はエージェント ビルダー、Google WorkspaceはGem、ChatGPT Businessはプラグイン、モデルを選びたいならDify
- **うまくいかない原因の多くは文書の側にある**。古い規程・同じ文書の重複・更新する人の不在を、配る前に片づける
:::

## 社内チャットボットの2つの型

チャットボットを入れたのに使われない、という話は生成AIが出る前からありました。当時の主流は想定した質問と答えを登録しておき、選択肢をたどらせるか近い質問を選んで返すシナリオ型です。いま増えているのは規程やマニュアルを読ませておき、質問のたびに該当する箇所を探して文章で答える型で、この仕組みをRAG（検索拡張生成）と呼びます。

| | シナリオ型 | 生成AI＋社内文書（RAG） |
|---|---|---|
| 答えの作り方 | 登録した答えをそのまま返す | 文書から探した箇所をもとに文章を作る |
| 向く質問 | 手順が決まった申請・パスワードの再設定 | 規程の読み方・どの書類が要るか |
| 手間がかかる所 | 質問と答えを1件ずつ登録して直す | 文書を整え、答えが合っているか試す |
| 外れたとき | 該当なしと返る | 文書に無いことを答えることがある |

<figure class="post-figure"><img src="/media/images/internal-chatbot/icb_01_types.png" alt="社内チャットボットの2つの型を縦に並べた図。シナリオ型は登録した答えを返し、決まった手続きに向く。生成AIと社内文書の型は文書から探した箇所で答えを作り、規程の読み方に向く" loading="lazy"></figure>

Microsoftの[請求レートと管理](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/requirements-messages-management)でも、Copilot Studioは作成者が書いた決まった返事の「従来型の回答」を1クレジット、生成回答を2クレジットと分けて数えています。**決まった手続きはシナリオ型、文書を読まないと答えられない質問は生成AIの型と、1つのボットの中で使い分けるのが現実的です。** 申請の締め日のように1字違うと困る答えまで生成に任せると、確かめる手間が増えます。

## 製品を買う場合

社内問い合わせ向けの製品は、TeamsやSlackのような社内チャットに窓口を置き、答えられない質問を担当者へ引き継ぐところまでを1つにしたものが中心です。たとえば[PKSHA AIヘルプデスク](https://aisaas.pkshatech.com/ai-helpdesk/)は、Teamsに窓口を集め、FAQで答える・文書を読んで答えを作る・人が対応した記録からFAQを作る、の3つを1つの製品に入れています。

選ぶときに差が出るのは機能の数より費用の決まり方です。2026年10月29日に各社の料金ページで確かめた例を並べます。

| 費用の決まり方 | 例 | 公式ページの記載 |
|---|---|---|
| 使う人数で月額 | [HiTTO](https://hitto.jp/price/) | 利用者数に応じた月額。質問と回答の数では課金せず、初期費用もなし。金額は問い合わせ |
| 定額と回数の上限 | [OfficeAI社員](https://officebot.jp/price/) | Basicは初期費用10万円・月15万円で質問応答が月5,000回。ユーザー数は無制限 |
| 見積もり | [PKSHA AIヘルプデスク](https://aisaas.pkshatech.com/ai-helpdesk/) | 製品ページに料金の記載なし |

**人数で決まる製品は社員が多いほど高くなり、定額の製品は質問の回数が上限に収まるかが分かれ目です。** OfficeAI社員のProは月20万円で、質問応答5,000回に加えて調査や資料作成のタスクが月1,000回付きます。EntraIDやOktaとのシングルサインオンは別のオプションで、初期費用5万円と月2万円です。

見積もりを取る前に、次の4つを各社に同じ形で聞いておくと比べやすくなります。

- 文書をどこから取り込むか（SharePointやGoogleドライブとつながるか、ファイルを手で上げるか）
- 答えに出典の文書を添えられるか
- 答えられない質問をだれに引き継ぎ、そのやり取りが記録に残るか
- データを保存する場所と、使う言語モデル

## 自社の契約で組む場合

社員の大半が使っている業務の基盤があるなら、新しい製品を買う前に、その契約の中で作れる範囲を確かめます。4つを並べると次のとおりです。

| 基盤 | 作る場所 | 配れる範囲 | 読ませる文書 | 費用のかかり方 |
|---|---|---|---|---|
| Microsoft 365 | エージェント ビルダー | 小さなチーム。組織全体はCopilot Studio | SharePointのファイル100個・OneDriveの50個など | M365 Copilotを持つ社員は追加なし。持たない社員はクレジット |
| Google Workspace | GeminiアプリのGem | 指定した人か組織内 | Googleドライブのファイル | Workspaceの1人あたりの料金 |
| ChatGPT Business | プラグイン | ワークスペースの中 | スキルの参照ファイルとつないだアプリ | 1人月3,050円（年額課金） |
| Dify | チャットのアプリとナレッジ | 公開したWebアプリ | Difyのナレッジか、外部の検索 | Teamは月159ドルで50人まで。モデルの代金は別 |

<figure class="post-figure"><img src="/media/images/internal-chatbot/icb_02_build.png" alt="自社の契約で社内チャットボットを組む4通りを縦に並べた図。Microsoft 365はエージェント ビルダーでSharePointの文書を読ませる。Google WorkspaceはGemでドライブの文書を読ませる。ChatGPT Businessはプラグインに参照ファイルを付ける。Difyはナレッジに文書を入れてWebアプリで配る" loading="lazy"></figure>

### Microsoft 365で組む

Microsoft 365 Copilotのアプリにあるエージェント ビルダーでは、知識の元としてSharePointのファイルをエージェントごとに100個まで、OneDriveのファイルを50個まで、手元から上げるファイルを20個まで選べます。[ナレッジ ソースを追加する](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/agent-builder-add-knowledge)のページによると、エージェントはファイルの既存のアクセス許可と秘密度ラベルに従います。**その文書を開く権限の無い社員が聞いても、文書の中身をもとにした答えは出てこない仕組みです。**

<figure class="post-figure"><img src="/media/images/internal-chatbot/icb_shot_learn_limits.png" alt="Microsoft Learnのナレッジ ソースの制限の表。SharePointのファイルはエージェントごとに最大100個、SharePointのリストは1つ、OneDriveのファイルは50個で、既存のアクセス許可と秘密度ラベルを尊重する" loading="lazy"><figcaption>Microsoft Learn「エージェント ビルダーでエージェントにナレッジ ソースを追加する」（2026年10月29日）</figcaption></figure>

M365 Copilotのライセンスを持つ社員がMicrosoft 365の中で使う分は追加の費用がかからず、持たない社員が使うとクレジットが減ります。部署を越えて配る、業務システムにつなぐ段になったらCopilot Studioに移す流れです。払い方の3通りは[Copilot Studioの料金](/media/copilot-studio/)で扱いました。

### Google Workspaceで組む

Geminiアプリで作るGemは、カスタムの指示と知識のファイルを持たせたボットです。[Gem を使用する](https://support.google.com/gemini/answer/15146780?hl=ja)のヘルプによると、Googleドライブから加えたファイルは最新の版が使われるので、規程を直せばGemの答えにも反映されます。

社内への配り方は[Gem を共有する](https://support.google.com/gemini/answer/16504957?hl=ja)にあり、特定のユーザーを閲覧者か編集者として加えるか、一般的なアクセスを［組織内］にします。気をつけたいのは共有の相手です。**Gemに上げた指示とファイルは、Gemを開ける全員が中身を見られます。**NotebookLMのノートブックは共有するGemのソースに使えず、共有そのものもドライブの共有設定に従い管理者が止められます。部署をまたいで社内のシステムにつなぐエージェントは、別の製品の[Gemini Enterprise](/media/gemini-enterprise/)の範囲です。

<figure class="post-figure"><img src="/media/images/internal-chatbot/icb_shot_gem_share.png" alt="Gemini アプリ ヘルプのGemを共有するのページ。Gemにアップロードしたカスタム指示とファイルはGemにアクセスできるすべてのユーザーが閲覧できるという注意書き" loading="lazy"><figcaption>Gemini アプリ ヘルプ「Gemini アプリで Gem を共有する」（2026年10月29日）</figcaption></figure>

### ChatGPT Businessで組む

ChatGPTで社内向けのボットといえばGPTsでしたが、GPTsは終了に向けてプラグインへ移る途中にあります。OpenAIの[移行ガイド](https://learn.chatgpt.com/docs/migrate-custom-gpts)によると、プラグインはスキル（作業の指示と参照ファイル）とアプリ（ほかのサービスとの接続）をまとめたものです。アプリはその社員がもともと開ける範囲でしか動かず、Googleドライブにつないでも他人の文書は読めません。

**これから作るなら、移行の手間を避けるためにプラグインで始めます。** 共有の範囲と移行の日程は[GPTsを社内だけで共有する方法](/media/gpts-internal-share/)、料金は[ChatGPT Businessの解説](/media/chatgpt-business/)にまとめました。

### Difyで組む

Difyは使うモデルを自分で選べ、社内のサーバーにも置ける開発基盤です。[従来型ナレッジベース](https://docs.dify.ai/ja/use-dify/knowledge/readme)のドキュメントでは、文書の切り方・探せる形にする方法・探し方を自分で設定し、すでに運用している外部の検索にもつなげられると説明しています。画面の操作で作れる反面、モデルの代金の見積もりと、設定を詰める担当者が要ります。プランと代金の見積もり方は[Difyの料金](/media/dify-pricing/)で扱いました。

## RAGの仕組み

RAGのモデルは社内文書を覚えるわけではなく、質問のたびに文書を探して読む手順を踏みます。流れは4段です。

1. 文書を数百字ごとの断片（チャンク）に切り、探せる形で保存する
2. 質問が来たら、意味の近い断片を探す
3. 見つけた断片を質問と一緒にモデルに渡す
4. モデルが断片をもとに答え、元の文書を出典として示す

<figure class="post-figure"><img src="/media/images/internal-chatbot/icb_03_rag.png" alt="RAGの流れを4段で縦に並べた図。文書を断片に切って保存する、質問に近い断片を探す、断片を質問と一緒にモデルに渡す、断片をもとに答えて出典を示す" loading="lazy"></figure>

Difyの[Test and Tune Retrieval](https://docs.dify.ai/en/cloud/use-dify/knowledge-base/test-and-tune)は、本当の試験は利用者が聞く質問に正しい断片が返るかどうかだ、と書いています。**答えの質はモデルより先に、正しい断片を探し出せるかで決まります。**

断片に切ると、文書の前提が抜け落ちる場合もあります。池田朋弘さんのチャンネルの[RAGの精度を上げる6つのポイント](https://www.youtube.com/watch?v=YIxOw0EbM4M)では、100ページのPDFで製品名が表紙にしか書かれておらず、本文の断片だけでは何の製品の話か分からなかった例が出てきました。文書名や対象を断片に添えると精度が2〜3割上がった、と出演者は話していました（出演者の経験値で、第三者の検証はありません）。添える情報の例です。

```text
文書名: 経費精算規程（2026年4月改定）
対象: 正社員・契約社員
担当部署: 経理
断片: 立て替えた交通費は、翌月5日までに申請する。
```

## 失敗しやすい4つの所

製品を買っても自社で組んでも、つまずく所はほぼ同じです。

### 古い文書が残る

同じ規程の旧版と新版が両方入っていれば、ボットはどちらも答えの材料にしてしまいます。Difyの[Maintain an Agent Knowledge Base](https://docs.dify.ai/en/cloud/use-dify/knowledge-base/maintain-knowledge-base)によると、同じ名前のファイルを上げても置き換わらず、2つ目の文書として加わる仕様です。同期が7日以上成功していない取り込み元には、古くなっているという警告が出ます。**配る前に最新版を1か所に集め、旧版は外すか無効にしておきます。**

### 答えの根拠が見えない

答えを信じてよいか社員が判断できなければ、問い合わせは担当者に戻ってきます。Gemには回答から知識の引用を消す設定がありますが、社内向けなら出典は残したほうが確かめやすいでしょう。Microsoftのナレッジ ソースのページも、知識の元を加えたら、その元で答えられる質問を試し、想定どおりの情報が使われたかを見るよう書いています。

### 更新する人がいない

規程は毎年変わるのに、ボットを作った人が異動すると中身はそこで止まったままです。OpenAIの移行ガイドは、GPTごとに担当者を決め、目的・使う相手・指示・参照ファイル・連携先を書き残すよう勧めています。**文書の持ち主（人事・総務・経理）と、ボットの設定を直す人を分けて名前で決めておきます。**

### 個人情報と権限

権限の広すぎるフォルダーを読ませれば、本来は見られない社員の答えにも中身が出かねません。Microsoftの[エージェント ビルダーの概要](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/agent-builder)は既知の制限として、SharePointのファイルの自動共有は特定のセキュリティ グループに共有するときだけで、組織の全員に共有するときには付かないと書いています。個人データを入力する場面について、[個人情報保護委員会の注意喚起](https://www.ppc.go.jp/news/careful_information/230602_AI_utilize_alert/)（2023年6月2日）は、本人の同意なく入力した個人データが応答の出力以外の目的で扱われれば、法の規定に違反するおそれがあるとしています。人事評価や給与の個別の情報は、最初の文書から外してください。

## 会社が決めること

作り方より先に決めておくことは4つです。

- **対象の問い合わせ**：人事・総務・情シスに届いた質問を多い順に並べ、上から選ぶ
- **最初に入れる文書**：対象の質問に答える規程とマニュアルの最新版だけ
- **答えられないときの引き継ぎ先**：部署ごとの窓口と、引き継いだ記録の置き場所
- **効いたかの測り方**：担当部署に届く問い合わせの件数と、ボットで終わった質問の割合（自己解決率）

<figure class="post-figure"><img src="/media/images/internal-chatbot/icb_04_decide.png" alt="社内チャットボットを入れる前に会社が決める4つを縦に並べた図。対象の問い合わせ、最初に入れる文書、答えられないときの引き継ぎ先、効いたかの測り方" loading="lazy"></figure>

問い合わせの件数は、入れる前と同じ数え方で比べないと増減が分かりません。答えられなかった質問も見ておきます。Difyのナレッジでは届いた質問を「何も見つからない」「見つかったが確度が低い」「答えた」に分けて数えられ、よく聞かれる質問を正解の断片と組で登録しておけば、設定を変えるたびに答えが崩れていないかを確かめられます。

買うか組むかの分かれ目になる条件を表にしました。

| 条件 | 向く方 |
|---|---|
| 社員の大半がMicrosoft 365かWorkspaceを使い、対象は社内規程の質問 | 自社の契約で組む |
| 担当者への引き継ぎと対応の記録まで1つの画面で回したい | 製品を買う |
| 作って直す担当者を社内に置けない | 製品を買う |
| モデルを選びたい・自社のサーバーに置きたい | Difyで組む |

作り方そのものの3通りの比較は[AIエージェントの作り方](/media/ai-agent-build/)にあります。

## よくある質問

### 社内チャットボットは無料で作れますか？

すでに契約している基盤の中なら、新しい契約なしで始められます。M365 Copilotのライセンスを持つ社員がエージェント ビルダーで作って使う分には追加の費用がかかりません。Difyの無料のSandboxは1人・200クレジットが一度きりで、試作向けです。

### M365 Copilotのエージェントは有料ですか？

ライセンスを持つ社員がMicrosoft 365の中で使う分はかかりません（公正利用の上限があります）。ライセンスを持たない社員が使う分と、社外に公開する分はCopilot Studioのクレジットが減ります。

### GeminiのGemは社内だけで共有できますか？

できます。特定のユーザーを加えるか、一般的なアクセスを［組織内］にします。Gemに上げた指示とファイルは共有した相手全員が見られるので、見せたくない文書は入れません。

### ChatGPTのGPTsで社内ボットを作れますか？

GPTsはプラグインへの移行が進んでいて、Enterpriseは2026年12月11日に終了する予定です。これから作るならプラグインで作り、ワークスペースの中で共有します。

### Difyの社内チャットボットは何人まで使えますか？

クラウド版のTeamはメンバー50人までで、月159ドルです。公開したWebアプリを使うだけの社員がメンバーの数に入るかは、料金ページに書かれていません。

### 社内チャットボットは製品と自作のどちらが安いですか？

人数と質問の回数で変わります。人数で月額が決まる製品は社員が多いほど高く、OfficeAI社員のBasicのような定額の製品は人数にかかわらず月15万円です。自社の契約で組むと追加の契約は小さく済む一方、文書を整えて直す人の時間がかかります。

### 社内チャットボットの効果は何で測りますか？

担当部署に届く問い合わせの件数と、ボットで終わった質問の割合を、入れる前と同じ数え方で比べます。答えられなかった質問の一覧は、次に足す文書を決める材料になります。

## 出典

- Microsoft Learn「[エージェント ビルダーの概要](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/agent-builder)」「[エージェント ビルダーでエージェントにナレッジ ソースを追加する](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/agent-builder-add-knowledge)」「[請求レートと管理](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/requirements-messages-management)」
- Microsoft「[Microsoft Copilot Studio プランと価格](https://www.microsoft.com/ja-jp/microsoft-365-copilot/pricing/copilot-studio)」
- Gemini アプリ ヘルプ「[Gemini アプリで Gem を使用する](https://support.google.com/gemini/answer/15146780?hl=ja)」「[Gemini アプリで Gem を共有する](https://support.google.com/gemini/answer/16504957?hl=ja)」
- Google Workspace「[料金プラン](https://workspace.google.com/intl/ja/pricing.html)」
- OpenAI「[Moving your custom GPT workflows to plugins](https://learn.chatgpt.com/docs/migrate-custom-gpts)」
- Dify Docs「[従来型ナレッジベース](https://docs.dify.ai/ja/use-dify/knowledge/readme)」「[Test and Tune Retrieval](https://docs.dify.ai/en/cloud/use-dify/knowledge-base/test-and-tune)」「[Maintain an Agent Knowledge Base](https://docs.dify.ai/en/cloud/use-dify/knowledge-base/maintain-knowledge-base)」、Dify「[料金](https://dify.ai/jp/pricing)」
- HiTTO「[料金体系](https://hitto.jp/price/)」、OfficeAI社員「[料金プラン](https://officebot.jp/price/)」、PKSHA「[PKSHA AIヘルプデスク](https://aisaas.pkshatech.com/ai-helpdesk/)」
- 個人情報保護委員会「[生成AIサービスの利用に関する注意喚起等について](https://www.ppc.go.jp/news/careful_information/230602_AI_utilize_alert/)」（2023年6月2日）
- 池田朋弘の生成AIビジネス活用研究所「[RAGの精度を上げる6つのポイント](https://www.youtube.com/watch?v=YIxOw0EbM4M)」
