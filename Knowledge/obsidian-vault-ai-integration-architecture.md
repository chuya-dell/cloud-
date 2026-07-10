---
date: 2026-06-21
theme: Obsidian Vault × AI統合アーキテクチャ全体図
status: reference
tags: [Obsidian, AI統合, アーキテクチャ]
related: ["Knowledge/ai-role-division-map", "Knowledge/obsidian-vault-google-drive-sync"]
---

## Obsidian Vault × AI統合アーキテクチャ

### 概要
Obsidianを知識の中心に置き、複数のAI（Claude・Gemini・NotebookLM）を役割分担で連携させるシステム設計。AIに依存せず、Vault所有権を保ちながら、どのAIからでも参照可能な仕組み。

### 全体構成図
```
Google Drive（データの家）
    ↓ Google Drive for Desktop（同期）
    ↓
Obsidian Vault（ローカルPC）
    ├─ PC → ClaudeのMCP（読み書き）
    ├─ iPhone → Remotely Save + Dropbox（読み書き）
    ├─ iPad → Remotely Save + Dropbox（読み書き）
    └─ その他デバイス → MCP設定コピー
        ↓
AI層（役割分担）
    ├─ Claude（日常的なVault操作・自動化・書き込み）※MCP経由
    ├─ NotebookLM（深い議論・複数ファ
