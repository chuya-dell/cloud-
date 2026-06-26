## Claude会話ログのObsidian自動整理システム

### 概要
Claude AIの会話ログを自動でObsidianに構造化して保存するシステム。PC起動時に自動実行され、新しい会話ログを検出して日次サマリーと知識・決定事項ファイルを生成する。

### システム構成

```
claud.セッション/
├── process_logs_to_obsidian.py  ← メイン処理スクリプト
├── config.env                    ← APIキー設定ファイル
├── run_process_logs.bat          ← 実行バッチ
├── register_task.ps1             ← タスクスケジューラ登録用
├── processed_logs.json           ← 処理済み管理（初回実行時に自動生成）
└── save_all_sessions.py          ← 既存の会話ログ収集スクリプト
```

### 処理フロー

1. **ログ収集**: save_all_sessions.pyがClaude会話ログをAI会話ログ/に保存
2. **未処理検出**: processed_logs.jsonから未処理ファイルを特定
3. **構造化**: Anthropic API（claude-haiku-4-5）で会話ログを分析
   - タスク・実験メモ・考察・アイデア・重要な決定に分類
4. **ファイル生成**:
   - Daily/YYYY-MM-DD.mdに日次サマリーを追記
   - Knowledge/に技術情報を保存
   - Decision/に重要な決定事項を保存
5. **マーク**: 処理済みとしてprocessed_logs.jsonに記録

### APIキー設定

config.envに記述:
```
ANTHROPIC_API_KEY=sk-ant-...
```

### 実行方法

**手動実行**:
```bash
cd "G:\マイドライブ\1.実験データ_gdrive\claud.セッション"
python process_logs_to_obsidian.py
```

**自動実行設定** (PowerShell 管理者権限):
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass; & "G:\マイドライブ\1.実験データ_gdrive\claud.セッション\register_task.ps1"
```

登録後はPC起動30秒後に自動実行（Google Driveマウント待ち）。

### コスト

- **モデル**: claude-haiku-4-5（最小コスト）
- **処理コスト**: 1ファイルあたり約$0.0005〜$0.001
- **Anthropic APIプリペイド**: $5で数年分のヘビーユース対応
- **課金形態**: 都度課金（月額固定費なし、残高方式）

### 注意事項

- Google Gemini無料APIはAI Pro契約時に無効化される
- バッチファイルで日本語コマンド混在時は文字化けするため、PowerShellで実装
- APIキーは環境変数またはconfig.envから読み込み
- Obsidianのフォルダ構成: Daily/, Knowledge/, Decision/, Logs/, Mistakes/

### 参考
- 日付: 2026-06-20
