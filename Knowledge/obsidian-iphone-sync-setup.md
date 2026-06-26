## iPhoneのObsidianをPC（Google Drive）と同期する方法

### 概要
iPhoneのObsidianはGoogle Driveを直接サポートしていないため、Remotely SaveプラグインとDropboxを使ってPC側のVaultをミラーリングする方法。

### 詳細

#### 対応しているクラウドサービス（iOSネイティブ）
- iCloud
- Dropbox
- OneDrive
- Obsidian Sync（有料）

#### 非対応
- Google Drive（直接接続不可）

#### 実装方法: Remotely Save + Dropbox

**PC側の設定:**
1. Obsidian → コミュニティプラグイン → 「Remotely Save」をインストール
2. 設定で「Remote Service」を「Dropbox」に選択
3. 「Auth」ボタンでDropboxアカウントと認証
4. 同期先は自動で `/Apps/remotely-save/Obsidian Vault` に設定される
5. 必要に応じて除外ファイルをRegex設定で指定

**iPhone側の設定:**
1. Obsidianアプリ → 既存のVault選択
2. 保存先を「Dropbox」に指定
3. コミュニティプラグイン → Remotely Save をインストール
4. Dropbox認証（同じアカウント）
5. 同期先をPC側と同じ `/Apps/remotely-save/Obsidian Vault` に設定

**同期実行:**
- 手動同期: PC側はコマンドパレット「Remotely Save: start sync」
- iPhone側: リボンの同期アイコン（↑↓）またはコマンドパレットから実行

#### トラブルシューティング

**レート制限エラー（too_many_write_operations）**
- 原因: Zoteroなど大量ファイルの一括アップロード時にDropboxのAPI制限に引っかかる
- 対応: 除外リストに追加
  ```
  Zotero/.*
  Templates/zotero-template\.md
  zotero-library.json
  ```
- Regex設定場所: Remotely Save設定 → 「Regex Of Paths To Ignore」

**ファイルが反映されない**
- 「Sync On Save」がオフになっていないか確認
- PC側で手動同期実行後、iPhone側でも同期実行が必要

### 参考
- 日付: 2026-06-20
