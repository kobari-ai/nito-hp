---
title: 【2026年10月】Work IQとは？Copilotのオン・オフ・ライセンス・Work IQ APIの料金
date: 2026-10-03
category: AI活用
description: Microsoft 365 CopilotのWork IQを公式ドキュメントから解説。使えるライセンス、Chat画面の左上のボタンでのオン・オフ、オフのときの答え方、Work IQ APIとCLIの従量課金、管理者が決めることまで。
cover_tag: 使い方
cover_headline: Work IQとは
cover_sub: オン・オフ・ライセンス・APIの料金
---

Work IQは、Microsoft 365 Copilotが社内のメールやファイル、会議、チャットを踏まえて答えるための仕組みです。Copilot Chatの画面では、左上の［Work IQ］ボタンとして目に入ります（日本語のサポート記事には「仕事 IQ」と訳されている箇所もあります）。以前あった［作業］と［Web］のタブは、このボタン1つに置き換えられました。

同じWork IQという名前で、開発者向けのWork IQ APIやCLIもあり、こちらはライセンスとは別の従量課金です。この記事は2026年10月3日に取得したMicrosoftの公式ドキュメントをもとに、使えるライセンス、オンとオフの違い、APIの課金、導入する側が先に決めることを整理します。

:::takeaways
- Work IQは、メール・ファイル・チャット・会議などを結び付けて、Copilotの答えに**仕事の文脈を乗せる層**
- 使えるのは**Microsoft Copilotのアドオン ライセンスを持つ人**。持っていれば**初期設定でオン**
- オン・オフは**Microsoft CopilotアプリのChat画面の左上の［Work IQ］ボタン**。以前の［作業］［Web］のタブはこれに置き換わった
- オフのときは、添付したもの・公開されているWebの情報・プロフィールと個人用設定だけで答える
- **Work IQ API・CLI・MCPはライセンスとは別の従量課金**。CLIは2026年6月16日に一般提供になった
:::

## Work IQは何をしているか

