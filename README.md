# Packaging Python Projects

## Create Package

### Create/activate python environment

```py
cd pyenv/
python3 -m venv env
source env/bin/activate

pip install setuptools
pip install wheel
```

### Get repository

```bash
cd ~/dev/
git clone https://github.com/alexiatoumpa/packaging_python_projects.git
```

### Create wheel package

```bash
cd packaging_python_projects
python setup.py bdist_wheel
```

### Install wheel package

```bash
cd dist
pip install <wheel_package_name>.whl
```

Check that package is installed in the python's environment:

| Package | Version |
|--|--|
|myproject| 1.0 |

### Uninstall wheel package

```bash
pip uninstall myproject
```

## Test Package
