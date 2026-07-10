---
date: 2026-06-21
theme: AutoHotkey 左クリック＋ホイールのタブ移動がExcelで効かない
status: open（未検証）
tags: [AutoHotkey, Excel, 未解決]
related: ["Knowledge/AutoHotkey_左クリックホイールタブ移動"]
---

# 【未対応】AutoHotkey 左クリック＋ホイールのタブ移動がExcelで効かない

## 問題
`~LButton & WheelUp` / `~LButton & WheelDown` のコンボホットキー方式は、ブラウザやエクスプローラーでは動作するが、**Excel上では発火しない**。

## 原因（推定）
Excelはセルのドラッグ選択などのためにマウス入力を強く制御しており、左ボタン押下中のAutoHotkeyコンボホットキー（`&`による同時押し判定）が正しく検出されない、既知の相性問題。

## 対応案（未検証・後で試す）
コンボ構文をやめ、ホイール入力を常時フックして `GetKeyState("LButton","P")` でその場の物理状態を判定する方式に変更する。

```ahk
#Requires AutoHotkey v2.0

*WheelUp::
{
    if GetKeyState("LButton", "P")
        Send "^{PgUp}"
    else
        Send "{WheelUp}"
}

*WheelDown::
{
    if GetKeyState("LButton", "P")
        Send "^{PgDn}"
    else
        Send "{WheelDown}"
}

~LButton Up::
{
    Send "{Ctrl Up}"
}
```

## ステータス
未検証。後日Excel上で動作確認する。ダメならExcelのみ除外し別キー（サイドボタン等）に切り替える方向も検討。
