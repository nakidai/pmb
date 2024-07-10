PythonMonoBuilder
--
This tool can build project of structure like
```
pmbproject.toml
src/
    firstproject/
    firstproject1/
    secondproject/
    ...
```
Project that uses pmb to build has compatible file structure with regular
`pyproject.toml` files, but `pyproject.toml` will build only 1 package, while
this project can create several ones.

Usage
--
Call `pmb` from the root (directory that contains `pmbproject.toml`)

How does it work?
--
It generates python projects (one for each package) with contents in
`pyproject.toml` based on info from `pmbproject.toml` and then installs it
