from typing import Literal, get_args

type FontSize = Literal[
    10,
    12,
    16,
]
font_sizes = list[FontSize](get_args(FontSize.__value__))
