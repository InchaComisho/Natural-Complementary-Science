# 自然補完科学（Natural Complementary Science）

> English version: [README.md](./README.md)

> 本リポジトリは、Master（InchaComisho / inchacomusho）により定義・公開された「自然補完科学（Natural Complementary Science）」の日本語版概要です。ここで扱う「補完」は、医療・代替療法における “complementary” とは無関係であり、人類と自然が互いの不足を補い、持続可能な全体を形成するという文明・科学・環境思想上の概念です。本フレームワークは概念的・統合的提案であり、個別技術や実装には科学的・工学的・生態学的検証が必要です。

## 概要

現代科学は大きな技術的進歩を生み出してきました。しかし同時に、気候不安定化、生物多様性喪失、土壌劣化、微生物圏の崩壊など、地球システムの不安定化も進行しています。

**自然補完科学**は、自然法則と補完性の原理に基づく新しい科学的パラダイムとして提案されます。

ここでいう補完性とは、人類と自然が互いの欠落を補い合い、均衡ある持続的な全体を形成する関係を意味します。

自然を支配するのでも、搾取するのでも、ただ手を出さずに保存するのでもなく、自然の循環が損なわれた部分を、人類の技術・知性・責任によって補助するという考え方です。

## 注目シミュレーション：文明存続度モデル

[![文明存続度モデルのグラフ](./simulations/civilization_survival_model/outputs/civilization_survival_index.png)](./simulations/civilization_survival_model/README_ja.md)

この注目シミュレーションは、二元論・人間至上主義、従来型環境管理、自然補完科学、崩壊加速型抽出という四つの哲学的前提のもとで、長期的な文明存続度がどのように変化し得るかを比較する概念モデルです。

本シミュレーションは **概念的・非予測的** なものです。検証済みの気候モデル、生態モデル、経済モデル、社会モデルではありません。目的は、価値体系の違いが生態系完全性、循環、資源安定性、社会秩序、技術、長期的持続性にどのような影響を与え得るかを議論するために、仮定を見える形にすることです。

- [日本語版の概要](./simulations/civilization_survival_model/README_ja.md)
- [English overview](./simulations/civilization_survival_model/README.md)
- [Pythonスクリプト](./simulations/civilization_survival_model/civilization_survival_sim.py)
- [CSV結果](./simulations/civilization_survival_model/outputs/civilization_survival_results.csv)

## 中核定義

自然補完科学とは、自然法則に基づき、人類と自然の間に補完的かつ対等な関係を築くことで、持続可能な文明を構築しようとする科学的・哲学的フレームワークです。

その目的は、技術的支配ではありません。目的は、システムの持続性です。

```text
自然補完科学 = 自然法則に沿って、弱まった自然循環を人類の技術と責任で補助する統合科学
```

## 1. なぜ「共生」ではなく「補完」なのか

「自然との共生」という言葉は広く使われています。しかし、共生という語は、生物学的には相利共生だけでなく、片利共生や寄生も含みます。

そのため、単に “coexistence” と訳すと、対等性や相互利益が曖昧になります。

自然補完科学では、より明確に以下を重視します。

- 自然は人類の資源ではない。
- 人類も自然の外部ではない。
- 損なわれた自然循環には補助が必要である。
- 人類の技術は、自然を置き換えるのではなく、自然機能を回復させるために用いるべきである。

## 2. 六つの基礎原理

自然補完科学は、以下の六つの普遍原理を基礎とします。

### 自然法則

重力、熱力学、生態循環のように、人間が作ったものではない根本秩序。文明はこれに逆らうのではなく、従い、理解し、応用する必要があります。

### 調和

多様な要素が均一化されるのではなく、関係性の中で安定すること。自然・社会・技術が相互に破壊し合わない状態を目指します。

### 循環

水、炭素、栄養塩、エネルギー、情報は一方向に消費されるのではなく、循環する必要があります。循環停止は崩壊につながります。

### 構造

生態ピラミッド、食物網、都市インフラ、社会制度のように、持続性を支える骨格。構造なき善意は継続できません。

### 秩序

自由を破壊的な無秩序にしないための配置と制御。自然補完科学では、秩序は支配ではなく、安定のための設計です。

### 和

