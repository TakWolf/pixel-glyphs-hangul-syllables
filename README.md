# 像素字形 - 谚文音节

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/TakWolf/pixel-glyphs-hangul-syllables?style=flat-square)](https://github.com/TakWolf/pixel-glyphs-hangul-syllables/releases)

`AC00..D7AF; Hangul Syllables`

## 原理

一个现代谚文音节由初声、中声和可选的终声组成：

- 初声：位于音节开头的辅音，共 19 个。
- 中声：构成音节核心的元音，共 21 个。
- 终声：位于音节末尾的辅音，也称收音，共 27 个，另有无终声的情况。

### 初声

```text
ㄱ ㄲ ㄴ ㄷ ㄸ ㄹ ㅁ ㅂ ㅃ ㅅ ㅆ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅎ
```

### 中声

```text
ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ
```

### 终声

```text
ㄱ ㄲ ㄳ ㄴ ㄵ ㄶ ㄷ ㄹ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅁ ㅂ ㅄ ㅅ ㅆ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ
```

### 字形组合

初声和中声必须存在，终声可以省略。各部分在同一个方块内组合，布局取决于中声元音的形态：

- 竖向元音，如 `ㅏ`、`ㅓ`、`ㅣ`：初声在左，中声在右。
- 横向元音，如 `ㅗ`、`ㅜ`、`ㅡ`：初声在上，中声在下。
- 横竖组合元音，如 `ㅘ`、`ㅝ`、`ㅢ`：中声分布在初声的下方和右侧。

如果存在终声，则将其置于整个组合的底部。

### 编码顺序

Unicode 按上述字母顺序排列现代谚文音节，其中终声变化最快，中声次之，初声最慢。终声的排列以“无终声”为第一项，其后依次为上面列出的 27 个终声。

将初声、中声和终声的索引分别记为 `L`、`V`、`T`，均从 0 开始，则音节码位的计算公式为：

```text
码位 = 0xAC00 + (L × 21 + V) × 28 + T
```

其中：

- `L` 的取值范围为 0～18。
- `V` 的取值范围为 0～20。
- `T` 的取值范围为 0～27，其中 0 表示无终声。

因此，遍历所有初声、中声和终声的组合，即可生成全部 `19 × 21 × 28 = 11,172` 个现代谚文音节字形。

## 程序依赖

- [Pixel Font Knife](https://github.com/TakWolf/pixel-font-knife)
- [Loguru](https://github.com/Delgan/loguru)

## 许可证

分为「字形」和「程序」两个部分。

### 字形

采用 [SIL Open Font License version 1.1](LICENSE-OFL) 授权。

### 程序

采用 [MIT License](LICENSE-MIT) 授权。
