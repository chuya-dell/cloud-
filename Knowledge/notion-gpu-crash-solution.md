---
date: 2026-06-21
theme: Notionデスクトップアプリ GPUクラッシュの解決法（Windows/Intel）
status: resolved
tags: [Notion, トラブルシューティング, GPU, Electron, Windows]
related: ["Knowledge/notion-desktop-cache-fix"]
session_id: bef69572-fa00-4e5f-81b2-738678ef5b35
---

## summary
Notion（Electronアプリ）起動時にGPUプロセスがIntelグラフィックスドライバーとの相性問題でクラッシュし、正常に起動しない問題の解決手順。ソフトウェアレンダリング起動で確実に回避できる。

## environment
- OS: Windows 11
- CPU: Intel 13th Gen Core i7-13700H
- Notion: 7.22.0

## symptom
- Notionをダブルクリックしても起動しない、プロセスが一瞬起動してすぐ消える
- ログに `child-process-gone: GPU crashed, exitCode: -2147483645` が記録される

## log_location
`C:\Users\chuya\AppData\Roaming\Notion\logs\main.log`

## fix
1. GPUキャッシュを削除
```powershell
Stop-Process -Name "Notion" -Force
Remove-Item "$env:APPDATA\Notion\GPUCache" -Recurse -Force
Remove-Item "$env:APPDATA\Notion\DawnGraphiteCache" -Recurse -Force
Remove-Item "$env:APPDATA\Notion\DawnWebGPUCache" -Recurse -Force
```
2. ソフトウェアレンダリングで起動
```powershell
Start-Process "$env:LOCALAPPDATA\Programs\Notion\Notion.exe" -ArgumentList '--disable-gpu --disable-gpu-compositing --use-gl=swiftshader --no-sandbox'
```
3. 恒久対策（未実施）: スタートメニューのショートカットを編集して上記フラグを追加、またはWindowsのグラフィックドライバーを更新

## troubleshooting_window_not_visible
- state.jsonのウィンドウ位置情報をリセット（画面中央に配置）
- PowerShellで強制的にウィンドウを前面表示
- タスクトレイの隠しアイコンも確認

## troubleshooting_full_reset
state.json・キャッシュディレクトリを完全削除すると新規起動時に全設定がリセットされる
