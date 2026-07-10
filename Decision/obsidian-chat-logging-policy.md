---
date: 2026-06-21
theme: Obsidianへのチャット記録ポリシー（セッションログ vs チャットログ）
status: superseded（2026-06-30に Decision/ios-chat-notion-others-obsidian で書き込み先ルールが更新）
tags: [記録ポリシー, Obsidian, Claude.ai]
related: ["Decision/ios-chat-notion-others-obsidian", "Decision/conversation-auto-save-strategy"]
---

## decision（2026-06-21時点）
- セッションログ（AI会話ログフォルダ）: `process_logs_to_obsidian.py` により自動処理でDaily/・Knowledge/・Decision/に記録
- Claude.ai のWeb/アプリチャット: 自動保存の仕組みがないため、内容をユーザーから聞き取り手動記録

## reason
セッションログとチャットログの処理方式の違いを明確化し、記録漏れを防ぐため。

## impact
Obsidian Vault全体の記録完全性、ユーザーの日次ログ管理。

## superseded_note
2026-06-30、書き込み先の最終ルールが `Decision/ios-chat-notion-others-obsidian` で確定（iOSのclaude.aiチャットのみNotion、それ以外はObsidian）。本ノートは経緯として残す。
