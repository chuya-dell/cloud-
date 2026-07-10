---
date: 2026-06-21
theme: NotionとObsidianの役割分担設計
status: superseded（2026-06-28に Decision/notion-obsidian-role-final で最終決定）
tags: [Notion, Obsidian, 運用設計]
related: ["Knowledge/ai-role-division-map", "Decision/notion-obsidian-role-final"]
---

## summary
NotionとObsidianを併用する上での役割分担設計。「理想設計」と「現実に採用した運用」の2案を比較検討した。

## roles
- **Claudeチャット**: メインの作業場、リアルタイムの指示・実行
- **Notion**: 参照用UI（忠さん・Claude閲覧用）。UIが使いやすい。ファイルアップロード制限あり（1ファイル5MB）、テキストはストレージ制限なし（無料版でも）
- **Obsidian**: Claudeの外部記憶（AI用）。Google Drive 5TB活用可、オフライン動作、AI乗り換え時の引き継ぎが容易、Markdownで汎用性が高い

## design_option_ideal（Obsidian正・Notion写し）
- Obsidian = マスターデータ・Claudeの作業台。全ての元データの一次置き場
- Notion = Obsidianの「写し」。タスク俯瞰・優先度・今日やることの閲覧用
- データフロー: 投げる → Obsidianに書く → Notionに反映
- 利点: 矛盾がなく、Obsidianが壊れてもNotionから復元できる
- 欠点: 毎回2箇所書く分設計が重い、Obsidian側のファイル構成が必須

## design_option_actual（Notion運用・Obsidian定期書き出し, 採用中）
- Notion = 直接運用。投げる → Notionに直接登録
- Obsidian = 定期的な蓄積。完了タスクを定期的にNotionからObsidianへ書き出し、長期保管・傾向分析用。マスターの厳密さは諦める
- 利点: 回り始めやすく段階的にObsidian運用を立ち上げられる
- 欠点: Obsidianが死蔵されるリスク、マスターの一意性が曖昧

## obsidian_retention_reasons
1. 容量: Google Drive 5TB活用可能
2. AI乗り換え対応: ベンダーロックインしない
3. 汎用性: Markdown形式で何にでも応用可能

## current_challenge
NotionとObsidianへの2重書き込みが発生し、毎回の同期が手間。運用方針としては「Notionを主軸に更新し、重要な内容だけObsidianにも入れる」温度感で、完全同期は目指さない（保険的位置づけ）。
