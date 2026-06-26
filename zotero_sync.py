"""
Zotero → Obsidian 自動同期スクリプト
Better BibTeXが出力するJSONを監視して、変更があったらObsidianノートを更新する
"""

import json
import os
import re
import time
from pathlib import Path
from datetime import datetime

VAULT = Path("F:/GoogleDrive_local/Obsidian Vault")
JSON_PATH = VAULT / "zotero-library.json" / "zotero-library.json"
OUTPUT_DIR = VAULT / "Zotero"

OUTPUT_DIR.mkdir(exist_ok=True)


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    return name[:80].strip()


def get_authors(creators):
    authors = []
    for c in creators:
        if c.get("creatorType") == "author":
            if "name" in c:
                authors.append(c["name"])
            else:
                parts = [c.get("lastName", ""), c.get("firstName", "")]
                authors.append(" ".join(p for p in parts if p))
    return authors


def get_year(date_str):
    if not date_str:
        return ""
    return date_str[:4] if len(date_str) >= 4 else date_str


def build_item_to_collections(data):
    """itemID → [collection名] のマッピングを作成"""
    mapping = {}
    for col in data.get("collections", {}).values():
        col_name = col["name"]
        for item_id in col.get("items", []):
            mapping.setdefault(item_id, []).append(col_name)
    return mapping


def build_note(item, collections):
    title = item.get("title", "Untitled")
    authors = get_authors(item.get("creators", []))
    year = get_year(item.get("date", ""))
    journal = item.get("publicationTitle", "")
    doi = item.get("DOI", "")
    abstract = item.get("abstractNote", "")
    citekey = item.get("citationKey", item.get("key", ""))
    uri = item.get("uri", "")
    zotero_link = f"zotero://select/library/items/{item.get('key', '')}"

    authors_str = ", ".join(authors) if authors else "Unknown"
    collections_yaml = "\n".join(f"  - {c}" for c in collections) if collections else "  []"
    collections_inline = ", ".join(collections) if collections else ""

    content = f"""---
title: "{title.replace('"', "'")}"
authors: "{authors_str}"
year: {year}
journal: "{journal}"
doi: "{doi}"
citekey: "{citekey}"
collections:
{collections_yaml}
tags:
  - literature
---

# {title}

## 書誌情報
- **著者**: {authors_str}
- **年**: {year}
- **雑誌**: {journal}
- **DOI**: {doi}
- **Zoteroリンク**: [Open in Zotero]({zotero_link})
- **コレクション**: {collections_inline}

## Abstract

{abstract}

## メモ

"""
    return content


def sync(data):
    item_to_collections = build_item_to_collections(data)
    items = [i for i in data.get("items", [])
             if i.get("itemType") not in ("attachment", "note")]

    updated = 0
    created = 0

    for item in items:
        title = item.get("title", "Untitled")
        filename = sanitize_filename(title) + ".md"
        filepath = OUTPUT_DIR / filename
        collections = item_to_collections.get(item.get("itemID"), [])

        new_content = build_note(item, collections)

        # 既存ファイルがあればcollectionsとfrontmatterだけ更新、メモは保持
        if filepath.exists():
            existing = filepath.read_text(encoding="utf-8")
            # 「## メモ」以降のユーザーメモを保持
            if "## メモ" in existing:
                user_notes = existing.split("## メモ", 1)[1]
                new_content = new_content + user_notes
            else:
                # コレクション情報だけ変わった場合はスキップしない
                if existing == new_content:
                    continue
            if existing != new_content:
                filepath.write_text(new_content, encoding="utf-8")
                updated += 1
        else:
            filepath.write_text(new_content, encoding="utf-8")
            created += 1

    return created, updated


def main():
    print(f"[{datetime.now():%H:%M:%S}] Zotero同期スクリプト起動")
    print(f"  監視ファイル: {JSON_PATH}")
    print(f"  出力先: {OUTPUT_DIR}")

    last_mtime = 0

    while True:
        try:
            mtime = JSON_PATH.stat().st_mtime
            if mtime != last_mtime:
                last_mtime = mtime
                print(f"[{datetime.now():%H:%M:%S}] JSONが更新されました。同期中...")
                with open(JSON_PATH, encoding="utf-8") as f:
                    data = json.load(f)
                created, updated = sync(data)
                print(f"[{datetime.now():%H:%M:%S}] 完了: 新規{created}件 / 更新{updated}件")
        except Exception as e:
            print(f"[{datetime.now():%H:%M:%S}] エラー: {e}")

        time.sleep(10)  # 10秒ごとにチェック


if __name__ == "__main__":
    main()
