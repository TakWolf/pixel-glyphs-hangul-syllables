from scripts import configs
from scripts.configs import path_define
from scripts.services import glyph_service, publish_service
from scripts.utils import fs_util


def main():
    fs_util.delete_dir(path_define.outputs_dir)
    fs_util.delete_dir(path_define.releases_dir)

    for font_size in configs.font_sizes:

        # TODO

        publish_service.make_release_zip(font_size)


if __name__ == '__main__':
    main()
