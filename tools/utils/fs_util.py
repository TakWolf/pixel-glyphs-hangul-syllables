import shutil
from pathlib import Path


def delete_dir(path: Path):
    if path.exists():
        shutil.rmtree(path)
