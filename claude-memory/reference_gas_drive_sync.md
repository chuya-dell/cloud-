---
name: reference-gas-drive-sync
description: remotefdtd→chuya2816 Google Drive一方向同期(GAS)設定
metadata: 
  node_type: memory
  type: reference
  created: 2026-07-04
  updated: 2026-07-09
  status: active
  tags: 
    - google-apps-script
    - google-drive
    - sync
    - remotefdtd
    - infra
  originSessionId: dd50376c-27b1-4e73-8e6f-5cd70daad5ae
---

## summary

remotefdtdアカウントのDrive内`データ移動`フォルダを、chuya2816アカウントの`4.生データ D`(旧名`5.生データ D`)フォルダへ10分おきに一方向コピーするGoogle Apps Script。2026-07-04にコード紛失により再作成。初版(`syncMirror`)は削除も反映する完全ミラー方式だったが、remotefdtd側でのデータ削除運用と衝突して既存データが消える事故が発生したため、同日中に**削除を反映しない追加コピー方式(`syncCopy`)へ切替済み**。

2026-07-09、OneDriveの自動保存活用のためコピー先フォルダを`5.生データ D`→`4.生データ D`にリネームし、親階層に`4.生データ`を追加(`1.実験データ_gdrive/4.生データ/4.生データ D`)。**Google DriveのフォルダIDはリネーム・移動では不変**なため、GASコード・トリガーとも無修正で動作継続中。

## 前提構成

- remotefdtd専用PC(remotefdtdアカウントのみ搭載)とchuya2816のPCは別マシン
- remotefdtdのDrive内`データ移動`フォルダはchuya2816アカウントに共有済み
- 実行主体: chuya2816アカウントのGoogle Apps Script(script.google.com)
- 運用フロー: remotefdtdで`データ移動`にデータを置く → 同期でchuya2816側にコピー → remotefdtd側は同期後に削除して容量整理する予定

## folder_ids

| 役割 | フォルダ名(現行) | 旧フォルダ名 | パス | 所有者 | folder_id |
|------|-----------|-----------|------|--------|-----------|
| コピー元 | データ移動 | - | - | remotefdtd@gmail.com(chuya2816へ共有済み) | `1lJyOa1TciJbSdjz6DWCjUPSkzRWdX3rm` |
| コピー先 | 4.生データ D | 5.生データ D | `1.実験データ_gdrive/4.生データ/4.生データ D` | chuya2816@gmail.com | `19XM79gcw2sV-7R74wDco3Pkgu-IPig0v` |

## current_version: syncCopy(追加コピーのみ・削除非反映)

- 実行する関数: `syncCopy`
- イベントのソース: 時間主導型
- タイプ: 分ベースのタイマー
- 間隔: **10分おき**
- 動作: srcにあってdstに無いファイル/フォルダ→コピー。src側が更新されていれば上書き更新。**srcから消えてもdstは削除しない**(remotefdtd側の削除運用と両立させるため)
- **ファイル/フォルダの同一判定はフォルダID固定ではなく「名前」ベース**(`mapByName`)。src側でファイル・サブフォルダを**リネーム**すると別物として扱われ、dst側に旧名のファイルが残ったまま新名のファイルが追加コピーされる(重複が発生・要手動整理)。一方、`SRC_FOLDER_ID`/`DST_FOLDER_ID`で指定している**トップレベルのフォルダ自体**はIDで固定されているため、そのフォルダ名や親階層(場所)を変えても同期には一切影響しない。

```javascript
const SRC_FOLDER_ID = '1lJyOa1TciJbSdjz6DWCjUPSkzRWdX3rm';
const DST_FOLDER_ID = '19XM79gcw2sV-7R74wDco3Pkgu-IPig0v';

function syncCopy() {
  const srcFolder = DriveApp.getFolderById(SRC_FOLDER_ID);
  const dstFolder = DriveApp.getFolderById(DST_FOLDER_ID);
  copyFolderAdditive(srcFolder, dstFolder);
  Logger.log('sync完了(追加コピーのみ): ' + new Date());
}

function copyFolderAdditive(srcFolder, dstFolder) {
  const srcFiles = mapByName(srcFolder.getFiles());
  const dstFiles = mapByName(dstFolder.getFiles());
  const srcSubfolders = mapByName(srcFolder.getFolders());
  const dstSubfolders = mapByName(dstFolder.getFolders());

  for (const name in srcFiles) {
    const srcFile = srcFiles[name];
    const dstFile = dstFiles[name];
    if (!dstFile) {
      srcFile.makeCopy(name, dstFolder);
    } else if (srcFile.getLastUpdated().getTime() > dstFile.getLastUpdated().getTime()) {
      dstFile.setTrashed(true);
      srcFile.makeCopy(name, dstFolder);
    }
  }

  for (const name in srcSubfolders) {
    let targetSubfolder = dstSubfolders[name];
    if (!targetSubfolder) {
      targetSubfolder = dstFolder.createFolder(name);
    }
    copyFolderAdditive(srcSubfolders[name], targetSubfolder);
  }
}

function mapByName(iterator) {
  const map = {};
  while (iterator.hasNext()) {
    const item = iterator.next();
    map[item.getName()] = item;
  }
  return map;
}
```

## incident_log

- **2026-07-04**: 初版`syncMirror`(完全ミラー・削除も反映)を10分おきで運用開始。まもなく「5.生データ D内の既存データが消えている」と発覚。原因は、コピー元(データ移動)に存在しないファイルをコピー先から自動削除する仕様と、remotefdtd側でデータを削除する運用が衝突したこと。対処: 消えたファイルはゴミ箱から復元案内、スクリプトを`syncCopy`(削除非反映の追加コピーのみ)に置き換え、トリガーも`syncMirror`→`syncCopy`に張り替えて解消。
- **2026-07-09**: OneDrive自動保存活用のため、コピー先フォルダを`5.生データ D`→`4.生データ D`へリネーム、親階層に`4.生データ`を追加して移動。フォルダIDは不変のためGAS・トリガーとも無修正で継続動作確認。

## open_questions / risks

- `データ移動`フォルダ内のデータ量・ファイル数が今後大きく増加した場合、GAS実行時間上限(6分)に抵触するリスクあり(1GB時点では3分39秒〜5秒で完了、現状は余裕あり)
- 追加コピー方式のため、dst側の容量は増え続ける一方(remotefdtd側の削除はdstに影響しないため)。dst側の不要データ整理は手動で行う必要がある
- 同名ファイルで内容が異なる場合の上書き判定は更新日時ベースなので、意図しない上書きに注意
- コピー先フォルダの命名規則が今後も流動的(OneDrive移行に伴う階層変更が継続する見込み)。**フォルダ自体の移動・リネームは影響なし**だが、**フォルダ内の個別ファイル・サブフォルダのリネーム**は重複を生むため注意

## next_action

- 特になし(syncCopy版で運用中、問題発生時に見直し)

## related

- [[user_computers]] — remotefdtd専用機・Dell Precision等のPC構成
- [[project_experiments]] — 生データDの実験データとの関係
