# 💡 Knowledge（知識・解決法）

## 使い方
トラブル解決・ツールの発見・環境構築メモなど再利用できる知識を蓄積する。

---

## Notion GPUクラッシュ解決法（Windows）

**症状**: Notionをダブルクリックしても起動しない / GPUプロセスがクラッシュ  
**環境**: Windows 11 / Intel 13th Gen / Notion 7.22.0

**解決手順:**
1. GPUキャッシュを削除（GPUCache, DawnGraphiteCache, DawnWebGPUCache）
2. ソフトウェアレンダリングで起動:

```powershell
Stop-Process -Name "Notion" -Force
Remove-Item "$env:APPDATA\Notion\GPUCache" -Recurse -Force
Remove-Item "$env:APPDATA\Notion\DawnGraphiteCache" -Recurse -Force
Remove-Item "$env:APPDATA\Notion\DawnWebGPUCache" -Recurse -Force
Start-Process "$env:LOCALAPPDATA\Programs\Notion\Notion.exe" -ArgumentList '--disable-gpu --disable-gpu-compositing --use-gl=swiftshader --no-sandbox'
```

**ログ場所**: `C:\Users\chuya\AppData\Roaming\Notion\logs\main.log`

---

## Claude Code hookメモ

- Stopフックはアプリを×で閉じると発火しない場合がある
- 手動保存は動作確認済み
- 設定ファイル: `C:\Users\chuya\.claude\settings.json`
- 保存スクリプト: `G:\マイドライブ\1.実験データ_gdrive\claud.セッション\save_session.py`
- 保存先: `G:\マイドライブ\AI会話ログ\`

---

## claude.ai → Obsidian MCP接続

- `obsidian-mcp-http.js`（カスタムMCPサーバー、port 8765）
- ngrok固定URL: `https://styling-shakily-underfed.ngrok-free.dev`
- PCオン・ターミナル起動必須（iOSからは不可）
- スタートアップフォルダに自動起動登録済み

---

## トークン節約・セッション運用

**問題**: Claude Codeのセッションを運用するとトークンをすぐ使い切る  
**対策**:
- `/clear` コマンドで会話履歴リセット（記録は消えない）
- 再開時は「Obsidianの最新Dailyを読んで再開して」でOK
- 作業の区切りで記録→/clear→新セッションの流れで運用
- セッション開始時の読み込みファイル数を絞る

---

## Claude会話自動保存の設定手順

毎日12時（PC未起動の場合は次回起動時）にClaude Codeの全会話をGoogle Driveに自動保存する。

**ファイル**:
- 保存スクリプト: `G:\マイドライブ\1.実験データ_gdrive\claud.セッション\save_all_sessions.py`
- 保存先: `G:\マイドライブ\AI会話ログ\`

**別PCでの設定手順**:
```powershell
$action = New-ScheduledTaskAction -Execute "python" -Argument "`"G:\マイドライブ\1.実験データ_gdrive\claud.セッション\save_all_sessions.py`""
$trigger = New-ScheduledTaskTrigger -Daily -At "12:00"
$settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Minutes 2) -StartWhenAvailable
Register-ScheduledTask -TaskName "Claude会話自動保存" -Action $action -Trigger $trigger -Settings $settings -Force
```

**注意**: Python・GoogleドライブのGドライブマウントが必要

---

## iPhoneでのAI連携メモ

**できること**:
- Geminiアプリ → DriveのZoteroフォルダ参照 ✅
- Obsidianアプリ → ノート読み書き ✅

**できないこと**:
- ClaudeのiOSアプリ → MCPなしのためVault参照不可 ❌

**未解決**:
- Remotely Save（Dropbox）の同期が更新されていない

---

## Mac環境構築手順

### Google DriveのMacパス
`/Users/[ユーザー名]/Library/CloudStorage/GoogleDrive-chuya2816@gmail.com/マイドライブ`

### インストールするもの
```bash
# Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Node.js / Python / Git
brew install node python git

# Claude Code
npm install -g @anthropic-ai/claude-code
```

### MCP設定（Obsidian Vault接続）
設定ファイル: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "obsidian-vault": {
      "command": "node",
      "args": ["/usr/local/lib/node_modules/@modelcontextprotocol/server-filesystem/dist/index.js",
        "/Users/[ユーザー名]/Library/CloudStorage/GoogleDrive-chuya2816@gmail.com/マイドライブ/Obsidian Vault"]
    }
  }
}
```

---

## 研究室PC環境構築手順

**インストール:** Node.js（v24以上）、Python 3.13、Git、Claude Code（`npm install -g @anthropic-ai/claude-code`）、Google Drive for Desktop

**Pythonライブラリ:** `pip install anthropic json-repair`

**MCP設定:** `C:\Users\[ユーザー名]\AppData\Roaming\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "obsidian-vault": {
      "command": "C:\\Program Files\\nodejs\\node.exe",
      "args": ["...server-filesystem/dist/index.js", "G:\\マイドライブ\\Obsidian Vault"]
    }
  }
}
```

**タスクスケジューラ設定（PowerShell管理者）:**
```powershell
$dir = "G:\マイドライブ\Claude\セッション"
$action = New-ScheduledTaskAction -Execute "python" -Argument "`"$dir\save_all_sessions.py`"" -WorkingDirectory $dir
Register-ScheduledTask -TaskName "Claude会話自動保存" -Action $action -Trigger (New-ScheduledTaskTrigger -Daily -At "12:00") -Force
```

