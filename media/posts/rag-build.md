---
title: 【2026年10月】RAG構築とは？作り方3通りと手順・費用・自社で作るか外注か
date: 2026-10-31
category: AI活用
description: RAG構築の方法を既製品の機能・ノーコード・クラウドの部品の3通りで比較。手順と表の多いPDFや権限でつまずく所、Azure・AWS・Google・OpenAIの公式料金での試算、自社で作るか外注かの分かれ目まで。
keyword: rag 構築
cover_tag: 導入担当向け
cover_headline: RAG構築の進め方
cover_sub: 作り方3通りと費用・自社か外注か
cta: ai_agent
---

Amazon Bedrockは、社内文書の取り込みから検索までをAWSに任せるManaged Knowledge Baseを料金表に載せています。Microsoft・Google・OpenAIも同じ役目の部品を出しており、RAGは一から組むより、どの部品をどこまで使うかを選ぶものになりました。

社内の文書にAIを答えさせたい情シス・DX担当や経営者に向けて、作り方の3通りと手順・つまずく所・公式の料金での試算、自社で作るか外注かの分かれ目を書きます。各社のサービスでの構築は試していません。

:::takeaways
- **RAG構築は既製品の機能・ノーコードの道具・クラウドの部品の3通りから選ぶ**。差は検索の部分をどこまで自分で持つか
- **検索の部品の月額は文書2GB・月1万回の試算で数千円から1.5万円ほど**。費用の大半は文書を整えて答えを確かめる人の時間
- **つまずくのは表や図の多いPDF・権限・答えの確かめ方**。どれも作る前に決めておくことがある
:::

## RAG構築とは

RAG（検索拡張生成）は質問のたびに社内の文書から関係する箇所を探し、その箇所をAIに渡して答えさせる仕組みです。AIが社内文書を覚えるわけではないので、規程を直せば次の質問から新しい版で答えます。**文書を取り込んで探せる形にし、探した結果をAIに渡す流れを自社用に組むのがRAG構築です。** 文書を断片に切って探す4段の流れは[社内チャットボットの選び方](/media/internal-chatbot/)で図にしました。ここではその流れを作る側の決めごとを扱います。

AIエージェントが道具の1つとして社内文書を探すときも、その中身はRAGと同じです。エージェントそのものの説明は[AIエージェントとは](/media/ai-agent-guide/)にあります。

## RAG構築の作り方は3通り

検索の部分をどこまで自分で持つかで、作り方は3つに分かれます。

| | ①既製品の機能 | ②ノーコード・ローコード | ③クラウドの部品 |
|---|---|---|---|
| 例 | M365 Copilotのエージェント ビルダー・GeminiのGem・ChatGPT Businessのプラグイン | Dify・Copilot Studio・n8n | Azure AI Search・Amazon Bedrock ナレッジベース・Google Agent Search・OpenAIのファイル検索 |
| 向く会社 | 社員の大半が同じ業務基盤を使っている | 担当者が画面で設定を詰められる | 自社のシステムや画面に組み込みたい |
| 試作までの手間 | 契約の中ですぐ試せる | アカウントと文書の取り込み | 開発者がAPIをつなぐ |
| 費用の数え方 | 1人あたりの月額に含まれる | プランの月額とモデルの代金 | 保存量と質問の回数 |
| 保守 | 提供元が直す | 設定と取り込みは自社 | 全部自社か外注先 |

<!-- SHOT: 図 rag1031_three.html → rag_01_three.png・alt「RAG構築の作り方3通りを縦に並べた図。既製品の機能は契約の中ですぐ試せる。ノーコードとローコードは画面で分け方や探し方を詰める。クラウドの部品は自社のシステムに組み込む」 -->

**選ぶ基準は答えが外れたときにどこまで自分で直したいかです。** ①は直せる所が少ない代わりに保守が要らず、③は分け方から権限まで全部を決められる代わりに直す人が要ります。AIエージェント全体の作り方を3通りに分けた[AIエージェントの作り方](/media/ai-agent-build/)では、Copilot Studioを既製の基盤の例に置きました。文書の取り込みと検索の設定を画面で触れるため、RAGの話では②に入れています。

### 既製品の機能で作る

