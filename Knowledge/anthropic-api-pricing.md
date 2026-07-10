---
date: 2026-06-20
theme: Anthropic API（Claude）の料金体系・キー取得・セットアップ
status: resolved
tags: [Anthropic API, 料金, セットアップ]
related: ["Knowledge/API選定経緯", "Knowledge/process-logs-to-obsidian-system"]
---

## summary
Anthropic APIは従量課金・プリペイド式（チャージ制、月額固定費なし、残高切れで自動停止）。会話ログ分類用途では低コストな claude-haiku-4-5 を採用。$5チャージで軽〜中使用なら数ヶ月〜数年もつ。

## pricing_by_model
| モデル | 1ファイルあたり | 月100件 | 月500件 | 推奨初回チャージ |
|---|---|---|---|---|
| claude-sonnet-4-6 | $0.005〜$0.02 | $0.5〜$2 | $2.5〜$10 | $20 |
| claude-haiku-4-5（採用） | $0.0005〜$0.002 | $0.05〜$0.2 | $0.25〜$1 | $5 |

- 月300回処理（ヘビー使用想定）でも $0.3〜$1程度／月
- $5チャージで軽・中使用なら5年以上、ヘビー使用でも1〜2ヶ月分

## key_acquisition
1. https://console.anthropic.com/ にログイン（アカウント作成必要）
2. 左サイドバー「Settings → Keys」→「Create Key」
3. キーをコピー（`sk-ant-...` 形式）

## billing_setup
1. https://console.anthropic.com/settings/billing にアクセス
2. クレジットカード登録
3. 「Top-up」で $5・$20・$50等をチャージ（任意金額も可）
4. 都度課金・プリペイド式・自動引き落としなし（残高切れで停止するのみ）

## config
**config.envに記述:**
```
ANTHROPIC_API_KEY=sk-ant-api03-xxxxxxxxxxxxxxxxx
```

**Python利用例:**
```python
import os
from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "..."}]
)
```

## note
Gemini APIとの比較検討・Anthropic採用の経緯は `Knowledge/API選定経緯` 参照。
