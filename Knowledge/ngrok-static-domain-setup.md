---
date: 2026-06-21
theme: ngrok固定URL（Static Domain）によるMCPサーバー公開設定
status: resolved
tags: [ngrok, MCP, claude.ai, リモート接続]
related: ["Knowledge/claude_ai_obsidian_mcp"]
security_note: authtokenは元ノートに平文記載されていたため本統合時に削除。実際のトークンは Knowledge/claude_ai_obsidian_mcp 側にも記載あり、要ローテーション検討
---

## summary
ngrokの無料アカウントでStatic Domain（固定URL）を1つ取得し、ローカルのMCPサーバーをHTTPSで安定公開してclaude.aiのRemote MCPとして接続する方法。Cloudflareのnamed tunnelと異なりドメイン登録不要。

## setup
1. インストール: `winget install ngrok`（または `choco install ngrok`）
2. https://ngrok.com でアカウント登録（Googleアカウント可）→ ダッシュボードからAuthtokenをコピー
3. 認証設定: `ngrok config add-authtoken <YOUR_AUTHTOKEN>`（⚠実トークンをコードに直書き・ノート保存しない）
4. Static Domain取得: ダッシュボード → Cloud Edge → Domains → 「+ New Domain」で自動生成（例: `styling-shakily-underfed.ngrok-free.dev`）
5. 起動（StreamableHTTPモード推奨）: `ngrok http --domain=<STATIC_DOMAIN> 8766`

## pros_cons
- 利点: 無料でstatic domain 1つ取得可、毎回同じURLで公開（URL変更なし）
- 制約: 無料プランはstatic domain 1つまで、ngrokプロセス常時実行が必要、認証なしでは外部から誰でもアクセス可能（要注意）

## troubleshooting
| 症状 | 原因 | 対応 |
|---|---|---|
| Acceptヘッダーエラー | サーバーが`Accept: application/json, text/event-stream`を要求するがclaude.aiは`Accept: */*`を送信 | プロキシでヘッダー書き換え、またはサーバー実装修正 |
| 502/503エラー | 多重SSE接続でサーバークラッシュ | StreamableHTTPモード（ポート8766）に変更 |
| OAuth動的登録失敗 | `/.well-known/oauth-authorization-server`エンドポイント欠如 | 登録エンドポイントをプロキシまたはサーバーに追加 |

## related
claude.ai側の接続設定（URL登録・OAuth等の詳細）は `Knowledge/claude_ai_obsidian_mcp` 参照
