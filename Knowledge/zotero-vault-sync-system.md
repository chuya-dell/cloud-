## Zotero×Obsidian自動同期システム

### 概要
ZoteroライブラリをObsidian Vaultに自動的にマークダウン化して保管・検索できるシステム

### 詳細

**実装状況**
- スクリプト: `zotero_to_obsidian.py`
- 対象: 406件のZoteroアイテム（論文386件 + 添付ファイル等20件）
- 出力先: `G:\マイドライブ\Obsidian Vault\Zotero\`
- 同期状況: 完全同期済み（386件全て）

**JSONエクスポート手順**
1. Zoteroを開く
2. ファイル → ライブラリをエクスポート
3. 形式: Better CSL JSON または Better BibTeX JSON
4. 保存先: `G:\マイドライブ\Obsidian Vault\zotero-library.json`（上書き）
5. スクリプト再実行で差分更新

**アイテム分類**
- 論文本体: 386件（mdファイル化対象）
- note・attachment: 20件（ファイル添付物）

**現在のコレクション統計**
- plasmon関連: 21件
- hmC関連: 多数（メインテーマ）

### 参考
- 日付: 2026-06-21
