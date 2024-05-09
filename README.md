# Packaging Python Projects

## Create/activate python environment
'''py
python3 -m venv env
source env/bin/activate
pip install setuptools
pip install wheel
'''

## Get repository
'''bash
git clone https://github.com/alexiatoumpa/packaging_python_projects.git
cd packaging_python_projects
'''

## Create wheel package
'''bash
cd packaging_python_projects
python setup.py bdist_wheel
'''

## Install wheel package
'''bash
cd dist
pip install <wheel_package_name>.whl
'''
