from collections.abc import Iterator
from enum import StrEnum
from typing import Final


class JamoType(StrEnum):
    LEADING = 'leading'
    VOWEL = 'vowel'
    TRAILING = 'trailing'


class VowelLayoutType(StrEnum):
    VERTICAL = 'vertical'
    HORIZONTAL = 'horizontal'
    WRAPPING = 'wrapping'


# 初声辅音（声母）共 19 个
LEADING_JAMOS: Final = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 中声元音（韵母）共 21 个
VOWEL_JAMOS: Final = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

# 终声辅音（韵尾）共 27 个
TRAILING_JAMOS: Final = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

VOWEL_LAYOUT_JAMOS: Final = {
    VowelLayoutType.VERTICAL: ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅣ'],
    VowelLayoutType.HORIZONTAL: ['ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ'],
    VowelLayoutType.WRAPPING: ['ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ'],
}


def _get_vowel_layout_type_by_chr(c: str) -> VowelLayoutType:
    for layout_type, jamos in VOWEL_LAYOUT_JAMOS.items():
        if c in jamos:
            return layout_type
    raise AssertionError('unknown layout type')


class LeadingJamo:
    @staticmethod
    def of(index: int):
        c = LEADING_JAMOS[index]
        return LeadingJamo(c)

    c: str

    def __init__(self, c: str):
        self.c = c


class VowelJamo:
    @staticmethod
    def of(index: int):
        c = VOWEL_JAMOS[index]
        layout_type = _get_vowel_layout_type_by_chr(c)
        return VowelJamo(c, layout_type)

    c: str
    layout_type: VowelLayoutType

    def __init__(self, c: str, layout_type: VowelLayoutType):
        self.c = c
        self.layout_type = layout_type


class TrailingJamo:
    @staticmethod
    def of(index: int):
        c = TRAILING_JAMOS[index]
        return TrailingJamo(c)

    c: str

    def __init__(self, c: str):
        self.c = c


class Syllable:
    @staticmethod
    def of(leading_index: int, vowel_index: int, trailing_index: int | None = None) -> 'Syllable':
        code_point = 0xAC00
        code_point += leading_index * len(VOWEL_JAMOS) * (len(TRAILING_JAMOS) + 1)
        code_point += vowel_index * (len(TRAILING_JAMOS) + 1)
        if trailing_index is not None:
            code_point += trailing_index + 1

        leading_jamo = LeadingJamo.of(leading_index)
        vowel_jamo = VowelJamo.of(vowel_index)
        trailing_jamo = TrailingJamo.of(trailing_index) if trailing_index is not None else None

        return Syllable(code_point, leading_jamo, vowel_jamo, trailing_jamo)

    code_point: int
    leading_jamo: LeadingJamo
    vowel_jamo: VowelJamo
    trailing_jamo: TrailingJamo | None

    def __init__(
            self,
            code_point: int,
            leading_jamo: LeadingJamo,
            vowel_jamo: VowelJamo,
            trailing_jamo: TrailingJamo | None = None,
    ):
        self.code_point = code_point
        self.leading_jamo = leading_jamo
        self.vowel_jamo = vowel_jamo
        self.trailing_jamo = trailing_jamo


def iter_syllables() -> Iterator[Syllable]:
    for leading_index in range(len(LEADING_JAMOS)):
        for vowel_index in range(len(VOWEL_JAMOS)):
            yield Syllable.of(leading_index, vowel_index)
            for trailing_index in range(len(TRAILING_JAMOS)):
                yield Syllable.of(leading_index, vowel_index, trailing_index)