---

## API選定経緯（会話ログ構造化システム）

**結論**: Anthropic API（claude-haiku-4-5-20251001）を採用

**試したAPIと結果**
- Gemini API（chuya2816アカウント）→ 失敗: Google AI Pro契約で無料ティア無効化
- Gemini API（別アカウント）→ 失敗: 支払い情報未設定で無料枠使えず
- Anthropic API → **成功**: $5チャージで数年分、月数十〜数百円程度

**キー保存場所**: `G:\マイドライブ\1.実験データ_gdrive\claud.セッション\config.env`

---

## AI役割分担マップ

| AI | 主な用途 |
|---|---|
| **Claude** | Vault読み書き・記録・自動化・日常補助・Googleカレンダー/Gmail/Notion操作 |
| **Gemini** | PDF/Googleドキュメント直接参照・実験データ分析・iPhone論文添付質問 |
| **NotebookLM** | hmC論文386件横断検索・議論・ソース引用付き回答 |
| **ChatGPT** | 画像生成（DALL-E）・Webブラウジング・別視点レビュー |

---

## FDTD ホール型角丸め実装メモ

**方針**: addrevolution で断面プロファイルを回転体にする。r_c_top（上端・内向き）と r_c_bot（底端・外向き）をパラメータスイープ

**断面セクション順**
1. 底面フラット: z=h_Au, r=0→r_hole-r_c_bot
2. 底端arc（外向き）: 中心=(r_hole-r_c_bot, h_Au+r_c_bot), θ=-π/2→0
3. 直線壁: r=r_hole, z=h_Au+r_c_bot → h_hole-r_c_top
4. 上端arc（内向き）: 中心=(r_hole+r_c_top, h_hole-r_c_top), θ=π→π/2
5. COP面で閉じる: r=r_hole+r_c_top→0, z=h_hole
6. 軸沿いで閉じる: r=0, z=h_hole→h_Au

**パラメータ**: r_c_top, r_c_bot = 10〜30 nm でスイープ（Au膜厚の10〜30%目安）

---

## iPhone×Obsidian同期：Remotely Save + Dropbox

**構成:**
```
G:\マイドライブ\Obsidian Vault
  ↓ Remotely Save（PC）
Dropbox (/Apps/remotely-save/Obsidian Vault)
  ↓ Remotely Save（iPhone）
iPhone Obsidian
```

**PC側設定:** コミュニティプラグイン → Remotely Save → Remote Service: Dropbox → Auth認証

**Dropboxレートリミットエラー対応 - Regex Of Paths To Ignore に追加:**
```
Zotero/.*
zotero-library.json
Templates/zotero-template\.md
```

---

## Google Drive マイドライブのClaude関連フォルダ構成
```
G:\マイドライブ\
├── Claude/
│   ├── セッション/     （旧: claud.セッション）
│   └── AI会話ログ/
├── 1.実験データ_gdrive/
└── antigravity_chat_logs/
```

---

## Google DriveでのMarkdownファイル検索インデックス問題

**原因:**
1. MIMEタイプが不確定
2. .md はプレーンテキストとして検索優先度が低い
3. Geminiのテキスト抽出時にパース失敗しやすい

**回避策:**
- **推奨:** NotebookLMをソースとして直接指定（インデックス問題を回避）
- Geminiには手動コピペ or PDF保存が最確実

---

