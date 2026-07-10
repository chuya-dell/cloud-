---
theme: Vaultインデックス・運用ガイド（統合版、常時更新）
status: active
tags: [インデックス, 運用ガイド]
---

# 🧠 Vault インデックス — 運用ガイド（統合版）

> 2026-06-30 統合: CLAUDE.md / Claudeの記憶.md / Claudeのログ.md / INDEX.md の4ファイルをここに一本化。

このページは忠さんの知識管理システムの中枢。新しいセッションを始めたら、まずこのページを読んで全体像を把握すること。

---

## ユーザープロフィール

| 項目 | 内容 |
|---|---|
| 名前 | 忠弥（ただや） |
| 職種 | 博士課程研究者（分析化学・バイオセンシング） |
| 研究テーマ | プラズモニック結晶×5-hmCのデジタルカウント検出 |
| キーワード | 5-hydroxymethylcytosine（5-hmC）、デジタルカウント、プラズモン、cfDNA、がんバイオマーカー |
| 環境（自宅PC） | Windows 11、Python 3.13、Google Drive 5TB、Google AI Pro |
| 環境（研究室PC） | Windows 11、Python 3.11.9 |
| メール | chuya2816@gmail.com |

---

## システム全体の構造

**Notion** = メインUI・正データ。タスク管理・実験ログ・会話記録の一次保存先。claude.aiからも書き込み可能。

**Obsidian**（`G:\マイドライブ\Obsidian Vault`）= 長期保管の倉庫。Notionの内容を定期的にアーカイブ。

**Zotero論文** = Obsidian Vaultの `Zotero/` フォルダに373件のmdファイルとして保存。Notion論文DBにも同期済み。

---

## セッション開始時に必ずやること

1. このページ（INDEX.md）を読む
2. `Preferences/プロフィール・ルール.md` を読む
3. `Mistakes/Mistakes.md` を読んで同じミスを繰り返さない
4. `Daily/` フォルダの最新ファイルで前回の作業内容を把握

## 🔒 憲法: frontmatter必須ルール（2026-07-10制定、例外なし）

**Obsidian Vault内にファイルを新規作成する場合、フォルダを問わず必ずYAML frontmatterを付与する。** 「軽いメモだから後で」は禁止（2026-07-09のボルト整理でKnowledge 137件→61件・Decision 58件→29件の重複統合が発生した反省による）。

最低限のキー: `date` / `theme`（一行要約） / `status` / `tags`。詳細は `claude-memory/note_format_policy.md` 参照。
手動作成時はTemplates/フォルダのテンプレート（`note-template.md`・Daily用は`daily-template.md`）が自動適用される設定済み。

## セッション中・終了時に必ずやること

- **Daily**: 今日やったことを `Daily/YYYY-MM-DD.md` に記録
- **Decision**: 重要な判断・方針を `Decision/` に記録
- **Knowledge**: 新しく得た知識・解決法を `Knowledge/` に記録
- **Mistakes**: ミスや修正点を `Mistakes/Mistakes.md` に追記
- 書き込んだらどこに何を書いたか報告する

---

## 重要フォルダ

| フォルダ | 役割 |
|---|---|
| `Daily/` | 日々の作業ログ |
| `Decision/` | 重要な判断・方針 |
| `Knowledge/` | 知識・解決法 |
| `Mistakes/` | ミス記録（必ず確認） |
| `Projects/` | 研究プロジェクトごとの進捗ログ |
| `Preferences/` | プロフィール・運用ルール |
| `Body/` | 体・筋トレ管理 |
| `Zotero/` | 論文373件（hmC関連多数） |
| `Logs/` | 環境構築ログ |
| `claude-memory/` | Claude記憶用フォルダ（MEMORY.mdが index） |

## Obsidian 書き込みルール

| 内容 | 保存先 |
|---|---|
| 作業ログ・今日の記録 | `Daily/YYYY-MM-DD.md` に追記（新規作成時はfrontmatter必須） |
| 知識・調査メモ・解決法 | `Knowledge/` に新規ファイル（frontmatter必須） |
| 重要な決定・方針 | `Decision/` に新規ファイル（frontmatter必須） |
| AIのミス・指摘 | `Mistakes/Mistakes.md` に追記 |
| 論文関連 | `Zotero/` 参照 |

