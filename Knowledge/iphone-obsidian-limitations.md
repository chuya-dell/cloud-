---
date: 2026-06-20
theme: iPhone ObsidianアプリがサポートするクラウドストレージとGoogle Drive非対応の回避策
status: reference
tags: [iPhone, Obsidian, クラウドストレージ]
related: ["Knowledge/obsidian-iphone-sync-remotely-save"]
---

## summary
iPhoneのObsidianアプリはiCloud Drive・Dropbox・OneDrive・Obsidian Sync（有料）を直接サポートするが、Google Driveは非対応。本Vault（Google Drive上）へのアクセスには回避策が必要。

## supported_storage
- **iCloud Drive**（Apple純正・推奨）: 設定が簡単、iOSネイティブ、50GB契約で十分
- **Dropbox**: Vault保存先として直接指定可能、ファイル同期が安定
- **OneDrive**（Microsoft）: Vault保存先として直接指定可能
- **Obsidian Sync**（有料・月$10）: 公式同期サービス、最も安定だが課金必要

## unsupported
- **Google Drive**: iPhone標準Obsidianではサポートなし

## workarounds_for_google_drive
1. **Remotely Save + iCloud**: PC（Google Drive＝マスター）→ Remotely Save → iCloudにミラー、iPhoneはiCloudから直接読込（公式対応で安定）。50GB契約済みなら活用価値高い
2. **Remotely Save + Dropbox**（採用中）: 無料2GBで十分、認証が安定。詳細手順は `Knowledge/obsidian-iphone-sync-remotely-save` 参照
3. **Obsidian Sync**: 公式サービス、最も安定だが月$10

## caveat
Remotely SaveでGoogle Driveに直接認証する方法も存在するが、iPhone側でGoogle Drive認証がうまく通らないケースが報告されており非公式・不安定。上記のDropbox/iCloud中継が推奨。
