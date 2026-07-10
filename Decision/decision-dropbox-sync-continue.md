---
date: 2026-06-20
theme: Dropbox経由でのObsidian同期を継続する決定
status: resolved
tags: [Obsidian, Dropbox, iPhone同期]
related: ["Knowledge/obsidian-iphone-sync-remotely-save", "Knowledge/iphone-obsidian-limitations"]
---

## decision
iPhone Obsidian同期はDropbox経由（Remotely Save）の現行方式を継続する。

## reason
iPhoneのObsidianアプリはGoogle Drive直接非対応のため、何らかの中継ストレージが必要。Dropboxは無料枠2GBで運用に十分、認証も安定しているため、iCloud経由やObsidian Sync（有料）への切り替えは見送り。

## note
実装手順の詳細は `Knowledge/obsidian-iphone-sync-remotely-save`、代替案の比較は `Knowledge/iphone-obsidian-limitations` を参照。
