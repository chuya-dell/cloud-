## Obsidian Vault を Google Drive に移行する手順

### 概要
Obsidianの.obsidian/フォルダ（設定・プラグイン）を含むVault全体をGoogle Drive上に移動し、Google Drive for Desktopで自動同期させる手順。

### 詳細

#### 準備
- Google Drive for Desktop（旧Backup and Sync）がPC側にインストール済み
- Google Drive上に G:\マイドライブ\ がマウントされている状態

#### ステップ1：Vaultをコピー
1. Obsidianを完全に閉じる（ファイルが壊れる可能性があるため）
2. 既存のVault（例：C:\Users\[username]\Documents\Obsidian Vault）全体をコピー
3. G:\マイドライブ\ 以下に貼り付け
4. コピー成功後、元のローカルVaultはバックアップとして保持

#### ステップ2：Obsidianでフォルダを再指定
1. Obsidianを起動
2. 左下の「Vault名」をクリック
3. 「保管庫を管理...」または「Open another vault」から「Open folder as vault」を選択
4. G:\マイドライブ\Obsidian Vault を指定
5. Vaultが切り替わる

#### 確認ポイント
- 設定ファイル「.obsidian/obsidian.json」で "open":true が新Vaultのパスに対して設定されているか
- 移行後、NotesやAttachmentsが正常に表示されるか

### 参考
- 日付: 2026-06-20
