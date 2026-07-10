---
date: 2026-06-21
theme: MCP obsidian-vault接続回復の対処方針
status: resolved
tags: [MCP, トラブルシューティング, Obsidian]
related: ["Knowledge/mcp-obsidian-vault-troubleshooting"]
---

## decision
MCP obsidian-vaultサーバーの接続切断時、以下の順序で段階的にトラブルシューティングする。

## reason
MCP obsidian-vaultサーバーが切断状態になり、Obsidian Vaultへの読み書きが不可能になる事象が発生。Google Drive同期フォルダのアクセス遅延、またはClaude Code初期化タイミングの問題が原因と推定。

## approach（優先順）
1. Claude Codeデスクトップアプリの完全再起動（タスクトレイからも完全終了）
2. 再起動後にMCP接続状態を確認
3. 復帰しない場合、MCPサーバーの手動リロード機能を使用
4. それでも解決しない場合、Google Driveストリーミングフォルダのパス遅延問題を深掘り調査（別パスへの移動も検討）

## impact
Obsidian Vaultへの読み書き機能全般（Vault関連のファイル操作全て）が、接続回復までの間制限される。
