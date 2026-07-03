# Notion GPUクラッシュ解決法（Windows）

## 症状
- Notionをダブルクリックしても起動しない
- プロセスは一瞬起動してすぐ消える
- ログに `child-process-gone: GPU crashed, exitCode: -2147483645` が出力される

## 環境
- Windows 11
- CPU: Intel 13th Gen Core i7-13700H
- Notion 7.22.0

## 原因
ElectronアプリのGPUプロセスがIntelグラフィックスドライバーとクラッシュする。

## ログ場所
`C:\Users\chuya\AppData\Roaming\Notion\logs\main.log`

## 解決手順

### 1. GPUキャッシュを削除
```powershell
Stop-Process -Name "Notion" -Force
Remove-Item "$env:APPDATA\Notion\GPUCache" -Recurse -Force
Remove-Item "$env:APPDATA\Notion\DawnGraphiteCache" -Recurse -Force
Remove-Item "$env:APPDATA\Notion\DawnWebGPUCache" -Recurse -Force
```

### 2. ソフトウェアレンダリングで起動
```powershell
Start-Process "$env:LOCALAPPDATA\Programs\Notion\Notion.exe" -ArgumentList '--disable-gpu --disable-gpu-compositing --use-gl=swiftshader --no-sandbox'
```

## 恒久的な対策（未実施）
スタートメニューのショートカットを編集して上記フラグを追加するか、
Windowsのグラフィックドライバーを更新する。

## 発生日
2026-06-21
