# coding: utf-8

import re
import ast
from setuptools import setup

description = 'Interactive command line for elasticsearch.'


install_requirements = [
    'Pygments >= 2.0',  # Pygments has to be Capitalcased. WTF?
    'prompt_toolkit>=1.0.10,<1.1.0',
    'six==1.10.0',
    'wcwidth==0.1.7',
    'requests==2.13.0'
]

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('estoolkit/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='estoolkit',
    author='wonzbak',
    description=description,
    version=version,
    install_requires=install_requirements
)
