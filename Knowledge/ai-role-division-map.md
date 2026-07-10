---
date: 2026-06-21
theme: 各AIツール（Claude/Gemini/NotebookLM/ChatGPT）の役割分担マップ
status: reference
tags: [AI運用, Claude, Gemini, NotebookLM, ChatGPT]
---

## 各AIツールの役割分担マップ

### Claude（メインツール）
**用途**: Vaultの読み書き・記録・管理・自動化・日常補助
- Obsidian Vault直接読み書き（MCP経由）
- スクリプト作成・実行
- Daily / Decision / Knowledge / Mistakes への自動記録
- Googleカレンダー・Gmail・Notion操作

### Gemini
**用途**: Google Drive内ファイルの直接参照・データ分析
- PDF・Googleドキュメントをそのまま渡して質問
- 実験データのスプレッドシートを直接分析
- iPhoneからの論文添付質問
- 長文コンテキスト（1.5M tokens）を活用した大量データ処理

### NotebookLM（最優先セットアップ対象）
**用途**: 複数論文の横断検索・議論・比較
- hmC関連論文386件をソース登録
- 「この仮説を支持する論文は？」「矛盾する研究は？」への回答
- ソース引用付き回答で信頼性確保
- 研究の深掘りに特化

### ChatGPT / GPT-4o
**用途**: 画像生成・ブラウジング・別視点レビュー
- 画像生成（DALL-E）
- Webブラウジングで最新情報収