## タスクスケジューラのパス修正
**誤:** `G:\マイドライブ\1.実験データ_gdrive\claud.セッション\`  
**正:** `G:\マイドライブ\Claude\セッション\`

```powershell
$correctPath = "G:\マイドライブ\Claude\セッション"
$action1 = New-ScheduledTaskAction -Execute "python" -Argument "`"$correctPath\save_all_sessions.py`"" -WorkingDirectory $correctPath
Set-ScheduledTask -TaskName "Claude会話自動保存" -Action $action1
$action2 = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c `"$correctPath\run_process_logs.bat`"" -WorkingDirectory $correctPath
Set-ScheduledTask -TaskName "ProcessLogsToObsidian" -Action $action2
```

---

## Claude会話ログ自動整理システムの構成

**処理フロー:** PC起動 → 30秒待機（Google Driveマウント待ち） → ログ収集 → 未処理判定 → Claude API（Haiku）で分類 → Daily/Knowledge/Decision/に書き込み

```
claud.セッション/
├── process_logs_to_obsidian.py  ← メイン処理スクリプト
├── config.env                    ← APIキー設定
├── processed_logs.json           ← 処理済み管理
└── save_all_sessions.py          ← 会話ログ収集
```

---

## ngrok固定URL（Static Domain）設定

```powershell
# インストール
winget install ngrok
# 認証
ngrok config add-authtoken 3FPL3H1y333UwBzTFnYyBZd0viY_7LWnwKouSQ4fxUWbq7W4U
# 起動
ngrok http --domain=styling-shakily-underfed.ngrok-free.dev 8080
```

Static Domain取得: https://dashboard.ngrok.com → Cloud Edge → Domains → New Domain  
固定URL: `https://styling-shakily-underfed.ngrok-free.dev`（無料プランで1つ）

---

## Anthropic API料金詳細
- **claude-haiku-4-5**: 会話ログ1件あたり約$0.0005〜$0.002
- **$5チャージ**: 2,500〜10,000件処理可能
- **月300回処理**: 約$0.3〜$1程度
- プリペイド式・自動引き落としなし

---

## Claude Code Hook機能による会話自動保存

**Hook対応イベント:**
- `Stop`: セッション終了時
- `PreToolUse`/`PostToolUse`: ツール実行前後

```json
{
  "hooks": {
    "Stop": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "python3 C:/path/to/save_session.py",
        "timeout": 60,
        "statusMessage": "会話をObsidianに保存中..."
      }]
    }]
  }
}
```

---

## Claude MCP + Obsidian Vault統合設定

**アーキテクチャ:**
- MCP: server-filesystem（Vault直接読み書き）
- ストレージ: `G:\マイドライブ\Obsidian Vault\`

**自動保存パイプライン:**
1. `save_session.py` → 個別セッションのログ取得
2. `save_all_sessions.py` → 全セッション一括保存
3. `process_logs_to_obsidian.py` → Claude APIで自動構造化
4. タスクスケジューラ → ログオン時に自動実行

---

## Obsidianの日記管理構造

- `Daily/`: 日付別ファイル（YYYY-MM-DD.md）
- `Knowledge/`: 技術的知識・手順
- `Decision/`: 確定した方針・決定事項
- `AI会話ログ/`: セッションログの自動保存

---

## ObsidianとNotionの役割分担設計

| 項目 | Obsidian | Notion |
|---|---|---|
| 確認の手間 | ファイル一覧で直感的 | ページ→DB→データ確認 |
| UI | シンプル | リッチ・豊富 |
| AI連携 | MCP経由で高速 | API経由 |
| 向いている用途 | Claudeの外部記憶 | 人間が見るダッシュボード |

---

## プラズモニック結晶 COPモールド仕様

**ピラー型モールド（六方配置）:**
- ピラー高さ: 200 nm / ピラー直径: 230 nm / 格子定数: 460 nm

**ホール型モールド（六方配置）:**
- ホール深さ: 200 nm / ホール直径: 200 nm / 格子定数: 460 nm

**金属層:** Au、真空蒸着

**シミュレーション:** FDTD法（Lumerical）。真空蒸着のため構造のエッジが丸まると予想される。

記録日: 2026-06-24

---

## タスク優先度・カテゴリ分類フレームワーク

**優先度（緊急度×重要度）:**
- 🔴 高: 締め切りあり、または直近で着手必須
- 🟡 中: 締め切りないが研究・仕事に直結
- 🟢 低: 後回し可能（重要度が低い）
- ⚪ 保留: 判断不要・アイデア段階（Someday/Maybe）

**カテゴリ（7分類）:** 実験、解析、文献、申請書、指導、環境整備、その他

---

## MCP接続管理のベストプラクティス

**推奨構成:**
- 必須: obsidian-vault、Notion、Google Calendar
- オプション: Claude in Chrome
- 削除推奨: Gmail、Google Drive（使用頻度低、トークン消費削減）

設定変更: Claude Codeの右上歯車マークから接続・切断操作

---

## Zotero-Obsidian統合フロー
```
Zotero (論文DB)
  ↓ Zotero Integration プラグイン
Obsidian Vault/Zotero/ (Markdown化)
  ↓ Google Drive同期
Claude MCP / NotebookLM でアクセス可能
```

**同期される情報:** 著者、発行年、雑誌名、DOI、タイトル、Abstract  
**同期されない情報:** ユーザーのメモ、ハイライト、PDF本文、アノテーション  
本VaultはZotLitプラグインを使用（書誌情報とAbstractのみ同期）
