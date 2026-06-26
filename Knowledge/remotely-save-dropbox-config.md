## Remotely SaveでDropbox同期する際の設定例

### 概要
Remotely SaveプラグインでDropboxを使用する際の具体的な設定値と除外ファイル設定。

### 設定項目

**基本設定:**
- Remote Service: Dropbox
- Authentication: はいちゅー（アカウント名）
- Sync Path: `/Apps/remotely-save/Obsidian Vault` （自動）

**除外ファイル設定（Regex Of Paths To Ignore）:**
```
.*\.canvas
.*\.base
Zotero/.*
zotero-library.json
Templates/zotero-template\.md
```

### Zoteroファイルを除外する理由

1. **ファイル数が多い**: Zoteroの同期済みファイルは386ファイル以上
2. **バイナリファイル**: PDFなど大容量ファイルが含まれる
3. **Dropboxレート制限**: 短時間に大量の書き込みでAPI制限に引っかかる
4. **iPhoneでの必要性**: Zoteroライブラリの参照はiPhoneのGeminiアプリで事足りる（Drive連携済み）

### 同期手順

**PC側:**
```
コマンドパレット（Ctrl+P）→「Remotely Save: start sync」
```

**iPhone側:**
```
リボンの同期アイコン（↑↓）をタップ
またはコマンドパレット（🔍）→「remotely save」検索
```

### トラブルシューティング

**「Failed to fetch」エラー**
- 原因: 大量同期によるレート制限、または除外ファイル不足
- 対応: 上記Regex除外リストを確認・追加

**認証が外れた場合**
- Revoke Auth → Auth で再認証
- ブラウザでのDropboxログイン認証を完了させる

### 参考
- 日付: 2026-06-20
