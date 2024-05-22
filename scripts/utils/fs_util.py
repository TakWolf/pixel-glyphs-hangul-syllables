import os
import shutil
import tomllib


def delete_dir(path: str | bytes | os.PathLike[str] | os.PathLike[bytes]):
    if os.path.exists(path):
        shutil.rmtree(path)


def read_toml(path: str | bytes | os.PathLike[str] | os.PathLike[bytes]) -> dict:
    with open(path, 'r', encoding='utf-8') as file:
        return tomllib.loads(file.read())
