from os import listdir, makedirs
from os.path import isfile
from shutil import copytree
from subprocess import check_call
from sys import executable

from toml import dump


def build(info: dict[str, dict], builddir: str = "build", verbose: bool = False) -> None:
    if verbose:
        print("Creating builddir")
    makedirs(f"{builddir}/dist", exist_ok=True)
    print(executable)
    for project in info:
        if verbose:
            print(f"Creating project {project}")
        path = f"{builddir}/src/{project}"
        for module in info[project]["meta"]["modules"]:
            makedirs(f"{path}/src/{module}", exist_ok=True)
            if verbose:
                print(f"Copying module {module}")
            copytree(f"src/{module}", f"{path}/src/{module}", dirs_exist_ok=True)
        if verbose:
            print("Generating pyproject.toml")
        with open(f"{path}/pyproject.toml", 'w') as f:
            dump(info[project], f)

        if verbose:
            print("Building")
        args = [executable, "-m", "build", "-s", "-o", f"{builddir}/dist", path]
        if verbose:
            args.append("-v")
        check_call(args)


def install(builddir: str = "build", verbose: bool = False) -> None:
    for filename in listdir(f"{builddir}/dist"):
        if isfile(path := f"{builddir}/dist/{filename}"):
            args = [executable, "-m", "pip", "install", path]
            if verbose:
                print("Installing {filename}")
                args.append("-v")
            check_call(args)
