## Obsidian Remotely SaveプラグインでDropbox同期を設定する方法

### 概要
ObsidianのRemotely Saveプラグインを使って、PC側のVaultをDropboxに同期し、iPhone側からアクセスする方法。Google DriveなどのメインVaultをDropbox経由でiPhoneに持ち出す構成。

### 詳細

#### 前提条件
- PC: Obsidian + Remotely Saveプラグイン（コミュニティプラグイン）
- iPhone: Obsidian + Remotely Saveプラグイン
- Dropboxアカウント（無料2GBで十分）

#### PC側設定
1. Obsidian → 左下の歯車（設定）
2. コミュニティプラグイン → 「Remotely Save」を検索・インストール
3. Remotely Saveプラグイン設定を開く
4. 「Remote Service」を「Dropbox」に選択
5. 「Auth」ボタンでDropboxログイン・認証
6. 設定画面で「Check Connectivity」をクリックして接続確認
7. 認証済み後、自動的に `/Apps/remotely-save/Obsidian Vault` にアップロード先が設定される

#### iPhone側設定
1. iPhoneにObsidianをインストール
2. Obsidian → 設定 → コミュニティプラグイン → Remotely Save をインストール
3. Remotely Saveで「Remote Service」を「Dropbox」に設定
4. 「Auth」でDropbox認証
5. VaultをDropboxの `/Apps/remotely-save/Obsidian Vault` フォルダに指定

#### 同期実行方法
- PC: コマンドパレット（Ctrl+P）→ 「Remotely Save: start sync」でDropboxにアップロード
- iPhone: 右下の雲アイコン（↑↓）をタップ、またはコマンドパレット → 「Remotely Save」で同期

### トラブルシューティング

#### エラー: too_many_write_operations
**原因**: Dropboxのレート制限。大量ファイル（特にZoteroなど）を一度にアップロードしようとすると429エラー

**解決策**:
1. 「Regex Of Paths To Ignore」に不要なフォルダを追加
   - 例: `Zotero/.*` （Zoteroフォルダ全体除外）
   - 例: `Templates/zotero-template\.md` （特定ファイル除外）
2. 数分待ってから再度同期実行

#### ファイルが同期されない
- iPhone側のVaultがDropboxの正しいフォルダを指しているか確認
- PC側で一度「Run Once」または同期実行してDropboxにアップロード
- iPhone側でしばらく待ってから同期実行

### Regex除外例
```
.*\.canvas
.*\.base
Zotero/.*
zotero-library.json
Templates/zotero-template\.md
```

### 参考
- 日付: 2026-06-20
- Remotely Save: PC・iPhone両方のObsidianで対応
- Dropbox無料容量: 2GBで小規模Obsidian Vault十分（Zoteroなど除外時）
