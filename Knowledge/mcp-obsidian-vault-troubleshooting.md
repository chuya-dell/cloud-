---
date: 2026-06-21
theme: MCP obsidian-vaultサーバー接続トラブルシューティング
status: reference
tags: [Claude, MCP, Obsidian, トラブルシューティング]
related: ["Knowledge/claude-mcp-obsidian-setup"]
---

## MCP obsidian-vault サーバー接続トラブルシューティング

### 概要
Claude Code デスクトップアプリで Obsidian Vault への MCP 接続が切断されている場合の対処方法。

### 考えられる原因

1. **Google Drive 同期の遅延**
   - `G:\マイドライブ\Obsidian Vault` などの Google Drive ストリーミングフォルダを使用している場合、アクセス時に遅延が発生して MCP がタイムアウトする可能性がある

2. **MCP サーバープロセスの起動タイミング問題**
   - MCP サーバーは Claude Code 起動時に接続されるため、起動順序の問題で未接続になることがある

3. **パス・アクセス権限の問題**
   - フォルダが削除されている、権限がない などの問題

### トラブルシューティング手順

**ステップ1: 完全な再起動**
- Claude Code デスクトップアプリをタスクトレイからも含めて完全に終了
- アプリを再起動
- 再起動後に MCP が `obsidian-vault` として表示されるか確認

**ステップ2: MCP サーバーの手動リロード**
- 左下の設定アイコン（または `...` メニュー）を開く
- 「MCP Servers」または「Extensions」の項目を探す
- `obsidian-vault` 横の再起動ボタンを押す

**ステップ3: タスクトレイからの再起動**
- タスクトレイ（右下の時計横）の Claude アイコンを右クリック
- 「Quit」を選択して完全終了
- アプリを再起動

### 参考
- 日付: 2026-06-21
