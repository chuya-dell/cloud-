---
name: reference-notion
description: NotionページID・DB・Obsidianとの役割分担
metadata: 
  node_type: memory
  type: reference
  originSessionId: f935b4f9-197f-46d4-aee1-90e4e4e311b8
---

## ページ・DB ID

| 項目 | ID |
|------|-----|
| 🧠 Claudeの記憶（メインページ） | 386e390406d18132a123e7b658b44b4b |
| 👤 プロフィール・ルール | 386e390406d181d7826bf469a57fdb6f |
| 📝 Claude会話ログ | 386e390406d181a298eef4243ce1e267 |
| 📅 Dailyログ | 386e390406d181219725f5219c9e4001 |
| 📌 Decision | 386e390406d181329967c9ff5b1de844 |
| タスク管理DB | c50f65b3-a948-4096-b35f-8ca3dc07e83a |
| ラボノートDB（廃止済み） | d0a10e9c-053b-4866-bc2c-fa832a31bd38（＝c38fbca3fc864b38b2a46e004d06069f）— 現存しない。実験記録はObsidianの「ラボノート/」フォルダのみ |
| 論文DB | 62a3ee51-c5f5-4c24-9249-2abc2c98c739（373件） |

## Notion／Obsidian 役割分担

| カテゴリ | Obsidian（一次保管） | Notion（同期） |
|---------|---------------------|---------------|
| 作業ログ | Daily/YYYY-MM-DD.md | 同期しない |
| 知識・解決法 | Knowledge/ | 同期しない |
| 決定事項 | Decision/ | 同期しない |
| タスク | タスク.md（ルート直下） | 📋 タスク管理DB（適宜） |
| ラボノート | ラボノート/（テーマ別ノート、note_format_policy.mdの形式） | 同期しない（DB廃止済み） |
| ミス記録 | Mistakes/ミス記録.md | 同期しない |

**Why:** NotionはClaudeが読むと10,000〜15,000トークン消費。ObsidianはファイルごとなのでOK数百〜2,000トークン。

## 運用ルール

- NotionはタスクのみUI。Obsidianが一次保管・Claude Codeとの作業拠点
- 「記録して」→ Claude会話ログに追記＋タスク成分があればタスクDBにも登録
- Dailyログは新規エントリを先頭挿入で運用
- 実験の話をした時はラボノート/の該当テーマノートに追記（なければ新規作成）。フォーマットはnote_format_policy.mdに従う（YAML frontmatter、params/result/open_questions等の固定キーで構造化、人間可読性よりClaudeの検索・抽出しやすさを優先）
- Claudeは常にObsidianから読み、必要なものだけNotionに反映。Notionの大きなページは要約用途以外で読まない
- （2026年7月更新）新規ノートのフォーマットはカテゴリを問わずDaily/Knowledge/Decision/Mistakes等すべてnote_format_policy.mdの方針に従う（YAML frontmatterでdate/tags/related等を付与し、本文は固定キーで構造化。人間可読性よりClaudeの検索・抽出しやすさを優先）。既存ノートは無理に一括リライトしない。論文原稿など「そのまま転用するプローズ本体」は例外としfrontmatterのみ付与し本文は構造化しない

## チャット記録の書き込み先（重要）

- （2026年7月更新）obsidian-vault MCPはPCブラウザ/claude.aiウェブチャットでも直接利用可能なことを確認済み。利用可能な環境ではまずobsidian-vault MCP（直接ファイル編集）を試す。使えなければGoogle Drive MCP経由のcreate_file（上書き不可・重複作成になる点に注意）。
- iOSはobsidian-vault MCPが使えない可能性があり、その場合のみGoogle Drive MCP直接書き込み→それも不可ならNotionフォールバック（Claude会話ログに追記→後日Claude CodeがObsidianに転記）
- Notionは「上記いずれも使えない場合の最終代替」として位置づけ

## 移行ルール（重要）

- **ObsidianにデータをコピーしたNotionページは削除（アーカイブ）する**
- アーカイブ方法: `notion-update-page` で `{"archived": "__YES__"}` を設定
- Notionにデータを二重管理しない。Obsidianを唯一の一次保管とする
