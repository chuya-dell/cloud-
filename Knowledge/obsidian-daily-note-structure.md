---
date: 2026-06-21
theme: Obsidianの日記管理構造（フォルダ構成）
status: reference
tags: [Obsidian, フォルダ構成]
---

## Obsidianの日記管理構造

### 概要
Obsidian Vaultは複数のディレクトリに分かれており、各タイプの情報が組織的に管理されている。

### 構成
- **Daily/**: 日付別の日記ファイル（YYYY-MM-DD.md形式）
- **Knowledge/**: 技術的な知識・手順の記録
- **Decision/**: 確定した方針・決定事項の記録
- **AI会話ログ/**: セッションログの自動保存ディレクトリ

### 自動処理
- process_logs_to_obsidian.py がセッションログを自動処理
- 処理対象: AI会話ログディレクトリ内のログファイル
- 処理内容: Daily、Knowledge、Decision各フォルダへの自動記録

### 参考
- 日付: 2026-06-21
