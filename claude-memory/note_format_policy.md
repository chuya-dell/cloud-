---
name: note-format-policy
description: ラボノート等のメモ運用方針（AI最適化フォーマット）
metadata: 
  node_type: memory
  type: reference
  created: 2026-07-03
  originSessionId: dd50376c-27b1-4e73-8e6f-5cd70daad5ae
---

## 前提

忠弥は生のノートファイル（ラボノート/、Knowledge/等）をほぼ直接読まない。
書き込み窓口はClaude（忠弥は自然文で話す/書くだけ）。構造化はClaude側の責務。

## 🔒 必須ルール（2026-07-10 憲法化・例外なし）

**Obsidian Vault内にファイルを新規作成する場合、フォルダを問わず必ずYAML frontmatterを付与する。frontmatterなしでのノート新規作成は禁止。**

最低限必須のキー（内容に応じて追加は自由）:
```yaml
---
date: YYYY-MM-DD
theme: 一行で内容を要約
status: open | in_progress | resolved | reference 等、内容に応じた状態
tags: [キーワード1, キーワード2]
---
```
- 既存ノートへの追記（Daily/への追記など）の場合は、そのノートの既存frontmatterを維持・必要なら更新する。新規追記のたびにfrontmatterを書き直す必要はない
- 関連ノートがあれば`related`フィールドで明示する（wikilink形式）
- 小さいメモ・作業ログでも省略しない（「軽いから後で」は禁止。後で一括整理するコストの方が高いことが2026-07-09のボルト整理で実証済み）
- セッション開始時にこのルールを忘れていないか、他の憲法ファイル（INDEX.md）と合わせて確認する

## フォーマット方針

- 保存形式は人間可読性より、Claudeによる検索・抽出・パースのしやすさを優先する
- YAML frontmatterを厚くする（date, project, theme, sample_ids, status, tags, related等、検索・フィルタ対象になるものは全部frontmatterに出す）
- 本文はプローズを避け、key: valueまたは固定キー見出し（params / result / open_questions / next_action等）で構造化する
- 数値パラメータは文章に埋め込まず、必ずkey: valueまたは表で分離する
- 指示語（「それ」「あの実験」等）は禁止。日付やノート名などの固有名詞、または`related`フィールド・wikilinkで明示する
- ただし要約1行（summary等）は自然文で残す。Claudeがセッションをまたいで人間向けに再構成する際の精度を上げるため

## 既存ノートへの遡及適用（2026-07-09 決定）

2026-07-09、Obsidianボルト整理の一環として方針転換：既存の古いノートにも遡ってこのフォーマットを適用する（従来は新規ノートのみだった）。
**Why:** ボルト内に同一トピックの重複ノートが大量発生していた（Knowledge 137件・Decision 58件など）。frontmatter構造化と同時に整理することで検索性向上とトークン削減を両立する狙い。
**How to apply:** 優先順位は ラボノート(35件) → Knowledge(137件) → Decision(58件) → Projects/claude-memory等その他。フォルダ単位で順次処理。Knowledge/Decisionは同一トピックの重複ノートが多いため、frontmatter付与と同時に内容が重複するノートは統合・削除する。

## 忠弥への提示（要約）の粒度ルール

聞かれた粒度に応じてClaudeが返す粒度を自動調整する：

- 単一の事実確認（例：「あの荷重何gだった？」）→ 要約不要、該当値を即答
- 1ノート分の把握（例：「あのSAM実験どうだった？」）→ 軽い要約（3〜5行程度）
- 複数ノートにまたがる把握（例：「今月のデジタルカウントの進捗まとめて」）→ 構造化要約（見出し+箇条書き、必要なら時系列）
- 大量・長期（例：「このプロジェクト始まってからの流れ全部」）→ 一度に出さず、まず目次的な一覧を出してから深掘りするか確認する
