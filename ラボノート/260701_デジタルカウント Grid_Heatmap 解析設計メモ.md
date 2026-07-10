---
date: 2026-07-01
project: digital_counting
theme: Grid_Heatmap 解析設計
status: anomaly_unresolved
tags: [Grid_Heatmap, ImageJ, Subtract, threshold, anomaly, ByteBlitter]
related: ["ラボノート/検量線作成（デジタルカウント）", "ラボノート/【デジタルカウント】SAM形成確認（カメラ＋スペクトル前後比較）", "ラボノート/デジタルカウント スループット問題の解決策検討 (1)"]
---

# デジタルカウント｜Grid_Heatmap 解析設計メモ

## summary
ImageJマクロGrid_Heatmap [F1]をベースにした検量線解析フロー。Subtract方向はpre-postと確定（生データ逆算検証）だがByteBlitter実装レベルは未確認。閾値は約2.0で確定。濃度系列データに複数の外れ値を確認、フォーカス不良説は撤回（反証も確定ではない）。2026-07-01時点で再現実験を実施し、指標を絶対数からグリッド率(%)に変更する決定。

## premise
- SAM検量線データの解析方法をすり合わせ中
- フロー：差分画像→グリッド輝度算出→閾値カウント→検量線
- サンプル：ピラーにAu 200nm蒸着、暗視野像撮影
- 200nm蒸着は原理的に構造が訛り、暗視野像は必ずぼやける（正常な現象）

## image_processing_flow
1. pre画像・post画像を撮影
2. Image Calculator（Subtract）で差分画像作成（8bit、クリップ）
   - 確定: Subtract=Image1-Image2、Image1=pre, Image2=post、すなわちpre-post
   - 根拠: ImageJ公式ソース(ij.plugin.ImageCalculator.java)のip1.copyBits(ip2,...,SUBTRACT)構造確認＋生データ9フィールドでpre-post方向を採用した場合のみ閾値≈2.0で報告カウント値と一致（post-preでは必要閾値が1.5-6.7とバラバラで不整合）
   - 未確認: Blitter実装クラス（ByteBlitter等）レベルでの演算式そのもの。忠弥指示で後日確認予定（保留タスク）
   - 注意: pre-postは「preの方がpostより明るい（輝度減少）グリッド」をカウントする方向。SAM形成・分子吸着によるシグナル増加検出という実験コンセプトとこの計算方向が整合するかは未検証（要検討）
3. 差分画像にGrid_Heatmap [F1]マクロを実行
   - グリッドサイズ: 8px固定（PC負荷の実務上の制約値）、8px≈実寸500nm（1px≈62.5nm）
   - 各グリッドの平均輝度(Mean)を算出、1枚あたり約65,280グリッド
4. カウント値の定義（確定）: Results の Mean列について閾値を超えた単純なグリッド数（後処理・粒子解析等は介在しない）

## threshold
value: 約2.0（生データ9フィールドの逆算検証で確定）
cross_check: 以前スクリーンショットから読み取ったN.C.3枚のave+3σ平均値(1.998)とほぼ一致
open_question: この閾値がN.C.データからどう算出されたか（画像ごと算出→平均の方式Bか等）の詳細手順は今回の逆算検証では未確認。値が一致したことと算出方法が方式Bであることの確証は別問題

## anomaly_observations
table:
  - condition: n（N.C.、条件1）
    rep1: 72
    rep2: 1734
    rep3: 1080
    outlier: 72が低外れ値
  - condition: 100pM（条件2）
    rep1: 4736
    rep2: 2061
    rep3: 2907
    outlier: 4736が高外れ値
  - condition: 10pM（条件3）
    rep1: 775
    rep2: 1007
    rep3: 4096
    outlier: 4096が高外れ値
  - condition: 1pM（条件4）
    rep1: 2241
    rep2: 2546
    rep3: 9192
    outlier: 9192が高外れ値
  - condition: 100fM（条件5）
    rep1: 13
    rep2: 26
    rep3: 1806
    outlier: 1806が高外れ値
  - condition: 10fM（条件6）
    rep1: 202
    rep2: 35
    rep3: 1125
    outlier: 1125が高外れ値
  - condition: 1fM（条件7）
    rep1: 1203
    rep2: 1699
    rep3: 495
    outlier: 明確な外れ値なし
note: 濃度依存性が完全に崩れている（100pMより1pMの方が高い、ネガコンより100fM/10fMの方が低い等）
filename_convention: (条件番号)-(基板番号)-(操作番号:0=pre,1=post)。基板番号は視野内で左から1,2,3

## anomaly_investigation_history
### stage1_focus_hypothesis
status: 撤回
initial_basis: 目視評価（外れ値視野のヒートマップが全体的にノイジー、正常視野との見た目の違い、pre→postでのぼやけ方の違い）から「pre撮影前の再焦点合わせの精度不足が原因」と一時結論
withdrawal_reason:
  - スクリーンショット経由で算出したstd値（コントラスト）が生データでは再現されなかった
  - 生データ(TIFF)でmean/std/Variance of Laplacianを計算したところ異常視野と正常視野に明確な差はなく、むしろ5/5すべての比較で異常視野の方がmean・VarLapが高く、ボケ仮説と逆方向の結果
  - ただしこの反証自体も指標選定の妥当性に疑義があり、フォーカス不良説の否定も確定結論として扱えない

