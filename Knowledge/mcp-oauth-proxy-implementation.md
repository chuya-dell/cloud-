## MCPサーバーのOAuth対応プロキシ実装

### 概要
claude.aiのRemote MCP連携で必要なOAuth認可機能をプロキシサーバー経由で追加する方法

### 詳細

#### 問題
- supergatewayがOAuthメタデータエンドポイント（`/.well-known/oauth-authorization-server`）非対応
- claude.aiが自動クライアント登録（Dynamic Client Registration）を要求
- Acceptヘッダーの厳密チェック（`application/json, text/event-stream`）が制限的

#### 解決策
1. OAuthプロキシレイヤーの追加（ポート8765）
2. Acceptヘッダー書き換え機能
3. Session ID付与機能
4. エンドポイント：`/mcp` で統一

#### 実装箇所
- プロキシ：`C:\Users\chuya\mcp-oauth-proxy.js`（Node.js Express）
- MCPサーバー：ローカルポート8080
- ngrokトンネル：`https://styling-shakily-underfed.ngrok-free.dev/mcp`

#### レジストレーション流れ
```
claude.ai → ngrok → プロキシ(8765) → supergateway(8080)
↓
OAuthメタデータ取得 → クライアント登録 → トークン取得 → MCP接続
```

### 参考
- 日付: 2026-06-21
