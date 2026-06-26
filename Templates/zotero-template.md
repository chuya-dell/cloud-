---
title: "{{title}}"
authors: "{{authorsAsList | join(', ')}}"
year: {{date | format("YYYY")}}
journal: "{{publicationTitle}}"
doi: "{{DOI}}"
citekey: "{{citekey}}"
collections:
{% for collection in collections %}  - {{collection}}
{% endfor %}tags:
  - literature
---

# {{title}}

## 書誌情報
- **著者**: {{authorsAsList | join(', ')}}
- **年**: {{date | format("YYYY")}}
- **雑誌**: {{publicationTitle}}
- **DOI**: {{DOI}}
- **Zoteroリンク**: [Open in Zotero]({{desktopURI}})
- **コレクション**: {% for collection in collections %}{{collection}}{% if not loop.last %}, {% endif %}{% endfor %}

## Abstract

{{abstractNote}}

## メモ

{% for annotation in annotations %}{% if annotation.annotatedText %}
> {{annotation.annotatedText}}

{{annotation.comment}}
{% endif %}{% endfor %}

## 自分のメモ

