# Always prefer setuptools over distutils
import re
from os import path
from setuptools import setup, find_packages

project = 'globber'
here = path.abspath(path.dirname(__file__))

verstrline = open('{}/{}/__init__.py'.format(here, project), 'r').read()
version_re = r'^__version__ = [\'"]([^\'"]*)[\'"]'
match = re.search(version_re, verstrline, re.M)
if match:
    version = match.group(1)
else:
    raise RuntimeError('Unable to find version string in __init__.py')

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

extras_require = {
}

setup(
    name=project,
    packages=find_packages(),
    version=version,
    description='An asynchronous logger',
    keywords='logging tool',

    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/assisken/globber',
    author='assisken',
    author_email='assisken@ya.ru',

    install_requires=requirements,
    extras_require=extras_require,

    classifiers=[
        'Development Status :: 1 - Planning',

        'Intended Audience :: Developers',
        'Topic :: Utilities',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
