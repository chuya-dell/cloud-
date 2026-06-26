## Obsidian マルチデバイス同期（Google Drive + Dropbox）構成

### 概要
Obsidian Vault をGoogle Drive（PC）とDropbox（スマホ同期用）で管理する構成。
メイン作業はPC（Google Drive自動同期）、サブはiPhone（Dropbox経由同期）

### 詳細

#### ステップ1: Vaultの Google Drive 移行
- **ツール**: Google Drive for Desktop（旧Backup and Sync）
- **方法**: 
  1. `C:\Users\<user>\Documents\Obsidian Vault` をコピー
  2. `G:\マイドライブ\Obsidian Vault` に貼り付け
  3. Obsidian 左下「vault名」→「保管庫を管理」→ Google Drive内のVaultを選択
- **注意**: `.obsidian/` フォルダ（設定・プラグイン）も含めて移動

#### ステップ2: PC側 Remotely Save + Dropbox 設定
- **プラグイン**: Remotely Save（無料版で Dropbox対応）
- **設定手順**:
  1. Obsidian設定 → コミュニティプラグイン → 「Remotely Save」検索・インストール
  2. Remotely Save設定 → 「Remote Service」を「Dropbox」に変更
  3. 「Auth」ボタン → ブラウザで Dropbox認証（アクセス許可）
  4. 「Schedule For Auto Run」→ 「every 30 minutes」に設定
  5. 左サイドバー同期ボタンで最初の同期実行

- **除外設定**: Dropbox無料プランの制限対応
  - 「Regex Of Paths To Ignore」に以下を設定:
    ```
    .*\.canvas$
    .*\.base$
    ```
  - (`.canvas` `.base` ファイルはスキップ)

#### ステップ3: iPhone側 Obsidian + Remotely Save 設定
1. iPhone App Store から「Obsidian」インストール
2. iPhone App Store から「Dropbox」インストール
3. Obsidian で新規 Vault 作成（名前例：`Obsidian Vault`）
4. Obsidian設定 → コミュニティプラグイン → 「Remotely Save」インストール
5. Remotely Save設定:
   - 「Remote Service」→「Dropbox」
   - 「Auth」→ Dropbox認証
   - **重要**: 「Change The Remote Base Directory」を PC と同じ「Obsidian Vault」に統一
6. 同期実行（左サイドバーの丸い矢印アイコン）

#### ファイル同期構成
```
G:\マイドライブ\Obsidian Vault
       ↓ Remotely Save（PC）
Dropbox
       ↓ Remotely Save（iPhone）
iPhone Obsidian
```

#### 容量管理
- **Dropbox無料**: 2GB（テキストノートなら数万ファイル分）
- **超過時**: iPhone同期が停止するだけ。PC作業は無影響
- **容量参考**: `.md`ファイルは通常1ファイル数KB～数十KB

### 設定上の注意点

1. **Base Directory名の統一**
   - PC側: `Settings` → `Remotely Save` → 表示される Base Directory を確認
   - iPhone側: 同じ名前に統一（スペース位置・大文字小文字も一致させる）

2. **ファイル形式の対応**
   - Dropbox無料で対応: `.md`（マークダウン）
   - 除外推奨: `.canvas`（キャンバス）、`.base`（データベース）

3. **有料版との違い**
   - Remotely Save PRO（月$8程度）: Google Drive直接対応
   - 現在の構成: Google Drive（PC）+ Dropbox（スマホ）の二層構成

### 参考
- 日付: 2026-06-20
