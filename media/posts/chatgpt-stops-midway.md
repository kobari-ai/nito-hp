---
title: 【2026年10月】ChatGPTが途中で止まる原因と続きを出す方法｜長文・続けるボタン・考え中
date: 2026-10-13
category: AI活用
description: ChatGPTの回答が途中で止まるときを、長い文章が切れる・続けるボタンがない・考え中のまま・エラーの4つに分け、続きを出す送り方と直し方をOpenAIのヘルプと2026年10月の実測で解説します。
cover_tag: トラブル
cover_headline: ChatGPTが途中で止まるとき
cover_sub: 長文・続けるボタン・考え中・エラー
fork_q: 止まった回答の続きを今すぐ出したい
fork_go: 2章を読む
fork_href: #s2
---

ChatGPTに長い文章を頼むと、回答が途中で止まったり、区切りのいいところで「続きは次で」と書いて終わったりします。ネットの解説記事には回答の下の「Continue generating（生成を続ける）」ボタンを押すよう書いたものが今も残っています。このボタンは2023年5月に入った機能で、2026年10月13日にログインしていないChatGPTで試したときは、回答の下にあったのはコピーと共有のボタンだけでした。

同じ日に、スマホ幅のブラウザで47都道府県を1県600字ずつ書くよう3回頼みました。**3回のうち2回は7〜10道県で区切って「次は〜から」と書いて終わり、「続けて」と送ると区切った所から続きが出ました。** 残りの1回は47都道府県を1回の回答で書き切り（約3万1,000字）、そこへ「続けて」と送ると北海道から書き直しが始まっています。

この記事では止まり方を4つの症状に分け、症状ごとに試すことをOpenAIのヘルプと試した結果で整理します。ヘルプとリリースノートは2026年10月13日に取得しました。

:::takeaways
- 途中で止まる症状は**長い文章が切れる・続けるボタンがない・考え中のまま止まる・エラーで止まる**の4つで、試すことがそれぞれ違う
- 長い文章が途中で終わったら、**同じチャットで「続けて」と送る**。試したときは区切った所から続きが出た
- 書き終えた回答に「続けて」と送ると、**最初から書き直しが始まることがある**（試したとき）。送る前に回答の最後の行を見る
- 回答の下の続けるボタンは2023年5月に入った機能で、**ログインせずに試した画面では出なかった**。自分で区切った回答だったので、上限で切れたときだけ出る可能性もあります。ボタンを探さずに「続けて」と送る
- 考え中のまま進まないときは、**ヘルプの順番どおり30〜60秒待ってから、生成を停止して再生成**する
:::

## 止まり方で分かれる4つの症状

文字が出ている途中で止まったのか、何も出ないまま考え中が続いているのかで、試すことは変わります。まず自分の画面がどれに近いかを見てください。

<figure class="post-figure"><img src="/media/images/chatgpt-stops-midway/csm_00_fig_types_v.png" alt="ChatGPTが止まる4つの症状の図。長い文章が切れる、続けるボタンがない、考え中のまま止まる、エラーで止まる、の4つを縦に並べ、それぞれ画面で起きていることを添えている" loading="lazy"><figcaption>ChatGPTが途中で止まるときの4つの症状</figcaption></figure>

| 症状 | 画面で起きていること | 最初に試すこと |
|---|---|---|
| 長い文章が切れる | 文の途中や区切りのいい所で回答が終わる | 同じチャットで「続けて」と送る |
| 続けるボタンがない | 解説記事にあるボタンが見当たらない | ボタンを探さずに「続けて」と送る |
| 考え中のまま止まる | Thinking…やGenerating…の表示のまま進まない | 30〜60秒待ち、生成を停止して再生成 |
| エラーで止まる | 回答の途中でエラーの文言が出る | 文言を読み、再生成か再読み込み |

## 長い文章が途中で切れるとき

OpenAIのヘルプには、ChatGPTが1回の回答で書ける長さの数字は載っていません。手がかりになるのは[2023年5月12日のリリースノート](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)で、上限のトークン数を超えて続きを生成できるようになったと書かれています。**2023年の時点で、1回の回答に長さの上限があったことがこの記述から分かります。** 今の上限の数字や、何字で切れるかは公開されていません。

試したときは47都道府県を1県600字ずつ（合わせて約2万8,000字）頼んだ1回目の回答が、群馬県まで書いたところで終わりました。最後の行は「次の範囲は11. 埼玉県から20. 長野県までです」で、文が途中で切れたのではなく、ChatGPTが自分で区切りを入れて止めていました。3回目は福島県までの7道県（約4,600字）で「第1部は以上です」と区切り、2回目は47都道府県を1回で書き切っています。**同じ頼み方でも、区切るかどうかと区切る位置は毎回違いました。**

