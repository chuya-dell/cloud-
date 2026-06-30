# 📅 Daily ログ

## 使い方
Claudeとの作業記録・会話ログをここに日付ごとに追記する。
**新しいログは先頭に挿入**（新しい順で表示）。

---

## 2026-06-27

### YouTube動画19本 トランスクリプト収集・外部脳活用方針まとめ
- YouTube動画A〜S（計19本）の要点を `Knowledge/AI外部脳としてのObsidian活用方針.md` に蓄積
- 19本を通じた収束点を整理し、忠さんの2つの痛みへの答えを明文化

**2つの痛みへの結論**
- 痛み1（トークン消費が心配）→ `pip install notebooklm-mcp-cli && nlm login` の2コマンドでNotebookLMにリサーチをアウトソース
- 痛み2（claude.aiからObsidianが見えない）→ Claude Codeセッションが根本解決。claude.aiはフロントエンド（外出先）と割り切る
- 二重管理問題 → 静的情報→Obsidian、動的情報→Notionと役割明文化

**次回TODO**
- [ ] NotebookLM連携実装を試す（2コマンドのみ）
- [ ] 静的/動的情報の役割分担をCLAUDE.mdに明文化するか決める
- [ ] AI生成物フォルダをIdeaverseから分離するか決める

---

## 2026-06-26

### Notion/Obsidian体制変更
- **Notionをメイン・正データに変更、Obsidianは長期保管の倉庫に**
- 変更箇所：🧠 Claudeの記憶（メイン）・👤 プロフィール・ルール・📝 Claude会話ログ・📌 Decision の各ページを更新

### Dailyログ整備
- 6/23〜6/25分のDailyログが未記録だったため遡って追記
- Dailyログを新しい順（先頭挿入）に再構成

---

## 2026-06-25

### FDTDシミュレーション
- Lumerical Analysis Groupセットアップスクリプト改善
  - スクリプトをµm単位に変更（旧：4.6e-07 → 新：0.46）
  - `adduserprop`実行時にa2・D2等が増殖するバグ修正（`getnamed`で存在確認し初回のみ実行）
  - `deleteall`を冒頭に移動
  - README.mdをGitHubリポジトリに追加
- リポジトリ：`chuya-dell/fdtd-nha-100-round`、ブランチ：`claude/fervent-tesla-0rw769`

### Notion整理
- SAM形成確認テスト・富本奨学会提出の2タスクを完了✅＋ステータス「完了」に更新

---

## 2026-06-24

### 文献調査
- 金ナノピラーspatioselective修飾の文献調査（Perplexity・Claude・Gemini 3AI比較）
- **結論：Au-thiol＋金ナノピラー上部のみの化学的spatioselective修飾を満たす論文はChattaway 2019のみ**
- DNA固定化まで含めた「上部のみ修飾」の金ナノピラー論文は現状ゼロ → 新規性を主張できる
- 引用の中核2本確定：Chattaway 2019（概念根拠）＋Li 2021（デジタル単分子計数の構造）
- AI評価：Perplexityが最も正確。Claudeは一部混同あり。Geminiは条件を満たさない論文を満たすように記述する傾向あり

### FDTDシミュレーション
- ナノホールアレイ形状の軽量化検討（round-3）
- N=32→8でオブジェクト数455→119に削減
- addcustomの「Custom」タブ（equation + revolution）で解析的曲面定義の可能性を調査

---

## 2026-06-23

### 実験
- SAM形成確認テスト：機器トラブルにより未実施（前日からの持ち越し）
- 富本奨学会 申請書類提出：✅ 完了（締切日）

### 研究議論・検討
- ピラー上部選択的DNA固定化の手法検討（Claude会話）
- **採用案確定：乾燥系接触転写（APTES修飾ガラスをドナーとしてDNAのみAu-S結合で転写）**
  - 界面強度差の設計：APTES-DNA静電相互作用（弱）→ Au-S結合（強、~40 kcal/mol）
  - 転写後すぐ緩衝液に浸漬してDNA変性を回避
  - 懸念点：接触均一性、側面への非特異接触、転写確認（蛍光標識DNA）
- スケジュール判断：7/8アブスト〆切には間に合わない → 現行jab-zuke法でデータ取得継続、接触転写は並行検討

---

## 2026-06-22

