## 会話ログ自動構造化スクリプト仕様

### 概要
Claude会話ログを自動読み込み→API分類→Obsidian書き込みするPythonスクリプト。PC起動時に自動実行される。

### スクリプト構成

**process_logs_to_obsidian.py**
- 未処理ログファイルを特定（processed_logs.jsonで管理）
- Anthropic API（claude-haiku-4-5）に各ログを送信
- タスク・知見・決定に自動分類
- Daily/YYYY-MM-DD.md に追記
- Knowledge/Decision フォルダに重要項目ファイルを生成
- 処理済みフラグを更新

**config.env**
- ANTHROPIC_API_KEY を保存
- APIキー: sk-ant-api03-5lNzypkWqrhzUHnyBa06JF-... (実装済み)

**processed_logs.json**
- 処理済みファイルの履歴管理
- 初回実行時に自動生成

**register_task.ps1**
- タスクスケジューラに登録するPowerShellスクリプト
- PC起動30秒後に実行トリガー
- 管理者権限必須

### 実行方法

**手動実行**
```
cd "G:\マイドライブ\1.実験データ_gdrive\claud.セッション"
python process_logs_to_obsidian.py
```

**自動実行登録**
PowerShell（管理者）で以下を実行：
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass; & "G:\マイドライブ\1.実験データ_gdrive\claud.セッション\register_task.ps1"
```

### 出力フォルダ構成
```
Obsidian Vault/
├── Daily/
│   ├── 2026-06-20.md （追記形式）
│   └── ...
├── Knowledge/
│   ├── xxxx-yyyy.md （自動生成）
│   └── ...
├── Decision/
│   ├── xxxx.md （自動生成）
│   └── ...
└── Logs/ （元ログ保存）
```

### API使用量
- モデル: claude-haiku-4-5（コスト最小化版）
- 1ログファイル = 1 API呼び出し
- 目安: 1回あたり $0.0001〜$0.001 (0.01〜0.15円)

### 参考
- 日付: 2026-06-20
