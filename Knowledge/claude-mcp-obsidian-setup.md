---
date: 2026-06-21
theme: Claude MCP（server-filesystem）によるObsidian Vault連携設定
status: resolved
tags: [Claude, MCP, Obsidian, server-filesystem, 自動化]
related: ["Knowledge/mcp-obsidian-vault-troubleshooting", "Knowledge/claude_ai_obsidian_mcp"]
---

## summary
Claude Desktop / claude.ai（Web・アプリ）から MCP（Model Context Protocol）の server-filesystem 経由で Obsidian Vault（Google Drive上）を直接読み書きできる環境を構築済み。claude.aiブラウザからの接続はngrok経由の別構成 → `Knowledge/claude_ai_obsidian_mcp` 参照。接続トラブル時 → `Knowledge/mcp-obsidian-vault-troubleshooting` 参照。

## config
- 設定ファイル: `C:\Users\<username>\AppData\Roaming\Claude\claude_desktop_config.json`
- マウントポイント: `G:\マイドライブ\Obsidian Vault`（実体は `F:\GoogleDrive_local\Obsidian Vault`）
- 設定例:
```json
{
  "mcpServers": {
    "obsidian-vault": {
      "command": "C:\\Program Files\\nodejs\\node.exe",
      "args": [
        "C:\\Users\\<username>\\AppData\\Roaming\\npm\\node_modules\\@modelcontextprotocol\\server-filesystem\\dist\\index.js",
        "G:\\マイドライブ\\Obsidian Vault"
      ]
    }
  }
}
```

## environment
- Windows 11 / Node.js v24.17.0 / Python 3.13

## connected_services
- server-filesystem（Obsidian Vault直接読み書き）
- Google Calendar / Gmail / Notion

## folder_structure
Daily/・Decision/・Knowledge/・Mistakes/・Logs/・Zotero/（論文386件）・INDEX.md（ナビゲーション）

## automation_pipeline
1. `save_session.py`: 個別セッションのログ取得
2. `save_all_sessions.py`: 全セッション一括保存
3. `process_logs_to_obsidian.py`: Claude APIで自動構造化
4. Windowsタスクスケジューラでログオン時に自動実行
- 出力先: `G:\マイドライブ\AI会話ログ\` → Vault統合 `G:\マイドライブ\Obsidian Vault\`

## claude_ai_web_usage
- MCP設定はClaude Desktopで管理され、Web版でも同じVaultに自動接続
- 完全自動ではなく、「この会話をObsidianに保存して」等の手動トリガーが基本

## session_start_procedure
1. INDEX.md を確認
2. MCPサーバーに自動接続
3. Vaultへの読み書き可能な状態を確認
