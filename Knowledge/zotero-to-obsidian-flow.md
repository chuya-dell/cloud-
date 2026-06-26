## Zotero論文のVault移行フロー

### 概要
Zoteroの406件（論文386件 + 添付ファイル20件）をObsidian VaultにMarkdown化する自動化システム。

### 現状
- **Zotero総件数**: 406件
  - 論文本体: 386件
  - note・attachment: 20件
- **Vault移行済み**: 386件のmdファイル完全同期
- **含有テーマ**: hmC関連が主（plasmonは21件）

### 移行スクリプト
- `zotero_to_obsidian.py`
- 入力: `zotero-library.json` (Better BibTeX形式)
- 出力: `Obsidian Vault/Zotero/` フォルダ

### JSONエクスポート手順
1. Zoteroを開く
2. `ファイル` → `ライブラリをエクスポート`
3. 形式: **Better CSL JSON** または **Better BibTeX JSON**
4. 保存先: `G:\マイドライブ\Obsidian Vault\zotero-library.json\zotero-library.json`
5. スクリプト再実行でVaultを更新

### 新規論文追加フロー
1. Zoteroで新規論文を追加
2. JSONをエクスポート（上書き）
3. `zotero_to_obsidian.py` を実行
4. 新しいmdファイルがVaultに追加される

### 参考
- 日付: 2026-06-21
