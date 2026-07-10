---
name: ""
metadata: 
  node_type: memory
  theme: Memory Index（claude-memoryの索引、常時更新）
  status: active
  tags: 
    - 記憶
    - インデックス
  originSessionId: dd50376c-27b1-4e73-8e6f-5cd70daad5ae
---

# Memory Index

## 📋 Claude Code セッション開始ルール

**【重要】セッション開始時の必須タスク：**
1. このファイル（MEMORY.md）を読み込む
2. 参照ファイルを確認して文脈を把握する
3. 新しい重要な情報が発生した場合、MEMORY.md または該当参照ファイルを更新する

**更新対象：** 研究の進捗、意思決定、ミス、実験結果、タスク完了状況、その他重要な変更

---

## 📝 更新ルール（重要）

### ラボノート連携
- **ラボノート/ 配下** の実験記録に変更があった場合 → **要点をMEMORY.mdに追記**
  - 例：実験結果、新しい知見、問題発見など
  - 詳細は ラボノート/ に、サマリーは MEMORY.md に

### タスク・意思決定連携
- **タスク管理・意思決定** は以下の **両方に反映**：
  - [[タスク.md]]（Vaultルート直下） — 優先度・締切ベースの実行リスト
  - [[Decision/]] — 意思決定のロジック・判断根拠を記録
  - MEMORY.md — 必要に応じて参照ファイルを更新

### 更新フロー（例）
```
ラボノート/実験ログ.md に新結果記入
  ↓
MEMORY.md の project_experiments.md に要点反映
  ↓
タスクが完了・変更
  ↓
Projects/タスク.md + Decision/ に同時反映
```

---

## 📚 参照ファイル一覧

- [ユーザープロフィール・研究](user_profile.md) — D1・大阪公立大・分析化学、研究テーマ・論文・就活
- [PC環境](user_computers.md) — 所持機器スペックと用途
- [Notion・Obsidian運用](reference_notion.md) — DB ID・役割分担・記録ルール
- [Googleカレンダー](reference_calendar.md) — カレンダーID・運用ルール
- [進行中実験・研究室](project_experiments.md) — デジタルカウント実験・DNA固定化・メンバー
- [DNA試薬メモ](project_dna_reagents.md) — チューズデイ購入チオールDNAはDTT不含、TE溶解→希釈のみ
- [対話スタイル・ルール](feedback_interaction_rules.md) — 回答方針・フォーマット指定
- [メモリ共有設定（Google Drive）](feedback_setup_memory_sync.md) — 複数PC間共有の設定内容
- [メモ運用方針（AI最適化フォーマット）](note_format_policy.md) — ラボノート等のフォーマット指針・要約粒度ルール
- [Dell（6階）環境詳細](reference_env_dell6f.md) — Claude Code設定・Obsidian Vault構成・npm/nodeバージョン
- [M1 MacBook（5階）環境詳細](reference_env_m1mac5f.md) — Claude Desktop/Cowork構成・共有メモリ設定・Obsidian Vault構成
- [remotefdtd→chuya2816 Drive同期（GAS）](reference_gas_drive_sync.md) — フォルダID・トリガー設定・一方向追加コピー（syncCopy）仕様
- [Googleカレンダー→Slack自動通知（GAS）](reference_gas_calendar_slack.md) — 分析化学研究グループアカウント、1日2回通知、Webhook URLは平文記載につき取り扱い注意
