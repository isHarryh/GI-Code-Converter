GI-Code-Converter
==========
Genius Invokation Code Converter, GICC.  
七圣召唤牌组分享码转换器  

<sup> This project only supports Chinese docs now. English docs will be translated later. </sup>

## 介绍 <sub>Intro</sub>
本项目旨在为“七圣召唤”的牌组分享码提供多语言的解码与编码的实现程序。这些元程序以算法精炼、易迁移性、低依赖性、高鲁棒性为目标。

<details>
<summary><b>术语</b></summary>

- “七圣召唤”（_Genius Invokation TCG_），是游戏《原神（_Genshin Impact_）》中的一种卡牌玩法。该玩法由2名玩家使用各自的牌组，按照一定的出牌顺序进行多轮对局，直到其中一方的角色牌全部被击倒时判定另一方获胜。

- 牌组（Deck），是由 3 张角色牌（Character Card）与 30 张行动牌（Action Card，包括装备牌、支援牌和事件牌）组成的 33 张卡牌的组合。

- 牌组分享码（Sharing Code，下简称“牌组码”），是代表某个特定牌组的完整卡牌组成的定长字符串。

- 解码（Decoding），在本项目中指的是将牌组码解析为 33 张卡牌的 ID 信息；编码（Encoding），则指的是将上述 ID 信息转换为牌组码。

</details>


## 实现概览 <sub>Overview</sub>
下表列出了目前各语言的解码与编码程序的实现情况。有关它们的 _环境要求、接口定义、用例和其他细节_，请查阅相应目录内的 README 文档。

|  | 解码 | 编码 | 作者 | 首次提交 |
|:---:|:---:|:---:|:---:|:---:|
| Python<br>`gicc-py` | √ | √ | Harry Huang | 2023-12-10 |
| C++<br>`gicc-cpp`  | 编码中 | 编码中 | Harry Huang | / |
| Java<br>`gicc-java`  | 计划中 | 计划中 | Harry Huang | / |
| JavaScript<br>`gicc-js`  | 计划中 | 计划中 | Harry Huang | / |


## 牌组码规则 <sub>Procedure</sub>
每个牌组码由 68 个 Base64 字符（包括 `A-Z`、`a-z`、`0-9`、`+` 和 `/`）组成，包含 33 个卡牌“位置”上所配置的卡牌的数字 ID 信息。

上述牌组码在经过常规 Base64 解码后，可转化为 408bit（68*6bit）长度的数据。其中只有前面的 396bit 有效，后面的 12bit 是用于补位的 `0`。

上述 396bit 数据在划分为 49.5Byte（8bit = 1Byte）后，令其中首个 Byte 的索引为 `0`。正确的读取顺序是，先从首个偶数索引 `0` 指向的 Byte 开始，依次读取每个“偶数 Byte”直到末尾，然后从首个奇数索引 `1` 指向的 Byte 开始，依次读取每个“奇数 Byte”直到末尾。读取过程中，每 12bit 代表的数值表示一个卡牌位置上的卡牌 ID。总共可读取 33 个卡牌 ID。

上述 33 个卡牌 ID，前 3 个 ID 为角色牌 ID，其顺序即为角色牌的实际顺序；后 30 个 ID 为手牌 ID，其顺序通常是各手牌 ID 的升序（ASC）。值为 `0` 的 ID 表示该位置没有卡牌；重复的 ID 表示多张相同的卡牌，但是各卡牌的最大数目不应超过相应的上限。

> 注意：  
> 上述编码规则由作者个人整理，如有错误欢迎斧正，如需引用请标明出处。

#### 牌组码示例
牌组码：
```
AvAA3wEOAAAg4D0PAxDQ8YEPCFAQ9pUPC2BA/LgPC9HQCr0QDLEgC9kQDeGQDt4QDfAA
```

对应的卡牌 ID 列表：
```
32, 1, 2, 61, 61, 129, 129, 149, 180, 184, 189, 189, 194, 217, 217, 222, 223, 223, 224, 224, 241, 241, 245, 246, 246, 252, 253, 266, 267, 267, 270, 270, 271
```

## 许可证 <sub>Licensing</sub>
本项目基于 **MIT 开源许可证**，详情参见 [License](https://github.com/isHarryh/GI-Code-Converter/blob/main/LICENSE) 页面。
