---
date: 2026-06-21
theme: Googleカレンダー運用ルール確定
status: resolved
tags: [Googleカレンダー, 運用ルール]
related: ["Knowledge/google-calendar-operation-rules", "Decision/calendar-migration-decision"]
---

## decision
カレンダー帰属・時間設定・通知設定の3点についてルールを確定し、以降の全予定入力（AIアシスタント含む）に自動適用する。

## reason
カレンダー管理を効率化し、研究予定（複数プロジェクト）と個人予定を明確に分類・管理するため。予定の時間情報の入力方針もまちまちだったため統一する必要があった。

## rules
**1. カレンダー帰属**
- 実験カレンダー: すべての研究関連予定
- Tuesdayカレンダー: Tuesday関連予定
- 忠カレンダー: 個人的で研究関連でない予定

**2. 時間設定（3パターン）**
- 開始時間のみ決定 → 開始・終了を同一時刻にし、イベント時間を0分に設定
- 開始・終了とも明確 → 両方を正確に記入
- 時間が決まっていない → 終日イベントに設定

**3. 通知設定**
- 全ての予定で通知なし（無効化）

## impact
- Googleカレンダー全体の予定管理・今後の予定入力の初期設定
- AIアシスタントの予定入力時の自動判定基準
- 過去の誤分類分は `Decision/calendar-migration-decision` に基づき移行