<figure class="post-figure post-figure--sp"><img src="/media/images/chatgpt-stops-midway/csm_01_sp_split.png" alt="スマホで開いたChatGPTのウェブ版で、47都道府県を頼んだ回答の終わり。1は第1部は以上です、ここまで北海道から福島県までの7道県を紹介しました、次のパートでは茨城県から続けます、という区切りの文。2は回答の下にあるコピーと共有の2つのボタンで、続けるボタンは無い" loading="lazy"><figcaption>3回目の試しで、7道県で区切って終えた回答。下にあるのはコピーと共有だけ（2026年10月13日、ログインなし）</figcaption></figure>

### 続けてと送る

区切られた回答の続きは同じチャットで「続けて」と送れば出ます。**試したときは1回目が埼玉県から長野県までの10県（約5,700字）、3回目が茨城県から愛知県までの16県（約1万字）で、どちらも区切った所の次から始まりました。**最後にはまた「次は三重県から」のように次の範囲が書かれていて、47都道府県をそろえるには何回か送ることになります。

送る前に、回答の最後の行を見てください。2回目の試しでは47都道府県を書き終えて「以上が、北海道から沖縄県までの47都道府県です」と締めた回答に「続けて」と送っています。するとChatGPTは「抜けていた北海道から愛知県までの23道県」を補うと書き、北海道から書き直し始めました。**最後が締めの文なら続きは無いので、「続けて」は送らないほうが無駄がありません。**

<figure class="post-figure post-figure--sp"><img src="/media/images/chatgpt-stops-midway/csm_02_sp_continue.png" alt="スマホで開いたChatGPTのウェブ版で、47都道府県を書き終えた回答のあとに続けてと送った画面。1は送った続けての吹き出し。2は回答の書き出しで、抜けていた北海道から愛知県までの23道県を紹介しますと書き、北海道から書き直している" loading="lazy"><figcaption>2回目の試しで、書き終えた回答に「続けて」と送ると、北海道から書き直しが始まった（2026年10月13日、ログインなし）</figcaption></figure>

### 最初から分けて頼む

長い文章が要るなら、最初から1回の範囲を決めて頼む手もあります（この頼み方は試していません）。「北海道から群馬県までの10道県を、1県600字で」のように範囲を書き、終わったら次の範囲を頼みます。どこまで書き終えたかを自分で追えるので、さっきのような書き直しにも気づきやすくなります。

報告書や小説なら章ごと、コードならファイルや関数ごとが区切りの目安です。前の回答の内容を引き継がせたいときは、同じチャットのまま次を頼みます。

## 続けるボタンが出ないとき

解説記事に「Continue generating」として出てくるボタンのもとは、2023年5月12日のリリースノートの「続きを生成できるようになった」という項目です。ボタンという言葉は無く、上限を超えて続きを生成でき、続きの1回もメッセージの回数に数えると書かれていました。

