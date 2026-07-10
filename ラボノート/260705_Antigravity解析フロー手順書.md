---
date: 2026-07-05
theme: Antigravity解析フロー手順書
tags: [digital-counting, antigravity, alignment, image-registration, procedure]
status: reference
---

# 概要

新しい実験データ(画像)が得られた際に、Antigravityパイプラインで解析を行うための実行手順。全プログラムは引数で指定した「データフォルダ(入力フォルダ)」を基準に動作し、そのフォルダ内部に解析結果(Excel等)を自動出力する。フォルダ単位の非破壊設計のため、以前の解析データが上書きされる心配はない。

# 前提

- 実行環境: 各自のPCのコマンドプロンプト / PowerShell
- 出力先: 指定した入力フォルダ内部(自動生成)

# フロー1: ピラー認識解析版(ピラー単位の輝度差解析)

## Step 1. 位置合わせ(アライメント)

```bash
python run_batch_alignment.py --input-dir "G:/マイドライブ/新しい実験データ/df" --output-dir "G:/マイドライブ/新しい実験データ/foranti_new" --method peak --min-dist 3 --threshold 0.2
```

- `--input-dir`: 元画像フォルダ(df)
- `--output-dir`: アライメント結果の出力先(新規フォルダ名を指定)
- `--method peak`: ピーク検出法
- `--min-dist 3`, `--threshold 0.2`: ピーク検出パラメータ

## Step 2. 共通ピラー間の輝度変化量算出(post - pre)

```bash
python run_intensity_comparison.py --data-dir "G:/マイドライブ/新しい実験データ/foranti_new" --output-dir "G:/マイドライブ/新しい実験データ/foranti_new"
```

- Step 1の出力フォルダを`--data-dir`に指定

## Step 3. Excelデータ集計出力

```bash
python export_intensity_excel.py "G:/マイドライブ/新しい実験データ/foranti_new"
```

- 指定フォルダ内に `pillar_intensity_analysis.xlsx` が生成される

# フロー2: グリッド差分解析版(ピクセル差分・6.29pxグリッド解析)

## Step 1. 画像アライメントワープ + グリッド差分解析(傷除外・ヒートマップ作成)

```bash
python run_grid_difference_analysis.py --img-dir "G:/マイドライブ/新しい実験データ/df" --pillar-dir "G:/マイドライブ/新しい実験データ/foranti_new"
```

- `--img-dir`: 元画像フォルダ
- `--pillar-dir`: フロー1 Step1で出力したピラーアライメント結果フォルダ
- 指定ピラーフォルダ直下に `grid_analysis` フォルダが自動生成され、各ペアのCSVとJETカラーヒートマップ画像(傷部分は黒マスク)が出力される

## Step 2. Excelデータ統合出力

```bash
python export_grid_intensity_excel.py "G:/マイドライブ/新しい実験データ/foranti_new/grid_analysis"
```

- `grid_analysis` フォルダを指定
- フォルダ内に `grid_intensity_analysis.xlsx` が生成される

# 依存関係の注意

- フロー2はフロー1のStep1(ピラーアライメント結果)に依存する一方向の流れ
- 全プログラムはフォルダ基準・非破壊設計のため、以前の解析データの上書き消失は発生しない

# 実行結果ログ(2026-07-05)

- ピラーID衝突バグ(プレ側)が解消され、正常に生成されることを確認
- 出力先:
  - `F:/GoogleDrive_local/1.実験データ_gdrive/5.生データ D/260704 sam 位置合わせ test/foranti/pillar_intensity_analysis.xlsx`
  - `F:/GoogleDrive_local/1.実験データ_gdrive/5.生データ D/260704 sam 位置合わせ test/foranti/grid_analysis/grid_intensity_analysis.xlsx`
- グリッド差分解析: 傷除外マスク適用済み、有効N数テーブル(縦書き)がN列・O列に格納された最新版
- GitHubリポジトリ `https://github.com/chuya-dell/PC-alignment-anti.git` に、プログラム一式とREADME.mdを引数受け取り型の最新仕様で同期完了

# 別PCでの実行手順(2026-07-05追記)

GitHubに公開済みのため、別PCでも以下の3ステップで同じ解析が実行可能。

## ステップ1: Pythonインストール(初回のみ)

- Python公式サイト等からインストーラーを取得
- インストール時に「Add Python to PATH」に必ずチェックを入れる

## ステップ2: 必要なライブラリのインストール

```bash
pip install numpy pandas opencv-python openpyxl scipy tqdm
```

## ステップ3: プログラムのダウンロード

- 方法A(推奨・Gitがある場合):
```bash
git clone https://github.com/chuya-dell/PC-alignment-anti.git
```
- 方法B: GitHubページ(`https://github.com/chuya-dell/PC-alignment-anti`)の「Code」→「Download ZIP」から取得し解凍

## 実行方法

解凍/cloneしたフォルダ内でコマンドプロンプトを開き、通常通りコマンドを実行するだけ。

```bash
python run_grid_difference_analysis.py --img-dir "新しいPCでの画像フォルダのパス" --pillar-dir "アライメント出力先フォルダのパス"
python export_grid_intensity_excel.py "アライメント出力先フォルダのパス/grid_analysis"
```

- 新PC上のGoogleドライブローカルフォルダ等に対しても問題なくExcel・ヒートマップ画像が自動生成される

# 別チャットのAI(Antigravity等)へ投げる標準プロンプト(2026-07-06追記)

「アンチに投げるプロンプト何だっけ」と聞かれた際に返す固定テンプレート。パス部分(df/foranti)は都度の実験フォルダに合わせて埋めて渡す。

```markdown
プラズモニック結晶の位置合わせと輝度変化解析を行いたいです。
解析用のPythonプログラムと詳しい動作手順は、以下のGitHubリポジトリにすべて公開されています。
https://github.com/chuya-dell/PC-alignment-anti.git
【依頼事項】
1. 上記のリポジトリをクローン(またはダウンロード)して、中にある README.md を読み込み、プログラムの仕組みと実行方法を把握してください。
2. 今回解析を行いたいフォルダのパスは以下の通りです。
   ・画像の入った入力フォルダ (df) : 「※ここに解析したい画像フォルダのパスを貼り付けてください」
   ・解析結果の出力先フォルダ (foranti) : 「※ここに出力先フォルダのパスを貼り付けてください」
3. README.md の手順に従って、アライメントの実行、輝度変化量の計算、グリッド解析(傷除外・ヒートマップ作成)、およびExcelレポート出力までを順番に実行してください。
```

# 関連

- 対比: Claude Code側 (`claude/batch-image-registration-qe4cp7`, scratch-landmark ECC) は47/64ペアで難航中
- Antigravity側 (PC-alignment-anti, ICP座標アライメント) は64/64ペア完了済み、RMSE平均0.97px、match rate 21.4%(ランダムベースライン比較は未実施)
