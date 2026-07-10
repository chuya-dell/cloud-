---
date: 2026-06-20
theme: Zotero-Obsidian連携プラグインの比較（検討時の調査メモ）
status: reference（本Vaultでの実際の実装はプラグインでなくカスタムスクリプト）
tags: [Zotero, Obsidian, プラグイン比較, 文献管理]
related: ["Knowledge/zotero-to-obsidian-flow"]
---

## summary
Zotero-Obsidian連携の検討時に比較したプラグイン方式のメモ。最終的に本Vaultではこれらのプラグインではなく、カスタムスクリプト `zotero_to_obsidian.py` による一括変換方式を採用した（詳細は `Knowledge/zotero-to-obsidian-flow` 参照）。

## plugin_comparison
| プラグイン | 同期方式 | 同期タイミング | 同期内容 |
|---|---|---|---|
| ZotLit | 自動 | Zoteroに論文追加時に自動でObsidianノート生成 | 著者・発行年・雑誌名・DOI・タイトル・Abstract |
| BetterBibTeX + Templater | 手動/トリガー | 手動または条件付き | テンプレートでカスタマイズ可能 |
| Mdnotes | エクスポート式 | 手動 | カスタマイズ可能、手動エクスポート作業必要 |

## sync_scope_general
- 同期される情報: 著者、発行年、雑誌名、DOI、タイトル、Abstract、タグ
- 同期されない情報: ユーザーの読書メモ・コメント、PDFハイライト・アノテーション（Zotero側の設定次第）

## limitations
- 自動同期でも本文PDFは参照不可（Abstractのみ）
- ファイルフォーマット（書誌情報レイアウト等）から使用プラグインを逆算可能
- 386件の論文ノートを全件読むとトークンコストが大きいため、検索機能での絞り込みが必須
