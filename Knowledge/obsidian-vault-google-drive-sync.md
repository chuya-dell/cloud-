---
date: 2026-06-20
theme: Obsidian VaultのGoogle Drive移行とマルチデバイス同期構成
status: resolved
tags: [Obsidian, Google Drive, 同期, マルチデバイス]
related: ["Knowledge/obsidian-iphone-sync-remotely-save"]
---

## summary
ObsidianのVault（ローカルまたはOneDrive）をGoogle Drive上に移行し、PC・Android・iOSの複数デバイスから統一的にアクセスできるようにする構成。OneDriveからの移行を想定。

## migration_steps
1. **Google Drive for Desktop**（旧Backup and Sync）をインストール → `G:\マイドライブ\` がローカルフォルダとして利用可能に
2. Obsidianを完全に閉じる（ファイル破損防止）
3. 既存Vault全体（`.obsidian/`フォルダの設定・プラグインを含む）を `G:\マイドライブ\Obsidian Vault` にコピー／移動
   - 元のローカルVaultはバックアップとして保持
4. Obsidianを起動 → 左下「Vault名」→「保管庫を管理」/「Open folder as vault」→ `G:\マイドライブ\Obsidian Vault` を指定
5. 確認: `.obsidian/obsidian.json` の"open"設定が新パスになっているか、Notes/Attachmentsが正常表示されるか

## multidevice_config
| デバイス | 方法 | 同期方式 | コスト |
|---|---|---|---|
| PC（Windows/Mac） | Google Drive for Desktop | 自動双方向同期（ミラーモード推奨、Streamモードより安定） | 無料 |
| Android | Obsidian公式アプリ + Remotely Saveプラグイン | Google Drive経由の手動・自動同期 | 無料 |
| iOS/iPad | Obsidian公式アプリ + Remotely Saveプラグイン（Dropbox経由、Google Drive非対応のため） | Dropbox経由同期。詳細は `Knowledge/obsidian-iphone-sync-remotely-save` | 無料 |

## notes
- `.obsidian/`フォルダをコピーするとプラグイン設定も継承されるため新デバイスでの再構築が不要
- Remotely Save PRO（月$8程度）ならGoogle Drive直接対応だが、現状は無料構成（PC: Google Drive／モバイル: Dropbox中継）を採用
