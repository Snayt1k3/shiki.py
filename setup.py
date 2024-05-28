from codecs import open
from pathlib import Path

import tomli
from setuptools import setup, find_packages

with open("pyproject.toml", "rb") as f:
    pyproject = tomli.load(f)


def get_long_description() -> str:
    return (Path(__file__).parent / "README.md").read_text()


extra_requirements = {
    "readthedocs": [
        "furo",
        "readthedocs-sphinx-search",
        "Sphinx",
        "sphinx-hoverxref",
    ]
}

setup(
    name=pyproject["tool"]["poetry"]["name"],
    version=pyproject["tool"]["poetry"]["version"],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    extras_require=extra_requirements,
    install_requires=["aiohttp>=3.9.1", "tomli>=2.0.1", "setuptools>=69.0.3"],
    author="Snayt1k3",
    author_email="snayt1k3@gmail.com",
    description=pyproject["tool"]["poetry"]["description"],
    long_description_content_type="text/markdown",
    long_description=get_long_description(),
    url="https://github.com/Snayt1k3/shiki.py",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
