---
date: 2026-06-20
theme: Claude Web と Claude Code の機能比較（会話自動保存対応状況）
status: reference
tags: [Claude, Claude Code, 比較]
related: ["Knowledge/conversation-auto-save-architecture"]
---

## Claude Web と Claude Code の機能比較

### 概要
Claudeのインターフェースは複数あり、会話自動保存機能の対応状況が異なる。

### 各インターフェースの特徴

| インターフェース | 別名 | UIタイプ | Hook機能 | MCP対応 | 自動保存 |
|-----------------|------|---------|---------|--------|----------|
| Claude Code | CLI/デスクトップアプリ | ターミナル風 | ✅ あり | ✅ あり | ✅ 可能 |
| Claude Web | claude.ai | Webアプリ/モバイル | ❌ なし | ✅ あり | ❌ 不可（手動のみ） |
| Claude Desktop | ネイティブアプリ | チャットUI | ❌ なし | ✅ あり | ❌ 不可（手動のみ） |

### 会話保存の実装方法

#### Claude Code（推奨：完全自動）
- `Stop` hookでシェルコマンド実行
- Pythonスクリプトでセッション情報をJSON化してGoogle Driveに保存
- 完全自動、手動操作不要

#### Claude Web/Desktop（手動トリガー）
- 会話終了時に「この会話をObsidianに保存して」と入力
- ClaudeがMCPでObsidian-vault経由でファイルに書き込み
- MCPは両プラットフォームで動作するため実装可能
- ただしユーザーが毎回命令する必要がある

#### Chrome拡張機能による自動化
- 技術的には可能（ページ監視 → API呼び出し → 保存）
- 実装コストが高い（カスタム開発必要）
- Make/Zapierの利用も検討可だが、Webhook非対応のため限界がある

### 推奨される運用方法
1. **Claude Code**: Hook設定で完全自動化
2. **Claude Web**: 手動トリガー（必要に応じて拡張機能化検討）

### 参考
- 日付: 2026-06-20