Microsoftのサポート記事「[Copilot はプロンプトに応答するためにどのような情報を使用しますか?](https://support.microsoft.com/ja-jp/microsoft-365-copilot/what-information-does-copilot-use-to-answer-my-prompt)」は、Work IQを、Copilotとエージェントが仕事を理解するのを助けるインテリジェンス層と説明しています。Microsoft 365やビジネスアプリに散らばった情報を、Copilotが使える文脈に変える役割です。

Copilotが理解するのに役立つものとして、次の4つが挙がっています。

- 一緒に仕事をしている人
- いま重要なこと
- 仕事の進み具合
- そのタスクに関係する情報

<figure class="post-figure"><img src="/media/images/copilot-work-iq/01_fig_layers.png" alt="Work IQの3つの層の図。データはファイル・メール・会議・チャット・ビジネスアプリのシグナルをまとめる。メモリは利用者やチームの働き方を継続して理解する。推論はモデル・スキル・ツールをまとめてエージェントが動けるようにする" loading="lazy"><figcaption>Work IQはデータ・メモリ・推論の3層（Copilot Studioのドキュメントの説明）</figcaption></figure>

データ・メモリ・推論の3層は、開発者がエージェントにWork IQを組み込むときの[Copilot Studioのドキュメント](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/add-work-iq)にある説明です。利用者が画面で意識するのは、次の節のオンとオフだけです。

## 使える人とライセンス

Work IQを使えるのは、Microsoft Copilotのアドオン ライセンスを持つ人です。サポート記事にはこう書かれていて、ライセンスを持っていれば**初期設定でオン**になっています。

開発者向けのMicrosoft Learnでは、課金の説明に「Microsoft 365 Copilot ライセンス」という名前が使われています。あとの節の課金の図もこちらの名前です。

別のサポート記事「[Microsoft Copilot Chatの回答のソースを制御および確認する](https://support.microsoft.com/ja-jp/Microsoft-365-Copilot/control-review-sources-copilot-chat)」にも、作業データにアクセスできるのはMicrosoft Copilotのサブスクリプションを持つユーザーだけ、とあります。ライセンスが無い人のCopilot Chatは、Webの情報と自分で添付したものを中心に答える形です。

ライセンスの3つの段（Copilot Chat、Microsoft 365 Copilotの基本、アドオンを足したプレミアム）の違いは、[Copilotの使い方の記事](/media/copilot-guide/)にまとめています。

## オンとオフを切り替える

切り替えるボタンの場所は**Microsoft CopilotアプリのChat画面の左上**です。以前の［作業］タブと［Web］タブはこのボタンに置き換えられた、とサポート記事に書かれています。作業とWebを行き来する代わりに、作業データを見せるかどうかを1つのボタンで決める形になりました。

<figure class="post-figure"><img src="/media/images/copilot-work-iq/02_help_toggle.jpg" alt="Microsoftのサポート記事の注。Copilotの個別の作業タブとWebタブは仕事 IQ（Work IQ）ボタンに置き換えられ、1つのオンオフのコントロールで作業データを参照できるかどうかを決められるようになったと書かれている。続く節にはCopilotは既存のアクセス許可を尊重し、会社のデータでパブリックモデルをトレーニングしないとある" loading="lazy"><figcaption>サポート記事「Copilot はプロンプトに応答するためにどのような情報を使用しますか?」の注</figcaption></figure>

| | Work IQ オン | Work IQ オフ |
|---|---|---|
| 作業データ（メール・ファイル・チャット・会議・人・プロジェクト） | 参照する | 参照しない |
| 添付したファイルや画像 | 参照する | 参照する |
| 公開されているWebの情報 | 参照する | 参照する |
| プロフィールと個人用設定 | 記載なし | 参照する |
| 向いている場面 | 仕事の文脈を踏まえた答えが欲しい | 一般的な答えが欲しい、組織の外の作業 |

オフにしても、Copilotは答えを返します。ただし社内の状況を知らない前提の答えになるので、**思ったより一般論しか返ってこないときは、まずこのボタンを見てください**。タスクに合わせて、いつでも切り替えられます。

### 社内のデータの一部だけを止める

Work IQをオンにしたまま、特定のデータだけを使わせないこともできます。メッセージの入力欄の［+］から［ソースの追加と管理］を開き、下の［データ ソースの変更］で、ソースごとのトグルを切り替えます。サポート記事が例に挙げているのは、Viva Engageだけをオフにする使い方です。

同じメニューの上の［すべて無効にする］を押すと、Web検索以外のデータソースがまとめてオフになります。

## 社内のデータはどう扱われるか

Work IQがオンでも、Copilotが見に行けるのは、その人がもともと見る権限を持っている作業データだけです。サポート記事は次の3点を挙げています。

- Copilotは既存のMicrosoft 365のアクセス許可を守る
- 会社のデータで公開モデルを学習させない。組織の外でモデルを学習させるためにプロンプトを保持しない
- コンテンツの過剰に共有されたコピーを別に作らない

逆に言えば、**共有の設定が広すぎるファイルは、Work IQ経由でも見えてしまいます**。権限の範囲で見えるものが答えに入るからです。導入前に共有の範囲を見直す話は、[Copilotの使い方の記事の「管理側で先に整えるもの」](/media/copilot-guide/)に書いています。

## Work IQ APIとCLIは別の従量課金

開発者向けの[Work IQ の概要](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/work-iq/)（Microsoft Learn）によると、Work IQには、自社のアプリやエージェントから呼び出すための入口が3種類あります。エージェント同士で仕事を渡すA2A、AIアシスタントからツールとして呼ぶMCPサーバー、アプリから呼ぶREST APIです。

<figure class="post-figure"><img src="/media/images/copilot-work-iq/03_fig_billing.png" alt="Work IQの課金の図。Microsoft 365 Copilotのライセンスを持つ人は、Microsoft 365 Copilotの画面とエージェントでWork IQを使える。自社やほかの会社が作ったエージェントから使う場合と、ライセンスを持たない人は使った分の従量課金。Work IQ API・CLI・MCPはライセンスとは別の従量課金" loading="lazy"><figcaption>ライセンスに含まれる範囲と、従量課金になる範囲</figcaption></figure>

課金はライセンスと分かれていて、コストはMicrosoft 365 管理センターで管理します。

<figure class="post-figure"><img src="/media/images/copilot-work-iq/04_learn_billing.jpg" alt="Microsoft LearnのWork IQの概要のアクセスと価格の節。Work IQ APIアクセスはMicrosoft 365 Copilotライセンスとは無関係で使用量ベースの課金、ライセンスを持つユーザーはすべてのMicrosoft 365 CopilotエクスペリエンスとエージェントでWork IQを利用でき、カスタムとサードパーティのエージェントは使用量ベースの課金、ライセンスの無いユーザーは使用量に基づいて課金、コストはMicrosoft 365管理センターで管理と書かれている" loading="lazy"><figcaption>Microsoft Learn「Work IQ の概要」のアクセスと価格</figcaption></figure>

コマンドラインから使う[Microsoft Work IQ CLI](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/work-iq-cli)は、**2026年6月16日に一般提供**になりました。使う条件はNode.js、Azureのサブスクリプションを割り当てたCopilot Studioの従量課金プラン、そのプランへの利用者の割り当て、テナントの管理者の同意の4つです。CLIのままターミナルで質問する使い方と、GitHub CopilotなどのAIアシスタントにMCPサーバーとしてつなぐ使い方があります。

## 導入する側が先に決めること

情報システムの担当者が決めることは、ドキュメントから拾うと次の4つです。

1. **誰にアドオン ライセンスを割り当てるか**。Copilot ChatのWork IQは、ライセンスを持つ人に初期設定でオンになる
2. **従量課金を使わせるか**。Work IQ APIの課金は、Microsoft 365 管理センターで管理する
3. **CLIとMCPを許可するか**。組織のデータに触れるにはテナント管理者の同意が要る
4. **書き込みを許可するか**。Copilot StudioのWork IQ（プレビュー）は、管理者が管理センターで書き込みを明示的にオンにしない限り読み取り専用で、利用には別の支出ポリシーを作る必要がある

4つ目はプレビューの機能についての記述で、管理センターでツールやMCPサーバーを許可・拒否する機能は、地域によってはまだ使えない場合がある、ともドキュメントに書かれています。

## AI検索での見え方は別の話

Work IQは社内のデータを答えに乗せる仕組みで、Copilotが社外の質問に答えるときに自社をどう紹介するかとは別の話です。そちらは[AI検索対策](https://nito-0210.com/llmo/)として扱います。

## よくある質問

### Work IQとは何ですか？
Microsoft 365 Copilotとエージェントが仕事を理解するのを助けるインテリジェンス層です。メール、ファイル、チャット、会議、接続したアプリに散らばった情報を結び付け、答えに仕事の文脈を乗せます。

### Work IQのオンとオフはどこで切り替えますか？
Microsoft CopilotアプリのChat画面の左上にある［Work IQ］ボタンです。以前の［作業］と［Web］のタブは、このボタンに置き換えられました。

### Work IQをオフにすると何が変わりますか？
メールやファイルなどの作業データを見ずに答えます。添付したもの、公開されているWebの情報、プロフィールと個人用設定は使います。

### Work IQは無料で使えますか？
Microsoft Copilotのアドオン ライセンスを持つ人は、Copilot ChatやMicrosoft 365 Copilotの画面で使えます。Work IQ APIやCLI、自社のエージェントからの利用は、使った分だけの従量課金です。

### Work IQのボタンが表示されません
サポート記事に書かれている条件は、Microsoft Copilotのアドオン ライセンスを持っていることです。ライセンスの割り当てを管理者に確かめてください。

### Work IQで他人のファイルも見られますか？
その人が見る権限を持つファイルだけを参照します。共有の範囲が広すぎると、他人のファイルも権限の範囲として見えます。Copilotは既存のMicrosoft 365のアクセス許可を守るので、見えるかどうかは共有の設定で決まります。

### Work IQ CLIはいつから使えますか？
Microsoft Learnのドキュメントによると、2026年6月16日に一般提供になりました。プレビュー版を使っていた場合は、一般提供版への更新が必要です。

## 出典

本文の内容は2026年10月3日に取得した次のページで確認しています。

- [Copilot はプロンプトに応答するためにどのような情報を使用しますか?](https://support.microsoft.com/ja-jp/microsoft-365-copilot/what-information-does-copilot-use-to-answer-my-prompt)（Microsoft サポート。Work IQとは、使えるライセンス、オンとオフ、作業・Webのタブの置き換え、アクセス許可）
- [Microsoft Copilot Chatの回答のソースを制御および確認する](https://support.microsoft.com/ja-jp/Microsoft-365-Copilot/control-review-sources-copilot-chat)（Microsoft サポート。データソースの変更、すべて無効にする）
- [Work IQ の概要](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/work-iq/)（Microsoft Learn。A2A・MCP・REST、ライセンスと従量課金）
- [Microsoft Work IQ CLI](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/work-iq-cli)（Microsoft Learn。一般提供の日付、使う条件）
- [Microsoft Copilot Studio での Work IQ（プレビュー）](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/add-work-iq)（Microsoft Learn。3つの層、読み取り専用、支出ポリシー）
- [Microsoft Copilot 従量課金制サービスの概要](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/pay-as-you-go/overview)（Microsoft Learn。Work IQ APIの課金を管理センターで管理）
