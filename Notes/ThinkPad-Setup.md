# ThinkPadでのセットアップ手順

このVaultをThinkPad（Windows/Linux）でも開いて、Macと同じようにGit経由で自動同期させるための手順です。

## 1. Obsidianをインストール

https://obsidian.md からThinkPad用のObsidianをインストールします。

## 2. このリポジトリをクローン

```bash
git clone https://github.com/chuya-dell/cloud-.git
```

任意のフォルダにクローンしてください（例: `C:\Users\<name>\Documents\cloud-` や `~/vaults/cloud-`）。

## 3. Obsidianでフォルダを開く

Obsidianを起動し、「Open folder as vault」からクローンしたフォルダを選択します。
`.obsidian` フォルダに設定・プラグイン一式が含まれているため、プラグインやエディタ設定はMacと同じ状態で開けます。

## 4. コミュニティプラグインを有効化

初回起動時、コミュニティプラグイン（`obsidian-git`）が無効化された状態になっていることがあります。
設定 → コミュニティプラグイン → 「制限モード」をオフにし、`Git` プラグインを有効化してください。

## 5. Git認証の設定

自動push/pullにはGit認証が必要です。ThinkPad側で以下のいずれかを設定してください。

- SSH鍵をThinkPadで生成し、GitHubアカウントに登録する（リモートURLを`git@github.com:chuya-dell/cloud-.git`に変更）
- もしくはGitHub Personal Access Token (PAT) を使い、資格情報マネージャーにキャッシュする

## 6. 同期設定の確認

プラグイン設定（`.obsidian/plugins/obsidian-git/data.json`）はすでにリポジトリに含まれており、Macと共通です。

- 10分ごとに自動pull
- ファイル変更後の自動コミット・push
- コミットメッセージ: `vault backup: {{date}}`

ThinkPad側で個別に変更する必要はありません。設定を変えたい場合はObsidian内の「Git」設定タブから調整してください。

## 7. 動作確認

ThinkPadでノートを1つ編集・保存し、数分待ってMac側（またはGitHub上のリポジトリ）に反映されるか確認してください。
