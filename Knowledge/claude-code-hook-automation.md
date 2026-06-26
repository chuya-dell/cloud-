## Claude Code Hook機能による会話自動保存

### 概要
Claude Codeには「hook」という機能があり、セッション終了時などのイベントに自動でシェルコマンドを実行できる。これを利用して会話をObsidianに自動保存する。

### 仕様

**対応プラットフォーム:**
- ✅ Claude Code（黒いターミナル風UI、`claude` コマンドで起動）
- ❌ Claude Desktop（claude.aiのネイティブアプリ）
- ❌ claude.ai Web/モバイルアプリ

**Hook対応イベント:**
- `PreToolUse`: ツール実行前
- `PostToolUse`: ツール実行後
- `Stop`: セッション終了時（会話終了時の自動保存に使用）
- `PreCompact`: コンパクト前
- `PostCompact`: コンパクト後
- `SessionStart`: セッション開始時
- `UserPromptSubmit`: ユーザーがプロンプト送信時

**Hook設定ファイル:**
- グローバル設定: `~/.claude/settings.json`
- プロジェクト設定: `.claude/settings.json`
- ローカル設定: `.claude/settings.local.json`（gitignore推奨）

### 設定例

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

**設定注意点:**
- 既存の設定を保持しながらマージする（全置換はNG）
- 複数hookがある場合は配列に追加
- `timeout`は実行時間の上限（秒）
- `statusMessage`はユーザーに表示されるメッセージ

### 実装手順

1. セッション情報をJSON形式で取得するPythonスクリプト作成
2. `G:\マイドライブ\AI会話ログ\` に自動保存
3. settings.jsonで「Stop」イベントに上記スクリプトを登録
4. セッション終了時に自動実行される

### 参考
- 日付: 2026-06-20
- セッションID: 148e92bd-dee6-4817-ac2b-45d83429d716
