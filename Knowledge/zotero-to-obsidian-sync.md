## Zotero論文の自動Obsidian同期方法

### 概要
Zoteroライブラリの全論文をMarkdown形式でObsidian Vaultに自動md化する仕組み

### 仕組み
- Zotero本体: 406件（論文386件 + 添付ファイル等20件）
- スクリプト `zotero_to_obsidian.py` がJSONを読込、論文のみを抽出・md化
- 保存先: `G:\マイドライブ\Obsidian Vault\Zotero\`

### JSONエクスポート手順
1. Zoteroを開く
2. `ファイル` → `ライブラリをエクスポート`
3. 形式: **Better CSL JSON** または **Better BibTeX JSON**
4. 保存先: `G:\マイドライブ\Obsidian Vault\zotero-library.json\zotero-library.json`（上書き）

### スクリプト再実行
- 新たに論文を追加したら、JSONをエクスポート後、スクリプトを実行
- 差分の20件が同期されない理由: JSONに含まれるnote・attachmentは論文ではなく、フィルタリングにより除外される

### 確認方法
- Pythonで `json.load()` 後、アイテムをカウント
- フィルタ後の論文数が同期対象

### 参考
- 日付: 2026-06-21
- 関連ファイル: `zotero_to_obsidian.py`
