## Claude MCP で Obsidian Vault を直接操作する設定

### 概要
Claude が Obsidian Vault（Google Drive 同期フォルダ）を MCP（Model Context Protocol）経由で直接読み書きできる環境構築方法。

### 環境
- Windows 11
- Node.js v24.17.0
- Python 3.13
- Obsidian Vault: `G:\マイドライブ\Obsidian Vault`

### 設定ファイル
**パス**: `C:\Users\<username>\AppData\Roaming\Claude\claude_desktop_config.json`

**内容例**:
```json
{
  "mcpServers": {
    "obsidian-vault": {
      "command": "C:\Program Files\nodejs\node.exe",
      "args":
