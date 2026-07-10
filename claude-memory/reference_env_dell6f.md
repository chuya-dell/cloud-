---
name: reference-env-dell6f
description: Dell Precision（研究室6階）のClaude Code・Obsidian環境設定詳細
metadata: 
  node_type: memory
  type: reference
  originSessionId: 28e5ca57-3465-4b8a-807f-5a243f294513
---

[[user_computers]] の「Dell Precision（6階）」機の詳細環境（2026-07-03時点で確認、2026-07-09ストレージ構成追記）。

## PC本体
- Dell Precision, Xeon W2223, 16GB RAM
- OS: Windows 11 Pro for Workstations
- ユーザー: chuya（ホーム: C:\Users\chuya）

## Claude Code
- インストール: npm経由（`C:\Users\chuya\AppData\Roaming\npm\claude` / `claude.cmd`）
- Node v24.17.0 / npm 11.13.0
- 設定ファイル: `~/.claude/settings.json`
  - `theme: dark`
  - `autoMemoryDirectory: F:\GoogleDrive_local\Obsidian Vault\claude-memory`（自動メモリの保存先がObsidian Vault内、Google Drive同期領域）
- 過去に開いたプロジェクト（`~/.claude/projects/`）:
  - `F--GoogleDrive-local-Claude`
  - `F--GoogleDrive-local-Obsidian-Vault`
  - `H--Downloads`

## Obsidian
- Vault本体: `F:\GoogleDrive_local\Obsidian Vault`（Google Drive同期フォルダ、F:ドライブ）
- `obsidian-vault` MCPサーバー経由でアクセス可能なディレクトリはこのVault配下のみ（`list_allowed_directories`で確認済み）
- claude-memory はVault内のサブフォルダとして存在し、Claude Codeの自動メモリ保存先と一致 → 他PC（HP OmniBook等）ともGoogle Drive同期でメモリ共有される仕組み（[[feedback_setup_memory_sync]]参照）
- **既知の不具合(2026-07-09時点)**: obsidian-vault MCPがタイムアウトして応答しないことがある（ローカルサーバー側の問題、原因未特定）。その場合はGoogle Drive MCP（create_file、上書き不可のため新規作成→旧ファイル手動削除が必要）で代替する。

## ストレージ構成（2026-07-09時点、C:ドライブ空き容量確保作業）

### ドライブ構成
- C: (OS) 236GB — システム・アプリ本体のみ、逼迫しやすいため肥大化フォルダはH:へ退避
- H: (ローカルディスク) 223GB — AppData退避先（`H:\AppData_Moved\`）、Claude Code関連の大容量データもここ
- F: (1T_Buffalo, 外付けSSD) 931GB — GoogleDrive_local本体、Obsidian Vaultもここ
- L: (ボリューム) 119GB
- G:/I:/K: — Google Drive 4アカウント分のマウントポイント（teamnanodevice, remotefdtd, opuanalchem, chuya2816）

### AppDataジャンクション化（robocopy /MOVE → mklink /J方式）
C:のAppData肥大化対策として、以下をH:へ実体移動しジャンクションでリンク。**この方式は単純なアプリキャッシュには有効だが、仮想ファイルシステム型ソフト（Google Drive DriveFS等）には不可**（後述）。

- `C:\Users\chuya\AppData\Roaming\Notion\Partitions` → `H:\AppData_Moved\Notion\Partitions`（12.2GB）✅稼働確認済み
- `C:\Users\chuya\AppData\Roaming\Claude\vm_bundles` → `H:\AppData_Moved\Claude\vm_bundles`（約9GB, Claude Codeサンドボックス用VMイメージ）✅稼働確認済み
  - 移動時、Claudeアプリ起動中だとrobocopyがファイル削除に失敗（エラー32）するため、事前に完全終了してから実行する必要あり
- **Google DriveFS（`AppData\Local\Google\DriveFS`, 3.8GB）→ ジャンクション化を試みたが失敗、ロールバック済み（C:に実体を戻し、現状もC:のまま）**
  - 原因: DriveFSは低レベル仮想ファイルシステムを自前実装しており、ベースフォルダがジャンクション越しだと`Called ListDir on non-directory`エラーで起動不能になる（`CANNOT_CREATE_UI`）
  - **教訓: DriveFSはジャンクション方式で移動不可。移動するなら公式のキャッシュ保存先変更機能を使うこと**

### OneDrive移動
- `OneDrive - 公立大学法人大阪`（8.7〜12GB）は公式機能で移動: OneDrive設定 →「このPCからリンクを解除」→ 再セットアップ時に「場所の選択」で`H:\OneDrive - 公立大学法人大阪`を指定
- ジャンクションではなくOneDrive自体の同期先変更機能を使うのが正解（Files On-Demand機構とジャンクションの相性が悪いため）

### 成果
- C:使用量: 209.1GB → 179.9GB（約29GB削減、Google Drive分3.8GBを除く）
- ProgramData/Program Files等の「アプリケーションファイル」領域（55GB超）はレジストリ参照のリスクが高く今回は対象外

### 詳細作業ログ
コマンド単位の詳細（robocopy実行順序・発生したエラーと対処）は `Logs/260709_PC容量整理_Cドライブ空き容量確保.md` 参照。
