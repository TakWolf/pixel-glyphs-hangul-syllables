from pathlib import Path

project_root_dir = Path(__file__).parent.joinpath('..', '..').resolve()

assets_dir = project_root_dir.joinpath('assets')
fragments_dir = assets_dir.joinpath('fragments')

build_dir = project_root_dir.joinpath('build')
outputs_dir = build_dir.joinpath('outputs')
releases_dir = build_dir.joinpath('releases')
