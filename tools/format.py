import sys

from pixel_font_knife.utils import fs_util

from tools.config import paths


def main() -> None:
    if sys.platform != 'win32':
        fs_util.format_glyph_files(paths.PARTS_DIR)


if __name__ == '__main__':
    main()
