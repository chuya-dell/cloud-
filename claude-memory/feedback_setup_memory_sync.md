---
name: feedback-setup-memory-sync
description: メモリをGoogle Drive経由で複数PCに共有する設定（2026-06-29完了）
metadata:
  type: feedback
---

メモリの保存先をGoogle Driveに設定済み。複数PC間で自動共有される。

**Why:** Dell Precision（6階）・M1 MacBook（5階）・HP OmniBook（審査中）の3台でClaude Codeのメモリを共有したい。

**How to apply:**
- メモリの読み書き先は `F:\GoogleDrive_local\claude-memory`（このWindowsPC）
- 設定ファイル：`C:\Users\chuya\.claude\settings.json` に `"autoMemoryDirectory"` として記載済み
- 他のPCでも同じ設定（そのPCのGoogle DriveパスのClaude-memoryフォルダを指定）をすれば共有可能
- MacではGoogle Driveのマイドライブ内 `claude-memory` フォルダを指定する
