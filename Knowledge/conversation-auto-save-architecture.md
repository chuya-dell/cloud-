---
date: 2026-06-21
theme: 会話自動保存のアーキテクチャ（プラットフォーム別2パターン）
status: resolved
tags: [Claude Code, claude.ai, 自動保存, MCP, hook]
related: ["Knowledge/Claude会話自動保存-設定手順", "Knowledge/claude-code-hook-system"]
---

## summary
Claude/Geminiとの会話をObsidian/Google Driveに保存する方法は、プラットフォームにより完全自動 or 手動トリガーの2パターンに分かれる。

## pattern_a_claude_code（完全自動）
1. ユーザーが会話を終了（Ctrl+C等、またはセッション終了操作）
2. `Stop` hookが自動実行（`Knowledge/claude-code-hook-system` 参照）
3. Python/Bashスクリプトが会話ログをJSONから抽出
4. `G:\マイドライブ\AI会話ログ\Claude\` にmdファイルとして保存
5. Google Drive経由でVaultに統合
6. さらに日次バッチ（`save_all_sessions.py`、毎日12時実行）で全セッションを一括保存。手順詳細は `Knowledge/Claude会話自動保存-設定手順` 参照

## pattern_b_claude_ai_web（手動トリガー、推奨・現実的）
claude.ai Web/モバイルアプリには会話終了時の自動トリガー機能がなく、完全自動保存は不可。Claude MCPサーバー（obsidian-vault）が設定済み（`C:\Users\chuya\AppData\Roaming\Claude\claude_desktop_config.json` → `G:\マイドライブ\Obsidian Vault`）であれば、会話の最後に以下のように指示することでClaudeがMCP経由でVaultに直接書き込み可能:
```
この会話をObsidianに保存して
「セッションを G:\マイドライブ\AI会話ログ\claude-web_[日時].md として保存してください」
```
- 制約: 毎回手動指示が必要（完全自動ではない）、複数デバイスからのアクセス時は保存漏れリスクあり
- 実装は簡単で確実、数秒で保存完了

## limitation
Claude.ai Web/アプリのチャット会話は自動ログ保存の仕組みが存在しない（セッション形式のClaude Codeログとは異なる）。ユーザーが明示的にエクスポート・コピー・保存指示をしない限りログは残らない。

## future_options（未実装・検討のみ）
- **Chrome拡張機能**: Claude AIページを監視し会話ツリー更新時に自動ファイル化。開発難易度高（Chrome Extensions API, content script, background service worker）、実装時間数時間、claude.ai仕様変更への追従コストあり
- **Make/Zapier連携**: claude.aiがWebhook非対応のため現状は限定的

## recommended_policy
1. 当面: 手動トリガー方式で全プラットフォーム統一運用
2. 将来: 不便さが目立てばChrome拡張機能開発を検討
