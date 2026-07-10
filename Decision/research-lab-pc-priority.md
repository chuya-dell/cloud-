---
date: 2026-06-21
theme: 研究室PC環境構築を最優先タスクに決定
status: resolved
tags: [PC環境構築, タスク優先度]
related: ["Knowledge/研究室PC環境構築手順"]
---

## decision
研究室PC（Windows）の環境構築を最優先タスクとする。Mac環境構築は後回し（優先度低）。

## reason
ユーザーが翌日（6/22）から研究室のPCを使用可能になるため、現在のPC環境と同じセットアップ（Claude Code、Google Drive、MCP設定など）を先に整備することで研究室での作業効率を最大化できる。

## priority_order
1. 現在のPC: タスクスケジューラのパス修正と動作確認
2. 準備作業: 研究室PCセットアップの手順書完成
3. 研究室PC: 環境構築実施（Claude Codeインストール、Google Drive for Desktop、Node.js、obsidian-vault MCP設定、タスクスケジューラ登録、config.env=APIキーのコピー）
4. Mac: 後日対応（優先度低）

## impact
- 研究室でのClaude Code + Obsidian連携作業が可能に
- セッションログの自動保存・処理が2環境で並行実行可能に（スケーラブル化）
- Zotero論文活用・研究データの一元管理（Google Drive経由）
