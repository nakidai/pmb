from os import makedirs
from subprocess import check_call
from shutil import copytree
from sys import executable

from toml import dump


def build(info: dict[str, dict], builddir: str = "build") -> None:
    makedirs(f"{builddir}/dist", exist_ok=True)
    for project in info:
        path = f"{builddir}/src/{project}"
        for module in info[project]["meta"]["modules"]:
            makedirs(f"{path}/src/{module}", exist_ok=True)
            copytree(f"src/{module}", f"{path}/src/{module}", dirs_exist_ok=True)
        with open(f"{path}/pyproject.toml", 'w') as f:
            dump(info[project], f)
        check_call([executable, "-m", "build", "-s", "-o", f"{builddir}/dist", path])
