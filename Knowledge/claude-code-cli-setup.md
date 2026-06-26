## Claude Code CLIセットアップと起動方法

### 概要
Claude CodeはPowerShellのCLIから特定のディレクトリで起動できる。実行ファイルはAppDataに格納されている。

### 詳細

#### 実行ファイルの場所
```
C:\Users\<ユーザー名>\AppData\Local\AnthropicClaude\claude.exe
```

#### ディレクトリを指定して起動
```powershell
claude "G:\パス\to\フォルダ"
```

#### 起動時の確認フロー
1. テーマ選択（Dark mode推奨、Enterで確定）
2. ログイン選択（Claude account with subscriptionを選択）
3. ブラウザログイン（必要に応じてURLをcキーでコピー）
4. ディレクトリ信頼確認（Yes, I trust this folder を選択）
5. ファイル読み込み許可（Obsidian Vaultなどの確認）

#### PATHへの追加
exe ファイルへのパスをWindowsのPATHに追加することで、PowerShellのどのディレクトリからも `claude` コマンドが使用可能になる。

#### デスクトップショートカットの作成
```
cmds: claude "G:\マイドライブ\Claude\セッション"
```
をショートカットのコマンドラインに指定してデスクトップに配置。ダブルクリックで起動可能。

### 参考
- 日付: 2026-06-20
