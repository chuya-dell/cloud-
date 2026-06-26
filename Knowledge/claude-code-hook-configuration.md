## Claude Codeのhook機能による会話自動保存

### 概要
Claude Code（デスクトップアプリ）には「hook」という機能があり、会話終了などのイベント時にシェルコマンドを自動実行できる。これを利用して、セッション終了時に会話ログをObsidianに自動保存する仕組みが実装できる。

### Claude Codeとclaude.ai Webの違い
- **Claude Code**（黒いターミナル風UI）
  - `claude` コマンドで起動するデスクトップアプリ
  - hook機能があり、イベント時に自動でコマンド実行可能
  - 会話終了時の自動保存に対応

- **claude.ai Web/アプリ**
  - ブラウザまたはネイティブアプリ
  - hook機能なし
  - MCPに対応しているため、会話内コマンド「保存して」で手動トリガー可能

### Hook設定対象
- 設定ファイル：`~/.claude/settings.json` または `.claude/settings.json`
- Hook事象：主に `Stop`（セッション終了時）を使用
- 実行内容：Pythonスクリプトにより会話ログをJSON形式で取得・加工・Googleドライブに保存

### 保存先
- Google Drive：`G:\マイドライブ\AI会話ログ\`
- ファイル形式：Markdownファイル（`YYYY-MM-DD_HH-MM-SS.md` 形式）

### 参考
- 日付: 2026-06-20
