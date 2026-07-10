---
date: 2026-06-20
theme: 会話自動保存の実装方針決定（Claude Code優先、段階的自動化）
status: resolved
tags: [自動保存, Claude Code, hook]
related: ["Knowledge/conversation-auto-save-architecture"]
---

## decision
Claude Code側を優先実装として、hook機能によるセッション終了時の自動Obsidian保存を導入する。claude.ai Web側は技術的制約（Webhook非対応）のため完全自動化を諦め、手動トリガー方式とする。

## reason
- ユーザーが「いちいち命令するのはめんどくさい」と指摘、完全自動化への要件が明確化
- claude.ai WebからのURL自動化はWebhook非対応のため技術的に困難
- Claude CodeのHook機能は既に利用可能で実装しやすい
- 完全自動化と実装現実性のバランスを取る必要があった

## approach
1. **Claude Code（優先実装）**: `Stop`イベントhookでセッション終了時に自動でObsidianへ保存
2. **claude.ai Web/アプリ**: 自動化不可のため手動トリガー方式（詳細は `Decision/ios-chat-notion-others-obsidian` および `Decision/obsidian-chat-logging-policy` 参照）

## note
実装の技術詳細（config例・対応イベント一覧）は `Knowledge/conversation-auto-save-architecture` を参照。
