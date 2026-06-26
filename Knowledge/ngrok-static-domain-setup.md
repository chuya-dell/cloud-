## ngrok固定URL（Static Domain）でのMCP公開設定

### 概要
ngrokの無料アカウントで1つ静的ドメイン（Static Domain）を取得し、ローカルMCPサーバーをHTTPSで安定公開する方法

### 詳細

#### 1. ngrokアカウント作成と認証
```powershell
# ngrok インストール
winget install ngrok

# authtoken設定（ダッシュボードからコピー）
ngrok config add-authtoken 3FPL3H1y333UwBzTFnYyBZd0viY_7LWnwKouSQ4fxUWbq7W4U
```

#### 2. Static Domain取得
1. https://dashboard.ngrok.com にログイン
2. Cloud Edge → Domains → New Domain
3. 自動生成されるドメイン（例：`styling-shakily-underfed.ngrok-free.dev`）をコピー

#### 3. トンネル起動
```powershell
ngrok http --domain=styling-shakily-underfed.ngrok-free.dev 8080
```

#### 注意点
- 無料プランは1つの静的ドメインのみ
- 起動のたびに同じURLが生成される
- 外部からのアクセス可能（認証なしではセキュリティ注意）

### 参考
- 日付: 2026-06-21
