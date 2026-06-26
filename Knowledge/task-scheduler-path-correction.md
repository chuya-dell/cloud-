## タスクスケジューラパス修正手順

### 問題
タスクスケジューラの参照パスが誤っている状態でログが保存されていない。

### 詳細
| タスク名 | 設定パス（誤） | 実際のパス（正） |
|---|---|---|
| Claude会話自動保存 | `G:\マイドライブ\1.実験データ_gdrive\claud.セッション\save_all_sessions.py` | `G:\マイドライブ\Claude\セッション\save_all_sessions.py` |
| ProcessLogsToObsidian | 同上 | `G:\マイドライブ\Claude\セッション\run_process_logs.bat` |

### 修正コマンド
PowerShellを管理者として実行：

```powershell
$correctPath = "G:\マイドライブ\Claude\セッション"

$action1 = New-ScheduledTaskAction -Execute "python" -Argument "`"$correctPath\save_all_sessions.py`"" -WorkingDirectory $correctPath
Set-ScheduledTask -TaskName "Claude会話自動保存" -Action $action1

$action2 = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c `"$correctPath\run_process_logs.bat`"" -WorkingDirectory $correctPath
Set-ScheduledTask -TaskName "ProcessLogsToObsidian" -Action $action2
```

### ステータス
実行完了したが、スクリプト実行時エラーが発生中。原因究明が必要。

### 参考
- 日付: 2026-06-21
