# 金ナノピラーspatioselective修飾 文献調査（3AI比較）

> Notion: https://app.notion.com/p/388e390406d1816ab5dcd794a8179d9e  
> 日付: 2026-06-24

---

## 最終結論
**「Au-thiol＋金ナノピラー上部のみの化学的spatioselective修飾」を満たす論文はChattaway 2019のみ。**  
DNA固定化まで含めた「上部のみ修飾」の金ナノピラー論文は現状ゼロ → 新規性を主張できる。

---

## 調査条件
**必須**: 金ナノピラーアレイ × Au-thiol SAM × ピラー上部選択的修飾  
**優先**: DNA固定化、バイオセンシング応用

---

## 実在確認済み論文

### ◎ tip選択修飾（化学的）
**Chattaway et al. 2019** — *Nanoscale Advances*, 1, 2208–2215  
DOI: 10.1039/C9NA00149B  
手法: PAAマスク＋空気プラズマエッチバックでピラー上部露出→チオラクトン共重合体をAu-S結合でグラフト  
tip選択性: ✅ 化学的に明示（唯一の例）／DNA: なし（AuNP＋RGDペプチド）

### △ 構造由来のtip集中（化学的spatioselective議論なし）
**Li et al. 2021** — *Nature Communications*, 12, 1087  
DOI: 10.1038/s41467-021-21431-w  
手法: EBL＋金蒸着＋RIEで構造的に金top面のみ→DSP（Au-S）で修飾→抗体固定  
重要数値: active pillar 20% vs 理論Poisson値10%→非特異吸着閾値の指標

**Yang et al. 2013** — *ACS Nano*  
DOI: 10.1021/nn401199k  
手法: 指向性EB蒸着でSiピラー先端のみに金キャップ→thiol修飾DNAアプタマー固定  
DNA: ✅（アプタマー、バソプレシン検出）

**Oh et al. (Mirkin群) 2017** — *J. Am. Chem. Soc.*  
DOI: 10.1021/jacs.7b03111  
手法: AAOテンプレート内でNi-Au-Ni多層ロッド→Ni犠牲層エッチで端部露出→thiol-DNA直交固定  
DNA: ✅（2配列を端部/側面に直交固定）

---

## 各AIの評価
- **Perplexity（Comet）**: 最も正確。条件を厳密に適用しChattaway 2019のみと結論。
- **Claude（自己評価）**: 一部混同あり。Li 2021の「構造由来」と「化学的spatioselective」を混同。
- **Gemini**: 条件を満たさない論文を「満たすかのように」詳述する傾向あり。注意が必要。

---

## 自分の研究への示唆
- **「Au-thiol＋金ナノピラー上部のみへのDNA固定化」論文は現状ゼロ** → 新規性を明確に主張できる
- 引用の中核2本：**Chattaway 2019**（概念根拠）＋**Li 2021**（デジタル単分子計数の構造）
- コンタクト転写によるtip選択固定の文献根拠はまだ弱い → 追加調査が必要
