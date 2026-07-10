---
date: 2026-07-01
theme: Cometブラウザ起動不具合の解決（GPUサンドボックス相性問題）
status: resolved
tags: [Comet, トラブルシューティング, GPU, Windows]
---

# Comet ブラウザ 起動不具合の解決

**日付**: 2026-07-01

## 症状
- comet.exe をダブルクリックしても起動しない（プロセスすら立ち上がらない）

## 原因
GPUプロセスが `STATUS_ACCESS_DENIED` で即座にクラッシュを繰り返していた（GPUサンドボックスとこの環境の相性問題）。
```
GPU process exited unexpectedly: exit_code=-1073741790（0xC0000022 = ACCESS_DENIED）
GPU process isn't usable. Goodbye.
```
副次的に、GPU永続キャッシュ（`User Data\GPUPersistentCache\DawnGraphiteCache\...`）への書き込みで共有違反（0x20）も発生していたが、これはGPUプロセスがクラッシュ→再試行を繰り返す過程で生じた二次的な症状で、根本原因ではなかった。

## 試したが効果がなかった対処
- GPUキャッシュフォルダ（GPUCache / GPUPersistentCache / GrShaderCache / DawnWebGPUCache）を削除
- Windows Defenderの除外設定に Comet フォルダ・comet.exe を追加
- `--disable-gpu`
- `--disable-gpu-shader-disk-cache --disable-gpu-program-cache`
- `--disable-features=SkiaGraphite,Vulkan`

## 解決策
`--disable-gpu-sandbox` フラグを付けて起動すると正常に起動する。
```
comet.exe --disable-gpu-sandbox
```

## 今後について
今回は手動起動のみで対応し、ショートカットの恒久修正は行っていない。次回同じ症状が出た場合：
1. 上記コマンドで一時的に起動
2. 再発するようならデスクトップ/スタートメニューのショートカットに `--disable-gpu-sandbox` を恒久的に追加、またはGPUドライバ更新・Windows Core Isolation（メモリ整合性）設定の確認を検討

## 環境
- OS: Windows 11
- Comet インストールパス: `C:\Users\chuya\AppData\Local\Perplexity\Comet\Application\comet.exe`
- バージョン: 149.0.7827.1095
