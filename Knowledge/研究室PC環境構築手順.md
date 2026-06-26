# 研究室PC環境構築手順

このPCと同じClaude Code環境を別のWindowsPC（研究室PC）に作る手順。

## 前提
- Google Drive for Desktopをインストール済みで `G:\マイドライブ\` がマウントされている
- （スクリプト類はGoogle Drive経由で共有されるので別途コピー不要）

---

## 1. インストールするもの

| ソフト | バージョン目安 | 入手先 |
|---|---|---|
| Node.js | v24以上 | nodejs.org |
| Python | 3.13 | python.org |
| Git | 最新 | git-scm.com |
| Claude Code | 最新 | `npm install -g @anthropic-ai/claude-code` |
| Google Drive for Desktop | 最新 | google.com/drive/download |

### Claude Codeのインストール
Node.jsインストール後、コマンドプロンプトで：
```
npm install -g @anthropic-ai/claude-code
```

---

## 2. Pythonライブラリのインストール

```
pip install anthropic json-repair
```

---

## 3. MCP設定（Obsidian Vault接続）

以下のファイルを作成・編集：
`C:\Users\[ユーザー名]\AppData\Roaming\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "obsidian-vault": {
      "command": "C:\\Program Files\\nodejs\\node.exe",
      "args": [
        "C:\\Users\\[ユーザー名]\\AppData\\Roaming\\npm\\node_modules\\@modelcontextprotocol\\server-filesystem\\dist\\index.js",
        "G:\\マイドライブ\\Obsidian Vault"
      ]
    }
  }
}
```

※ `[ユーザー名]` は実際のWindowsユーザー名に変更する。
※ server-filesystemは `npm install -g @modelcontextprotocol/server-filesystem` でインストール。

---

## 4. タスクスケジューラ設定

**PowerShellを管理者として開いて**以下を実行：

```powershell
$python = "C:\Users\[ユーザー名]\AppData\Local\Programs\Python\Python313\python.exe"
$dir = "G:\マイドライブ\Claude\セッション"

# Claude会話自動保存（毎日12時）
$action1 = New-ScheduledTaskAction -Execute $python -Argument "`"$dir\save_all_sessions.py`"" -WorkingDirectory $dir
$trigger1 = New-ScheduledTaskTrigger -Daily -At "12:00"
$settings1 = New-ScheduledTaskSettingsSet -StartWhenAvailable
Register-ScheduledTask -TaskName "Claude会話自動保存" -Action $action1 -Trigger $trigger1 -Settings $settings1 -Force

# ProcessLogsToObsidian（ログオン時30秒後）
$action2 = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c `"$dir\run_process_logs.bat`"" -WorkingDirectory $dir
$trigger2 = New-ScheduledTaskTrigger -AtLogOn
$settings2 = New-ScheduledTaskSettingsSet -StartWhenAvailable
Register-ScheduledTask -TaskName "ProcessLogsToObsidian" -Action $action2 -Trigger $trigger2 -Settings $settings2 -RunLevel Highest -Force
```

※ `$python` のパスはPythonのインストール先に合わせて変更する。
※ `where python` コマンドでパスを確認できる。

---

## 5. config.envのAPIキー設定

`G:\マイドライブ\Claude\セッション\config.env` にAnthropicのAPIキーが必要。
このファイルはGoogle Drive経由で共有されるので、自動的に使える。

---

## 6. 動作確認

```powershell
schtasks /Run /TN "ProcessLogsToObsidian"
```

`G:\マイドライブ\Claude\セッション\process_logs.log` にエラーがなければOK。

---

## 注意事項（このPCで学んだこと）

- タスクスケジューラは `python` ではなくフルパスを使う（PATHが通らない）
- バッチファイルはShift-JIS（CP932）で保存する
- タスクの変更には管理者権限が必要
- `claude_desktop_config.json` のパスに日本語が含まれる場合は文字化けに注意
