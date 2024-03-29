from setuptools import setup, find_packages
from codecs import open
from pathlib import Path

import tomli

with open("pyproject.toml", "rb") as f:
    pyproject = tomli.load(f)


setup(
    name=pyproject["tool"]["poetry"]["name"],
    version=pyproject["tool"]["poetry"]["version"],
    packages=find_packages(),
    install_requires=[
        "pydantic==2.5.3",
        "aiohttp>=3.9.1",
        "tomli==2.0.1"
    ],
    author='Snayt1k3',
    author_email='snayt1k3twitch@gmail.com',
    description='Description of your library',
    url='https://github.com/Snayt1k3/shiki.py',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
