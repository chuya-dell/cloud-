---
date: 2026-06-20
theme: Claude Code hook機能の仕組みと会話自動保存への応用
status: reference
tags: [Claude Code, hook, 自動化, Obsidian]
related: ["Knowledge/Claude-Code-hookメモ"]
---

## summary
Claude Code（CLIの`claude`コマンド起動アプリ）には「hook」機能があり、セッションのライフサイクルイベント発生時に自動でシェルコマンドを実行できる。これを利用してセッション終了時に会話ログをObsidian/Google Driveへ自動保存する。Claude Desktop・claude.ai Web/モバイルアプリはhook機能非対応（MCPで「保存して」と手動トリガーするのみ）。

## supported_events
| イベント | 説明 |
|---------|------|
| SessionStart | セッション開始時 |
| UserPromptSubmit | ユーザー入力提出時 |
| PreToolUse | ツール使用前 |
| PostToolUse | ツール使用後（成功時） |
| PostToolUseFailure | ツール使用後（失敗時） |
| Stop | セッション終了時（clear, resume, compact含む。会話自動保存に使用） |
| PreCompact / PostCompact | コンパクト実行前後 |
| Notification | 通知時 |

## config_location
- グローバル: `~/.claude/settings.json`
- プロジェクト: `.claude/settings.json`
- ローカル: `.claude/settings.local.json`（.gitignore推奨）

## config_example
```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "python3 C:/path/to/save_session.py",
            "timeout": 60,
            "statusMessage": "会話をObsidianに保存中..."
          }
        ]
      }
    ]
  }
}
```

## notes
- 既存の設定を読み込んでからマージする（全置換はNG）
- 複数hookは配列で追加可能
- matcherで特定ツール（Bash, Write等）に限定可能
- timeoutは秒単位

## implementation_flow
1. セッション情報をJSON形式で取得するPythonスクリプト作成
2. `G:\マイドライブ\AI会話ログ\` に自動保存（`YYYY-MM-DD_HH-MM-SS.md`形式）
3. settings.jsonの「Stop」イベントにスクリプト登録
4. セッション終了時に自動実行

## known_issues
実運用上の不安定さ・現在の設定パスは `Knowledge/Claude-Code-hookメモ` 参照（アプリを×で閉じるとStopフックが発火しないケースあり）。
