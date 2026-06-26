## claude.ai WebUIからのMCP利用（手動保存）

### 概要
claude.ai WebUI / スマホアプリからは会話終了時の自動トリガー機能がないため、完全自動保存はできない。代わりにMCPを活用した手動保存が可能。

### 実装方法
会話の最後に以下のようにClaudeに指示：
```
この会話をObsidianに保存して
```

ClaudeがMCPでVaultに直接書き込む。

### 前提条件
- Claude MCPサーバー（obsidian-vault）が設定済み
  - 設定場所：`C:\Users\chuya\AppData\Roaming\Claude\claude_desktop_config.json`
  - マウント先：`G:\マイドライブ\Obsidian Vault`

### 制約
- 手動で「保存して」と言う必要がある（完全自動ではない）
- 複数デバイスからのアクセス時は保存漏れのリスク

### 将来案
- Chrome拡張機能で会話を監視し自動保存（高難易度）
- Make/Zapier連携（claude.ai Webhook対応待ち）

### 参考
- 日付: 2026-06-20
