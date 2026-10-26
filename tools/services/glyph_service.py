from loguru import logger

from tools.config import paths
from tools.config.spec import GlyphSpec


def make_glyphs(glyph_spec: GlyphSpec) -> None:
    outputs_dir = paths.OUTPUTS_DIR.joinpath(f'{glyph_spec.glyph_size}-{glyph_spec.glyph_style}', 'AC00-D7AF Hangul Syllables')
    outputs_dir.mkdir(parents=True, exist_ok=True)

    # TODO

    logger.info("Make glyphs: {}px {}", glyph_spec.glyph_size, glyph_spec.glyph_style)
