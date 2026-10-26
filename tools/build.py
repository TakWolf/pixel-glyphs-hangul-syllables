import shutil

from tools.config import paths, options
from tools.services import glyph_service, publish_service


def main() -> None:
    if paths.BUILD_DIR.exists():
        shutil.rmtree(paths.BUILD_DIR)

    for glyph_spec in options.GLYPH_SPECS:
        glyph_service.make_glyphs(glyph_spec)
        publish_service.make_release_zip(glyph_spec)


if __name__ == '__main__':
    main()
