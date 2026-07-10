---
date: 2026-06-20
theme: iPhone Obsidian同期（Remotely Save + Dropbox経由）
status: resolved
tags: [Obsidian, iPhone, Remotely Save, Dropbox, 同期]
---

## summary
iPhoneのObsidianはGoogle Driveを直接サポートしていない（対応: iCloud/Dropbox/OneDrive/Obsidian Sync有料のみ）ため、無料のRemotely SaveプラグインでDropbox（無料2GB）経由にミラーリングしてPC（Google Drive上のVault）とiPhoneを同期する。Obsidian公式Sync（月$4〜）の代替。2026-06-20時点で設定完了・動作確認済み。

## architecture
```
PC（G:\マイドライブ\Obsidian Vault, Google Drive）
  ↕ Remotely Save
Dropbox（無料2GB、/Apps/remotely-save/Obsidian Vault）
  ↕ Remotely Save
iPhone（Obsidianアプリ）
```

## setup_pc
1. Obsidian → 設定 → コミュニティプラグイン → 「Remotely Save」を検索・インストール・有効化
2. Remote Service を「Dropbox」に選択
3. 「Auth」→ コピーされたURLをブラウザで開きDropboxログイン・許可
4. 「Check Connectivity」で接続確認（"Great! We can connect to Dropbox!"）
5. 同期先は自動設定: `/Apps/remotely-save/Obsidian Vault`
6. 「Schedule For Auto Run」を「every 30 minutes」等に設定、または「Sync On Save」オンで自動同期
7. 除外設定（Regex Of Paths To Ignore、後述）
8. 手動同期: コマンドパレット（Ctrl+P）→「Remotely Save: start sync」

## setup_iphone
1. App StoreからObsidianアプリをインストール
2. 新規Vault作成（例: 「Obsidian Vault」）または既存Vault選択
3. Vault保存先を「Dropbox」に指定
4. 設定 → コミュニティプラグイン有効化 → 「Remotely Save」インストール・有効化
5. Remote Serviceを「Dropbox」に設定 → Auth（Safari経由でログイン・許可、PC側と同一アカウント）
6. 「Change The Remote Base Directory」をPC側と完全一致させる（スペース・タイプミス注意）
7. 同期アイコン（リボンの↑↓）タップ、またはコマンドパレットから「remotely save」検索して同期実行

## exclusion_config
Dropbox無料プランのレート制限・容量対策のため、Remotely Save設定「Regex Of Paths To Ignore」に以下を追加:
```
.*\.canvas
.*\.base
Zotero/.*
zotero-library.json
Templates/zotero-template\.md
```
Zotero除外理由: ファイル数386件以上・PDF等バイナリ含む・レート制限に抵触しやすい。iPhoneでのZotero参照はGeminiアプリ（Drive連携済み）で代替可能。

## troubleshooting
| 症状 | 原因 | 対応 |
|---|---|---|
| `too_many_write_operations`（429） / "Failed to fetch" | 大量ファイル一括アップロードでDropbox APIレート制限 | 除外リスト追加、数分待って再同期 |
| ファイルが表示・反映されない | PC/iPhone間の Remote Base Directory 不一致、または「Sync On Save」オフ | ディレクトリ名を完全一致させる、手動同期を両側で実行 |
| .canvas / .base が同期エラー | Dropbox無料プランで一部形式非対応 | Regex除外に追加 |
| 認証が外れた | トークン失効 | Revoke Auth → 再Auth |

## verification
- PC: 「Remotely Save: start sync」実行 → 「Successfully synced」表示
- iPhone: 同期ボタン押下 → Daily, Knowledge, Mistakes等のフォルダが表示されることを確認
