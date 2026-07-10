---
date: 2026-06-28
theme: NotionとObsidianの役割分担（2026-06-28時点の決定、Obsidian主軸案）
status: superseded（2026-06-30のINDEX.md統合でNotion=正データ・Obsidian=長期保管の倉庫という現行方針に再度変更）
tags: [Notion, Obsidian, 運用設計]
related: ["Knowledge/notion-obsidian-role-design", "Decision/obsidian-primary-decision"]
---

# NotionとObsidianの役割分担（最終決定 2026-06-28）

## 原則
- **Obsidian** = 保存する場所（マスターデータ・Claudeの外部記憶）
- **Notion** = 目に見える形にする場所（ユーザーが操作・閲覧するUI）

## 全カテゴリの適用

| カテゴリ | 保存（Obsidian） | 表示・操作（Notion） |
|---|---|---|
| Daily作業ログ | Daily/YYYY-MM-DD.md | 📅 Daily ログ |
| 知識・解決法 | Knowledge/ | 💡 Knowledge |
| 決定事項 | Decision/ | 📌 Decision |
| タスク管理 | Projects/ or Daily/ | 📋 タスク管理DB |
| ラボノート | Daily/ or Projects/ | 🗒️ ラボノートDB |
| ミス記録 | Mistakes/ミス記録.md | ⚠️ Mistakes |

## 運用フロー
1. 何かを記録する → まずObsidianに書く
2. 忠さんが見る必要があるもの → Notionにも反映
3. Claudeが参照する → Obsidianから読む（トークン節約）