その後、[OpenAIのコミュニティ](https://community.openai.com/t/where-is-the-button-continue-generation/691846)にはボタンが消えたという投稿が続きます。2024年3月20日の投稿は「昨日はあったボタンが今日は無い」というもので、戻ったという返信が付いたのは約1週間後の3月28日と29日でした。ボタンは上限で切れたときだけ出るという返信も同じスレッドに付いていました。2024年9月には[長いコードでボタンが1回しか効かない](https://community.openai.com/t/continue-generating-button-no-longer-working/954559)という報告も出ています。リリースノートを「continue generating」で探しても出てくるのは2023年5月の項目だけで、外したという告知は見つかりませんでした。

2026年10月13日にログインせずスマホ幅で試したときは、3回とも**回答の下にあったのはコピーと共有のボタンだけ**でした。区切って終えた回答にも、続けるボタンは出ていません。自分で区切った回答だったので、上限で切れたときだけ出る可能性もあります。ログインした画面とアプリでは確かめていないため、そちらで出るかは分かりません。ボタンが無くても、同じチャットで「続けて」と送れば続きは出ました。

### 考えながら答え始めるGPT-6

[2026年10月7日のリリースノート](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)によると、GPT-6は考えたりツールを使ったりしながら答え始め、追加の指示なしで見つけたことを書き足します。回答が全部できる前に読み始められる、とも書かれています。提供の範囲は2つの資料で食い違っていて、リリースノートは「FreeとGoにも翌日から広げ、FreeとGoはGPT-6 Luna」、[モデルのヘルプ](https://help.openai.com/ja-jp/articles/11909943-gpt-5-in-chatgpt)は「ChatのGPT-6はPro・Plus・Enterprise・Business向けに順次提供し、FreeとGoはGPT-5.6 Lunaに移行中」としています。ログインしない画面でどのモデルが使われるかは、どちらにも書かれていません。

止まったように見えても、まだ書き足している途中のことがあります。試したときは書いている間、入力欄の右に「生成を中止」のボタンが出ていました。このボタンが出ている間は回答はまだ終わっていません。

<figure class="post-figure"><img src="/media/images/chatgpt-stops-midway/csm_03_rn_gpt6.png" alt="OpenAIのChatGPTリリースノートの2026年10月7日の項目、GPT-6 and Intelligent UI in ChatGPT。1はGPT-6が考えたりツールを使ったりしながら答え始め、追加のプロンプトなしで見つけたことを書き足すという段落" loading="lazy"><figcaption>ChatGPTのリリースノート（2026年10月7日の項目）</figcaption></figure>

## 考え中のまま止まるとき

何も書かれないまま「Thinking…」「Generating…」の表示が続くときについて、[OpenAIのヘルプ](https://help.openai.com/ja-jp/articles/7996703-troubleshooting-chatgpt-error-messages)は試す順番を示しています。上から順に試し、直ったところで止めます。

1. 回答が終わるか30〜60秒待つ
2. 生成を停止してから再生成する
3. 新しいチャットで送り直す
4. ハード更新（Cmd またはCtrlとShiftとR）か、デスクトップアプリの再読み込み
5. サインアウトして入り直す
6. 拡張機能を止めたシークレットウィンドウで開く
7. VPN・プロキシ・セキュアDNSを切る
8. 別のブラウザ・回線・端末で試す
9. [ステータスページ](https://status.openai.com/)で障害を確かめる

<figure class="post-figure"><img src="/media/images/chatgpt-stops-midway/csm_04_help_steps.png" alt="OpenAIのヘルプ、ChatGPTのエラーメッセージのトラブルシューティングの日本語版。1はChatGPTが応答を完了せずに止まっているように見える場合の手順で、30〜60秒待つ、生成を停止して再生成、新しいチャット、ハード更新などが順に並ぶ" loading="lazy"><figcaption>OpenAIのヘルプにある止まったときの順番（日本語版）</figcaption></figure>

同じヘルプは、会話が長いときややり取りの回数が多いときにも新しいチャットを始めるよう書いています。**同じ会話だけで止まるなら、新しいチャットで送り直すのが先です。**それぞれの手順の詳しい説明は[ChatGPTのエラーメッセージ一覧](/media/chatgpt-error-messages/)に、遅さそのものの原因は[ChatGPTが重い・遅いとき](/media/chatgpt-slow/)にまとめています。

## エラーで止まるとき

回答の途中でエラーの文言が出たら、文言で見分けます。ヘルプに載っている文言のほかに、コミュニティで報告が続いている文言もありました。

| 文言 | 載っている所 | 試すこと |
|---|---|---|
| 応答の生成中にエラーが発生しました | ヘルプ | 再生成を押す。続くならブラウザか端末を再起動 |
| 接続が途切れました。回答全体の受信を待っています（検索の言い方。画面は未確認） | コミュニティの報告（英語の表示） | 回答をコピーしてから再読み込み |
| Error in message stream | コミュニティの報告 | ヘルプの止まったときの手順を上から試す |
| ネットワークエラーが発生しました | ヘルプ | VPNやプロキシを切り、別の回線で試す |
| 上限に達しました | モデルのヘルプ（リセットの時刻） | リセットの時刻まで待つ |

ネットワーク構成の問題やClientErrorの直し方は[ChatGPTのネットワーク構成の問題とClientError](/media/chatgpt-network-error/)、上限の種類とリセットの時刻は[ChatGPTで上限に達したとき](/media/chatgpt-limit-reached/)で詳しく扱っています。

### 接続が途切れたと出たとき

「接続が途切れました。回答全体の受信を待っています」は検索で探されている言い方で、日本語の画面では確かめていません。英語の画面の「Connection interrupted. Waiting for the complete answer」はコミュニティで報告されている表示で、ヘルプには載っていません。2026年6月の[コミュニティの投稿](https://community.openai.com/t/switch-for-gpt-image-gen-in-long-context-prompts-lead-to-connection-interrupted-waiting-for-the-complete-answer/1385186)には、画像の生成で、この表示か「Image generation failed」が3割ほど出たという報告もあります。5.5 Instantで画像を作ったときだけ出るという返信も付いていました。同じ投稿者はページを読み込み直すと「Too many requests」と出てその会話が失われたとも書いています。

報告は1人分ですが、**読み込み直す前に、そこまでに出た回答をコピーしておけば失わずに済みます。**10月7日には読み込みの失敗や「Resume stream unavailable」と一緒にこの表示が出るという[別の投稿](https://community.openai.com/t/is-anyone-else-experiencing-recurring-chatgpt-loading-failures-stream-errors-and-stuck-tasks/1404071)もありました。

### Error in message streamと出たとき

2026年9月23日の[コミュニティの投稿](https://community.openai.com/t/chatgpt-android-error-in-message-stream-interrupts-long-conversations/1399948)は、Androidのアプリで、ファイルを添付した長い会話が「Thinking」のあと止まり、この表示が出たという報告です。最初の投稿に付いたリアクションは4つで、ウェブ版やデスクトップアプリで出たという返信も同じスレッドにあり、Androidだけの話ではありません。投稿者も原因を特定できておらず、公式の説明はまだありません。

どの症状でも直らないときは、ヘルプのとおり、タイムスタンプ付きのHARファイルとブラウザのコンソールのエラーを集め、使ったモデルと会話のURLかIDを添えてサポートに問い合わせます。

## よくある質問

### ChatGPTの回答が途中で止まるのはなぜですか？

文の途中で切れる原因の1つとして、OpenAIは2023年に1回の回答の上限を挙げていました。今の上限の数字は公開されていません。試したときは文の途中では切れず、ChatGPTが自分で区切りを入れて終えました。何も出ないまま止まるときは、ヘルプの手順を上から試します。

### ChatGPTに続きを書いてもらうにはどうすればいいですか？

同じチャットで「続けて」と送ります。試したときは区切った範囲の次から続きが出ました。回答の最後が締めの文なら続きは無いので、送る前に最後の行を見てください。

### ChatGPTの続けるボタンは無くなったのですか？

外したという公式の告知は見つかりません。2026年10月13日にログインせずに試した画面では、回答の下にコピーと共有のボタンしかありませんでした。ログインした画面とアプリは確かめていません。

### ChatGPTは有料版なら途中で止まりませんか？

プランごとの1回の回答の長さは、ヘルプに書かれていません。この記事の実測はログインしていない画面だけで、有料版では試していません。長い文章はプランにかかわらず、範囲を分けて頼むと、どこまで書いたかを追えます。

### ChatGPTのコードが途中で止まるときはどうしますか？

同じチャットで「続けて」と送れば続きは出ますが、2024年9月のコミュニティの報告ではコードの書式が崩れることがありました。ファイルや関数ごとに分けて頼むと、どこまで書いたかを追えます。

### ChatGPTが考え中のまま止まったら何秒待てばいいですか？

ヘルプは30〜60秒としています。それでも終わらなければ、生成を停止してから再生成し、次に新しいチャットで送り直します。

### ChatGPTで接続が途切れましたと出たらどうしますか？

この日本語の文言は検索で探されている言い方で、日本語の画面では確かめていません。英語の「Connection interrupted」はコミュニティで報告されている表示で、ヘルプには載っていません。コミュニティには読み込み直したら会話が失われたという報告があるため、出ている回答をコピーしてから再読み込みします。あわせてステータスページで障害が出ていないかも確かめてください。

### ChatGPTが繰り返し止まるのはなぜですか？

同じ会話でだけ止まるなら、会話が長くなっていることを疑います。ヘルプも長い会話では新しいチャットを始めるよう書いています。どの会話でも止まるなら、ステータスページで障害を確かめ、別の回線やブラウザで比べます。

## 出典

- OpenAI Help Center「[ChatGPTのエラーメッセージのトラブルシューティング](https://help.openai.com/ja-jp/articles/7996703-troubleshooting-chatgpt-error-messages)」（2026年10月13日取得）
- OpenAI Help Center「[ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)」（2023年5月12日と2026年10月7日の項目、同）
- OpenAI Help Center「[ChatGPT の GPT-6 とその他のモデル](https://help.openai.com/ja-jp/articles/11909943-gpt-5-in-chatgpt)」（同）
- OpenAI「[OpenAI Status](https://status.openai.com/)」
- OpenAI Developer Community「[Where is the button continue generation](https://community.openai.com/t/where-is-the-button-continue-generation/691846)」（2024年3月）
- OpenAI Developer Community「[Continue Generating Button No Longer Working](https://community.openai.com/t/continue-generating-button-no-longer-working/954559)」（2024年9月）
- OpenAI Developer Community「[Connection interrupted. Waiting for the complete answer](https://community.openai.com/t/switch-for-gpt-image-gen-in-long-context-prompts-lead-to-connection-interrupted-waiting-for-the-complete-answer/1385186)」（2026年6月）
- OpenAI Developer Community「[ChatGPT Android: Error in Message Stream Interrupts Long Conversations](https://community.openai.com/t/chatgpt-android-error-in-message-stream-interrupts-long-conversations/1399948)」（2026年9月）
- OpenAI Developer Community「[Is anyone else experiencing recurring ChatGPT loading failures, stream errors and stuck tasks?](https://community.openai.com/t/is-anyone-else-experiencing-recurring-chatgpt-loading-failures-stream-errors-and-stuck-tasks/1404071)」（2026年10月）
- 実測: ChatGPT のウェブ版（ログインなし、スマホ幅のブラウザ）で同じ依頼を3回（2026年10月13日）