すべての新規ファイルはfrontmatter必須（上記「🔒 憲法」参照）。

## Notion 書き込みルール

以下の場合のみNotionに記録する：
- 忠さんが後で確認・対応する必要があるタスク
- 期限のあること
- 忠さんへのリマインダー
- ※ iOSのclaude.aiチャット記録のみNotionに書く（iOSからObsidianへ直接書き込みできないため。決定: `Decision/ios-chat-notion-others-obsidian.md`）

---

## Notion 主要ID

| ページ/DB | ID | URL |
|---|---|---|
| 🧠 Claudeのログ（記憶ルートページ） | 386e390406d18132a123e7b658b44b4b | https://app.notion.com/p/386e390406d18132a123e7b658b44b4b |
| 👤 プロフィール・ルール | 386e390406d181d7826bf469a57fdb6f | https://app.notion.com/p/386e390406d181d7826bf469a57fdb6f |
| 📝 Claude会話ログ（一時保管） | 386e390406d181a298eef4243ce1e267 | https://app.notion.com/p/386e390406d181a298eef4243ce1e267 |
| 📅 Daily ログ | 386e390406d181219725f5219c9e4001 | https://app.notion.com/p/386e390406d181219725f5219c9e4001 |
| 💡 Knowledge | 386e390406d181fabc06f76c3c8f9884 | https://app.notion.com/p/386e390406d181fabc06f76c3c8f9884 |
| 📌 Decision | 386e390406d181329967c9ff5b1de844 | https://app.notion.com/p/386e390406d181329967c9ff5b1de844 |
| ⚠️ Mistakes | 386e390406d18143b580f9741d4ef742 | https://app.notion.com/p/386e390406d18143b580f9741d4ef742 |
| 🔬 Projects | 386e390406d1814aa710f0764b4332eb | https://app.notion.com/p/386e390406d1814aa710f0764b4332eb |
| 📚 論文DB（Zotero） | 80075a96e4ed4cc9a86555f6c05403a9 | https://app.notion.com/p/80075a96e4ed4cc9a86555f6c05403a9 |
| 📋 タスク管理DB | f46eaa900f42498d873191f37e85867c | https://app.notion.com/p/f46eaa900f42498d873191f37e85867c |
| 💪 体・筋トレ管理 | 386e390406d18199b6f7f49d13b1d6a9 | https://app.notion.com/p/386e390406d18199b6f7f49d13b1d6a9 |
| 🗒️ ラボノートDB | c38fbca3fc864b38b2a46e004d06069f | https://app.notion.com/p/c38fbca3fc864b38b2a46e004d06069f |

---

## タスク優先度・カテゴリ

| 記号 | 意味 |
|---|---|
| 🔴 高 | 締切あり・直近で着手必須 |
| 🟡 中 | 締切ないが研究・仕事に直結 |
| 🟢 低 | 直結しない・後回し可能 |
| ⚪ 保留 | 判断不要・アイデア段階 |

カテゴリ: 実験 / 解析 / 文献 / 申請書 / 指導 / 環境整備 / その他

## 応答スタイル

- タスクは「雑に投げる」→ Claudeが自動振り分け（優先度・カテゴリ）
- 実績時間は完了後に口頭申告 → ClaudeがNotionとObsidianに記録
- 基本は日本語で応答

---

## 📌 AI運用方針（2026-06-21 決定）

- **Claude** → メイン。会話・Notion管理・論文執筆・研究議論。迷ったらここ。
- **Gemini** → Google Drive / NotebookLM連携専用。Zotero論文373件をNotebookLMに投入済み。文献サーベイはここ。
- **ChatGPT** → GPT-5.6評価中、様子見。基本触らない。
- 3つで同じことをしない。「どのAIで聞くか」で迷う時間をなくす。

---

## 環境設定メモ

