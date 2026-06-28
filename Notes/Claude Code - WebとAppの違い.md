# Claude Code：Web版 vs アプリ版の違い

## Web版（claude.ai/code）

- セットアップ不要、ブラウザで即使える
- どのデバイスからでもアクセス可能（PC・スマホ・タブレット）
- クラウド上で実行されるため、ローカル環境が不要
- PCを閉じても長時間タスクが継続実行される
- 複数セッションを並列実行可能

## デスクトップアプリ版

- diff を視覚的にレビューできるUI
- 複数セッションをサイドバイサイドで表示
- マシン上でスケジュールタスクを実行可能
- Web版で開始した長時間タスクへ接続できる
- Windows / Mac 対応

## CLI版（ターミナル）

- ターミナルから全機能を利用
- シェルスクリプト・CI/CD との統合が容易
- Git・ローカルツールと直接連携
- 開発者の日常ワークフローに最適

## IDE拡張版（VS Code / JetBrains）

- インラインでdiff表示
- `@`メンションでファイル参照
- 会話履歴をIDE内で確認
- エディタを離れずに作業完結

## Windowsインストールエラー対処（HRESULT 0x80073CF6）

インストーラーが `AddPackage failed with HRESULT 0x80073CF6` で失敗する場合：

1. インストーラーを右クリック →「管理者として実行」
2. Microsoft Store で「App Installer」を更新
3. 既存のClaudeを完全削除してから再インストール
   - `C:\Users\<ユーザー名>\AppData\Local\AnthropicClaude` を削除
4. Windows Updateで最新バージョンに更新
5. 解決しない場合は https://support.anthropic.com へログを送付

> デスクトップアプリが使えない間は **Web版（claude.ai/code）** で同等の機能が使えます。
