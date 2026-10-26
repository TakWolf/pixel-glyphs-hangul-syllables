from zipfile import ZipFile

from loguru import logger

from tools.config import paths, project
from tools.config.spec import GlyphSpec


def make_release_zip(glyph_spec: GlyphSpec) -> None:
    paths.RELEASES_DIR.mkdir(parents=True, exist_ok=True)

    zip_file_path = paths.RELEASES_DIR.joinpath(f'pixel-glyphs-hangul-syllables-{glyph_spec.glyph_size}px-{glyph_spec.glyph_style}-v{project.VERSION}.zip')
    with ZipFile(zip_file_path, 'w') as file:
        file.write(paths.PROJECT_ROOT_DIR.joinpath('LICENSE-OFL'), 'OFL.txt')

        outputs_dir = paths.OUTPUTS_DIR.joinpath(f'{glyph_spec.glyph_size}-{glyph_spec.glyph_style}')
        for file_path in sorted(outputs_dir.rglob('*.png')):
            if not file_path.is_file():
                continue
            file.write(file_path, file_path.relative_to(outputs_dir))
    logger.info('Make release zip: {!r}', str(zip_file_path))
