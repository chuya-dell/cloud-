---
date: 2026-06-21
theme: Zotero論文のObsidian Vault同期フロー（実装：カスタムスクリプト）
status: resolved
tags: [Zotero, Obsidian, 同期, 文献管理]
related: ["Knowledge/zotero-obsidian-sync-formats"]
---

## summary
"AIに依存しない個人知識ベース"を実現するため、Zoteroのローカルデータベース（SQLite）をAIに直接触らせず、Markdownテキスト化を経由してClaude/Gemini/NotebookLMからアクセス可能にする設計。実装はObsidianプラグイン（ZotLit等）ではなく、カスタムスクリプト `zotero_to_obsidian.py` による一括変換方式。2026-06-21時点で386件のmdファイル完全同期済み（hmC関連が主、plasmon関連21件）。

## architecture
```
Zotero（論文DB, SQLite）
  ↓ ライブラリエクスポート（Better CSL/BibTeX JSON）
zotero-library.json
  ↓ zotero_to_obsidian.py（論文のみ抽出・md化、note/attachment除外）
Obsidian Vault/Zotero/（386件のmdファイル）
  ↓ Google Drive同期
Claude（MCP直接）/ Gemini・NotebookLM（Drive経由）
```

## stats
- Zotero総件数: 406件（論文本体386件 + note・attachment等20件）
- Vault移行済み: 386件（論文のみ、note/attachmentはフィルタで除外）

## sync_procedure
1. Zoteroを開く → `ファイル` → `ライブラリをエクスポート`
2. 形式: **Better CSL JSON** または **Better BibTeX JSON**
3. 保存先: `G:\マイドライブ\Obsidian Vault\zotero-library.json\zotero-library.json`（上書き）
4. `zotero_to_obsidian.py` を実行 → 新規/更新分のmdファイルがVaultに反映される

## verification
Pythonで `json.load()` 後、フィルタ後の論文アイテム数をカウントし同期対象件数を確認。

## note
プラグイン方式（ZotLit等）の比較検討は `Knowledge/zotero-obsidian-sync-formats` を参照。本Vaultでの実装はプラグインではなくカスタムスクリプト方式。
