# Claude Desktop - Windowsインストールエラー対処法

## エラー内容

```
Installation failed: AddPackage failed with HRESULT 0x80073CF6
```

MSIXパッケージのインストール失敗。主な原因はWindowsのAppxサービス不具合、権限不足、古いApp Installer。

## 対処手順（上から順番に試す）

### 1. 管理者として実行
インストーラーを右クリック →「管理者として実行」

### 2. App Installerを更新
Microsoft Store → 「App Installer」を検索 → 更新 → 再起動

### 3. Windows Updateを実行
設定 → Windows Update → すべて適用して再起動

### 4. 既存Claudeを完全削除してから再インストール
```
設定 → アプリ → Claude → アンインストール
```
その後、以下のフォルダを手動削除：
```
C:\Users\<ユーザー名>\AppData\Local\AnthropicClaude
C:\Users\<ユーザー名>\AppData\Roaming\Claude
```

### 5. PowerShellで手動インストール（管理者権限）
```powershell
Add-AppxPackage -Path "C:\path\to\ClaudeSetup.exe"
```

### 6. AppxサービスをPowerShellでリセット
```powershell
# 管理者PowerShellで実行
Get-AppxPackage *Claude* | Remove-AppxPackage
```

## 上記で解決しない場合

ログファイルを取得してサポートに送付：
- エラーダイアログの「OK」を押すと自動でExplorerが開く
- ログファイルを https://support.anthropic.com に添付して問い合わせ

## 代替手段（アプリが使えない間）

| 手段 | URL | 特徴 |
|------|-----|------|
| Web版 | claude.ai/code | ブラウザで全機能使用可 |
| CLI版 | npm install -g @anthropic-ai/claude-code | ターミナルで使用 |
| VS Code拡張 | Marketplace検索 | エディタ内で使用 |
