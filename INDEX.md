# Vault インデックス（セッション開始時にまずこれを読む）

## ユーザー
- 名前: 忠さん（hmC関連の研究者）
- 環境: Windows 11、Python 3.13、Google Drive 5TB、Google AI Pro

## 最近の作業
- 最新Dailyログ: `Daily/2026-06-22.md`
- 2026-06-22: 研究室PC環境セットアップ完了

## 重要フォルダ
- `Daily/` - 日々の作業ログ
- `Decision/` - 重要な判断・方針
- `Knowledge/` - 知識・解決法（別PCセットアップ手順など）
- `Mistakes/` - ミス記録（必ず確認）
- `Zotero/` - 論文386件（hmC関連多数）
- `Logs/` - 環境構築ログ

## 完成している環境
- Claude Code → Obsidian Vault（MCP/server-filesystem）✅
- claude.ai（ブラウザ）→ Obsidian Vault（ngrok+カスタムMCPサーバー）✅
- Gemini → Google Drive参照✅
- Zotero → Vault md化済み✅
- iPhone → Geminiで論文参照✅
- 会話自動保存 → 毎日12時タスクスケジューラ✅
- **研究室PC → Obsidian Vault MCP接続✅（2026-06-22）**

## 残タスク
- gemini.google.comのDrive直接検索（インデックス待ち）
- ProcessLogsToObsidianタスクスケジューラ（管理者権限で手動登録が必要）
- Mac環境構築
- NotebookLM連携

## 環境設定メモ（研究室PC）
- Obsidian Vault実体: `F:\GoogleDrive_local\Obsidian Vault\`
- AI会話ログ: `F:\GoogleDrive_local\AI会話ログ\`
- 作業スクリプト: `F:\GoogleDrive_local\Claude\セッション\`
- Python: `C:\Users\chuya\AppData\Local\Programs\Python\Python311\python.exe`
- Node.js: `C:\Program Files\nodejs\node.exe`

---

## AIへの記録ルール

### ObsidianとNotionの使い分け
- **Obsidian** → すべての記録（作業ログ・知識・調査メモ・AI外部記憶）
- **Notion** → 忠さんが知る必要があること・行動が必要なもの（タスク・リマインダー・期限あり）

### Obsidian 書き込みルール

| 内容 | 保存先 |
|---|---|
| 作業ログ・今日の記録 | Daily/YYYY-MM-DD.md に追記 |
| 知識・調査メモ・解決法 | Knowledge/ に新規ファイル |
| 重要な決定・方針 | Decision/ に新規ファイル |
| AIのミス・指摘 | Mistakes/ミス記録.md に追記 |
| 論文関連 | Zotero/ 参照 |

### Notion 書き込みルール
以下の場合のみNotionに記録する：
- 忠さんが後で確認・対応する必要があるタスク
- 期限のあること
- 忠さんへのリマインダー

### 基本方針
- 作業完了時・節目に自動でObsidianに書き込む
- 書き込んだらどこに何を書いたか報告する
- このINDEX.mdの「最近の作業」も随時更新する
