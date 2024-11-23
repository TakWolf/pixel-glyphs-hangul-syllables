from loguru import logger

from tools.configs import path_define, FontSize
from tools.utils import hangul_util
from tools.utils.part_bitmap import PartBitmap


class DesignContext:
    @staticmethod
    def load(font_size: FontSize) -> 'DesignContext':
        parts_dir = path_define.parts_dir.joinpath(str(font_size))

        trailing_parts = {}
        trailing_jamo_dir = parts_dir.joinpath('trailing')
        if trailing_jamo_dir.is_dir():
            for file_path in trailing_jamo_dir.iterdir():
                if file_path.suffix != '.png':
                    continue
                trailing_parts[file_path.stem] = PartBitmap.load_png(file_path)

        return DesignContext(trailing_parts)

    trailing_parts: dict[str, PartBitmap]

    def __init__(
            self,
            trailing_parts: dict[str, PartBitmap],
    ):
        self.trailing_parts = trailing_parts


def make_glyphs(font_size: FontSize):
    outputs_dir = path_define.outputs_dir.joinpath(str(font_size), 'AC00-D7AF Hangul Syllables')
    outputs_dir.mkdir(parents=True, exist_ok=True)

    design_context = DesignContext.load(font_size)
    for syllable in hangul_util.iter_syllables():
        if syllable.trailing_jamo is None:
            canvas = PartBitmap.create(font_size - 1, font_size - 1, -1)
        elif syllable.trailing_jamo.c in design_context.trailing_parts:
            canvas = design_context.trailing_parts[syllable.trailing_jamo.c].copy()
        else:
            continue

        for canvas_row in canvas:
            for x, alpha in enumerate(canvas_row):
                if alpha == -1:
                    canvas_row[x] = 0
        canvas.save_png(outputs_dir.joinpath(f'{syllable.code_point:04X}.png'))
    logger.info("Make glyphs: {}px", font_size)
