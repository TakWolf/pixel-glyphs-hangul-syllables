import shutil

from tools.configs import path_define, options
from tools.services import glyph_service, publish_service


def main():
    if path_define.build_dir.exists():
        shutil.rmtree(path_define.build_dir)

    for font_size in options.font_sizes:
        glyph_service.make_glyphs(font_size)
        publish_service.make_release_zip(font_size)


if __name__ == '__main__':
    main()
