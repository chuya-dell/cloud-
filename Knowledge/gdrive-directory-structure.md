## Google Drive マイドライブのClaude関連フォルダ構成

### 概要
マイドライブ内のClaude関連フォルダを統一・整理した構成

### 実装済み構成
```
G:\マイドライブ\n├── Claude/                    （新規統合フォルダ）
│   ├── セッション/             （旧: claud.セッション）
│   └── AI会話ログ/             （旧: AI会話ログ）
├── 1.実験データ_gdrive/        （そのまま）
└── antigravity_chat_logs/     （別管理）
```

### 移動したファイル・フォルダ
1. `1.実験データ_gdrive\claud.セッション` → `Claude\セッション`
2. `AI会話ログ` → `Claude\AI会話ログ`

### 保持したフォルダ
- `antigravity_chat_logs` （Claude統合外で独立管理）

### プロジェクト設定の更新
- Claude Code プロジェクト設定ファイルのパスを新ディレクトリに更新
- Memory（会話記憶）も新パスに移行済み
- セッションデータは `C:\Users\chuya\.claude\projects\` から新パスに移動

### 参考
- 日付: 2026-06-20
