## 研究室PC環境構築チェックリスト

### 概要
研究室のWindowsおよびMacを、メインPC同様の環境にセットアップするための手順。
Macは優先度低め。

### 必須セットアップ（優先度高）

1. **Claude Code インストール**
   - `npm install -g @anthropic-ai/claude-code` または公式インストーラー

2. **Google Drive for Desktop インストール**
   - `G:\マイドライブ` のマウント確認

3. **Node.js インストール**
   - MCP サーバー実行用

4. **obsidian-vault MCP 設定**
   - `claude_desktop_config.json` に以下を追記：
   ```json
   "obsidian-vault": {
     "command": "node",
     "args": ["<obsidian_vault_mcp_path>"]
   }
   ```

5. **タスクスケジューラ登録**
   - `register_task.ps1` を修正して実行
   - パス設定に注意：`G:\マイドライブ\Claude\セッション`

6. **config.env のコピー**
   - Anthropic APIキーを設定

### 参考
- 日付: 2026-06-21
