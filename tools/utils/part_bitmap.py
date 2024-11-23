from collections import UserList
from os import PathLike
from typing import Any

import png


class PartBitmap(UserList[list[int]]):
    @staticmethod
    def load_png(file_path: str | PathLike[str]) -> 'PartBitmap':
        width, height, pixels, _ = png.Reader(filename=file_path).read()
        bitmap = PartBitmap()
        bitmap.width = width
        bitmap.height = height
        for pixels_row in pixels:
            bitmap_row = []
            for i in range(0, width * 4, 4):
                red = pixels_row[i]
                green = pixels_row[i + 1]
                blue = pixels_row[i + 2]
                alpha = pixels_row[i + 3]
                if red == 255 and green == 0 and blue == 255:
                    bitmap_row.append(-1)
                elif alpha > 127:
                    bitmap_row.append(1)
                else:
                    bitmap_row.append(0)
            bitmap.append(bitmap_row)
        return bitmap

    width: int
    height: int

    def __init__(self, bitmap: list[list[int]] | None = None):
        super().__init__()
        if bitmap is None:
            self.width = 0
            self.height = 0
        else:
            self.width = len(bitmap[0])
            self.height = len(bitmap)
            for bitmap_row in bitmap:
                if self.width != len(bitmap_row):
                    raise ValueError('rows with different widths')
                self.append([alpha if alpha == -1 or alpha == 0 else 1 for alpha in bitmap_row])

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, PartBitmap):
            return (self.width == other.width and
                    self.height == other.height and
                    super().__eq__(other))
        return super().__eq__(other)

    def save_png(self, file_path: str | PathLike[str]):
        pixels = []
        for bitmap_row in self:
            pixels_row = []
            for alpha in bitmap_row:
                if alpha == -1:
                    pixels_row.append(255)
                    pixels_row.append(0)
                    pixels_row.append(255)
                    pixels_row.append(255)
                elif alpha == 0:
                    pixels_row.append(0)
                    pixels_row.append(0)
                    pixels_row.append(0)
                    pixels_row.append(0)
                else:
                    pixels_row.append(0)
                    pixels_row.append(0)
                    pixels_row.append(0)
                    pixels_row.append(255)
            pixels.append(pixels_row)
        png.from_array(pixels, 'RGBA').save(file_path)
