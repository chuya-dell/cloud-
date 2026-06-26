## Google DriveにおけるMarkdownファイルの検索インデックス問題

### 概要
Google Driveの全文検索システムは公式サポート形式（Google Docs、PDF、画像）を優先的にインデックス登録する仕様上、.mdファイルはインデックス登録が不安定になり、Geminiからの検索ヒット率が劇的に低下する。

### 技術的な3つの理由

#### 1. MIMEタイプの判定の曖昧さ
- Google Docs: `application/vnd.google-apps.document`
- PDF: `application/pdf`
- .md ファイル: `text/markdown` / `text/plain` / `application/octet-stream` など環境による

結果：.mdファイルがバイナリデータとして弾かれたり、テキストパース失敗が発生

#### 2. プレーンテキストの検索優先度
公式サポート形式がインデックス作成を最優先される一方、開発者向けのプレーンテキスト形式は：
- ファイル名のみヒット、ファイル内全文検索が不安定
- リッチドキュメントより大幅に劣る精度

#### 3. RAG（検索拡張生成）におけるデータ抽出の壁
Geminiのバックエンドがファイルをテキスト抽出する際：
- 非標準形式は「空のファイル」or「非対応形式」として弾かれる
- パース（解析）失敗でテキストがGeminiに届かない

### 確実な対処策

#### 方法1: 拡張子を .txt に統一
- 中身はMarkdown記述のままで問題なし
- Google Drive側が「100%プレーンテキスト」と認識
- 全文インデックスに自動登録される
- **制限**: Obsidianは .md以外では正常動作しないため、Vault本体には不適用

#### 方法2: 別フォルダで .txt 運用
- Obsidian Vaultは .md のまま維持
- 同期用の参照フォルダだけ .txt に変換
- Obsidianプラグインで両形式を管理

#### 方法3: NotebookLM経由（推奨）
- Google DriveフォルダをNotebookLMの「ソース」として直接指定
- インデックス問題を回避してMarkdownを完全にパース
- ファイルサイズ制限あり（100ファイル程度、数十万語規模が目安）

#### 方法4: Geminiには手動コピペ or PDF保存
- ObsidianのテキストをコピーしてGeminiチャットに直接ペースト
- or Claudeのセッション全体をPDF保存してGoogle Driveに配置
- Geminiは @Drive で PDF参照が極めて得意

### 実装推奨フロー

| ツール | 用途 | アクセス方法 |
|--------|------|-------------|
| Claude | 日常的なVault読み書き・自動化 | MCP（直接接続） |
| NotebookLM | 複数ノート・論文の深い議論 | Google Drive ソース登録 |
| Gemini | その場限りの参照 | 手動コピペ or PDF @Drive |

### 参考
- 日付: 2026-06-20
- 関連: Claude会話ログ5ffb6195-a989-4557-a90a-c241a7c814ce
