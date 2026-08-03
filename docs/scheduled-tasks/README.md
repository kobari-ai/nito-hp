# 定期タスクのバックアップ

Claude Codeの定期タスク（scheduled task）の実体は `~/.claude/scheduled-tasks/<タスク名>/SKILL.md`。
`~/.claude/` はClaudeアカウント単位で保存され、**リポジトリには含まれない**。アカウント移行やアプリの再設定で消えるため、ここに写しを置いている。

## 一覧

| ファイル | タスク名 | スケジュール | 内容 |
|---|---|---|---|
| [nito-seo-daily.md](nito-seo-daily.md) | `nito-seo-daily` | 平日 朝9時ごろ | GA4（江東区除くオーガニック）とGSCを見て、新規記事の候補を3本提案する。提案のみで執筆・pushはしない |

## 復元のしかた

Claudeに、このファイルを指してこう頼めば復元できる。

> `docs/scheduled-tasks/nito-seo-daily.md` の内容で、平日朝9時の定期タスクを作り直して

手動でやる場合は、`~/.claude/scheduled-tasks/<タスク名>/SKILL.md` として配置し、Claude Codeのサイドバー「Scheduled」からスケジュールを設定する。

## 更新のしかた

`~/.claude/` 側のSKILL.mdを編集したら、このディレクトリにも反映する。

```bash
cp ~/.claude/scheduled-tasks/nito-seo-daily/SKILL.md docs/scheduled-tasks/nito-seo-daily.md
```

## 補足

- 定期タスクはClaude Codeアプリが起動している間に実行される。閉じている間に時刻が来た場合は、次回起動時に実行される
- タスク内で使う認証情報（`~/.nito/ga4-key.json` など）はリポジトリに含めない。パスだけをSKILL.md内に直書きしている
