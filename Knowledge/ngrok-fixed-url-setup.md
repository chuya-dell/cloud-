## ngrokを使った固定URL（Static Domain）の取得と設定

### 概要
ngrokの無料アカウントを使用して固定のstatic domainを1つ取得し、ローカルサーバーをHTTPS公開する方法。Cloudflareのnamed tunnelと異なり、ドメイン登録が不要。

### 手順

#### 1. ngrokのインストール
```powershell
choco install ngrok
```

#### 2. アカウント登録
- https://ngrok.com にアクセス
- Googleアカウントで登録
- ダッシュボードから **Authtoken** をコピー

#### 3. Authtokenの設定
```powershell
ngrok config add-authtoken <YOUR_AUTHTOKEN>
```

#### 4. Static Domainの取得
1. ngrokダッシュボード → **Cloud Edge** → **Domains**
2. **「+ New Domain」** をクリック
3. 自動生成されたstatic domain（例：`styling-shakily-underfed.ngrok-free.dev`）をコピー

#### 5. サーバーの起動
```powershell
ngrok http --domain=<YOUR_STATIC_DOMAIN> <PORT>
```
例：
```powershell
ngrok http --domain=styling-shakily-underfed.ngrok-free.dev 8080
```

### 利点
- 無料でstatic domain 1つ取得可能
- Cloudflareと異なりドメイン登録不要
- 毎回同じURLで公開できる（URL変更が発生しない）

### 注意点
- 無料プランではstatic domainは1つまで
- ngrokプロセスを常時実行する必要がある

### 参考
- 日付: 2026-06-21
