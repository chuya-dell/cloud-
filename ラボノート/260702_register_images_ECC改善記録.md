---
date: 2026-07-02
project: substrate_alignment
theme: register_images.py ECC化・一致率改善
status: resolved
tags: [ECC, register_images, PC-alignment-claude, NCC]
related: ["ラボノート/基板位置合わせ_スクリプト仕様一覧"]
github: https://github.com/chuya-dell/PC-alignment-claude
branch: claude/ichiritsutsu-optimization-333opv
---

# register_images.py（Claude Code版）ECC化・一致率改善記録（2026-07-02）

## summary
「一致率100%まで改善」指示を受け、実データでregister_images.pyの位置合わせ精度を検証・改善。旧アルゴリズム（縦線傾き検出）はノイズに弱く悪化するケースもあったため、ECC（Enhanced Correlation Coefficient）ベースに置き換え、一致率83-88%→94%前後まで改善。残差は撮像ノイズ＋試料の実変化と結論し、これを現実的上限として採用終了。

## old_algorithm_issue
- 手法: 列範囲(30,250)内の各行の最暗点を線形回帰しスクラッチの傾きを検出→回転・並進補正
- 問題: スクラッチが幅広くテクスチャの多い暗帯のため各行最暗点がノイズ支配（残差std≈28px、探索範囲220pxに対し過大）
- 結果: 無補正より悪化するケースあり

## ncc_before_after
- 1-1.tif: 無補正0.852 → 旧アルゴリズム0.500（悪化）→ 新ECC 0.889
- 1-2.tif: 無補正0.803 → 旧アルゴリズム0.767 → 新ECC 0.893
- 1-3.tif: 無補正0.839 → 旧アルゴリズム0.835 → 新ECC 0.893

## new_algorithm_ecc
1. cv2.phaseCorrelate（位相相関）で粗い並進量を推定
2. その推定値を初期値としてcv2.findTransformECC（MOTION_EUCLIDEAN）で回転・並進をサブピクセル精緻化
3. 一致率（|Δ|≤5階調の画素割合）とNCCを算出し品質定量評価
4. 出力bit深度を元画像dtypeに合わせて保持するよう修正（旧版はuint8決め打ちでclipしていた）

## match_rate_results
- 1-1.tif: 旧83.4% → 新94.07%（NCC 0.500→0.889）
- 1-2.tif: 旧87.8% → 新94.39%（NCC 0.767→0.893）
- 1-3.tif: 旧87.5% → 新94.25%（NCC 0.835→0.893）

## conclusion_100percent
各フレームの平均輝度・標準偏差はほぼ同一（差0.3-0.5階調）で系統的な明るさズレなし。剛体変換で説明できる位置ズレはECCで解消済み。残る約6%の不一致は撮像ノイズ＋DNA/SAM成長過程での試料自体の実変化に由来と推定。無理に100%を追うとデータを歪めるため、現在値を現実的な達成上限として採用し終了。

## changed_files
- register_images.py: ECCベースに置き換え（in-place更新）
- register_images_v2.py: 最新版を別名でも追加保存

## relation_to_antigravity_version
Antigravity版（PC-alignment-anti、本採用パイプライン）はピラー座標のICPマッチングで「マッチ率（距離≤1.5px）」を評価。Claude Code版はTIFF画像そのものが対象のサブ／参照用スクリプトのため、ピラー検出ではなく画像全体の輝度相関（NCC/ECC）ベースの一致率を独自定義して評価した。
