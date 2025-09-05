# 像素字形 - 谚文音节

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/TakWolf/pixel-glyphs-hangul-syllables)](https://github.com/TakWolf/pixel-glyphs-hangul-syllables/releases)

`AC00 ~ D7AF; Hangul Syllables`

## 原理

一个谚文音节由初声辅音（声母）、中声元音（韵母）和终声辅音（韵尾）三个部分组成。

- 初声辅音（声母）共 19 个

```text
ㄱ ㄲ ㄴ ㄷ ㄸ ㄹ ㅁ ㅂ ㅃ ㅅ ㅆ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅎ
```

- 中声元音（韵母）共 21 个

```text
ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ
```

- 终声辅音（韵尾）共 27 个

```text
ㄱ ㄲ ㄳ ㄴ ㄵ ㄶ ㄷ ㄹ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅁ ㅂ ㅄ ㅅ ㅆ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ
```

声母和韵母一定存在，韵尾可以没有。每个音节，将声部按照“从左到右，自上而下”的方式组合而成。

在 Unicode 区块中，谚文音节按照规律依次排列。也就是说，按照上面的顺序进行排列组合，即可遍历全部的 `19 * 21 * (27 + 1) = 11172` 个音节字符。

## 程序依赖

- [Pixel Font Knife](https://github.com/TakWolf/pixel-font-knife)
- [Loguru](https://github.com/Delgan/loguru)

## 许可证

分为「字形」和「程序」两个部分。

### 字形

使用 [「SIL 开放字体许可证第 1.1 版」](LICENSE-OFL) 授权。

### 程序

使用 [「MIT 许可证」](LICENSE-MIT) 授权。
