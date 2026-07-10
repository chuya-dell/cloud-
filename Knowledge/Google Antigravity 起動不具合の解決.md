---
date: 2026-06-30
theme: Google Antigravity起動不具合の解決（GPUプロセスクラッシュ）
status: resolved
tags: [Antigravity, トラブルシューティング, GPU, Windows]
---

# Google Antigravity 起動不具合の解決

**日付**: 2026-06-30

## 症状
- Windows PC で Antigravity.exe をダブルクリックしても起動しない
- 起動しても黒画面のまま

## 原因
Intel Iris Xe Graphics のGPUプロセスがクラッシュ（Electronアプリのバグ）
```
GPU process exited unexpectedly: exit_code=-2147483645
GPU process isn't usable. Goodbye.
```

## 解決策
以下のフラグを付けて起動する：
```
Antigravity.exe --disable-gpu --no-sandbox --disable-gpu-sandbox
```

## デスクトップショートカット
上記フラグ付きのショートカットをデスクトップに作成済み。次回からはそれをダブルクリックするだけでOK。

## 環境
- OS: Windows 11
- GPU: Intel Iris Xe Graphics (ドライバー: 32.0.101.5768)
- Antigravity: v2.2.1
