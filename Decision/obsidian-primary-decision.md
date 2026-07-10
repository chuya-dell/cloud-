---
date: 2026-06-28
theme: Obsidianをマスターデータとして運用（2026-06-28時点の決定）
status: superseded（2026-06-30のINDEX.md統合でNotion=正データの方針に再度変更。運用方針は何度か往復しているため、現行の正は必ずINDEX.mdを確認すること）
tags: [Notion, Obsidian, 運用設計]
related: ["Decision/notion-obsidian-role-final"]
---

# Obsidianをマスターデータとして運用（2026-06-28）

**決定**: Obsidianを主軸、Notionはミラー・運用UIに戻す

**理由**: Notionのトークン消費がObsidianより大幅に多い（まとめページ1つで10,000〜15,000トークン vs Obsidian数百〜2,000トークン）。Claude Codeとの相性はObsidianが圧倒的に有利。

**役割分担**:
- **Obsidian** = マスターデータ・Claudeの外部記憶（全記録の一次保管）
- **Notion** = 忠さんが見るUI（タスク・リマインダー・期限あり情報）

**2026-06-26の「Notionをメイン」決定を撤回**
