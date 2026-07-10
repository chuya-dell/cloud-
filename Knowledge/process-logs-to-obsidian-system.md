---
date: 2026-06-20
theme: Claude会話ログ自動構造化システム（process_logs_to_obsidian.py）
status: resolved
tags: [自動化, Claude API, Obsidian, ログ処理]
related: ["Knowledge/claude-code-hook-system", "Knowledge/task-scheduler-path-fix"]
---

## summary
Claude会話ログを自動収集→Claude API（Haiku）で分類→Obsidianへ書き込みするPythonパイプライン。PC起動30秒後（Google Driveマウント完了待ち）にタスクスケジューラで自動実行される。

## file_structure
```
claud.セッション/
├── process_logs_to_obsidian.py  ← メイン処理スクリプト
├── config.env                    ← APIキー設定ファイル（⚠取り扱い注意、下記参照）
├── run_process_logs.bat          ← Windows実行バッチ
├── register_task.ps1             ← タスクスケジューラ登録スクリプト
├── processed_logs.json           ← 処理済みファイル管理
└── save_all_sessions.py          ← 既存ログ保存スクリプト
```

## process_flow
1. PC起動時トリガー（タスクスケジューラ）
2. 30秒待機（Google Driveマウント完了待ち）
3. `save_all_sessions.py` で新規会話ログ取得
4. `processed_logs.json` で未処理ファイルを判定
5. 各ログをClaude API（claude-haiku-4-5、コスト最小化）に送信し、タスク・知見・決定に自動分類
6. `Daily/YYYY-MM-DD.md` に追記、`Knowledge/`・`Decision/` に重要項目を新規ファイル生成
7. 処理済みフラグを更新

## execution
**手動実行:**
```
cd "G:\マイドライブ\1.実験データ_gdrive\claud.セッション"
python process_logs_to_obsidian.py
```

**自動実行登録（PowerShell管理者）:**
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass; & "G:\マイドライブ\1.実験データ_gdrive\claud.セッション\register_task.ps1"
```

## api_cost
- モデル: claude-haiku-4-5
- 1ログファイル = 1 API呼び出し、目安 $0.0001〜$0.001/回

## security_note
⚠ config.envにANTHROPIC_API_KEYを平文保存する構成。元のノートにキーの先頭部分（`sk-ant-api03-...`）が平文記載されていたため本統合時に削除した。config.envの実ファイルにはキー全体が残っているはずなので、他者と共有・公開しないよう注意。心配な場合はAnthropic Console上でキーのローテーション（再発行）を検討。

## limitations
- Claude.ai Web/アプリのチャットログは自動キャプチャ対象外。セッション形式（Claude Code）のログのみ処理対象