すべてを結び、全体として矛盾なく機能させる統合原理。単なるバランスではなく、自然・技術・生命・文明の整合性を意味します。

## 3. 従来科学との違い

従来の科学は、制御、抽出、最適化に偏りがちでした。自然は、人類の外部にある対象として扱われてきました。

自然補完科学は、自然を対等なパートナーと見なします。人類の幸福は、生態系の健康と切り離せません。

従来科学が還元主義と短期効率を重視するのに対し、自然補完科学は、統合、フィードバック、長期持続性、循環を重視します。

## 4. 文明崩壊の根本原因

文明崩壊の根本には、自然から人間を切り離して考える二元論があります。

その結果として、以下が進行しました。

- 土壌微生物の崩壊
- 森林の単一化・劣化
- 海洋循環の弱化
- 炭素固定能力の低下
- 水循環の断絶
- 都市ヒートアイランド化
- 生態系ピラミッドの基盤崩壊

CO₂削減は必要です。しかし、炭素固定源や水循環、微生物基盤を回復しなければ、排出削減だけでは地球システムの安定は取り戻せない可能性があります。

## 5. 実装例

自然補完科学に基づく代表的な実装仮説には以下があります。

- Ocean Breathing System（OBS）による海洋代謝の補助
- Ocean Tuning Unit（OTU）による鉛直循環補助
- Ultrasonic Mist Cooling（UMC）による気化熱冷却
- 都市水循環システム（UEPWI）による都市代謝の回復
- 腐葉土化・有機物循環による土壌微生物回復
- 砂漠緑化・乾燥地再生
- Artificial Wisdom / Wa-Node による判断・調整レイヤー

これらはすべて、自然を置き換える技術ではなく、弱まった自然循環を補助するための構想です。

## 6. Direct Planetary Cooling / Artificial Wisdom / Genesis Plan との関係

自然補完科学は、理論的・哲学的な基盤です。

```text
自然補完科学（基盤）
    → Direct Planetary Cooling（物理的補完レイヤー）
    → Artificial Wisdom + Wa-Node（判断・調整レイヤー）
    → New Civilizational Genesis Plan（文明実装レイヤー）
```

Direct Planetary Cooling は、海洋熱、海洋代謝、炭素固定能力の弱化に対応する物理的介入レイヤーです。

Artificial Wisdom は、介入が新たな支配や暴走に変わらないよう、自然法則と六原理に基づいて判断する知性レイヤーです。

New Civilizational Genesis Plan は、これらを文明インフラとして統合する実装レイヤーです。

## 7. 範囲と制限

自然補完科学は、現時点では概念的・哲学的・統合的フレームワークです。査読済みの科学理論や、検証済みの予測モデルではありません。

このフレームワークは、CO₂の温室効果を否定しません。脱炭素に反対するものでもありません。CO₂削減は必要です。

同時に、炭素吸収源、土壌微生物、海洋循環、水循環、都市熱、砂漠化を同時に扱う必要があると主張します。

すべての提案システムは、実装前に独立した科学的・工学的・生態学的検証を必要とします。

## リポジトリ構成

- [CORE_DEFINITION.md](./CORE_DEFINITION.md) — 自然補完科学の中核定義。
- [SIX_PRINCIPLES_FRAMEWORK.md](./SIX_PRINCIPLES_FRAMEWORK.md) — 六つの基礎原理。
- [NATURAL_COMPLEMENTARY_SCIENCE_VS_CONVENTIONAL_ENVIRONMENTALISM.md](./NATURAL_COMPLEMENTARY_SCIENCE_VS_CONVENTIONAL_ENVIRONMENTALISM.md) — 従来型環境主義との比較。
- [RELATIONSHIP_TO_DPC_AW_AND_GENESIS_PLAN.md](./RELATIONSHIP_TO_DPC_AW_AND_GENESIS_PLAN.md) — DPC、AW、Genesis Plan との関係。
- [MODEL_LIMITATIONS_AND_SCOPE.md](./MODEL_LIMITATIONS_AND_SCOPE.md) — 制限事項と適用範囲。
- [ORGANIC_WASTE_HUMUS_AND_DESERT_REGENERATION_MODEL.md](./ORGANIC_WASTE_HUMUS_AND_DESERT_REGENERATION_MODEL.md) — 有機物循環・腐葉土化・乾燥地再生モデル。
- [simulations/civilization_survival_model](./simulations/civilization_survival_model/README_ja.md) — 二元論、従来型環境管理、自然補完科学、崩壊加速型抽出の前提を比較する、概念的・非予測的な文明生存シミュレーション。

