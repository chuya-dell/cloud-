---
date: 2026-06-21
theme: Claude運用時のトークン消費最適化
status: reference
tags: [トークン節約, Claude Code, セッション運用]
---

## summary
Claude Code / claude.ai運用時にトークン消費が急激に増える問題への対策。最も効果的なのは早期の記録＋新セッション開始（`/clear`）。

## causes
- `system-reminder`のdeferred tools一覧が毎ターン読み込まれる（制御不可）
- MCP接続数が多いほどsystem-reminderが重くなる
- セッション開始時の複数ファイル読み込み（INDEX・Daily・Mistakes・長いNotionページ等）
- 会話が長くなるほどコンテキスト（会話履歴全体）が増大し、毎ターンの処理コストが増える

## countermeasures（優先度順）
1. **早期の記録＋新セッション開始（最強）**: 記録 → `/clear`（Claude Codeのみ）→ 「Obsidianの最新Dailyを読んで再開して」で再開。Obsidian・Notionの記録自体は消えない
2. **MCP接続数の削減**: 使っていないMCP（Gmail、Google Driveなど）を切断し、必要なもの（Calendar, Notion, Obsidian, Chromeなど）のみ残す
3. **セッション開始時の読み込みを絞る**: INDEX・Daily・Mistakesの3点フル読みではなく、超短縮サマリー1ページのみ等に絞る案
4. **質問のまとめ**: 1ターンに複数質問を含める
5. **作業の区切りで/clearする**: 大きな作業が終わったらObsidian/Notionに記録→`/clear`→新セッションで再開

## context_note
コンテキスト＝会話の全履歴。Claudeは毎ターン「今までの会話全部」を送信して処理するため、会話が長いほど1回の返答あたりのトークン消費が増える。
