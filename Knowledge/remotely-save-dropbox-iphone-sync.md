## Remotely Save で Dropbox 経由の iPhone 同期設定

### 概要
Obsidian PRO版のSync（月$4〜）ではなく、無料のRemotely SaveプラグインとDropbox（無料2GB）を使ってPC-iPhone間でノートを同期する方法。

### 詳細

#### 同期フロー
```
PC（Google Drive上のObsidian Vault）
  ↕ Remotely Save で定期同期
Dropbox（無料、2GB）← iPhone との橋渡し
  ↕ Remotely Save で定期同期
iPhone（Obsidian アプリ）
```

#### PC側の設定
1. Obsidianで Remotely Save プラグインをインストール・有効化
2. 設定画面で「Choose A Remote Service」を「Dropbox」に変更
3. 「Auth」ボタンをクリック → コピーされたURLをブラウザで開く
4. Dropboxのログイン → 許可
5. 認証完了後、「Schedule For Auto Run」を「every 30 minutes」に設定
6. 「Regex Of Paths To Ignore」で除外ファイルを設定
   - 例：`\.canvas$` と `\.base$` を除外（Dropbox無料プランの制限対応）
7. 最初の同期を実行（丸い矢印アイコンをクリック）

#### iPhone側の設定
1. App StoreからObsidianアプリをインストール
2. 新しいVaultを作成（「Create new vault」→ 名前は「Obsidian Vault」）
3. 設定 → 「コミュニティプラグイン」 → 「有効化」
4. 「閲覧」で「Remotely Save」を検索 → インストール → 有効化
5. Remotely Save設定で「Choose A Remote Service」を「Dropbox」に選択
6. 「Auth」をタップ → Safariで開かれたページでログイン → 許可
7. 「Change The Remote Base Directory」で PC側と同じフォルダ名を指定（例：「Obsidian Vault」）
   - **注意**：スペースやタイプミスに注意。PC側と完全に一致させる必要がある
8. 同期ボタンをタップして初回同期を実行

#### トラブルシューティング
- **ファイルが表示されない場合**：PC側とiPhone側の「Remote Base Directory」が一致しているか確認
- **同期エラー（.canvas / .base）**：これらはDropbox無料プランで同期不可。「Regex Of
