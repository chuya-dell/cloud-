## Claudeセッション・ファイル構成の一元化決定

**決定日**: 2026-06-20

**理由**: マイドライブ内に分散していたClaude関連フォルダ（claud.セッション、AI会話ログ、antigravity_chat_logs）を整理し、一元管理して作業効率を向上させるため

**内容**: 
- マイドライブ直下に `Claude/` フォルダを新規作成
- `1.実験データ_gdrive\claud.セッション` → `Claude/セッション/` に移動
- `AI会話ログ` → `Claude/AI会話ログ/` に移動
- `antigravity_chat_logs` は独立のまま（別プロジェクト扱い）

**影響範囲**: 
- Claude Code のプロジェクト設定ファイル（`C:\Users\chuya\.claude\projects\`）の更新が必須
- パス参照を含むすべてのスクリプト・設定を新しいディレクトリ構成に対応させる必要あり
