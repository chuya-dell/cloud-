## MCP接続管理のベストプラクティス

### 概要
Claude Codeで複数のMCPツールを接続する際の最適な構成

### 削減効果
- MCPを減らすことで `system-reminder` のツール一覧が半分以下になる可能性
- 毎ターン自動で全リストが読み込まれるため、削減効果は継続的

### 推奨構成（優先度順）

**必須**
- obsidian-vault：外部記憶として重要
- Notion：主要な記録先
- Google Calendar：タスク管理連携

**オプション**
- Claude in Chrome：たまに使う場合は残す

**削除推奨**
- Gmail：Claudeとの会話では使わない
- Google Drive：システムが多いと不要
- 他の未使用MCP

### 設定変更方法
Claude Codeの設定画面（右上の歯車マーク）から接続・切断操作が可能

### 参考
- 日付: 2026-06-21
