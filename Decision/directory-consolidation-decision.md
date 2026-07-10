---
date: 2026-06-20
theme: Google Drive上のClaude関連ファイル一元管理決定
status: resolved
tags: [Google Drive, ディレクトリ構成, Claude]
related: ["Knowledge/google-drive-directory-structure", "Knowledge/claude-code-cli-setup"]
---

## decision
マイドライブ直下に `Claude/` 統合フォルダを新規作成し、散在していたClaude関連フォルダを一元管理する。

## reason
マイドライブ内でClaude関連ファイル（`claud.セッション`、`AI会話ログ`など）が散在しており、管理効率・アクセス効率が悪かったため。

## before_after
```
変更前:
G:\マイドライブ
├── 1.実験データ_gdrive
│   └── claud.セッション
├── AI会話ログ
└── antigravity_chat_logs

変更後:
G:\マイドライブ
├── Claude/
│   ├── セッション/（旧 claud.セッション）
│   └── AI会話ログ/（旧 AI会話ログ）
├── 1.実験データ_gdrive（セッション削除後）
└── antigravity_chat_logs（変更なし・別管理のため対象外）
```

## implementation
1. `Claude/セッション/`・`Claude/AI会話ログ/` へファイル移動
2. Claude Codeのプロジェクト設定（memory含む、`C:\Users\chuya\.claude\projects\`）を新パスに更新
3. CLI版Claude Codeをセットアップし、デスクトップショートカット経由で起動可能に（詳細: `Knowledge/claude-code-cli-setup`）
4. 旧フォルダ（`1.実験データ_gdrive\claud.セッション`）を削除

## impact
- Claude Code作業ディレクトリの一元化
- 会話ログ・セッションの参照パス全般の変更
- 今後の新規セッション開始時の起動方法