### 研究室PC環境セットアップ完了
- Obsidian Vault確認: `F:\GoogleDrive_local\Obsidian Vault\` ✅
- CLAUDE.md更新（NotionID全件・優先タスク・プロフィール） ✅
- obsidian-vault MCP接続・読み書き確認 ✅
- Node.js: `C:\Program Files\nodejs\node.exe` ✅
- Python 3.13.14インストール ✅
- anthropic / json-repair インストール ✅
- Claude会話自動保存タスク（毎日12時） ✅
- ProcessLogsToObsidian（ログオン時・動作確認済み） ✅
- config.env（Drive経由で共有済み） ✅
- Git 2.54.0 ✅

### Mac環境構築手順を保存
- Notion「💡 Knowledge」に「💻 Mac環境構築手順」ページ作成済み

### 次回やること（TODO）
- [ ] Mac環境構築（`whoami` でMacユーザー名確認）
- [ ] 年会要旨執筆（7/8締切）
- [ ] MNC対応（7/1）
- [ ] JAIMA発表準備（7/3）

---

## 2026-06-21

### Notionアプリが起動しない問題を解決
- 原因: Intel 13th Gen + ElectronのGPUクラッシュ
- 解決: `Notion.exe --disable-gpu --disable-gpu-compositing --use-gl=swiftshader --no-sandbox`

### claude.ai→Obsidian接続完了
- obsidian-mcp-http.js（port 8765）+ ngrok固定URL: `https://styling-shakily-underfed.ngrok-free.dev`
- スタートアップ自動起動登録済み

### タスク管理システム確定
- 優先度: 🔴締切あり / 🟡研究直結 / 🟢後回し可 / ⚪保留
- カテゴリ: 研究 / 申請書 / 指導 / 環境整備 / その他
- 実績時間は完了時に口頭申告 → Notion＋Obsidianに記録

### Notion知識管理システム整備
- Zotero論文373件をNotion論文DBにインポート完了
- トップレベルを「タスク管理・ラボノート・🧠 Claudeの記憶」の3つに整理

### 新規作成
- 👤 プロフィール・ルール
- 💪 体・筋トレ管理（筋トレ週1回・体組成データは後日）
- Obsidian: Body/ フォルダ新規作成

### Googleカレンダー運用ルール確定
- 研究関連 → 実験カレンダー / Tuesday関連 → Tuesdayカレンダー / 個人 → 忠カレンダー
- 特に時間がないもの → 終日 / 開始時間のみ → 0分（開始=終了）
- 通知：全て不要

### 夜セッション：タスクスケジューラ修正
- 誤: `G:\マイドライブ\1.実験データ_gdrive\claud.セッション\`
- 正: `G:\マイドライブ\Claude\セッション\`
- `process_logs_to_obsidian.py`: `item["content"]` KeyErrorバグ修正
- 両タスク正常動作確認済み

---

## 2026-06-20

### 完成したこと
- Claude会話の自動保存（`save_session.py`・タスクスケジューラ毎日12時）
- GeminiからGoogle Drive参照設定（アプリ連携オン）
- Zotero386件をObsidianにmd化（`zotero_to_obsidian.py`）
- Obsidian外部記憶システム構築（Daily/Decision/Knowledge/Mistakes/INDEX.md/CLAUDE.md）
- iPhone同期（Remotely Save + Dropbox）
- 会話ログ→Obsidian自動構造化システム構築（`process_logs_to_obsidian.py`）
- Google Drive内Claude関連ファイルの整理（`Claude/セッション/`・`Claude/AI会話ログ/`）

### 重要な気づき
- Gemini APIはAI Pro契約で無料枠が無効化される → Anthropic APIに切り替え（$5チャージ、数年分）
- GeminiはMarkdownファイルを検索できない（NotebookLM経由が確実）
- AI役割分担：Claude（日常作業・自動化）→ NotebookLM（深い議論・複数ファイル横断）→ Gemini（手動添付参照）

### 環境メモ
- Windows 11、Node.js v24.17.0、Python 3.13
- Obsidian Vault: `G:\マイドライブ\Obsidian Vault`
- MCP設定: `C:\Users\chuya\AppData\Roaming\Claude\claude_desktop_config.json`

### 残タスク（当時）
- [ ] gemini.google.comからのDrive直接検索（インデックス待ち）
- [ ] 別Windows PC環境構築
- [ ] Mac環境構築
- [ ] Zotero新規追加時の更新フロー確立
- [ ] NotebookLM連携
