## Claude Code 新しいディレクトリでの起動方法

### 概要
Claude Code CLI版をPATHに追加し、デスクトップショートカット経由で特定ディレクトリで起動する方法

### 詳細

#### Claude Code実行ファイルの場所
```
C:\Users\chuya\AppData\Local\AnthropicClaude\claude.exe
```

#### 起動コマンド（PowerShell）
```powershell
claude "G:\マイドライブ\Claude\セッション"
```

#### デスクトップショートカット作成済み
- 次回からはショートカットをダブルクリックするだけで起動
- ターミナルが開き、自動的にClaude Codeが `G:\マイドライブ\Claude\セッション` で起動

#### 初回起動時のセットアップ手順
1. テーマ選択（デフォルトはDark mode） → Enterで確定
2. ログイン選択（Claude account with subscription） → Enterで確定
3. ブラウザでログイン（cキーでURLコピー、必要なら）
4. フォルダ信頼確認 → Enterで許可
5. Obsidian Vault読み込み許可 → 2キー + Enterで今後聞かれなくする

#### ディレクトリ構成
```
G:\マイドライブ\n└── Claude/
    ├── セッション/        （メイン作業ディレクトリ）
    └── AI会話ログ/       （会話記録）
```

### 参考
- 日付: 2026-06-20
