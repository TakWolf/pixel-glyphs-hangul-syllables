from loguru import logger
from pixel_font_knife.mono_bitmap import MonoBitmap

from tools.configs import path_define, FontSize
from tools.utils import hangul_util


def make_glyphs(font_size: FontSize):
    outputs_dir = path_define.outputs_dir.joinpath(str(font_size), 'AC00-D7AF Hangul Syllables')
    outputs_dir.mkdir(parents=True, exist_ok=True)

    for syllable in hangul_util.iter_syllables():
        canvas = MonoBitmap.create(font_size, font_size)
        canvas.save_png(outputs_dir.joinpath(f'{syllable.code_point:04X}.png'))
    logger.info("Make glyphs: {}px", font_size)