- Obsidian Vault実体: `F:\GoogleDrive_local\Obsidian Vault\`（`G:\マイドライブ` はショートカット）
- AI会話ログ: `F:\GoogleDrive_local\AI会話ログ\`
- 作業スクリプト: `F:\GoogleDrive_local\Claude\セッション\`
- Python（研究室PC）: `C:\Users\chuya\AppData\Local\Programs\Python\Python311\python.exe`
- Node.js: `C:\Program Files\nodejs\node.exe`

---

## 修論サマリー（プラズモニック結晶×5-hmC検出）

**著者**: 白石 忠弥（大阪公立大学院 工学研究科）/ 学籍番号: BJF24228
**指導教員**: 久本秀明 教授、遠藤達郎 准教授
**提出**: 令和7年度（令和8年3月）/ 127ページ、全7章
**タイトル**: プラズモニック結晶を用いたヒドロキシメチル化シトシンの迅速・低コストな検出法の開発

- 第1章: 5-hmC（「第6の塩基」）はがん・脳疾患と関連。既存検出法（BS-seq）は高コスト・長時間が課題。
- 第3章: COP製モールド（d:230nm, h:200nm, a:460nm）に金200nm蒸着でPC作製。
- 第4章: バルク屈折率感度 S=490 nm/RIU、R²=0.997。FDTDシミュレーションとLSPR起因を確認。
- 第5章: DTT混合固定化25 mol%でSNP識別達成。
- 第6章: β-GT反応で5-hmC特異的検出。濃度LOD 2.3 nM、混合率LOD 7.2 mol%。APC遺伝子のがん初期（約18%）は検出可能、正常細胞（約6%）はギリギリ検出不可。
- 学会発表: 第84回・第85回分析化学討論会、第18回近畿支部若手夏期セミナー。

詳細な章別サマリーは修論PDFおよびnpj Biosensing投稿用ドラフトを参照。

---

## 完成している環境（2026-06時点）

- Claude Code → Obsidian Vault（MCP/server-filesystem）✅
- claude.ai（ブラウザ・iOS）→ Google Drive MCP経由でObsidian Vaultアクセス✅
- Gemini → Google Drive参照✅
- Zotero → Vault md化済み（373件）✅
- 研究室PC → Obsidian Vault MCP接続✅

## 残タスク

- gemini.google.comのDrive直接検索（インデックス待ち）
- Mac環境構築
- NotebookLM連携

---

## 過去ログアーカイブ（旧4ファイルより集約・要約）

過去の詳細な会話ログ・ゼミ議論・FDTD作業ログは `Daily/` および `Projects/` の該当日付ファイルを正とする。以下は統合前の旧ファイルに残っていた主要な記録の要約。

- **2026-06-20**: Google Drive上のClaude関連ファイル一元管理を決定（`Decision/directory-consolidation-decision.md`）。NotebookLMセットアップを次アクションに設定。
- **2026-06-21**: AI運用方針（Claude/Gemini/ChatGPT役割分担）を決定。研究室PC環境構築を最優先タスクに設定。Googleカレンダー運用ルール確定（`Decision/google-calendar-rules-adoption.md`）。修論PDF確認。
- **2026-06-22**: SAM試料調製・プレシピテーション・JASSO書類提出完了。SAM形成確認テストは機器トラブルで未実施。ゼミにて久本先生からDNA固定手法（ジャブ漬け）に厳しい指摘、ピラー上面選択的固定が必須と方針決定。コンタクトプリンティング（転写法）を提案される。
- **2026-06-23**: ピラー上部選択的DNA固定化の文献調査プロンプト設計。Deep Research活用方針。
- **2026-06-24**: FDTDシミュレーション（LumericalのAnalysis Groupスクリプト）改善。µm単位化、`adduserprop`増殖バグ修正。リポジトリ `chuya-dell/fdtd-nha-100-round`。
- **2026-06-27以降**: PC環境・ディスプレイ構成整理、デジタルカウントのスループット問題対策案検討、ピラー上部選択的固定化は乾式コンタクト転写（APTES-glass donor）方式に決定。

---

## このページの運用ルール

- 作業完了時・節目に自動でObsidianに書き込む
- 書き込んだらどこに何を書いたか報告する
- このINDEX.mdの「最近の作業」「残タスク」は随時更新する
