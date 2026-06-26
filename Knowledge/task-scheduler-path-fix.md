## タスクスケジューラのパス修正

### 概要
Claudeセッション自動保存のタスクスケジューラが誤ったパスを参照していため、自動実行に失敗していた。正しいパスに修正する手順。

### 詳細
**問題点**:
- 設定パス（誤）: `G:\マイドライブ\1.実験データ_gdrive\claud.セッション\`
- 実際のパス（正）: `G:\マイドライブ\Claude\セッション\`

**修正方法**（PowerShell管理者実行）:
```powershell
$correctPath = "G:\マイドライブ\Claude\セッション"

# タスク1: Claude会話自動保存
$action1 = New-ScheduledTaskAction -Execute "python" -Argument "`"$correctPath\save_all_sessions.py`"" -WorkingDirectory $correctPath
Set-ScheduledTask -TaskName "Claude会話自動保存" -Action $action1

# タスク2: ProcessLogsToObsidian
$action2 = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c `"$correctPath\run_process_logs.bat`"" -WorkingDirectory $correctPath
Set-ScheduledTask -TaskName "ProcessLogsToObsidian" -Action $action2
```

**テスト実行**:
- `Set-ScheduledTask` 後、タスクスケジューラから手動実行でテスト
- エラー発生時はスクリプトを直接実行して詳細を確認

### 参考
- 日付: 2026-06-21
- 関連: `Knowledge/Claude会話自動保存-設定手順.md`
