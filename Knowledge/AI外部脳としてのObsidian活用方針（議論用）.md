---
date: 2026-06-27
theme: AI外部脳としてのObsidian活用方針（議論用、YouTube19本サーベイ）
status: reference
tags: [Obsidian, AI外部脳, 運用方針]
notion_url: https://app.notion.com/p/38ce390406d181f098caf736d4ebbeb0
---

# AI外部脳としてのObsidian活用方針（議論用）

> Notion: https://app.notion.com/p/38ce390406d181f098caf736d4ebbeb0  
> 日付: 2026-06-27

YouTube動画A〜S（計19本）のトランスクリプトを収集・整理し、Obsidianの外部脳活用方針をまとめた。

---

## 忠さんの2つの痛みへの結論

**痛み1：トークン消費が心配**  
→ `pip install notebooklm-mcp-cli && nlm login` の2コマンドでNotebookLMにリサーチをアウトソース。ClaudeのトークンはDiscussion・アウトプット生成に集中。

**痛み2：claude.aiからObsidianが見えない**  
→ Claude Codeセッションが根本解決。claude.aiはフロントエンド（外出先）と割り切る。

**二重管理問題**  
→ 静的情報→Obsidian、動的情報→Notionと役割を明文化。

---

## 19本の収束した原則（3本以上が独立して同意）

- AI生成物と自分の思考を物理的に分離せよ（C/K/P）
- 動的情報と静的情報を分離せよ（C/D/L/Q/R）
- ルールは物理的に強制せよ（E/L）
- 考える時間を人間に残せ（C/L/P）
- ObsidianとNotionは役割分担（H/Q/R）

---

## TODO（次回）
- [ ] NotebookLM連携実装（`pip install notebooklm-mcp-cli && nlm login`）
- [ ] 静的/動的情報の役割分担をCLAUDE.mdに明文化するか決める
- [ ] AI生成物フォルダをIdeaverseから分離するか決める
