## Windows スタートアップフォルダでの自動起動登録

### 概要
タスクスケジューラより簡易的に、PCログイン時に自動起動スクリプトを実行する方法

### 詳細

#### スタートアップフォルダのパス
```
C:\Users\[Username]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

#### バッチファイルの配置
1. 実行スクリプト（例：`obsidian-mcp-start.bat`）を作成
2. 上記Startupフォルダにコピー
3. PC再起動時に自動実行

#### バッチファイル例
```batch
@echo off
cd C:\Users\chuya
node mcp-server.js
ngrok http --domain=styling-shakily-underfed.ngrok-free.dev 8765
```

#### 利点
- 管理者権限不要
- タスクスケジューラより設定簡単
- 遅延起動による競合回避

#### 注意
- コマンドプロンプトウィンドウが見える（非表示にはVBScriptラッパーが必要）
- 順序保証のためスリープを含める

### 参考
- 日付: 2026-06-21
