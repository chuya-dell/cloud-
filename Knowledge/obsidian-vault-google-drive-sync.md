## Obsidian VaultのGoogle Drive同期方法と多端末運用

### 概要
Obsidianの知識ベース（Vault）をGoogle Drive上に配置することで、複数デバイスとAIツールからの統一的なアクセスを実現する構成。OneDriveからの移行を想定した設定方法。

### 詳細

#### ステップ1: VaultをGoogle Driveに移行
1. **Google Drive for Desktop** をインストール
   - Googleの公式ツール（旧Backup and Sync）
   - インストール完了後、`G:\マイドライブ\` がローカルフォルダとして利用可能

2. **VaultフォルダをGoogle Drive配下に移動**
   - 既存Vault（例：`D:\Obsidian Vault`）を `G:\マイドライブ\Obsidian Vault` に移動
   - `.obsidian/` フォルダ（設定・プラグイン）も含めて移動することが必須

3. **Obsidianで再指定**
   - Obsidian起動 → 「Open folder as vault」
   - `G:\マイドライブ\Obsidian Vault` を選択して完了

#### ステップ2: マルチデバイス同期構成

| デバイス | 方法 | 同期方式 | コスト |
|---------|------|---------|--------|
| PC（Windows/Mac） | Google Drive for Desktop | 自動双方向同期 | 無料 |
| Android | Obsidian公式アプリ + Remotely Saveプラグイン | Google Drive経由の手動・自動同期 | 無料 |
| iOS/iPad | Obsidian公式アプリ + Remotely Saveプラグイン | Google Drive経由の手動・自動同期 | 無料 |

#### ステップ3: Remotely Save設定（スマホ・タブレット）
- Obsidianアプリ内で「Remotely Save」プラグインをインストール
- Google Driveアカウントを認証
- 同期方向（アップロード、ダウンロード、双方向）を設定

#### 注意点
- OneDrive契約の終了予定がある場合、早めにGoogle Drive移行を進めることが重要
- `.obsidian/` フォルダをコピーするとプラグイン設定も継承されるため、新デバイスでの再構築が不要
- Google Drive for Desktopは「Stream」モードではなく「ミラー」モードで運用すると安定

### 参考
- 日付: 2026-06-20
