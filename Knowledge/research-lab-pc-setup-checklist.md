## 研究室PC環境構築チェックリスト

### 概要
明日（6/22）の研究室PCで、現在のWindows PCと同様の環境を構築するための準備リスト。Macは優先度低め。

### 優先順位順チェックリスト

1. **Claude Code インストール**
   - 方法: `npm install -g @anthropic-ai/claude-code` または公式インストーラー
   - 用途: ログ処理・環境構築スクリプト実行

2. **Google Drive for Desktop インストール**
   - 用途: `G:\マイドライブ` マウント
   - データ: セッションログ、Notionエクスポート、研究データ保存

3. **Node.js インストール**
   - 用途: MCP (Model Context Protocol) サーバー実行
   - バージョン: LTS推奨

4. **obsidian-vault MCP設定**
   - ファイル: `claude_desktop_config.json`
   - 内容: Obsidian Vault へのアクセス設定を追記
   - 参照: `Knowledge/Claude会話自動保存-設定手順.md`

5. **タスクスケジューラ登録**
   - スクリプト: `register_task.ps1` を研究室PC用に修正して実行
   - タスク:
     - Claude会話自動保存（日次実行）
     - ProcessLogsToObsidian（ログ処理）

6. **config.env のコピー**
   - 内容: Anthropic APIキー
   - 場所: `G:\マイドライブ\Claude\セッション\`

### 参考
- 日付: 2026-06-21
- 現在のPC設定: Windows 11、Python環境、Obsidian Vault接続済み
- Mac環境: 後日対応（優先度低）
