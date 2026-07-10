---
date: 2026-07-09
theme: FDTDで下に凸な円柱（バルジ形状）構造をLumericalで作成
tags: [FDTD, Lumerical, 構造定義, スクリプト]
status: 検討中（構造が消える問題は未解決の可能性あり）
---

## params
- ソフトウェア: Lumerical FDTD
- 目的: 下に凸な二次関数状（樽型・砂時計型）の円柱構造を作成
- 元テンプレート: Lumerical公式サンプル「Hexagonal lattice PC array」スクリプトをベースに改変
- 実装方針: 単一円柱を高さ方向にnum_layers枚の薄い円盤（addcircle）に分割し、各層のzに応じて半径を二次関数的に変化させる（多層近似）
- 初期パラメータ案:
  - z_min = 0, z_max = 0.2 μm, r_end = 0.05 μm, r_middle = 0.1 μm, num_layers = 20
- 強調版パラメータ案（変化を目視確認しやすくするため）:
  - z_min = 0, z_max = 0.5 μm, r_end = 0.02 μm, r_middle = 0.15 μm, num_layers = 40
  - 半径分布式を (1 - normalized_z^2) から (1 - normalized_z^4) に変更しより急峻な湾曲に

## result
- スクリプトの雛形は複数バージョン作成（Meep版→Lumerical版→六角格子対応版→単一円柱簡略版→強調版）
- 「structures > circle > script」という操作パスはLumerical標準GUIには存在しないことを指摘し、スクリプトエディタ（File > New > Script File）またはオブジェクトのScriptタブでの実行を提案
- deleteall; の存在により既存構造が消える問題が発生 → コメントアウトを提案したが、忠弥側での動作確認は未完了
- properties定義の要否について: 単純作成ならスクリプトエディタ直接実行で十分、再利用可能なカスタムオブジェクトにする場合のみpropertiesでのパラメータ化が必要、と回答

## open_questions
- 強調版パラメータでLumerical上に構造が実際に描画されたか未確認
- deleteall;除去後も構造が消える場合、原因が別にある可能性（層のz spanとz位置の重なり、材料指定エラー等）は未検証
- addcircleの積層方式がLumericalのメッシュ・境界条件上、意図通りの滑らかな曲面として扱われるか（角の分解能誤差）は未検証

## anomalies
- （報告なし。忠弥から「構造が消える」との報告のみで、エラーメッセージ等の詳細情報は未取得）

## time_log
- 2026-07-09: 一連のチャットでの検討・スクリプト試作（本記録は会話ログのまとめ）
