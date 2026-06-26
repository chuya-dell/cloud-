## Claude MCP（server-filesystem）による環境構築

### 概要
Claude MCPを使用してObsidian VaultをGoogle Drive上で直接読み書き可能にした環境。

### 接続済みサービス
- **server-filesystem**: Obsidian Vault直接読み書き
- **Google Calendar**: カレンダー操作
- **Gmail**: メール操作
- **Notion**: Notion操作

### 実現できる操作
- Vault内のDaily / Decision / Knowledge / Mistakes フォルダへの自動記録
- Zotero 386件の論文をVault内で参照・検索
- Google Drive / スプレッドシートとの連携

### セッション開始手順
1. INDEX.mdを確認
2. MCPサーバーに自動接続
3. Vaultへの読み書きが可能な状態

### メリット
- CloudベースのVaultをClaudeが直接管理
- 複数デバイスからの一元管理が可能
- 自動化スクリプトとの連携

### 参考
- 日付: 2026-06-21
