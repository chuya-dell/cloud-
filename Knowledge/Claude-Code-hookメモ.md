# Claude Code hookメモ

## Stopフックの挙動
- アプリを×で閉じてもStopフックが発火しない場合がある
- SessionEndも同様に不安定
- 手動保存は動作確認済み：
  `echo '{"session_id":"..."}' | python save_session.py`

## 現在の設定
- 設定ファイル: `C:\Users\chuya\.claude\settings.json`
- 保存スクリプト: `G:\マイドライブ\1.実験データ_gdrive\claud.セッション\save_session.py`
- 保存先: `G:\マイドライブ\AI会話ログ\`

## 未解決
- ログオフ時の自動保存（Windowsタスクスケジューラで設定予定）
