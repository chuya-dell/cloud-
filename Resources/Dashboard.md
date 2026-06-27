# 外部脳 ダッシュボード

## 📥 Inbox（未整理）

```dataview
TABLE file.ctime AS "作成日"
FROM "Inbox"
SORT file.ctime DESC
```

## 📅 最近のデイリーノート

```dataview
TABLE file.ctime AS "日付"
FROM "Daily"
SORT file.name DESC
LIMIT 7
```

## 📝 最新のパーマネントノート

```dataview
TABLE file.ctime AS "作成日", tags AS "タグ"
FROM "Notes/Permanent"
SORT file.ctime DESC
LIMIT 10
```

## 🗂 進行中のプロジェクト

```dataview
TABLE status AS "状態", file.mtime AS "更新日"
FROM "Projects"
WHERE status = "active"
SORT file.mtime DESC
```
