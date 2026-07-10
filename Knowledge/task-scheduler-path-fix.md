---
date: 2026-06-21
theme: タスクスケジューラのパス誤り修正（Claude会話自動保存）
status: open（修正後もスクリプト実行エラーが発生中・原因究明必要）
tags: [Windows, タスクスケジューラ, Claude, 自動保存]
related: ["Knowledge/Claude会話自動保存-設定手順"]
---

## summary
Claude会話自動保存用のタスクスケジューラが誤ったパスを参照しており自動実行に失敗していた。正しいパスへ修正。修正コマンド実行は完了したが、スクリプト実行時エラーが別途発生中で原因究明が必要。

## path_correction
| タスク名 | 誤パス | 正パス |
|---|---|---|
| Claude会話自動保存 | `G:\マイドライブ\1.実験データ_gdrive\claud.セッション\save_all_sessions.py` | `G:\マイドライブ\Claude\セッション\save_all_sessions.py` |
| ProcessLogsToObsidian | 同上ディレクトリ内 `run_process_logs.bat` | `G:\マイドライブ\Claude\セッション\run_process_logs.bat` |

## fix_command
PowerShellを管理者として実行:
```powershell
$correctPath = "G:\マイドライブ\Claude\セッション"

$action1 = New-ScheduledTaskAction -Execute "python" -Argument "`"$correctPath\save_all_sessions.py`"" -WorkingDirectory $correctPath
Set-ScheduledTask -TaskName "Claude会話自動保存" -Action $action1

$action2 = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c `"$correctPath\run_process_logs.bat`"" -WorkingDirectory $correctPath
Set-ScheduledTask -TaskName "ProcessLogsToObsidian" -Action $action2
```

## verification
`Set-ScheduledTask` 後、タスクスケジューラから手動実行でテスト。エラー発生時はスクリプトを直接実行して詳細確認。

## status_note
2026-06-21時点：パス修正コマンド自体は実行完了したが、スクリプト実行時エラーが別途発生中。
