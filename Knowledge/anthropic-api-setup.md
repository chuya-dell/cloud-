## Anthropic API キーの取得と設定

### 概要
Claude APIを利用するためのAPIキー取得と設定手順。

### キー取得手順

1. https://console.anthropic.com/ にアクセス
2. ログイン（Anthropicアカウント作成が必要）
3. 左サイドバーで「Settings → Keys」を選択
4. 「Create Key」ボタンをクリック
5. キーをコピー（`sk-ant-...` で始まる文字列）

### 課金セットアップ

1. https://console.anthropic.com/settings/billing にアクセス
2. 「Overview」でクレジットを確認
3. 「Top-up」で金額を追加チャージ
   - $5、$20、$50などの選択肢
   - または任意の金額を入力
4. クレジットカード情報を入力して完了

### 設定方法

**config.envに記述**:
```
ANTHROPIC_API_KEY=sk-ant-api03-xxxxxxxxxxxxxxxxx
```

**Pythonコードでの利用**:
```python
import os
from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY\
