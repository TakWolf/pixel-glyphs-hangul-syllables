from zipfile import ZipFile

from loguru import logger

from tools import configs
from tools.configs import path_define
from tools.configs.options import FontSize


def make_release_zip(font_size: FontSize) -> None:
    path_define.RELEASES_DIR.mkdir(parents=True, exist_ok=True)

    zip_file_path = path_define.RELEASES_DIR.joinpath(f'pixel-glyphs-hangul-syllables-{font_size}px-v{configs.VERSION}.zip')
    with ZipFile(zip_file_path, 'w') as file:
        file.write(path_define.PROJECT_ROOT_DIR.joinpath('LICENSE-OFL'), 'OFL.txt')

        outputs_dir = path_define.OUTPUTS_DIR.joinpath(str(font_size))
        for file_path in sorted(outputs_dir.rglob('*.png')):
            if not file_path.is_file():
                continue
            file.write(file_path, file_path.relative_to(outputs_dir))
    logger.info("Make release zip: '{}'", zip_file_path)
