---
date: 2026-06-21
theme: MCPサーバーのOAuth対応・軽量Node.jsプロキシ実装
status: resolved
tags: [MCP, OAuth, Node.js, ngrok, claude.ai]
related: ["Knowledge/ngrok-static-domain-setup", "Knowledge/claude_ai_obsidian_mcp"]
---

## summary
claude.aiのRemote MCP連携には、既存のsupergatewayでは対応できないOAuth認可・Acceptヘッダー要件があったため、Node.jsで独自の軽量MCPプロキシサーバーを実装して解決した。

## problem
- supergatewayがOAuthメタデータエンドポイント（`/.well-known/oauth-authorization-server`）非対応
- claude.aiが自動クライアント登録（Dynamic Client Registration）を要求
- Acceptヘッダーの厳密チェック（`application/json, text/event-stream`）が制限的で、claude.aiが送る`Accept: */*`を弾く
- 多重SSE接続でsupergatewayがクラッシュ（502/503エラー）

## solution
Node.jsで軽量MCPサーバー（`mcp-server.js`）を自作し、Obsidian Vault MCPをプロキシする形で以下を実装:
- Acceptヘッダー厳密チェックを無効化
- OAuth動的登録エンドポイント追加
- `POST /mcp` エンドポイントでStreamableHTTP対応
- `mcp-session-id` ヘッダー追加

**起動:**
```powershell
node mcp-server.js
```

## architecture
```
claude.ai → ngrok → mcp-server.js（Node.js, ポート8766, OAuth+ヘッダー対応込み）→ Obsidian Vault
```
旧構成（supergateway使用時）で検討したプロキシレイヤー案:
```
claude.ai → ngrok → OAuthプロキシ(8765) → supergateway(8080) → OAuthメタデータ取得 → クライアント登録 → トークン取得 → MCP接続
```
最終的にはsupergateway自体を自作サーバーで置き換える方式に統合。

## related
- ngrokによる公開設定: `Knowledge/ngrok-static-domain-setup`
- claude.ai側の接続設定: `Knowledge/claude_ai_obsidian_mcp`
