import shutil

from tools.configs import path_define, options
from tools.services import glyph_service, publish_service


def main():
    if path_define.BUILD_DIR.exists():
        shutil.rmtree(path_define.BUILD_DIR)

    for font_size in options.FONT_SIZES:
        glyph_service.make_glyphs(font_size)
        publish_service.make_release_zip(font_size)


if __name__ == '__main__':
    main()
