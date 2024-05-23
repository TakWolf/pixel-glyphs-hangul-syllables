import shutil
import tomllib
from pathlib import Path


def delete_dir(path: Path):
    if path.exists():
        shutil.rmtree(path)


def read_toml(path: Path) -> dict:
    return tomllib.loads(path.read_text('utf-8'))
