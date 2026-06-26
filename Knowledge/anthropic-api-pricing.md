## Anthropic API（Claude）の料金体系と使用方法

### 概要
Anthropic APIはClaudeを外部スクリプトやアプリケーションから呼び出すためのAPI。従量課金式で、使用した分だけ請求される。

### 料金詳細
- **モデル**: claude-haiku-4-5（推奨）
- **会話ログ1件あたり**: 約$0.0005〜$0.002（0.075〜0.3円）
- **$5チャージの処理能力**: 2,500〜10,000件のログ処理が可能
- **月300回処理時**: 約$0.3〜$1程度（45〜150円）
- **5年以上使用可能**: $5チャージで軽・中程度の使用なら5年以上の利用期間

### 課金方式
- **都度課金（従量課金）**: 使った分だけ引き落とされる
- **プリペイド式**: チャージした残高から消費される
- **月額固定費なし**: 使わなければ費用は発生しない
- **自動引き落としなし**: 残高がなくなったら停止するだけ

### APIキー取得
1. https://console.anthropic.com/settings/billing でチャージ（$5推奨）
2. https://console.anthropic.com/settings/keys でAPIキーを作成
3. キーは `sk-ant-` で始まる形式

### セットアップ
```python
import anthropic

client = anthropic.Anthropic(api_key="sk-ant-xxxx...")
message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "..."}
    ]
)
```

### 参考
- 日付: 2026-06-20
- セッション: Claude Code会話内での実装
