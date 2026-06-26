## ngrokを使ったMCP Server公開設定

### 概要
ローカルのMCPサーバーをngrokのHTTPSトンネルで公開し、claude.aiのRemote MCPとして接続する方法。ngrokの無料プランでもStatic Domain（固定URL）が1つ使用可能。

### 詳細

#### 1. ngrokインストール
```powershell
winget install ngrok
```

#### 2. ngrokアカウント作成
- https://ngrok.com でSign up
- ダッシュボードから Authtoken をコピー

#### 3. Authtokenを設定
```powershell
ngrok config add-authtoken <YOUR_AUTHTOKEN>
```

#### 4. Static Domain取得
- ngrokダッシュボード → Cloud Edge → Domains → New Domain
- 無料のstatic domain自動生成（例：`styling-shakily-underfed.ngrok-free.dev`）

#### 5. ngrok起動（StreamableHTTPモード）
```powershell
ngrok http --domain=<STATIC_DOMAIN> 8766
```

### トラブルシューティング

#### Acceptヘッダーエラー
- 問題：サーバー側が`Accept: application/json, text/event-stream`を要求するが、claude.aiが`Accept: */*`を送信
- 解決：プロキシでヘッダーを書き換えるか、サーバー実装を修正

#### 502/503エラー
- 原因：多重SSE接続でサーバークラッシュ
- 解決：StreamableHTTPモード（ポート8766）に変更

#### OAuth動的登録失敗
- 原因：`/.well-known/oauth-authorization-server`エンドポイント欠如
- 解決：登録エンドポイントをプロキシまたはサーバーに追加

### 参考
- 日付: 2026-06-21
