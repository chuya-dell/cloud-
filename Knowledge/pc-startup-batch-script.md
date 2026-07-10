---
date: 2026-06-21
theme: Windowsスタートアップフォルダによる自動起動バッチ設定（MCPサーバー・ngrok）
status: reference
tags: [Windows, スタートアップ, バッチ, ngrok, MCP]
---

## summary
PC起動時にObsidian MCPサーバーとngrokトンネルを自動起動するため、タスクスケジューラより簡易な「スタートアップフォルダ」にバッチファイルを配置する方法。管理者権限不要。

## location
`C:\Users\<USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

## batch_example
```batch
@echo off
cd /d C:\Users\chuya
start "Obsidian MCP Server" node mcp-server.js
timeout /t 2 /nobreak
start "ngrok tunnel" ngrok http --domain=styling-shakily-underfed.ngrok-free.dev 8766
```

## caveat
- 起動ポート番号の記録に8765と8766のブレが過去にあり。実際の稼働設定は `Knowledge/claude_ai_obsidian_mcp` 側の最新情報を正とする
- 遅延起動（timeout/sleep）でMCPサーバー→ngrokの起動順序を保証

## pros
- 管理者権限不要、タスクスケジューラより設定簡単
- バッチファイル削除で簡単に無効化可能

## cons
- ターミナルウィンドウが自動表示される（非表示化にはVBScriptラッパーが必要）
- 複数コマンドは複数バッチファイルまたは`start`コマンドで並列実行
