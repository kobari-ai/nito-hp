---
title: 【2026年9月】ChatGPTで上限に達したときのリセット時間と対処｜無料版・Plus・Pro・Codex
date: 2026-09-25
category: AI検索対策
description: ChatGPTで上限に達したと表示されたときに、どの上限に当たったかを5種類に分けて整理。リセット時刻の見方、Pro・Businessのモデル別の上限、WorkとCodexの5時間枠と週間枠、即時リセットの購入までOpenAI公式ヘルプで確認。
cover_tag: 使い方
cover_headline: ChatGPTの上限とリセット時間
cover_sub: 無料版・Plus・Pro・Codexの違いと対処
---

ChatGPTで上限に達したと表示されても、止まっているのはアカウント全体ではなく、特定の機能かモデルです。OpenAIのProプランのヘルプには、**モデルの利用枠に達するとリセットまでそのモデルが一時的に使えなくなるが、アカウントの制限やサブスクリプションの終了を意味しない**と書かれています。

9月25日時点のヘルプを読むと、上限の種類は1つではありません。GPT-6 Proには週ごとの件数があり、WorkとCodexの枠には有料の即時リセットと、9月上旬に配られた保存済みのリセットがあります。この記事ではOpenAIのヘルプの9月25日時点の記述をもとに、どの上限に当たったかの見分け方、リセットの時刻、待つ以外の手を整理します。

:::takeaways
- 上限は**ツール・思考・Proモデル・WorkとCodex・一時的な利用制限**の5種類。止まるのはその機能かモデルだけ
- 無料版とGoのテキストのチャットは回数無制限。上限があるのは画像やアップロードなどのツール
- リセットの時刻は、分かる場合はChatGPTの画面に表示される。**サポートに頼んでも上限はリセットされない**
- WorkとCodexの5時間枠は、**前の枠が終わったあと最初のメッセージを送った時点から始まる**
- Plus・Proの個人アカウントは、WorkとCodexの枠を**有料ですぐに戻せる**。戻すと週の区切りも変わる
:::

## 上限は5種類

