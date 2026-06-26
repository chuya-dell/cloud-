## Claude会話ログ自動整理システムの構成

### 概要
Claude.aiの会話ログをObsidianに自動で分類・整理するシステム。PC起動時に自動実行される。

### システム構成
```
claud.セッション/
├── process_logs_to_obsidian.py  ← メイン処理スクリプト
├── config.env                    ← APIキー設定ファイル
├── run_process_logs.bat          ← Windows実行バッチ
├── register_task.ps1             ← タスクスケジューラ登録スクリプト
├── processed_logs.json           ← 処理済みファイル管理
└── save_all_sessions.py          ← 既存ログ保存スクリプト
```

### 処理の流れ
1. **PC起動時トリガー**: タスクスケジューラが自動実行
2. **30秒待機**: Google Driveのマウント完了を待つ
3. **ログ収集**: save_all_sessions.pyで新規会話ログ取得
4. **未処理判定**: processed_logs.jsonで処理済みを確認
5. **API処理**: Claude API（Haiku）で会話
