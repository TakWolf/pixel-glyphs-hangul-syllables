from tools.configs import path_define, FontSize
from tools.utils.hangul_util import VowelLayoutType, LEADING_JAMOS, VOWEL_LAYOUT_JAMOS, TRAILING_JAMOS
from tools.utils.part_bitmap import PartBitmap


def format_parts(font_size: FontSize):
    parts_dir = path_define.parts_dir.joinpath(str(font_size))

    for layout_type in VowelLayoutType:
        for leading_jamo in LEADING_JAMOS:
            leading_jamo_dir = parts_dir.joinpath('leading', layout_type, leading_jamo)
            leading_jamo_dir.mkdir(parents=True, exist_ok=True)

    for layout_type, vowel_jamos in VOWEL_LAYOUT_JAMOS.items():
        for vowel_jamo in vowel_jamos:
            vowel_jamo_dir = parts_dir.joinpath('vowel', layout_type, vowel_jamo)
            vowel_jamo_dir.mkdir(parents=True, exist_ok=True)

    trailing_jamo_dir = parts_dir.joinpath('trailing')
    trailing_jamo_dir.mkdir(parents=True, exist_ok=True)
    for file_path in trailing_jamo_dir.iterdir():
        if file_path.suffix != '.png':
            continue
        assert file_path.stem in TRAILING_JAMOS, f"[{font_size}px] unknown trailing jamo part file: '{file_path}'"
        PartBitmap.load_png(file_path).save_png(file_path)
