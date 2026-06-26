## MCP接続ツールの設定と役割

### 概要
Claude Codeから接続可能なMCPツール一覧と、実装における取捨選択。多すぎる接続はsystem-reminderを肥大化させトークン消費増加につながる。

### 詳細

#### 2026-06-21現在の接続状態

**Web接続カテゴリ**
- Gmail（カット）
- Google Calendar（保持）
- Google Drive（カット）
- Notion（保持）

**デスクトップカテゴリ**
- Claude in Chrome（保持）
- obsidian-vault（保持）

**未接続**
- Obsidian Vault（カスタム）← エラーあり
- GitHub連携

#### 接続の意思決定基準

**Google Calendar を残した理由**
- タスク管理システムとして流用
- 定期的な参照が必要

**Notion を残した理由**
- 記録システムの主要媒体
- ユーザーとの参照用UI

**obsidian-vault を残した理由**
- Claude のAI外部記憶
- MCPアクセスが高速

**Claude in Chrome を残した理由**
- たまに使用（明言あり）

**Gmail/Google Drive を切断した理由**
- 日常の会話で使用機会が低い
- トークン消費削減が優先

### 参考
- 日付: 2026-06-21
