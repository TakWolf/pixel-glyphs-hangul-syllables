import os

project_root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

assets_dir = os.path.join(project_root_dir, 'assets')
fragments_dir = os.path.join(assets_dir, 'fragments')

build_dir = os.path.join(project_root_dir, 'build')
outputs_dir = os.path.join(build_dir, 'outputs')
releases_dir = os.path.join(build_dir, 'releases')
