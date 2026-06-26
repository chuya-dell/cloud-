## Claude MCP経由でObsidian Vaultの読み書き

### 概要
Claude MCPを使用することで、ClaudeがObsidian Vault内のファイルを直接読み書きできる状態が構築済み。これは claude.aiのWeb版・アプリでも同様に利用可能。

### 詳細

#### 既存の設定
- **MCP設定ファイル**: `C:\Users\chuya\AppData\Roaming\Claude\claude_desktop_config.json`
- **マウントポイント**: `G:\マイドライブ\Obsidian Vault`
- **Server**: `server-filesystem` で Vault全体にアクセス可能

#### 動作確認済みの操作
- Obsidian Vaultへのmdファイル読込
- mdファイルの直接編集・作成
- フォルダ構造の認識

#### Claude.ai（Web/アプリ）での利用
- MCP設定は Claude Desktopで管理されているため、Web版でも同じVaultに自動接続
- 手動トリガー（「この会話をObsidianに保存して」と命令）により、ClaudeがMCP経由でファイル作成可能
- 完全自動化ではないが、確実性が高い

### 参考
- 日付: 2026-06-20
- 環境: Windows 11、Google Drive 5TB
- 前回セッション: Obsidian Vault Google Drive sync architecture
