---
date: 2026-06-21
theme: ログ保管場所一覧
status: reference
tags: [ログ, 保存先, Google Drive]
related: ["Knowledge/conversation-auto-save-architecture"]
---

## ログ保管場所一覧

### AI会話ログ
- 保存先: `G:\マイドライブ\AI会話ログ\`
- 内容: Claude APIセッションログ
- 自動保存: PC起動時にタスクスケジューラで実行
- ディレクトリ構成案: `AI会話ログ/Claude/`・`AI会話ログ/Gemini/`・`AI会話ログ/その他/`
- ファイル命名規則: `{セッションタイトル}-{YYYYMMDD}.md`（例: `obsidian-vault-gdrive-sync-20260620.md`）

### 環境構築ログ
- 保存先: `G:\マイドライブ\Obsidian Vault\Logs\`
- 内容: システム設定・トラブルシューティング記録

### 日々の作業ログ（Dailyノート）
- 保存先: `G:\マイドライブ\Obsidian Vault\Daily\`
- 内容: 日常作業・実験・学習内容

### Zoteroライブラリ
- 保存先: `G:\マイドライブ\Obsidian Vault\Zotero\`
- 内容: 406件中論文386件をmd化済み（自動同期）
- 形式: Better CSL JSONまたはBetter BibTeX JSON

### 参考
- 日付: 2026-06-21
- 管理ツール: Obsidian Vault（Google Drive連携）、Claude MCP(server-filesystem)
