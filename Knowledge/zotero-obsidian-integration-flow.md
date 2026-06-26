## Zotero → Obsidian → AI の単方向データフロー設計

### 概要
"AIに依存しない個人知識ベース" を実現するため、Zotero の文献データを Obsidian を経由して AI に提供するアーキテクチャ。Zotero のローカルデータベース（SQLite）を外部 AI が直接参照するセキュリティ・技術的ハードルを回避し、**Markdown テキスト化** を経由することで、すべての AI（Claude、Gemini、NotebookLM）からシームレスにアクセス可能にする。

### データフロー

```
Zotero
  ↓（Zotero Integration プラグイン）
Obsidian Vault（Markdown ノート）
  ↓（Google Drive 同期）
Google Drive
  ↓（MCP / NotebookLM / 手動添付）
Claude / Gemini / NotebookLM
```

### 実装手順

#### 1. Obsidian プラグインのインストール
- **プラグイン名**：`Zotero Integration`
- 入手先
