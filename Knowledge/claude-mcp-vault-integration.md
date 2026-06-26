## Claude MCPでObsidian VaultへのAI読み書き統合

### 概要
ClaudeがModel Context Protocol（MCP）を通じてObsidian Vaultを直接読み書きできるようにする設定。ローカルPC上でMCPサーバーを起動し、`claude_desktop_config.json` に接続設定を記述することで実現。

### 詳細

#### MCP設定ファイルの場所と形式
- **ファイルパス**: `C:\Users\<ユーザー名>\AppData\Roaming\Claude\claude_desktop_config.json`
- **設定例**:
```json
{
  "mcpServers": {
    "obsidian-vault": {
      "command": "C:\Program Files\nodejs\node.exe",
      "args": [
        "C:\Users\<ユーザー名>\AppData\Roaming\npm\node_modules\@modelcontextprotocol\server-filesystem\dist\index.js",
        "G:\マイドライブ\Obsidian Vault"
