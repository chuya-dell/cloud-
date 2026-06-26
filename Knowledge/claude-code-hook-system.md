## Claude Code Hook機能の仕組み

### 概要
Claude Code（CLI/デスクトップアプリ）には「hook」という機能があり、セッションのライフサイクル内の特定のイベント発生時に自動でシェルコマンドを実行できる。

### Hook の対応イベント
| イベント | 説明 |
|---------|------|
| SessionStart | セッション開始時 |
| PreToolUse | ツール使用前 |
| PostToolUse | ツール使用後（成功時） |
| PostToolUseFailure | ツール使用後（失敗時） |
| Stop | セッション終了時（clear, resume, compact含む） |
| PreCompact | コンパクト実行前 |
| PostCompact | コンパクト実行後 |
| Notification | 通知時 |
| UserPromptSubmit | ユーザー入力提出時 |

### Hook設定例
```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "-",
        "hooks": [
          {
            "type": "command",
            "command": "python /path/to/save_transcript.py",
            "timeout": 60,
            "statusMessage": "セッションをObsidianに保存中..."
          }
        ]
      }
    ]
  }
}
```

### 設定ファイルの場所
- グローバル: `~/.claude/settings.json`
- プロジェクト: `.claude/settings.json`
- ローカル: `.claude/settings.local.json`（.gitignore推奨）

### 重要なポイント
- 既存の設定を読み込んでから更新する（置換不可）
- 複数のhookを配列で登録可能
- matcherで特定のツール（Bash, Write等）に限定可能
- タイムアウト値は秒単位で指定

### 参考
- 日付: 2026-06-20
