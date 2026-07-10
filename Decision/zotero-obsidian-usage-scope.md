---
date: 2026-06-20
theme: Zotero論文ライブラリの参照範囲決定（Abstract＋書誌情報のみ）
status: resolved
tags: [Zotero, Obsidian, 参照範囲]
related: ["Knowledge/obsidian-vault-zotero-folder-structure", "Knowledge/zotero-obsidian-sync-formats"]
---

## decision
Zotero論文（386件）の参照は、Abstractと書誌情報（著者・年・雑誌・DOI）に限定する。ユーザーの読書メモ・ハイライト・本文PDFは参照しない。

## reason
- 現行のZotLit/カスタムスクリプト同期ではメモ・ハイライトが反映されていない
- 本文PDF参照はObsidianを通じては不可能
- 386件の全件読込はトークンコストが大きく非効率

## implementation
- ユーザーが「〇〇について調べて」と指示した際にキーワード検索で関連論文を抽出（全件自動読み込みはしない）
- 5hmC系・プラズモン系いずれのテーマも対象。必要に応じて複数論文のAbstractを並列参照して比較検討
- 詳細な内容確認・読書メモが必要な場合はZotero本体またはPDFリーダーを参照するようユーザーに促す
- Zoteroへの新規論文追加は自動的にObsidianへ反映される（同期フロー: `Knowledge/zotero-to-obsidian-flow`）

## impact
- 会話内での論文参照効率（素早い一覧化・Abstractによる概要把握）とトークン使用量の最適化を両立
- AI側の研究補助はあくまで補助的範囲（根拠付け・最新知見の確認）にとどまる
