---
date: 2026-06-20
theme: Obsidian Vault内Zoteroフォルダの参照方法と制限
status: reference
tags: [Zotero, Obsidian, 検索, トークン管理]
related: ["Knowledge/zotero-to-obsidian-flow"]
---

## summary
Obsidian VaultのZoteroフォルダに386件の論文ノート（.md）が格納されており、Claude/MCP経由で参照可能。全件読み込みはトークンコストが大きいため、キーワード検索での絞り込みが必須。

## access_methods
- 検索: `search_files` で特定キーワードを含む論文ノートを探索
- 直接読込: `mcp__obsidian-vault__read_file` で個別ノートの内容を確認
- ユーザーの質問に応じて必要な1-2件のみ都度検索・参照する運用

## limitations
- 全件自動読み込みは非推奨（386件×トークンコスト＝過大）
- ノートの充実度（Abstractのみ／notes・highlights付き）でファイルごとに情報量が変動
- Zotero側のユーザーメモ・ハイライトはObsidianノートに含まれない

## content_examples
- 5hmC（5-Hydroxymethylcytosine）関連: がん研究文脈で多数（メインテーマ）
- プラズモン関連: 21件（例: `Plasmonics Fundamentals and Applications.md`, `Plasmonic Biosensors for Single-Molecule Biomedical.md`, `High Q-Factor Plasmonic Surface Lattice Resonances.md` 等）
