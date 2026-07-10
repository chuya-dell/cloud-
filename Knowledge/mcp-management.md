---
date: 2026-06-21
theme: MCP接続管理の方針（トークン削減のための取捨選択）
status: resolved
tags: [MCP, Claude Code, トークン節約]
related: ["Knowledge/token-consumption-optimization"]
---

## summary
Claude Codeで接続するMCPツールが多いほど`system-reminder`のツール一覧が肥大化し、毎ターンのトークン消費が増える。使用頻度に基づき接続を取捨選択した（2026-06-21時点）。

## decision（2026-06-21時点の接続状態）
| ツール | 判断 | 理由 |
|---|---|---|
| obsidian-vault | 保持 | ClaudeのAI外部記憶、MCPアクセスが高速 |
| Notion | 保持 | 記録システムの主要媒体、ユーザーとの参照用UI |
| Google Calendar | 保持 | タスク管理システムとして流用、定期参照が必要 |
| Claude in Chrome | 保持（オプション） | たまに使用するため残す |
| Gmail | 削除 | 日常の会話で使用機会が低い |
| Google Drive | 削除 | システムが多いと不要、トークン消費削減優先 |
| Obsidian Vault（カスタム実装） | 未接続 | エラーあり |
| GitHub連携 | 未接続 | 未設定 |

## effect
MCPを減らすことで`system-reminder`のツール一覧が半分以下になる可能性。毎ターン自動で全リストが読み込まれるため削減効果は継続的。

## how_to_change
Claude Codeの設定画面（右上の歯車マーク）から接続・切断操作が可能。
