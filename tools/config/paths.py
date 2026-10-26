from pathlib import Path

PROJECT_ROOT_DIR = Path(__file__).parents[2]

ASSETS_DIR = PROJECT_ROOT_DIR.joinpath('assets')
PARTS_DIR = ASSETS_DIR.joinpath('parts')

BUILD_DIR = PROJECT_ROOT_DIR.joinpath('build')
OUTPUTS_DIR = BUILD_DIR.joinpath('outputs')
RELEASES_DIR = BUILD_DIR.joinpath('releases')
