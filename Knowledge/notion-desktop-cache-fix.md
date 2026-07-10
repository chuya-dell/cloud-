---
date: 2026-06-21
theme: Notionデスクトップアプリ キャッシュ破損クラッシュの解決法
status: resolved
tags: [Notion, トラブルシューティング, キャッシュ, Windows]
related: ["Knowledge/notion-gpu-crash-solution"]
---

## summary
Notionデスクトップアプリが起動時にクラッシュする場合、多くはキャッシュ破損が原因。`%AppData%\Notion` 削除で大半解決する。GPUクラッシュ（`child-process-gone: GPU crashed`）が原因の場合は別問題 → `Knowledge/notion-gpu-crash-solution` 参照。

## symptom
- アプリがマークをタップすると即座に落ちる／起動時にクラッシュする
- Webブラウザ版（notion.so）は正常に動作する

## cause
デスクトップアプリのローカルキャッシュ破損

## fix
1. キャッシュフォルダの削除（最も効果的・推奨）
   - Windowsキー+R → `%AppData%\Notion` を入力して実行
   - フォルダごと削除
   - PowerShell: `Remove-Item -Path "$env:APPDATA\Notion" -Recurse -Force`
2. アプリ再起動
3. 解決しない場合は再インストール
   - コントロールパネルからNotion削除 → https://www.notion.so/desktop から再ダウンロード

## workaround
キャッシュ削除待ち・再インストール待ちの間はWebブラウザ版（https://notion.so）を使用可能。デスクトップアプリとほぼ同機能。

## notes
- キャッシュ削除でもログインデータ・ページデータ（Notionクラウド側）は失われない
- 削除後の初回起動はキャッシュ再構築のため時間がかかる場合あり
