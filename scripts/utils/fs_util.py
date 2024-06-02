import shutil
import tomllib
from pathlib import Path
from typing import Any


def delete_dir(path: Path):
    if path.exists():
        shutil.rmtree(path)


def read_toml(path: Path) -> Any:
    return tomllib.loads(path.read_text('utf-8'))
