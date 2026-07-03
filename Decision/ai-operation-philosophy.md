# AI運用理念

作成日: 2026-06-21

## 基本方針：「AIに依存しない知識ベース」

データ主権と可搬性を最優先にする。AIツールが変わっても、知識はVaultに残る設計。

## データフロー（単方向）

```
Zotero → Obsidian（Markdown化）→ AI参照
```

AIにデータを預けない。VaultがマスターデータでAIは参照するだけ。

## 各AIの役割分担

| AI | 役割 |
|---|---|
| **Claude** | 日常作業・自動化・Vault読み書き・記録 |
| **NotebookLM** | 論文横断・深い議論（hmC×plasmon等） |
| **Gemini** | Google Driveファイル直接分析・手動添付参照 |
| **Perplexity** | リアルタイム情報・最新論文サーチ |
| **ChatGPT** | 補助（上記で対応できない場合のみ） |

## データ管理の役割分担

| システム | 役割 |
|---|---|
| **Obsidian** | マスターデータ・長期蓄積・AI外部記憶 |
| **Notion** | 運用UI・タスク管理・忠さんが見るもの |
| **Zotero** | 論文原本管理（386件） |
| **Google Drive** | ファイルストレージ・同期基盤（5TB） |

## 運用上の決定事項

- Obsidian → Notion の方向で同期（Notionはコピー）
- 「記録して」→ ObsidianとNotion両方に書き込む
- AI乗り換え時もVaultはそのまま使える
- トークン節約のため、セッションが長くなったら /clear → Obsidianから再開
