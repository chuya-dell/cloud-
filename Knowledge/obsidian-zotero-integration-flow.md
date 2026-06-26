## Obsidian-Zotero統合: AIに依存しない文献管理フロー

### 概要
Zoteroのデータベース（SQLite）を直接AIに読み込ませるのではなく、Zotero → Obsidian(Markdown化) → AI参照というデータフローを構築。Obsidian VaultがGoogle Driveに同期されているため、自動的にClaudeとNotebookLMが文献情報にアクセス可能になる。

### アーキテクチャ

```
Zotero (論文DB)
  ↓ [Zotero Integration プラグイン
