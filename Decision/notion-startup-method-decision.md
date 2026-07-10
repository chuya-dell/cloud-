---
date: 2026-06-21
theme: Notion起動方法をスタートメニュー統一に決定（GPUフラグ組み込み）
status: resolved
tags: [Notion, GPU, 起動方法]
related: ["Knowledge/notion-gpu-crash-solution"]
---

## decision
Notionはスタートメニューのショートカットのみから起動する運用に統一する。デスクトップショートカットは削除する。

## reason
GPU相性問題（Intelグラフィックス環境での不安定性）の根本的解決にはソフトウェアレンダリングでの起動が必須だが、毎回手動でフラグを入力するのは運用負荷が高い。デスクトップショートカットはフラグが正しく適用されないリスクもある。

## implementation
- デスクトップのNotionショートカットを削除
- スタートメニューのショートカットに `--disable-gpu --no-sandbox --use-gl=swiftshader` フラグを組み込み
- 今後はスタートメニューからのみ起動

## impact
Notionアプリの起動方法・デスクトップのアイコン管理がスタートメニュー起動のみに限定される。
