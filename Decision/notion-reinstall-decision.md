---
date: 2026-06-21
theme: Notionデスクトップアプリ再インストール実施決定
status: resolved
tags: [Notion, トラブルシューティング, 再インストール]
related: ["Decision/notion-cache-deletion-decision", "Knowledge/notion-gpu-crash-solution"]
---

## decision
Notionデスクトップアプリを完全アンインストール後、notion.so/desktopから最新版を再ダウンロード・新規インストールする。

## reason
キャッシュ削除（`Decision/notion-cache-deletion-decision`）実施後も起動時クラッシュが継続。Webブラウザ版は正常動作するため、キャッシュ破損ではなくアプリインストール自体の破損と判断。

## impact
- 再インストール中はデスクトップアプリ使用不可（Webブラウザ版は継続使用可能、データロスなし）
- ログイン情報はサーバー側保持のため再ログインで復旧
