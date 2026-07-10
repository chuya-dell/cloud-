---
date: 2026-06-20
theme: Google Drive上のClaude関連ディレクトリ再編
status: resolved
tags: [Google Drive, ディレクトリ構成, Claude]
---

## summary
Google Drive（`G:\マイドライブ`）内に散在していたClaude関連ファイルを `Claude/` フォルダへ一元化した整理記録。

## before
```
G:\マイドライブ
├── 1.実験データ_gdrive
│   └── claud.セッション  ← 実験データ配下に配置（移動対象）
├── AI会話ログ  ← 単体フォルダ（移動対象）
└── antigravity_chat_logs  ← 別管理（対象外）
```

## after
```
G:\マイドライブ
├── 1.実験データ_gdrive  ← claud.セッション は削除
├── Claude/  ← 新規統合フォルダ
│   ├── セッション/  ← 旧 claud.セッション
│   └── AI会話ログ/  ← 旧 AI会話ログ
└── antigravity_chat_logs  ← 変更なし（Claude統合外で独立管理）
```

## moved
1. `1.実験データ_gdrive\claud.セッション` → `Claude\セッション`
2. `AI会話ログ` → `Claude\AI会話ログ`

## follow_up_updates
- Claude Codeプロジェクト設定ファイルのパスを新ディレクトリに更新
- プロジェクトキー名の再計算
- セッションデータ（Memory含む）を `C:\Users\chuya\.claude\projects\` から新パスへ移行済み