### stage2_counter_evidence_doubt
target: std, Variance of Laplacianという反証指標への疑義（自己検証）
issues:
  - 全体統計量であり局所的なボケを検出できない（画像全体2048x2044pxのstd/VarLapは局所フォーカス不良を希釈し検出できない可能性。局所解析(8pxグリッド単位VarLap等)は未実施）
  - 暗視野・疎な散乱点画像への指標妥当性が未検証（Variance of Laplacianは一般自然画像向け指標、今回の暗視野・疎な輝点画像での有効性は未確認）
  - ダイナミックレンジが極端に狭い（実測画素値は8bitのうちmin≈91-94, max≈136-146程度、40-55階調程度。量子化ノイズの影響を強く受けている可能性）
  - フォーカスとの較正実験が未実施（意図的にピントをずらした画像でのstd/VarLap変化較正データがない状態で採用）
conclusion: フォーカス不良説は「支持されていないが、反証もされていない」という原因不明の状態

## raw_data_reference
note: 参考データとして保存、解釈は保留。スクリーンショット経由で算出した旧std値（12.30/8.34/2.15等）は生データと矛盾しており誤りだったため撤回済み
fields:
  - field: 4-2-0（1p正常pre）
    reported_count: 2546
    mean_pre: 116.787
    std_pre: 5.580
    varlap_pre: 47.904
  - field: 4-3-0（1p異常pre）
    reported_count: 9192
    mean_pre: 120.679
    std_pre: 5.502
    varlap_pre: 48.629
  - field: 1-1-0（n異常pre）
    reported_count: 72
    mean_pre: 122.326
    std_pre: 5.609
    varlap_pre: 48.565
  - field: 2-1-0（100p異常pre）
    reported_count: 4736
    mean_pre: 118.859
    std_pre: 5.432
    varlap_pre: 48.350
  - field: 2-2-0（100p正常pre）
    reported_count: 2061
    mean_pre: 117.872
    std_pre: 5.763
    varlap_pre: 48.012
  - field: 3-3-0（10p異常pre）
    reported_count: 4096
    mean_pre: 126.390
    std_pre: 6.221
    varlap_pre: 49.417
  - field: 3-1-0（10p正常pre）
    reported_count: 775
    mean_pre: 123.230
    std_pre: 5.601
    varlap_pre: 48.797
  - field: 5-3-0（100f異常pre）
    reported_count: 1806
    mean_pre: 110.344
    std_pre: 5.052
    varlap_pre: 47.131
  - field: 5-1-0（100f正常pre）
    reported_count: 13
    mean_pre: 108.025
    std_pre: 4.383
    varlap_pre: 46.181
  - field: 6-3-0（10f異常pre）
    reported_count: 1125
    mean_pre: 115.902
    std_pre: 5.119
    varlap_pre: 47.873
  - field: 6-1-0（10f正常pre）
    reported_count: 202
    mean_pre: 114.277
    std_pre: 4.906
    varlap_pre: 47.398

## open_questions
1. pre-postという計算方向が実験コンセプト（結合によるシグナル増加検出）と整合するか：未検証。輝度減少を検出している可能性
2. 異常値の原因：不明。フォーカス不良説は支持も反証もされていない
3. 局所的な指標（8pxグリッド単位でのVariance of Laplacian等）での再検証：未実施
4. Blitter実装クラスでのSubtract演算式の直接確認：忠弥指示待ち（保留タスク）

## decision_2026-07-01
action: 再現実験を実施
change: 指標を「閾値超えグリッド数（絶対数）」から「閾値超えグリッド率（%）」に変更
reason: 視野内に物理的なスクラッチ溝（縦・横）を位置合わせのランドマークとして使用しており、スクラッチ部分は解析対象から除外される（または位置合わせによるクロップで有効領域が変動する）ことを忠弥が確認済み。基板ごとに解析可能な有効面積が異なるため、絶対数では基板間の有効面積変動が比較を歪める
unverified: 有効面積の変動幅が未定量化（「若干」の程度が不明）。この変動が今回の異常値（9192、4736等）と直接関連するかは未検証。スクラッチ由来の有効面積縮小は通常グリッド数を減らす方向のはずで、異常に高いカウントとの関連は論理的に未整理。安易に原因説明へ転用しないこと
see_also: デジタルカウント スループット問題の解決策検討（基板固定＋2段階リローカライズの文脈）

## next_actions
- 再現実験の実施（指標：閾値超えグリッド率）
- pre-post方向と実験コンセプトの整合性を検証
- 8pxグリッド単位での局所鮮鋭度指標を設計・検証（フォーカス不良説の再検証）
- Blitter実装クラスのソースコード確認（忠弥指示待ち）
- Grid_Heatmapマクロへの閾値カウント（率）処理の実装

## related_context
- 修論PCバイオセンサーのLOD=2.3nM（バルク応答）。デジタルカウントはこれより低濃度側を狙う
- 過去の研究報告（260605_研究報告_白石）：SH-C6吸着実験で同様のave+3σ閾値・分割画像解析手法を使用。測定は3濃度点（1fM/1pM/1nM）を各1回のみで、傾き0.6（≠1）の説明（強結合サイト・通常サイトの混在）は独立した実証データを伴わない事後的仮説
