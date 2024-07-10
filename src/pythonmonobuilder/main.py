import argparse
from toml import load
from pathlib import Path

from .builder import build, install


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="pmb"
    )
    parser.add_argument(
        "action", nargs="?",
        type=str,
        choices=["build", "install"],
        default="build"
    )
    parser.add_argument(
        "-b", "--builddir",
        type=Path,
        default="build",
        help="Project where store build files"
    )
    parser.add_argument(
        "-f", "--file",
        type=Path,
        default="pmbproject.toml",
        help="Project file"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true"
    )
    
    args = parser.parse_args()
    with open(args.file, 'r') as f:
        info = load(f)
    build(info, args.builddir, args.verbose)
    if args.action == "install":
        install(args.builddir, args.verbose)
