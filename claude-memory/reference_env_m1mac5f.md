---
name: reference-env-m1mac5f
description: M1 MacBook Pro（5階、遠藤先生借用）のClaude Code・Obsidian環境設定詳細
metadata: 
  node_type: memory
  type: reference
  originSessionId: 903f0fe3-b0e7-4e27-96e5-c158b44791fd
---

[[user_computers]] の「M1 MacBook（5階）」機の詳細環境（2026-07-03時点で確認）。

## PC本体
- MacBookPro17,1 / Apple M1 / 8GB RAM
- OS: macOS 15.4 (Sonoma系, Build 24E248)
- ホスト名: shiraishichuuyanoMacBook-Pro.local
- ユーザー: shiraishichuuya（ホーム: /Users/shiraishichuuya）

## Claude Code
- 動作形態: Claude Desktopアプリ経由（Cowork）に加え、2026-07-03にnpm経由のスタンドアロンCLIも整備済み
  - Node.js/npmは`nvm`（`~/.nvm`）経由でインストール（sudo不要）。Node v24.18.0 / npm 11.16.0、`nvm install --lts`で導入
  - `nvm`の読み込み設定は`~/.zprofile`に追記済み（新規ターミナルでも`claude`/`node`/`npm`がそのままPATH上で使える）
  - Claude Code CLI本体は`npm install -g @anthropic-ai/claude-code`でインストール（v2.1.199、実体は`~/.nvm/versions/node/v24.18.0/bin/claude`）
- 設定ファイル: `~/.claude/settings.json`（未作成だったため新規作成）
  - `autoMemoryDirectory`: Google Drive上のObsidian Vault内`claude-memory`フォルダに設定 → Dell（6階）と同じ共有メモリ領域を参照する
- Claude Desktopのユーザーファイルパス: `/Users/shiraishichuuya/Claude`（`claude_desktop_config.json`の`coworkUserFilesPath`）

## Obsidian
- Vaultは2つ登録されている
  - `/Users/shiraishichuuya/Documents/Obsidian Vault`（ローカルのみ、Google Drive同期対象外、現在は未オープン）
  - `/Users/shiraishichuuya/Library/CloudStorage/GoogleDrive-chuya2816@gmail.com/マイドライブ/Obsidian Vault`（Google Drive同期、現在オープン中の本体Vault）
- macOSのGoogle Drive連携は「CloudStorage」方式（`~/Library/CloudStorage/GoogleDrive-<account>/`）。Windows機のような`F:\GoogleDrive_local`というドライブレターは存在しない
- claude-memoryはこのGoogle Drive同期Vault内のサブフォルダとして存在し、Dell（6階）・HP OmniBookと共有される（[[feedback_setup_memory_sync]]参照）
- 他に`/Users/shiraishichuuya/obsidian-vault`という無関係のローカルgitリポジトリも存在するので混同注意
- Obsidian Vaultへの直接ファイルアクセス用に`obsidian-vault` MCPサーバー（`@modelcontextprotocol/server-filesystem`）をuserスコープで追加済み（`claude mcp add --scope user obsidian-vault -- npx -y @modelcontextprotocol/server-filesystem "<Vaultパス>"`）。接続確認済み（`claude mcp list`で`✔ Connected`）。アクセス範囲はこのVault配下のみ
  - **重要**: これは`~/.claude.json`（標準CLI設定）に書き込まれるため、**ターミナルで`claude`コマンドを直接起動した場合のみ**有効。Claude Desktopアプリ（Cowork）のセッションでは反映されないことを確認済み（2026-07-03）
  - Claude Desktop側の`claude_desktop_config.json`には`mcpServers`キー自体が存在せず、Google Drive/Notion/カレンダー等はアカウント側（クラウド）のコネクタとして提供されている。CoworkにローカルMCPサーバーを追加したい場合はDesktopアプリのSettings→Connectors経由で別途設定が必要（未検証）
