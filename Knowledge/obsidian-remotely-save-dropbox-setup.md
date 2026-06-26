## Remotely Save + Dropbox で iPhone Obsidian同期（Google Drive マスター）

### 概要
PC側のVaultがGoogle Driveにある場合、iPhoneのObsidianはGoogle Driveを直接サポートしていないため、Remotely SaveプラグインでDropbox経由でミラーリングして同期する方法。

### 構成
- **PC（マスター）**: Google Drive上の Obsidian Vault
- **PC**: Remotely Saveプラグイン → Dropboxに同期
- **iPhone**: Obsidianアプリ → Dropbox上のVaultを参照

### PC側設定
1. Obsidian → コミュニティプラグイン → 「Remotely Save」をインストール
2. 設定画面で「Remote Service」を「Dropbox」に選択
3. 「Auth」ボタンをクリックしてDropboxアカウントで認証
4. 同期先: `/Apps/remotely-save/Obsidian Vault`（自動設定）
5. 「Sync On Save」オンにすると自動同期（推奨）
6. または手動で「Remotely Save: start sync」コマンドを実行

### iPhone側設定
1. Obsidianアプリ → Vault選択
2. Vault保存先を「Dropbox」に指定
3. `/Apps/remotely-save/Obsidian Vault` フォルダを選択
4. Remotely Saveプラグインもインストール → Dropbox認証
5. 同期ボタン（雲のアイコン）を押して同期実行

### 同期の検証
- PC: 「Remotely Save: start sync」実行 → ステータス「Successfully synced」確認
- iPhone: 同期ボタン押して Daily, Knowledge, Mistakesなどのフォルダが表示されることを確認

### Dropboxレートリミットエラーへの対応
**エラー**: `too_many_write_operations`（429）
**原因**: 大量ファイル（300+）を一度にアップロードしようとしてDropboxのレート制限に引っかかる

**解決策**: Remotely Saveの除外リスト（Regex Of Paths To Ignore）を設定

### 除外リスト設定例
```
.*\.canvas
.*\.base
Zotero/.*
zotero-library.json
Templates/zotero-template\.md
```

### Check Connectivity
Dropbox接続確認: 「Check Connectivity」ボタン押下 → 「Great! We can connect to Dropbox!」が表示されればOK

### 参考
- 日付: 2026-06-20
- Remotely Save: PCとiPhoneの両デバイスにインストール必須
- iPhone Obsidianの制限: Google Drive直接非対応のため、このDropbox経由の方法が必要
