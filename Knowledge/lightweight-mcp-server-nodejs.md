## Node.jsで実装した軽量MCPサーバー

### 概要
supergatewayの制限（Acceptヘッダー厳密チェック、多重SSE接続でクラッシュ）を回避するため、Node.jsで独自の軽量MCPサーバーを実装。

### 詳細

#### 主な機能
- Obsidian Vault MCPをプロキシ
- Acceptヘッダー厳密チェックを無効化
- OAuth動的登録エンドポイント追加
- POST /mcp エンドポイントでStreamableHTTP対応
- mcp-session-id ヘッダー追加

#### 起動
```powershell
node mcp-server.js
```

#### 設定
