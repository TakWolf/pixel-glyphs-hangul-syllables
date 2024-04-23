import os

import png


def load_png(file_path: str | bytes | os.PathLike[str] | os.PathLike[bytes]) -> tuple[list[list[int]], int, int]:
    width, height, pixels, _ = png.Reader(filename=file_path).read()
    data = []
    for pixels_row in pixels:
        data_row = []
        for x in range(0, width * 4, 4):
            alpha = pixels_row[x + 3]
            if alpha > 127:
                data_row.append(1)
            else:
                data_row.append(0)
        data.append(data_row)
    return data, width, height


def save_png(
        data: list[list[int]],
        file_path: str | bytes | os.PathLike[str] | os.PathLike[bytes],
):
    pixels = []
    for data_row in data:
        pixels_row = []
        for x in data_row:
            pixels_row.append(0)
            pixels_row.append(0)
            pixels_row.append(0)
            if x == 0:
                pixels_row.append(0)
            else:
                pixels_row.append(255)
        pixels.append(pixels_row)
    png.from_array(pixels, 'RGBA').save(file_path)
