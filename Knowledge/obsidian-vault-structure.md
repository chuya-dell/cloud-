---
date: 2026-06-21
theme: Obsidian Vaultシステム構成全体
status: reference
tags: [Obsidian, Vault, システム構成]
related: ["Knowledge/obsidian-vault-zotero-folder-structure", "Knowledge/zotero-to-obsidian-flow"]
---

## Obsidian Vault システム構成

### 概要
Google Drive上でObsidian Vaultを構築し、Claude MCPによる読み書き、自動ログ保存システムを実装した知識管理基盤。

### 保管場所
- **AI会話ログ**: `G:\マイドライブ\AI会話ログ\`
- **環境構築ログ**: `G:\マイドライブ\Obsidian Vault\Logs\`
- **Dailyノート**: `G:\マイドライブ\Obsidian Vault\Daily\`
- **主要フォルダ**: Daily / Decision / Knowledge / Mistakes
- **Zotero論文**: `G:\マイドライブ\Obsidian Vault\Zotero\`

### 構成ファイル
- INDEX.md: Vaultの目次・全体構成
- CLAUDE.md: Claude用ガイド・操作マニュアル

### 自動化スクリプト
- `save_session.py`: 単一セッションログ保存
- `save_all_sessions.py`: 全セッション一括保存
- `process_logs_to_obsidian.py`: Claude APIによる自動構造化
- `zotero_to_obsidian.py`: Zotero論文をmd化

### 実行スケジュール
- Windowsタスクスケジューラでログオン時に自動実行

### 同期方法
- iPhone: Remotely Save + Dropbox
- Web: Geminiアプリ × Google Drive

### 参考
- 日付: 2026-06-21
