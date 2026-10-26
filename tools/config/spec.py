
class GlyphSpec:
    glyph_size: int
    glyph_style: str

    def __init__(
            self,
            glyph_size: int,
            glyph_style: str,
    ) -> None:
        self.glyph_size = glyph_size
        self.glyph_style = glyph_style
