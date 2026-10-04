---
title: 【2026年10月】ChatGPTで上限に達したときのリセット時間と対処｜無料版・Plus・Pro・Codex
date: 2026-09-25
category: AI検索対策
description: ChatGPTで上限に達したと表示されたときに、どの上限に当たったかを5種類に分けて整理。リセット時刻の見方、Pro 500の追加とProのWorkとCodexの5時間枠の廃止、即時リセットの購入まで公式ヘルプで確認。
cover_tag: 使い方
cover_headline: ChatGPTの上限とリセット時間
cover_sub: 無料版・Plus・Pro・Codexの違いと対処
---

ChatGPTで上限に達したと表示されても、多くの場合止まっているのはアカウント全体ではなく、特定の機能かモデルです。OpenAIの[ChatGPTでのGPT-5.6とGPT-6 Pro](https://help.openai.com/ja-jp/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt)のヘルプには、Proプランについて**利用枠に達しただけでアカウントが制限されたことにはならない**と書かれています。

10月5日にヘルプを読み直すと、9月末から上限の決まりがいくつか変わっていました。Proは月500ドルのPro 500が加わって3段階になり、Proの3プランにはWorkとCodexの5時間ごとの上限が今はありません。この記事ではOpenAIのヘルプの10月5日時点の記述をもとに、どの上限に当たったかの見分け方、リセットの時刻、待つ以外の手を整理します。

:::takeaways
- 上限は**ツール・思考・Proモデル・WorkとCodex・一時的な利用制限**の5種類。止まるのはその機能かモデルだけ
- 無料版とGoのテキストのチャットは回数無制限（不正利用を防ぐ制限の範囲内）。上限があるのは画像やアップロードなどのツール
- リセットの時刻は、分かる場合はChatGPTの画面に表示される。**サポートに頼んでも上限はリセットされない**
- WorkとCodexの5時間枠があるのはPlusとBusiness Standard。**Pro 100・Pro 200・Pro 500には今は5時間ごとの上限がなく、週の枠だけ**
- Plus・Proの個人アカウントは、WorkとCodexの枠を**有料ですぐに戻せる**（次の週の枠を前倒しで使う）。戻すと週の区切りも変わる
:::

## 上限は5種類

上限に達したという表示はどの機能を使っていたかで意味が変わります。OpenAIの[ChatGPTでのGPT-5.6とGPT-6 Pro](https://help.openai.com/ja-jp/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt)と[WorkとCodexでのGPT-6 Astraの利用量管理](https://help.openai.com/ja-jp/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)を読むと、上限は5つに分かれます。

<figure class="post-figure"><img src="/media/images/chatgpt-limit-reached/00_fig_kinds_v2.jpg" alt="ChatGPTの上限5種類を並べた図。画像とファイルのアイコンのツールの上限、電球のアイコンの思考の上限、星のアイコンのProモデルの上限、コードの括弧のアイコンのWorkとCodexの上限、盾のアイコンの一時的な利用制限" loading="lazy"><figcaption>どこで止まったかで戻り方が違う</figcaption></figure>

| 上限 | 対象のプラン | 何が止まるか | 戻り方 |
|---|---|---|---|
| ツールの上限 | 無料版・Go | 画像生成・アップロード・音声・データ分析 | 表示された時刻まで待つ。Plus以上に変える |
| 思考の上限 | 有料プラン | 中程度・高・超高で使うGPT-5.6 Sol | 別のモデルで続くことがある。時刻まで待つ |
| Proモデルの上限 | Pro・Business | GPT-6 ProとGPT-5.6 Sol Pro | 別のモデルを使う。枠の回復を待つ |
| WorkとCodexの上限 | Plus・Pro・Business | WorkとCodexでの作業 | 5時間枠と週間枠の回復、リセットの利用 |
| 一時的な利用制限 | 全プラン | 不正利用と判断された操作 | ChatGPTの通知に従う |

**表示が出たときに使っていた機能を思い出すと、どの行に当たるかが分かります。**チャットで画像を頼んでいたならツールの上限、Codexで作業していたならWorkとCodexの上限です。

## 無料版とGoの上限

無料版とGoでは日常のテキストのチャットは、不正利用を防ぐ制限の範囲内で回数無制限です。[ChatGPT 無料版に関するよくある質問](https://help.openai.com/ja-jp/articles/9275245-chatgpt-free-tier-faq)によると、ファイルのアップロード、画像生成、音声、データ分析などのツールには、それぞれ別の上限があります。上限に達するとChatGPTから通知が出ます。

<figure class="post-figure post-figure--sp"><img src="/media/images/chatgpt-limit-reached/clr_04_help_free_v2.jpg" alt="OpenAI公式ヘルプのChatGPT無料版に関するよくある質問のページをスマホで開いた画面。無料プランのレート制限の仕組みの見出しの下に、日常的なテキストチャットは回数無制限、ファイルのアップロードや画像生成などのツールにはそれぞれ個別の利用上限があると書かれ、下に画像作成の上限に達したときの通知の例が載っている" loading="lazy"><figcaption>無料版の上限の仕組みと通知の例（2026年10月5日に取得）</figcaption></figure>

通知の例には、Plusに変えるか翌朝の9時17分以降にもう一度試すよう英語で書かれています。**同じFAQによると、無料版で上限に達したあとPlus・Pro・Businessに変えると、上限はその場でリセットされます。**Goはこの対象に書かれていません。

画像生成の上限は[ChatGPTの画像生成ができない原因の記事](/media/chatgpt-image-limit/)で、アップロードの回数と容量は[ChatGPTのファイルアップロード上限の記事](/media/chatgpt-file-upload-limit/)で詳しく扱っています。

## 有料プランの思考とProモデルの上限

有料プランでは思考のレベル（中程度・高・超高）を選ぶとGPT-5.6 Solが使われます。**思考の上限に達すると、ChatGPTは別の利用可能なモデルで処理を続けることがあります。**止まらずに答えが返ってきても、使われたモデルが変わっている場合があるということです。

### 考えてと頼んでも切り替わらない

PlusとProでは即時モードのまま「もっとよく考えて」「深く考えて」と頼んでも、ChatGPTが上の思考レベルへ自動で切り替えることはありません（安全上の理由を除く）。上の思考レベルで答えてほしいときは、モデルメニューで自分で選ぶ必要があります。

Businessは扱いが別です。[ChatGPT Businessのモデルと制限](https://help.openai.com/ja-jp/articles/12003714-chatgpt-business-models-and-limits)によると、即時モードを選んでいてもChatGPTが推論を自動で足すことがあり、**そのときは推論の利用枠が使われることがあります。**この動きは設定の［一般］にある［より高い応答性能］で変更可能です。

### GPT-6 Proの件数

ProプランとBusinessでは、GPT-6 ProとGPT-5.6 Sol Proに件数の上限があります。公式ヘルプには**Proの契約にGPT-6 Proの無制限の利用は含まれない**と明記されています。

<figure class="post-figure post-figure--sp"><img src="/media/images/chatgpt-limit-reached/clr_01_help_pro_v2.jpg" alt="OpenAI公式ヘルプのChatGPTでのGPT-5.6とGPT-6 Proのページをスマホで開いた画面。GPT-6 ProとGPT-5.6 Sol Proの利用上限の見出しの下に、Proの契約でもGPT-6 Proを無制限には使えないこと、Pro 200ドルは週の上限に達すると思考の中程度に切り替わること、Pro 100ドルとBusinessは2つのモデルで1つの枠を共有することが書かれている" loading="lazy"><figcaption>Proモデルの上限の説明。Proの件数の表は消えている（2026年10月5日に取得）</figcaption></figure>

9月25日に読んだときには、このページにPro $200で週200件、Pro $100で週50件という件数の表がありました。**10月5日時点ではその表がなくなり、Proの件数は書かれていません。**Businessのモデルと制限のページには、Businessの件数が今も載っています。

| プラン | GPT-6 Proの枠（チャット） | GPT-5.6 Sol Proとの関係 |
|---|---|---|
| Pro $200 | 週ごとの上限（件数の記載なし） | Sol Proは1日の枠と、2つを合わせた1日の枠の両方に残りがあるときだけ使える |
| Pro $100 | 週ごとの枠（件数の記載なし） | 2つのモデルで1つの週の枠を共有 |
| Business Standard | 月15件 | 2つのモデルで月15件を共有 |
| Business Premium | 週50件 | 2つのモデルで週50件を共有 |

Pro 500のGPT-6 Proの件数と扱いは、ヘルプに記載がありません（10月5日時点）。

Pro $200でGPT-6 Proの週の上限に達すると、ChatGPTは自動で思考「中程度」のGPT-5.6に切り替わります。Pro $100とBusinessは2つのモデルで1つの枠を共有しているため、**モデルを切り替えても件数は増えません。**これらはチャットでの上限で、WorkとCodexには別の枠があります。

### Pro 500の追加とPro 200の枠

[ChatGPT Proの各プランについて](https://help.openai.com/ja-jp/articles/9793128-about-chatgpt-pro-tiers)によると、Proは月100ドル・200ドル・500ドルの3プランになりました。Pro 500は3つの中でいちばん枠が多く、GPT-6 Astraの応答を速くするUltrafastを使えるのもPro 500だけです。日本の[料金ページ](https://chatgpt.com/ja-JP/pricing/)では、Proは月16,800円からと表示されています。

Pro 200は新しい申し込みが再開しましたが、**新しく入った人の枠は以前のPro 200より少なくなりました。**2026年9月22日から9月29日午前10時（太平洋時間）までの間にPro 200が有効だった人は、契約が続いていれば10月29日まで以前の枠を使えます。前から続けている人も、この間に有効なら対象です。そのあとは料金が月200ドルのまま、少ない枠に移る決まりです。

## WorkとCodexの上限

WorkとCodexはプランに含まれる1つの利用枠を共有していて、プランによっては5時間枠と週間枠の両方があります。**その場合は続けて使うには両方に枠が残っている必要があります。**現在の残りとリセットの時刻を見る場所は、設定の［使用状況］です。

5時間枠が残るのはPlusとBusiness Standardです。Pro 100・Pro 200・Pro 500には今は5時間ごとの上限がなく、Business Premiumにも5時間の上限はありません。どちらもプランに含まれる週の枠は残ります。

<figure class="post-figure post-figure--sp"><img src="/media/images/chatgpt-limit-reached/clr_05_help_work_v2.jpg" alt="OpenAI公式ヘルプのWorkとCodexでのGPT-6 Astraの利用量管理のページをスマホで開いた画面。Pro 100、Pro 200、Pro 500ではWorkとCodexに5時間ごとの利用上限はないと書かれ、その下にPlusとStandard Businessで5時間に送れるローカルメッセージ数の目安の表がある。GPT-6 Astraは5から45、GPT-6.1 Solは15から160、GPT-6 Solは15から150、GPT-6 Lunaは350から3,000" loading="lazy"><figcaption>Proの5時間枠の扱いとPlusの目安（2026年10月5日に取得）</figcaption></figure>

PlusとBusiness Standardで5時間に送れるローカルのメッセージ数は、GPT-6 Astraで5〜45件、GPT-6 Lunaで350〜3,000件が目安です。ヘルプは目安であって保証ではないとしており、クラウドのタスクはローカルより多く枠を使うことがあります。Proの各プランについてのヘルプでは、**Fastモードは標準の2.5倍、Ultrafastは8倍の速さで枠を使う**と書かれています。

枠の戻り方、配られた保存済みリセットの使い方、PlusとProの個人アカウントで買える即時リセットの違いは、[Codexの制限とリセット](/media/codex-limits/)にまとめました。プランごとの枠の大きさは[ChatGPT Workのプランと上限の記事](/media/chatgpt-work-plans/)で比べられます。

## 上限に達したときの対処

取れる手を並べると次のとおりです。最後の行のサポートへの依頼は、上限を戻す手段にはなりません。

| 手 | 使える場面 | 注意 |
|---|---|---|
| 待つ | すべての上限 | 時刻は分かる場合だけ画面に出る |
| 別のモデルを使う | 有料プランの思考・Proモデル | 同じ枠を共有するモデルでは増えない。WorkとCodexの共有の枠も戻らない |
| プランを上げる | 無料版のツールの上限 | Plus・Pro・Businessに変えると上限がリセット |
| リセットを使う | WorkとCodex | 週のリセット日が変わる。購入分は次の週の前倒し |
| クレジットで続ける | WorkとCodexなど（アカウントによる） | 含まれる枠を使い切ったあと、従量課金の残高から引かれる |
| サポートに頼む | 使えない | 数え間違いや、時刻を過ぎても戻らないときの調査だけ |

即時リセットを買えるのはPlusとProの個人アカウントです。[WorkとCodexの週間レート制限の有料リセット](https://help.openai.com/ja-jp/articles/20001507-paid-weekly-work-and-codex-rate-limit-resets)では、購入できる場所としてChatGPTのウェブ版とCodexのデスクトップアプリが挙がっています。ただし買えるかどうかはアカウントと請求先の国によって違い、同じプランでも出ないことがあります。手順に出てくる押す場所は、デスクトップアプリの［使用状況］にある［即時リセットを購入］と、週の上限に達したときに出るバナーです。5時間の上限だけではバナーは出ません。クレジットはCodexとWorkのほか、ChatGPT for WordやExcel、PowerPointの対象の機能にも使えます。

### サポートは上限をリセットしない

ChatGPTでのGPT-5.6とGPT-6 Proのヘルプには、**OpenAIのサポートはChatGPTやCodexの利用上限をリセットしない**とはっきり書かれています。問い合わせてよいのは使用量が誤って数えられたと思うときと、表示されたリセット時刻を過ぎても使えないときです。

<figure class="post-figure post-figure--sp"><img src="/media/images/chatgpt-limit-reached/clr_03_help_faq_v2.jpg" alt="OpenAI公式ヘルプのChatGPTでのGPT-5.6とGPT-6 ProのページのFAQをスマホで開いた画面。サポートで利用上限をリセットできますか、という質問に、いいえ、OpenAIサポートではChatGPTまたはCodexの利用上限をリセットできません、と答え、利用量が誤ってカウントされた場合や表示されたリセット時刻を過ぎてもアクセスが戻らない場合は調査のためサポートに問い合わせるよう書かれている" loading="lazy"><figcaption>サポートでのリセットはできないと書かれたFAQ（2026年10月5日に取得）</figcaption></figure>

### 会話の長さで止まったとき

1つの会話が長くなりすぎて止まる場合は、ここまでの上限とは別の問題です。料金ページの注記にはChatGPTが共有のコンテキストウィンドウを管理しており、利用者が入力に使える領域はウィンドウ全体より小さいと書かれています。**会話が長くなって続けられないときは、要点をまとめて新しいチャットで続けてください。**まとめ方は[ChatGPTが重い・遅いときの記事](/media/chatgpt-slow/)の長くなった会話の節で扱っています。

## よくある質問

### ChatGPTの上限に達したらリセットされますか？

リセットされます。上限に達した機能やモデルは、リセットされるまで一時的に使えなくなるだけです。リセットの時刻は情報を取得できる場合にChatGPTの画面に表示されます。

### ChatGPTの無料版は1日何回まで使えますか？

テキストのチャットは不正利用を防ぐ制限の範囲内で回数無制限です。画像生成、ファイルのアップロード、音声、データ分析などのツールにはそれぞれ上限があり、無料版のFAQには回数が書かれていません。

### ChatGPT Plusの上限は何時にリセットされますか？

決まった時刻はありません。思考やWork、Codexなど上限の種類ごとに戻る時刻が違い、分かる場合は画面に表示されます。WorkとCodexの残りとリセットの時刻は、設定の［使用状況］に出ています。

### 上限に達したらアカウントが制限されたのですか？

アカウントの制限ではありません。Proプランの公式ヘルプの説明では、モデルの利用枠に達したことはアカウントの制限やサブスクリプションの終了を意味しないとされています。

### ProプランにもCodexの5時間制限はありますか？

10月5日時点ではありません。Pro 100・Pro 200・Pro 500では、WorkとCodexに5時間ごとの上限がなく、プランに含まれる週の枠だけが残ります。PlusとBusiness Standardは5時間枠と週間枠の両方です。

### Codexの上限をすぐに戻す方法はありますか？

PlusとProの個人アカウントなら、ChatGPTのウェブ版かCodexのデスクトップアプリで即時リセットを買える場合があります。買えるかどうかはアカウントと請求先の国によって違います。Plus・Pro・Businessで保存済みリセットが配られていれば、デスクトップアプリの［設定］→［使用状況］から使えます。

### GPT-6 ProはProプランなら無制限ですか？

無制限ではありません。Pro $100とPro $200のチャットでのGPT-6 Proには週ごとの上限があります。10月5日時点のヘルプには件数が書かれていないので、残りとリセットの時刻は画面の表示で確かめてください。

### 無料版で上限に達したあと有料プランにすればすぐ使えますか？

使えます。無料版で上限に達したあとPlus・Pro・Businessに変えると、利用上限がリセットされると公式FAQに書かれています。

## 出典

- OpenAI Help Center「[ChatGPT での GPT-5.6 と GPT-6 Pro](https://help.openai.com/ja-jp/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt)」（2026年10月5日取得）
- OpenAI Help Center「[ChatGPT 無料版に関するよくある質問](https://help.openai.com/ja-jp/articles/9275245-chatgpt-free-tier-faq)」（同）
- OpenAI Help Center「[ChatGPT Pro の各プランについて](https://help.openai.com/ja-jp/articles/9793128-about-chatgpt-pro-tiers)」（同）
- OpenAI Help Center「[ChatGPT Business のモデルと制限](https://help.openai.com/ja-jp/articles/12003714-chatgpt-business-models-and-limits)」（同）
- OpenAI Help Center「[Work と Codex での GPT-6 Astra の利用量管理](https://help.openai.com/ja-jp/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)」（同）
- OpenAI Help Center「[保存済み Codex リセットの仕組み](https://help.openai.com/ja-jp/articles/20001498-how-banked-codex-resets-work)」（同）
- OpenAI Help Center「[Work と Codex の週間レート制限の有料リセット](https://help.openai.com/ja-jp/articles/20001507-paid-weekly-work-and-codex-rate-limit-resets)」（同）
- ChatGPT「[料金](https://chatgpt.com/ja-JP/pricing/)」（同）
