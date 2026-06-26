## 研究室PC環境構築チェックリスト

### 概要
研究室のWindowsPC（およびMac・二番優先）で現在のPC環境と同じセットアップをするための準備リスト。

### 優先タスク

1. **Claude Code のインストール**
   - 方法1: `npm install -g @anthropic-ai/claude-code`
   - 方法2: 公式インストーラーから

2. **Google Drive for Desktop のインストール**
   - `G:\マイドライブ` がマウントされることを確認
   - 設定: ストレージ最適化またはミラーリングモード選択

3. **Node.js のインストール**
   - MCP（Model Context Protocol）サーバー実行用
   - LTS版推奨

4. **obsidian-vault MCP の設定**
   - `claude_desktop_config.json` に以下を追記:
   ```json
   "mcpServers": {
     "obsidian-vault": {
       "command": "node",
       "args": ["/path/to/obsidian-vault-mcp"]
     }
   }
   ```

5. **タスクスケジューラ登録**
   - `register_task.ps1` を修正（パスを研究室PC用に）
   - PowerShell管理者実行

6. **config.env のコピー**
   - Anthropic APIキーを設定
   - セッション保存パスを確認

### Mac環境構築
- 優先度: 低め（将来対応）
- 内容: 上記と同様だが、MacのパスやPackage Manager対応を調整

### 参考
- 日付: 2026-06-21