上限に達したという表示はどの機能を使っていたかで意味が変わります。OpenAIの[ChatGPTでのGPT-5.6とGPT-6 Pro](https://help.openai.com/ja-jp/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt)と[WorkとCodexでのGPT-6 Astraの利用量管理](https://help.openai.com/ja-jp/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)を読むと、上限は5つに分かれます。

<figure class="post-figure"><img src="/media/images/chatgpt-limit-reached/00_fig_kinds.png" alt="ChatGPTの上限5種類の図。無料版とGoのツールの上限は画像やアップロードなどでテキストは無制限、有料プランの思考の上限はGPT-5.6 Solで別のモデルで続くことがある、Pro・BusinessのProモデルの上限はGPT-6 ProでPro 100ドルは週50件、Plus・ProのWorkとCodexの上限は5時間枠と週間枠、全プランの一時的な利用制限は不正利用を防ぐ仕組み" loading="lazy"><figcaption>どこで止まったかで戻り方が違う</figcaption></figure>

| 上限 | 対象のプラン | 何が止まるか | 戻り方 |
|---|---|---|---|
| ツールの上限 | 無料版・Go | 画像生成・アップロード・音声・データ分析 | 表示された時刻まで待つ。Plus以上に変える |
| 思考の上限 | 有料プラン | 中程度・高・超高で使うGPT-5.6 Sol | 別のモデルで続くことがある。時刻まで待つ |
| Proモデルの上限 | Pro・Business | GPT-6 ProとGPT-5.6 Sol Pro | 別のモデルを使う。枠の回復を待つ |
| WorkとCodexの上限 | Plus・Pro・Business | WorkとCodexでの作業 | 5時間枠と週間枠の回復、リセットの利用 |
| 一時的な利用制限 | 全プラン | 不正利用と判断された操作 | ChatGPTの通知に従う |

**表示が出たときに使っていた機能を思い出すと、どの行に当たるかが分かります。**チャットで画像を頼んでいたならツールの上限、Codexで作業していたならWorkとCodexの上限です。

## 無料版とGoの上限

無料版とGoでは日常のテキストのチャットは回数無制限です。[ChatGPT 無料版に関するよくある質問](https://help.openai.com/ja-jp/articles/9275245-chatgpt-free-tier-faq)によると、ファイルのアップロード、画像生成、音声、データ分析などのツールには、それぞれ別の上限があります。上限に達するとChatGPTから通知が出ます。

<figure class="post-figure"><img src="/media/images/chatgpt-limit-reached/clr_04_help_free.jpg" alt="OpenAI公式ヘルプのChatGPT無料版に関するよくある質問のページ。無料プランのレート制限の仕組みとして、日常的なテキストチャットは回数無制限、ファイルのアップロードや画像生成などのツールにはそれぞれ個別の利用上限があると書かれ、下に画像作成の上限に達したときの通知の例が載っている" loading="lazy"><figcaption>無料版の上限の仕組みと、通知の例（2026年9月25日取得）</figcaption></figure>

通知の例には「Plusにアップグレードするか、明日の9:17以降にもう一度試してください」という内容が書かれています。**同じFAQによると、無料版で上限に達したあとPlus・Pro・Businessに変えると、上限はその場でリセットされます。**Goはこの対象に書かれていません。

画像生成の上限については[ChatGPTの画像生成ができない原因の記事](/media/chatgpt-image-limit/)で、原因の見分け方を詳しく扱っています。

## 有料プランの思考とProモデルの上限

有料プランでは思考のレベル（中程度・高・超高）を選ぶとGPT-5.6 Solが使われます。**思考の上限に達すると、ChatGPTは別の利用可能なモデルで処理を続けることがあります。**止まらずに答えが返ってきても、使われたモデルが変わっている場合があるということです。

### GPT-6 Proの週ごとの件数

ProプランとBusinessでは、GPT-6 ProとGPT-5.6 Sol Proに件数の上限があります。公式ヘルプには**Proの契約にGPT-6 Proの無制限の利用は含まれない**と明記されています。

<figure class="post-figure"><img src="/media/images/chatgpt-limit-reached/clr_01_help_pro.jpg" alt="OpenAI公式ヘルプのChatGPTでのGPT-5.6とGPT-6 Proのページ。思考の利用上限と代替モデルの説明の下に、GPT-6 Pro and GPT-5.6 Sol Pro limitsの表があり、Pro 200ドルは週200件、Pro 100ドルは週50件、Business Standardは月15件、Business Premiumは週50件と書かれている" loading="lazy"><figcaption>Proモデルの件数が載っている公式ヘルプ（2026年9月25日取得）</figcaption></figure>

| プラン | GPT-6 Proの件数（チャット） | GPT-5.6 Sol Proとの関係 |
|---|---|---|
| Pro $200 | 週200件 | Sol Proは別に1日170件。2つ合わせて1日200件まで |
| Pro $100 | 週50件 | 2つのモデルで週50件を共有 |
| Business Standard | 月15件 | 2つのモデルで月15件を共有 |
| Business Premium | 週50件 | 2つのモデルで週50件を共有 |

Pro $200でGPT-6 Proの週の上限に達すると、ChatGPTは自動で思考「中程度」のGPT-5.6に切り替わります。Pro $100とBusinessは2つのモデルで1つの枠を共有しているため、**モデルを切り替えても件数は増えません。**これらの件数はチャットでの上限で、WorkとCodexには別の枠があります。

## WorkとCodexの上限

WorkとCodexはプランに含まれる1つの利用枠を共有しています。プランによっては5時間枠と週間枠の両方があり、**続けて使うには両方に枠が残っている必要があります。**

<figure class="post-figure"><img src="/media/images/chatgpt-limit-reached/01_fig_work.png" alt="WorkとCodexの枠がいつ戻るかの図。5時間の枠は前の枠が終わったあと最初のメッセージを送った時点から次の枠が始まり、週の枠が残っていても先に尽きることがある。週間の枠は1週間に使える作業量の上限で、残りと時刻は設定の使用状況で見られる。即時リセットの購入はPlusとProの個人アカウントが対象で、次の週の区切りは購入後の最初の依頼から7日後に変わる" loading="lazy"><figcaption>WorkとCodexの枠の戻り方</figcaption></figure>

公式ヘルプによると、5時間枠は**前の枠が終わったあと、WorkかCodexで最初のメッセージを送った時点から次の枠が始まります。**しばらく使っていなければ、次に送った時点から新しい5時間が数えられます。週間枠が残っていても、5時間が経つ前に5時間枠を使い切ることはあります。

現在の残りとリセットの時刻を見る場所は、設定の「使用状況」です。プランごとの枠の大きさは[ChatGPT Workのプランと上限の記事](/media/chatgpt-work-plans/)にまとめました。

### 保存済みリセット

GPT-6 Astraの提供開始に合わせて、OpenAIは対象のPlus・Pro・Businessのアカウントに**保存済みのリセット**を配りました。[保存済みCodexリセットの仕組み](https://help.openai.com/ja-jp/articles/20001498-how-banked-codex-resets-work)によると、これはCodexの5時間枠と週間枠を1回だけ戻せる特典で、使うまでアカウントに残ります。

設定の「使用状況」に「利用可能なリセット：1回」などと出ていれば、そこから選んで使えます。使うと週のリセット日が変わり、期限を過ぎると復元や再発行はできません。今後も配られるとは限らない、とも書かれています。

## 即時リセットを購入する

WorkとCodexの枠は、お金を払ってすぐに戻すこともできます。[Paid weekly Work and Codex rate limit resets](https://help.openai.com/ja-jp/articles/20001507-paid-weekly-work-and-codex-rate-limit-resets)によると、対象はPlusとProの個人アカウントで、無料版・Go・Business・Enterprise・Eduでは使えません。

<figure class="post-figure"><img src="/media/images/chatgpt-limit-reached/clr_02_help_reset.jpg" alt="OpenAI公式ヘルプのPaid weekly Work and Codex rate limit resetsのページ。PlusとProの利用者はデスクトップ版の使用状況の設定か、週の上限に達したときのアプリ内の案内から即時リセットを購入でき、5時間と週間の両方の枠がすぐ戻ること、新しい週の期間はリセット後のWorkかCodexでの最初の依頼から始まり次の自動リセットはその7日後になることが書かれている" loading="lazy"><figcaption>即時リセットの購入を説明した公式ヘルプ（英語版のみ、2026年9月25日取得）</figcaption></figure>

買う場所は2つあります。

1. デスクトップ版の使用状況の設定で、使用量のメーターの横にある「Buy an instant reset」を選ぶ
2. 週の上限に達したときにアプリ内に出る案内を選ぶ

**購入するとその場で5時間枠と週間枠が戻り、枠が残っていても待たずに適用されます。**後で使うために取っておくことはできません。次の週の区切りはリセット後にWorkかCodexで最初の依頼を送った時点から7日後に変わります。返金は原則として受けていないと書かれているので、残りの枠を使い切ってから買うかどうかを決めます。

5時間枠だけに達した場合、アプリ内の案内は出ません。その場合でも、デスクトップ版の設定から買える場合があります。価格は画面に表示され、アカウントや請求の国によって買えるかどうかが変わります。

## 上限に達したときの対処

どの上限でも、取れる手は次の5つのどれかです。

<figure class="post-figure"><img src="/media/images/chatgpt-limit-reached/02_fig_choices.png" alt="上限に達したときに取れる手の図。待つは全プランで表示されたリセット時刻まで待つ。別のモデルは有料プランで、上限は機能やモデルごとなのでほかのモデルは使える。プランを上げるは無料版からPlus・Pro・Businessに変えると上限がリセット。リセットを使うはWorkとCodexで保存済みリセットか即時リセットの購入。サポートに頼むはできず、数え間違いの調査だけ" loading="lazy"><figcaption>上限に達したときの5つの手</figcaption></figure>

| 手 | 使える場面 | 注意 |
|---|---|---|
| 待つ | すべての上限 | 時刻は分かる場合だけ画面に出る |
| 別のモデルを使う | 有料プランの思考・Proモデル | 同じ枠を共有するモデルでは増えない |
| プランを上げる | 無料版のツールの上限 | Plus・Pro・Businessに変えると上限がリセット |
| リセットを使う | WorkとCodex | 週のリセット日が変わる |
| サポートに頼む | 使えない | 数え間違いや、時刻を過ぎても戻らないときの調査だけ |

### サポートは上限をリセットしない

ChatGPT Proのヘルプには、**OpenAIのサポートはChatGPTやCodexの利用上限をリセットしない**とはっきり書かれています。問い合わせてよいのは使用量が誤って数えられたと思うときと、表示されたリセット時刻を過ぎても使えないときです。

<figure class="post-figure"><img src="/media/images/chatgpt-limit-reached/clr_03_help_faq.jpg" alt="OpenAI公式ヘルプのChatGPT Proのページのよくある質問。サポートに利用上限をリセットしてもらえますか、という質問に、いいえ、OpenAIサポートではChatGPTまたはCodexの利用上限のリセットは行っていません、上限に達した場合はリセットされるまで待つかアカウントに表示されている別の利用可能なオプションを使用してください、と答えている" loading="lazy"><figcaption>サポートでのリセットはできないと書かれた公式ヘルプ（2026年9月25日取得）</figcaption></figure>

### 会話の長さで止まったとき

1つの会話が長くなりすぎて止まる場合は、ここまでの上限とは別の問題です。料金ページの注記にはChatGPTが共有のコンテキストウィンドウを管理しており、利用者が入力に使える領域はウィンドウ全体より小さいと書かれています。**会話が長くなって続けられないときは、要点をまとめて新しいチャットで続けてください。**

## よくある質問

### ChatGPTの上限に達したらリセットされますか？

されます。上限に達した機能やモデルは、リセットされるまで一時的に使えなくなるだけです。リセットの時刻は情報を取得できる場合にChatGPTの画面に表示されます。

### ChatGPTの無料版は1日何回まで使えますか？

テキストのチャットは回数無制限です。画像生成、ファイルのアップロード、音声、データ分析などのツールにはそれぞれ上限があり、回数は公開されていません。

### ChatGPT Plusの上限は何時にリセットされますか？

決まった時刻はありません。思考やWork、Codexなど上限の種類ごとに戻る時刻が違い、分かる場合は画面に表示されます。WorkとCodexの残りとリセットの時刻は、設定の「使用状況」に出ています。

### 上限に達したらアカウントが制限されたのですか？

アカウントの制限ではありません。Proプランの公式ヘルプの説明では、モデルの利用枠に達したことはアカウントの制限やサブスクリプションの終了を意味しないとされています。

### ChatGPTの上限をサポートに解除してもらえますか？

できません。OpenAIのサポートは利用上限のリセットを行っていません。表示された時刻を過ぎても使えないときや、使用量が誤って数えられたと思うときは調査を頼めます。

### Codexの上限をすぐに戻す方法はありますか？

PlusとProの個人アカウントなら、デスクトップ版の使用状況の設定か、週の上限に達したときの案内から即時リセットを買えます。保存済みリセットが配られていれば、設定の「使用状況」から使えます。

### GPT-6 ProはProプランなら無制限ですか？

無制限ではありません。チャットでのGPT-6 Proは、Pro $200で週200件、Pro $100で週50件までです。

### 無料版で上限に達したあと有料プランにすればすぐ使えますか？

使えます。無料版で上限に達したあとPlus・Pro・Businessに変えると、利用上限がリセットされると公式FAQに書かれています。

## 出典

- OpenAI Help Center「[ChatGPT での GPT-5.6 と GPT-6 Pro](https://help.openai.com/ja-jp/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt)」（2026年9月25日取得）
- OpenAI Help Center「[ChatGPT 無料版に関するよくある質問](https://help.openai.com/ja-jp/articles/9275245-chatgpt-free-tier-faq)」（同）
- OpenAI Help Center「[ChatGPT Pro プランの概要](https://help.openai.com/articles/9793128)」（同）
- OpenAI Help Center「[Work と Codex での GPT-6 Astra の利用量管理](https://help.openai.com/ja-jp/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)」（同）
- OpenAI Help Center「[保存済み Codex リセットの仕組み](https://help.openai.com/ja-jp/articles/20001498-how-banked-codex-resets-work)」（同）
- OpenAI Help Center「[Paid weekly Work and Codex rate limit resets](https://help.openai.com/ja-jp/articles/20001507-paid-weekly-work-and-codex-rate-limit-resets)」（同）
- ChatGPT「[料金](https://chatgpt.com/ja-JP/pricing/)」（同）
