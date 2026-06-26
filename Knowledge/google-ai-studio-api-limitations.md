## Google AI Studio Gemini APIの無料枠制限

### 概要
Google AI StudioのGemini APIは表面上は無料枠を提供しているが、実際の利用には多くの制限がある。

### 無料枠の理論値
- **Gemini 2.0 Flash**: 1日1500リクエスト、1分15リクエスト
- **支払い情報登録**: 無料枠でも支払い情報登録が必須（最近の仕様）

### 実際の制限
- **AI Pro契約アカウント**: 無料APIティアが自動的に無効化される（limit: 0）
- **キーの形式**: 無料APIキーは `AIza` で始まるが、制限されたキーは `AQ.` で始まる
- **クォータ設定**: limit: 0 になっていると使用不可

### 回避策
- AI Pro契約していない別のGoogleアカウントでキーを作成
- ただし支払い情報の登録は必須

### 結論
Geminiの無料枠は理論値では存在するが、実運用ではほぼ使用不可。既にAI Pro契約がある場合、Anthropic APIの方が単価が安く確実。

### 参考
- 日付: 2026-06-20
- Google AI Studio: https://aistudio.google.com/app/apikey