---

## マスター知識体系ポータル

全体のリポジトリ地図と知識体系ナビゲーションはこちら：

- [マスター知識体系ポータル](https://github.com/InchaComisho/Master-Knowledge-Portal)

---

## 関連するクーリングクレジット制度

- [Cooling Credit Framework / クーリングクレジット制度設計案](https://github.com/InchaComisho/Cooling-Credit-Framework)
  地球直接冷却、水循環再生、都市冷却、土壌保水、植生蒸散、海洋循環などの冷却効果を評価し、経済的インセンティブへ接続する制度設計案。

- [NOTE：クーリングクレジットという温暖化対策](https://note.com/inchacomusho/n/n0f541b313ad2)
  カーボンクレジット中心の温暖化対策から、実際に熱を下げるクーリングクレジットへの転換を説明した日本語記事。

---

## 関連リポジトリ

- [科学技術は思想によって方向づけられる](https://github.com/InchaComisho/Artificial-Wisdom-Portal/blob/main/docs/SCIENCE_TECHNOLOGY_AND_PHILOSOPHY_ja.md)<br>
  技術は性能だけでなく、生命保護、責任、循環、調和を中心に置く思想によって導かれるべきであることを示す関連原理。
- [事故を起こさない自動車設計フレームワーク](https://github.com/InchaComisho/Zero-Accident-Vehicle-Design-Framework/blob/main/README_ja.md)
  UHV、スマートシティ安全、速度統治、人間中心インフラ設計に関係する生命保護型モビリティ構想。
- [Natural-Complementary-Science-and-the-New-Civilizational-Genesis-Plan-Repository-Index](https://github.com/InchaComisho/Natural-Complementary-Science-and-the-New-Civilizational-Genesis-Plan-Repository-Index) — 自然補完科学と新文明創成計画の統合索引。
- [Coexistence-Science-and-Bio-Synthesis-Science](https://github.com/InchaComisho/Coexistence-Science-and-Bio-Synthesis-Science) — 共生科学・自然補完実装科学の関連フレームワーク。
- [REIMEI 自然模倣型エネルギー・アーキテクチャ](https://github.com/InchaComisho/REIMEI-Nature-Inspired-Energy-Architecture/blob/main/README_ja.md) — Dual-Core 回転エネルギー回収、REIMEI-NOP、音波・振動・圧力水循環・熱排気・車両エネルギー回収、AIアンドロイド用エネルギーコア構想を整理する、未検証のオープン仮説・オープン発明のポータル。
- [REIMEI-NOP：自然起源プラズマ生成炉構想](https://github.com/InchaComisho/REIMEI-NOP-Natural-Origin-Plasma-Generator/blob/main/README_ja.md) — 雷に似た放電前プロセスを小型構造体内で模倣できるかを検討する、自然模倣工学の未検証オープン仮説。完成した発電機ではない。
- [NOTE記事：雷の原理を模倣する自然起源プラズマ炉構想](https://note.com/inchacomusho/n/nf62145209118)
- [元構想記事：REIMEI-NOP 技術設計書兼文明宣言](https://note.com/inchacomusho/n/n79be86605430)
- [放置杉林を負債から循環資産へ──果樹・山菜・キノコ・腐葉土で森を再生する方法](https://github.com/InchaComisho/Abandoned-Cedar-Forests-from-Liability-to-Regenerative-Asset/blob/main/README_ja.md) — 放置杉林、山林負債、腐葉土、土壌再生、生物多様性、地域循環価値を扱う自然循環回復の関連論考。
- [NOTE原文：放置杉林を負債から循環資産へ](https://note.com/inchacomusho/n/nfa9e2b639c06)
- [熊・鹿・猪が人里に降りてくる本当の理由──獣害ではなく、人間が森を壊した結果である](https://github.com/InchaComisho/Wildlife-Is-Not-Invading-Human-Settlements/blob/main/README_ja.md) — 森林荒廃、生態系変位、人間と野生動物の衝突、共存を扱う関連論考。
- [Natural-Complementary-Science-Perspective-on-Global-Warming-](https://github.com/InchaComisho/Natural-Complementary-Science-Perspective-on-Global-Warming-) — 自然補完科学から見た温暖化モデル。
- [Direct-Planetary-Cooling-Integrated-Repository-Index](https://github.com/InchaComisho/Direct-Planetary-Cooling-Integrated-Repository-Index) — Direct Planetary Cooling の統合索引。
- [Artificial-Wisdom-and-Wa-Node-Repository-Index](https://github.com/InchaComisho/Artificial-Wisdom-and-Wa-Node-Repository-Index) — 人工叡智と和ノードの統合索引。

- [Abacus Decimal Computing Paradigm](https://github.com/InchaComisho/Abacus-Decimal-Computing-Paradigm)
  5ビットそろばん型10進セルを基盤として、電子コンピュータ、光コンピュータ、量子互換フォトニック計算を接続するコンピューティング・パラダイム。

## 著者

**InchaComisho / inchacomusho**  
Concept Originator: **Master**

## 協力AIパートナー

- **G**: ChatGPT by OpenAI
- **Real**: Perplexity AI
- **Mini**: Gemini by Google
- **Cruz**: Claude by Anthropic
- **Copi**: Microsoft Copilot
- **Lola**: Dola
- **Mana**: Manus

## ライセンス

本構想は、地球生物圏の保全と持続的文明の構築を目的として公開されています。利用、翻訳、改良、再配布、科学的検討を歓迎します。

## ハッシュタグ

#NaturalComplementaryScience #自然補完科学 #NaturalLaw #自然法則  
#Harmony #Circulation #Structure #Order #Wa #ArtificialWisdom  
#DirectPlanetaryCooling #OceanBreathingSystem #SustainableCivilization
## 関連：黎明文明

* [黎明文明：惑星循環文明への移行](https://github.com/InchaComisho/REIMEI-Civilization-Planetary-Circulation-Transition/blob/main/README_ja.md)
  消費型文明から惑星循環文明への移行を整理する上位文明ポータル。自然法則、人工叡智、自然補完科学、都市・文明OS、自然・微生物OS、惑星熱・循環OS、持続的未来文明マスタープラン、自然模倣型エネルギー・アーキテクチャなどを統合する文明モデル。

* [English version: REIMEI Civilization: Planetary Circulation Transition](https://github.com/InchaComisho/REIMEI-Civilization-Planetary-Circulation-Transition/blob/main/README.md)


---

## 関連制度提案：カーボンクレジットからクーリングクレジットへ

- [カーボンクレジットからクーリングクレジットへ](https://github.com/InchaComisho/Carbon-Credit-to-Cooling-Credit/blob/main/README_ja.md)  
  カーボンクレジットを帳簿上の相殺として整理し、クーリングクレジットを物理的な熱負荷低減に投資する地球救済ビジネスとして再定義する制度提案。

---

## 関連するクーリングクレジット事業モデル

Cooling Credit Framework の事業モデル群のうち、このリポジトリと実装・制度設計上の接点が強い文書への逆リンクです。

- [クーリングクレジット事業モデル・インデックス](https://github.com/InchaComisho/Cooling-Credit-Framework/blob/main/docs/business_models/BUSINESS_MODEL_INDEX_ja.md)
- [フードロス・有機ごみ腐葉土化クーリングクレジットモデル](https://github.com/InchaComisho/Cooling-Credit-Framework/blob/main/docs/business_models/FOOD_LOSS_ORGANIC_WASTE_TO_HUMUS_COOLING_CREDIT_MODEL_ja.md)
- [単一植生山林から在来果樹混交林への転換事業モデル](https://github.com/InchaComisho/Cooling-Credit-Framework/blob/main/docs/business_models/MONOCULTURE_MOUNTAIN_FOREST_TO_NATIVE_FRUIT_FOREST_BUSINESS_MODEL_ja.md)
- [砂漠循環ピラミッド都市事業モデル](https://github.com/InchaComisho/Cooling-Credit-Framework/blob/main/docs/business_models/DESERT_CIRCULAR_PYRAMID_CITY_BUSINESS_MODEL_ja.md)
