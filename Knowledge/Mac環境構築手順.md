# Mac環境構築手順

このPCと同じClaude Code環境をMacに作る手順。

## Google DriveのMacパス

```
/Users/[ユーザー名]/Library/CloudStorage/GoogleDrive-chuya2816@gmail.com/マイドライブ
```

※ `[ユーザー名]` はMacのユーザー名（`whoami` コマンドで確認）

---

## 1. インストールするもの

### Homebrew（パッケージマネージャー）
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Node.js / Python / Git
```bash
brew install node python git
```

### Claude Code
```bash
npm install -g @anthropic-ai/claude-code
```

### Google Drive for Desktop
- google.com/drive/download からダウンロード
- インストール後、chuya2816@gmail.com でログイン
- 同期完了後、上記パスでアクセス可能になる

---

## 2. Pythonライブラリのインストール

```bash
pip3 install anthropic json-repair
```

---

## 3. MCP設定（Obsidian Vault接続）

設定ファイルの場所：
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

内容：
```json
{
  "mcpServers": {
    "obsidian-vault": {
      "command": "node",
      "args": [
        "/usr/local/lib/node_modules/@modelcontextprotocol/server-filesystem/dist/index.js",
        "/Users/[ユーザー名]/Library/CloudStorage/GoogleDrive-chuya2816@gmail.com/マイドライブ/Obsidian Vault"
      ]
    }
  }
}
```

※ nodeのパスは `which node` で確認。`/opt/homebrew/bin/node`（Apple Silicon）の場合もある。
※ server-filesystemは `npm install -g @modelcontextprotocol/server-filesystem` でインストール。

---

## 4. 自動起動設定（launchd）

Windowsのタスクスケジューラ相当はMacでは `launchd` を使う。

### シェルスクリプトを作成

```bash
# スクリプト作成
cat > ~/run_process_logs.sh << 'EOF'
#!/bin/bash
GDRIVE="/Users/[ユーザー名]/Library/CloudStorage/GoogleDrive-chuya2816@gmail.com/マイドライブ"
SESSION_DIR="$GDRIVE/Claude/セッション"
cd "$SESSION_DIR"
export ANTHROPIC_API_KEY=$(grep ANTHROPIC_API_KEY config.env | cut -d= -f2)
python3 save_all_sessions.py
python3 process_logs_to_obsidian.py >> process_logs.log 2>&1
EOF

chmod +x ~/run_process_logs.sh
```

### launchdのplistファイルを作成

```bash
cat > ~/Library/LaunchAgents/com.claude.processlogs.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.claude.processlogs</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>/Users/[ユーザー名]/run_process_logs.sh</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>StartInterval</key>
    <integer>43200</integer>
    <key>StandardOutPath</key>
    <string>/tmp/claude_processlogs.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/claude_processlogs_err.log</string>
</dict>
</plist>
EOF
```

### 登録して起動

```bash
launchctl load ~/Library/LaunchAgents/com.claude.processlogs.plist
```

---

## 5. 動作確認

```bash
# 手動実行テスト
bash ~/run_process_logs.sh

# ログ確認
tail -20 "/Users/[ユーザー名]/Library/CloudStorage/GoogleDrive-chuya2816@gmail.com/マイドライブ/Claude/セッション/process_logs.log"
```

---

## 注意事項

- Apple SiliconのMacは `node` のパスが `/opt/homebrew/bin/node` になる場合がある（`which node` で確認）
- Google DriveのパスはGmailアドレスが含まれる（`chuya2816@gmail.com` の部分）
- `launchd` の `StartInterval: 43200` = 12時間ごとに実行（Windowsの毎日12時相当）
- plist内の `[ユーザー名]` は必ず実際のMacユーザー名に変更する
