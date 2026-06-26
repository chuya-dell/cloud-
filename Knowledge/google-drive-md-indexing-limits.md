## Google Drive のMarkdown ファイルインデックス登録の技術的制限

### 概要
Google Drive の全文検索システムと Gemini の連携は、Google Docs・PDF・画像に対して高度に最適化されているが、.md（Markdown）ファイルは検索インデックス対象から漏れやすく、Gemini による内容抽出が失敗することが多い。

### 3つの技術的原因

#### 1. MIMEタイプの判定の曖昧さ
- Google Docs: `application/vnd.google-apps.document`（明確）
- PDF: `application/pdf`（明確）
- Markdown: `text/markdown`, `text/plain`, `application/octet-stream` など環境により異なる
- 結果：インデックス処理の対象から漏れたり、テキストパースが失敗しやすい

#### 2. プレーンテキストの検索優先度が低い
- Google Drive の内部検索は公式サポート対象（Googleドキュメント、Office系、PDF、画像OCR）を最優先
- .md のような開発者向けプレーンテキストは、ファイル名はヒットしても、**ファイル内テキストの全文インデックスが不安定**

#### 3. RAG（検索拡張生成）におけるデータ抽出の失敗
- Gemini がファイル参照時、バックエンド側でテキスト抽出を試みるが、非標準形式は "空のファイル" または "サポート外形式" として弾かれやすい
- パース失敗時、Gemini までテキストが届かない

### 回避策

#### 確実な運用方法A：拡張子を .txt に変更
- 中身はMarkdown記述（# や - など）のまま維持
- 拡張子だけ .md → .txt に変更
- Google Drive が "100% プレーンテキスト" と認識し、全文インデックスに確実に掲載される
- **制限**：Obsidian は .md 以外では動かないため、Vault 内では使用不可

#### 確実な運用方法B：Googleドキュメント変換またはチャット直貼り
- 重要なノートを Googleドキュメント形式で保存し直す
- または Obsidian からテキストをコピーして Gemini チャットに直接ペースト

#### 推奨：NotebookLM 経由での参照
- Google Drive 内のフォルダを NotebookLM の「ソース」として直接指定
- MIMEタイプやインデックス問題を回避し、**ソースとしての直接読み込み** で対応
- ファイル形式に依存しない安定性

### 参考
- 日付: 2026-06-20
- 関連：Obsidian Vault × Google Drive 同期、NotebookLM 連携
