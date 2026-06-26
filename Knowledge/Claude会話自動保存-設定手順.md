# Claude会話自動保存の設定手順

## 概要
毎日12時（PC未起動の場合は次回起動時）にClaude Codeの全会話をGoogle Driveに自動保存する。

## ファイル
- 保存スクリプト: `G:\マイドライブ\1.実験データ_gdrive\claud.セッション\save_all_sessions.py`
- 保存先: `G:\マイドライブ\AI会話ログ\`

## 別PCでの設定手順
1. `save_all_sessions.py` をそのPCからアクセスできる場所に置く（Google Drive経由でOK）
2. PowerShellを管理者で開いて以下を実行：
```powershell
$action = New-ScheduledTaskAction -Execute "python" -Argument "`"G:\マイドライブ\1.実験データ_gdrive\claud.セッション\save_all_sessions.py`""
$trigger = New-ScheduledTaskTrigger -Daily -At "12:00"
$settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Minutes 2) -StartWhenAvailable
Register-ScheduledTask -TaskName "Claude会話自動保存" -Action $action -Trigger $trigger -Settings $settings -Force
```
3. 完了

## 注意
- Pythonがインストールされている必要がある
- Google DriveのパスがGドライブにマウントされている必要がある
