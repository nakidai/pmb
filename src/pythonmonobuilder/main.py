from toml import load

from .builder import build


def main() -> None:
    with open("pmbproject.toml", 'r') as f:
        info = load(f)
    build(info)
