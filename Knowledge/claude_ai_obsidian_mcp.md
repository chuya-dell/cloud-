# claude.ai（ブラウザ）からObsidian Vaultへ接続する方法

## 構成

```
claude.ai → ngrok（固定URL）→ obsidian-mcp-http.js → server-filesystem → Obsidian Vault
```

## ファイル場所

| ファイル | 場所 |
|---|---|
| MCPサーバー | `C:\Users\chuya\obsidian-mcp-http.js` |
| 起動バッチ | `C:\Users\chuya\obsidian-mcp-start.bat` |
| 自動起動 | `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\ObsidianMCP.bat` |
| ngrok設定 | `%LOCALAPPDATA%\ngrok\ngrok.yml` |

## URL

- 固定URL: `https://styling-shakily-underfed.ngrok-free.dev`
- MCPエンドポイント: `https://styling-shakily-underfed.ngrok-free.dev/mcp`

## claude.aiの設定

`https://claude.ai/customize/connectors` → Obsidian Vault → URL: `/mcp`

## 起動方法

PC起動時に自動起動。手動で起動する場合は `obsidian-mcp-start.bat` をダブルクリック。

## トラブルシューティング

- supergaetewayはNG（Acceptヘッダー `application/json, text/event-stream` を強制するがclaude.aiは `*/*` を送る）
- OAuth動的クライアント登録（`/oauth/register`）が必要
- ngrok認証トークン: `3FPL3H1y333UwBzTFnYyBZd0viY_7LWnwKouSQ4fxUWbq7W4U`
