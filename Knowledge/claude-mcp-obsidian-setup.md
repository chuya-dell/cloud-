## Claude MCP + Obsidian Vault統合設定

### 概要
Claude APIを通じてObsidian VaultをGoogle Drive上で直接読み書きする環境構築

### 詳細

**アーキテクチャ**
- MCP: server-filesystem（Vault直接読み書き）
- ストレージ: Google Drive (`G:\マイドライブ\Obsidian Vault\`)
- 自動化: Windowsタスクスケジューラで定期実行

**フォルダ構成**
- Daily/: 日々の作業ログ
- Decision/: 決定事項
- Knowledge/: 技術的知識
- Mistakes/: 失敗事例
- Logs/: 環境構築ログ
- Zotero/: 論文ライブラリ（386件）
- INDEX.md: ナビゲーション
- CLAUDE.md: AI向けシステムプロンプト

**自動保存パイプライン**
1. `save_session.py`: 個別セッションのログ取得
2. `save_all_sessions.py`: 全セッション一括保存
3. `process_logs_to_obsidian.py`: Claude APIで自動構造化
4. Windowsタスクスケジューラ: ログオン時に自動実行

**出力先**
- AI会話ログ: `G:\マイドライブ\AI会話ログ\`
- Vault統合: `G:\マイドライブ\Obsidian Vault\`

### 参考
- 日付: 2026-06-21
