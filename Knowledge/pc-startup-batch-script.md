## Windows スタートアップフォルダを使った自動起動バッチ設定

### 概要
PC起動時に自動的にMCPサーバーとngrokトンネルを起動するため、スタートアップフォルダにバッチファイルを配置する方法。管理者権限不要。

### 詳細

#### バッチファイル配置
ファイル: `C:\Users\<USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\obsidian-mcp-start.bat`

#### バッチ内容例
```batch
@echo off
cd /d C:\Users\chuya
start "Obsidian MCP Server" node mcp-server.js
timeout /t 2 /nobreak
start "ngrok tunnel" ngrok http --domain=styling-shakily-underfed.ngrok-free.dev 8766
```

#### スタートアップフォルダ場所
- Windows 10/11: `C:\Users\<USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
- ショートカット作成でも可能

### 利点
- 管理者権限不要
- タスクスケジューラより簡単
- バッチファイル削除で簡単に無効化可能

### 注意
- ターミナルウィンドウが自動で表示される
- 複数のコマンドは複数のバッチファイルまたは`start`コマンドで並列実行

### 参考
- 日付: 2026-06-21