Microsoft 365・Google Workspace・ChatGPT Businessの契約があれば、その中で文書に答えるボットを作れます。M365 Copilotのエージェント ビルダーはSharePointのファイルを100個まで読み、GeminiのGemはGoogleドライブの最新の版を使います。分け方や探し方は選べません。規程集やマニュアルのように文章が中心の文書から始める用途に向き、基盤ごとの上限と共有の範囲は[社内チャットボットの選び方](/media/internal-chatbot/)で比べました。

### ノーコード・ローコードで作る

Difyは文書の切り方と探し方を画面で選べる道具です。[Difyのチャンク設定](https://docs.dify.ai/ja/use-dify/knowledge/create-knowledge/chunking-and-cleaning-text)には、すべての断片を同じ長さで切る汎用モードと、小さな断片で探して前後を含む大きな断片を返す親子モードがあります。Copilot Studioは[ファイルのアップロード](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/knowledge-add-file-upload)で500個までのファイルを持たせられ、SharePointにもつなげます。n8nは業務の自動化の流れに検索を差し込む使い方が中心です。料金はそれぞれ[Difyの料金](/media/dify-pricing/)・[Copilot Studioの料金](/media/copilot-studio/)・[n8nの料金](/media/n8n-pricing/)にまとめました。

### クラウドの部品で組む

自社の業務システムや社外向けの画面に組み込むなら、クラウドの検索の部品を使います。**Amazon Bedrockの[ナレッジベースの概要](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)によると、Managed Knowledge BaseはS3・SharePoint・Confluence・Googleドライブ・OneDriveにつなぎ、文書ごとの権限で検索結果を絞れます。** 自分で検索の土台を選ぶ従来の型では、外部へのコネクタと文書単位の権限は使えません。Googleは同じ役目の製品をVertex AI SearchからAgent Searchへ改名中で、社内データの検索を含む全体は[Gemini Enterprise](/media/gemini-enterprise/)の範囲です。

## RAG構築の手順

上位の解説記事が挙げる手順は、文書の収集・分割・ベクトル化・検索・回答の生成の5段が中心でした。会社で作るときはその前後に目的の決定と権限・運用が入ります。

<!-- SHOT: 図 rag1031_steps.html → rag_02_steps.png・alt「RAG構築の手順を6段で縦に並べた図。目的と問いを決める、文書を集めて整える、分け方と探し方を決める、答えを確かめる、権限とログを決める、運用で直し続ける」 -->

### 目的と問いを決める

人事・総務・情シスに届いた質問を集め、答えに使う文書がはっきりしている質問から30〜50問を選びます。だれのどんな質問に答えさせるかが決まらないと、入れる文書も決まりません。**この質問の一覧が後の手順で答えを確かめる試験問題になります。**

### 文書を集めて整える

対象の質問に答える文書の最新版だけを集めます。旧版や下書きが混ざるとAIは古い規程を根拠に答えてしまうため、置き場所は1か所にまとめます。断片に切った後も何の文書か読み取れるよう、文書名・改定日・対象者を文書に添えておくのが基本です。

### 分け方と探し方を決める

Microsoftの[チャンク分割の解説](https://learn.microsoft.com/ja-jp/azure/search/vector-search-how-to-chunk-documents)は、200語や600文字ほどの固定の長さに10〜15%の重なりを持たせる方法を最初に挙げています。[OpenAIのファイル検索](https://developers.openai.com/api/docs/guides/retrieval)の既定は800トークンで、前後400トークンを重ねる設定です。意味の近さで探すベクトル検索と語の一致で探す全文検索を組み合わせるハイブリッド検索も、各社の部品で選べます。

### 答えの確かめ方を決める

選んだ質問を流し、正しい文書の断片が返ったかと答えが文書に沿っているかを見ます。正解の文書と答えを質問と組にしておけば、設定を変えるたびに同じ問題で比べられるでしょう。

```text
質問: 立て替えた交通費はいつまでに申請する？
正解の文書: 経費精算規程（2026年4月改定）第5条
正解: 翌月5日まで
```

### 権限とログを決める

だれがどの文書の中身を答えとして受け取れるかを、元の文書の権限に合わせます。質問と答えと使った文書のログを、どこに何日残すかもこの段階で決めておきます。

### 運用で直し続ける

答えられなかった質問と、利用者が誤りと指摘した答えを週に1度読み、足す文書と直す設定を決めます。文書の持ち主と設定を直す人は、分けて名前で決めておくのが前提です。

## RAG構築でつまずく所

上位の記事が共通して挙げるのはデータの質と評価の不足でした。ここでは公式の文書に書かれた仕様のうち、作り始めてから気づきやすいものを4つ挙げます。

### 表や図の多いPDF

**既定の読み取り方のままだと、表や図の中身が失われることがあります。** Amazon Bedrockの[解析の設定](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-advanced-parsing.html)によると、既定のパーサーはテキストだけを取り出す仕様です。そのため図・グラフ・表・画像を含む文書には、Bedrock Data Automationか基盤モデルでの解析を勧めています。Googleの[ドキュメントの解析とチャンク化](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents?hl=ja)でも、既定のデジタル パーサーは表・リスト・見出しを検出しません。料金表や手当の一覧が表で書かれた規程なら、解析の方法を変えて試すか、表を文章に直してから取り込みます。

<!-- SHOT: 画面 https://docs.aws.amazon.com/bedrock/latest/userguide/kb-advanced-parsing.html・Only parses text in text files・赤枠「Amazon Bedrock default parser – Only parses text」の段落と「Because the default parser only outputs text」の段落・PC・alt「Amazon Bedrockのユーザーガイド。既定のパーサーはテキストファイルのテキストだけを解析し、図やグラフや表や画像を含む文書にはBedrock Data Automationか基盤モデルでの解析を勧めると書かれている」・figcaption「Amazon Bedrock ユーザーガイド「Parsing options for your data source」（2026年10月31日）」 -->

Copilot Studioに上げたファイルの画像は、PDFに埋め込まれて代替テキストが付いたものしか読みません。秘密度ラベルやパスワードで暗号化したファイルも上げられない仕様です。

### 分け方を後から変えられない

Difyのナレッジベースは、作った後に汎用か親子かのチャンクモードを変えられません。高品質のインデックスで作ったものを、エコノミーへ切り替えることもできない仕様です。**試作の段階で2つのモードを別のナレッジベースとして作り、同じ質問で比べてから本番の形を決めます。**

### 権限が検索に効かない

元のフォルダーで見られない社員でも、取り込んだ後の検索では中身が出てしまうことがあります。Azure AI Searchの[ドキュメント レベルのアクセス制御](https://learn.microsoft.com/ja-jp/azure/search/search-document-level-access-overview)では、SharePointの権限や秘密度ラベルをそのまま使う方法が2026年10月31日時点でプレビューでした。一般提供の方法で作るなら、文書にだれが見られるかの情報を持たせて検索のたびに絞り込みます。

**n8nのSimple Vector Storeは検証だけに使う置き場です。** [n8nのドキュメント](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory/)によると、データはメモリにだけ置かれ、n8nを再起動するとすべて消えます。保存先のキーもワークフローごとに分かれておらず、同じn8nを使う全員が読めてしまいます。

<!-- SHOT: 画面 https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory/・Data safety limitations・赤枠「Vector store data isn't persistent」と「All instance users can access vector store data」の2つの小見出しと本文・PC・alt「n8nのSimple Vector Storeノードのドキュメント。データはメモリだけに保存されn8nの再起動で消えること、保存先のキーは全体で共通でインスタンスの全ユーザーが読めることが書かれている」・figcaption「n8n Docs「Simple Vector Store node」（2026年10月31日）」 -->

### 答えの確かめ方がない

試験問題を作らずに公開すると、設定を変えたときに良くなったのか悪くなったのかが分かりません。Amazon Bedrockの[RAGの評価の指標](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-metrics.html)は、検索だけの評価と検索と答えの両方の評価に分かれています。返した断片が正解の文書をどれだけ含むかを測る指標には、正解を添えた質問の一覧が必要です。答えが取り出した文書に沿っているか、引用が正しいかを見る指標も並んでいます。

## RAG構築の費用

**費用は作る人の時間・検索の部品・答えを作るモデルの3つに分かれます。** このうち公式の料金表で数えられるのは検索の部品とモデルの代金です。2026年10月31日に各社の料金ページで確かめた単価を並べました。

| 部品 | 保存 | 質問 |
|---|---|---|
| [Azure AI Search](https://azure.microsoft.com/ja-jp/pricing/details/search/) Basic（東日本） | 1時間0.133ドルの定額で15GBまで | 定額に含む |
| [Amazon Bedrock](https://aws.amazon.com/bedrock/pricing/) Managed Knowledge Base | 元データ1GBあたり月5ドル | 1,000回あたり1ドル |
| [Google Agent Search](https://cloud.google.com/generative-ai-app-builder/pricing) | 1GiBあたり月約5ドル（月10GiBは無料） | Standardは1,000回あたり1.5ドル（月1万回の無料トライアルあり） |
| [OpenAIのファイル検索](https://developers.openai.com/api/docs/pricing) | 1GBあたり1日0.1ドル（1GBは無料） | 1,000回あたり2.5ドル |

Azureの金額はMicrosoftの価格APIで東日本の単価を引き、月730時間で数えています。Bedrockは文書の解析・ベクトル化・並べ替えに標準のモデルを使う限り0ドルで、自分で選んだモデルを使うと別料金です。GoogleのEnterpriseは1,000回あたり4ドルで、検索結果からの答えの生成まで含みます。

同じ前提で月額を試算しました（試算。文書2GB・月1万回の質問を仮定し、答えを作るモデルの代金は含めていません）。円は三菱UFJ銀行の[公示仲値](https://www.murc-kawasesouba.jp/fx/index.php)1ドル157.54円（2026年10月30日）での換算です。

| 部品 | 試算の内訳 | 月額 |
|---|---|---|
| Azure AI Search Basic | 0.133ドル×730時間 | 約97ドル（約1.5万円） |
| Bedrock Managed Knowledge Base | 2GB×5ドル＋1万回×1ドル/1,000回 | 20ドル（約3,200円） |
| Google Agent Search Standard | 保存・回数とも無料枠の範囲 | 0ドル |
| OpenAIのファイル検索 | 超過1GB×0.1ドル×30日＋1万回×2.5ドル/1,000回 | 28ドル（約4,400円） |

**この規模なら検索の部品の代金は月数千円から1.5万円ほどに収まります。** Bedrockの料金ページの例でも、SharePointから50GB・約10万文書を取り込んで月10万回検索し、月350ドルです。表の多い文書をData Automationで解析すると1ページ0.01ドルかかり、1,000ページで10ドルになります。予算を左右するのは部品の単価より、文書を整えて試験問題を作り、答えを直し続ける人の時間です。

## 自社で作るか外に頼むか

開発を外に頼むときの相場は、一次の資料で確かめられるものが見つかりませんでした。公開されている金額の例では、横浜市が2025年10月に入札した[RAG機能と高度モデルを備えた生成AIサービスの提供及び活用支援業務委託](https://www.city.yokohama.lg.jp/business/nyusatsu/kakukukyoku/2025/itaku/digital/rag.html)が税抜5,261,600円で落札されています（もう1社の入札は850万円）。サービスの提供と活用の支援をまとめた契約で、個別の開発費ではありません。仕様書の掲載が終わっていたため、期間と利用人数は確かめられませんでした。

金額より先に次の条件で向く方を決めます。

| 条件 | 向く方 |
|---|---|
| 既製品の機能かノーコードで足り、設定を直す担当者を置ける | 自社で作る |
| 自社のシステムや社外向けの画面に組み込む | 外に頼むか開発者を置く |
| 文書ごとの権限を検索に効かせる必要がある | 外に頼むか開発者を置く |
| 公開後に試験問題を回して直す人を社内に置けない | 運用まで含めて外に頼む |

試験問題の質問と正解・文書の持ち主は外に頼む場合でも社内で用意するものです。**対象の質問・文書の量・権限の条件・ログの残し方の4つを書面にしてから見積もりを取ると、各社の答えを同じ形で比べられます。**

## 会社が決めること

作り方より先に社内で決めることが5つあります。

- **対象の質問**：だれのどんな質問に答えさせるかと、試験に使う30〜50問
- **最初に入れる文書**：対象の質問に答える最新版だけ。表の多い文書は解析の方法も
- **権限の扱い**：元の文書の権限を検索に効かせるか、全員が見てよい文書だけにするか
- **ログと保存場所**：質問と答えをどこに何日残すか、データをどの地域に置くか
- **直す人**：文書の持ち主と、設定を直す担当の名前

<!-- SHOT: 図 rag1031_decide.html → rag_03_decide.png・alt「RAG構築の前に会社が決める5つを縦に並べた図。対象の質問、最初に入れる文書、権限の扱い、ログと保存場所、直す人」 -->

## よくある質問

### RAG構築はCopilotやGemの機能でできますか？

社内規程やマニュアルのように文章が中心の文書なら、M365 Copilotのエージェント ビルダー・GeminiのGem・ChatGPT Businessのプラグインで作れます。断片の切り方や探し方は選べません。表の多い文書や自社のシステムへの組み込みが要るなら、②か③の作り方に進みます。

### Amazon BedrockのRAGは月いくらですか？

Managed Knowledge Baseなら保存が元データ1GBあたり月5ドル、検索が1,000回あたり1ドルです。文書2GB・月1万回の試算では検索の部品が月20ドルで、答えを作るモデルの代金が別にかかります。

### Azure AI Searchで権限は効きますか？

SharePointの権限をそのまま使う方法は、2026年10月31日時点でプレビューです。一般提供の方法で作るなら、文書にだれが見られるかの情報を持たせて検索のたびに絞り込みます。

### Difyのチャンクの設定は後から変えられますか？

区切り文字や最大の長さはいつでも変えられます。汎用か親子かのチャンクモードは、ナレッジベースを作った後には変えられません。

### n8nで作ったRAGのデータは消えますか？

Simple Vector Storeに入れたデータは、n8nの再起動で消えます。本番では外部のベクトルデータベースのノードに保存先を変えてください。

### Agent Searchの旧名は何ですか？

Vertex AI Searchです。Googleのドキュメントには、Vertex AI SearchをAgent Searchに改名中と表示されています。

### RAG構築を外注するといくらかかりますか？

公開された相場の資料は見つかりませんでした。対象の文書の量や権限の条件、運用まで頼むかで費用は変わるため、条件を書面にそろえて複数の会社から見積もりを取ります。

## 出典

- Microsoft「[Azure AI Search の価格](https://azure.microsoft.com/ja-jp/pricing/details/search/)」、Microsoft Learn「[ドキュメント レベルのアクセス制御](https://learn.microsoft.com/ja-jp/azure/search/search-document-level-access-overview)」「[RAG とベクター検索用の大きなドキュメントをチャンクする](https://learn.microsoft.com/ja-jp/azure/search/vector-search-how-to-chunk-documents)」
- Microsoft Learn「[ナレッジ ソースとしてファイルをアップロードする](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/knowledge-add-file-upload)」
- AWS「[Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)」、Amazon Bedrock ユーザーガイド「[Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)」「[Parsing options for your data source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-advanced-parsing.html)」「[Use metrics to understand RAG system performance](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-metrics.html)」
- Google Cloud「[Agent Search pricing](https://cloud.google.com/generative-ai-app-builder/pricing)」「[ドキュメントを解析してチャンク化する](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents?hl=ja)」
- OpenAI「[Pricing](https://developers.openai.com/api/docs/pricing)」「[Retrieval](https://developers.openai.com/api/docs/guides/retrieval)」
- Dify Docs「[チャンク設定](https://docs.dify.ai/ja/use-dify/knowledge/create-knowledge/chunking-and-cleaning-text)」「[インデックス方法と検索設定](https://docs.dify.ai/ja/use-dify/knowledge/create-knowledge/setting-indexing-methods)」
- n8n Docs「[RAG in n8n](https://docs.n8n.io/advanced-ai/rag-in-n8n/)」「[Simple Vector Store node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory/)」
- 横浜市「[RAG機能と高度モデルを備えた生成AIサービスの提供及び活用支援業務委託](https://www.city.yokohama.lg.jp/business/nyusatsu/kakukukyoku/2025/itaku/digital/rag.html)」入札結果（2025年10月14日）
- 三菱UFJリサーチ&コンサルティング「[外国為替相場](https://www.murc-kawasesouba.jp/fx/index.php)」（2026年10月30日）
