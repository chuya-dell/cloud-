---
date: 2026-06-20
theme: Claude Code CLIセットアップと起動方法
status: resolved
tags: [Claude Code, CLI, セットアップ]
---

## summary
Claude Code CLI版をPATHに追加し、デスクトップショートカット経由で特定ディレクトリで起動する設定。

## executable_location
```
C:\Users\<ユーザー名>\AppData\Local\AnthropicClaude\claude.exe
```

## launch_command
```powershell
claude "G:\マイドライブ\Claude\セッション"
```

## path_setup
exeファイルへのパスをWindowsのPATHに追加すると、PowerShellのどのディレクトリからも`claude`コマンドが使用可能になる。

## desktop_shortcut
コマンドライン `claude "G:\マイドライブ\Claude\セッション"` を指定したショートカットをデスクトップに配置。ダブルクリックで起動し、自動的に該当ディレクトリでClaude Codeが立ち上がる。

## first_launch_setup
1. テーマ選択（Dark mode推奨）→ Enterで確定
2. ログイン選択（Claude account with subscription）→ Enterで確定
3. ブラウザでログイン（必要ならcキーでURLコピー）
4. フォルダ信頼確認（Yes, I trust this folder）→ Enterで許可
5. Obsidian Vault読み込み許可 → 2キー+Enterで以降は聞かれなくする

## directory_structure
```
G:\マイドライブ\Claude\
├── セッション/        （メイン作業ディレクトリ）
└── AI会話ログ/       （会話記録）
```
