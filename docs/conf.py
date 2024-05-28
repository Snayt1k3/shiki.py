# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import tomli
import os
import sys

sys.path.insert(0, os.path.abspath(".."))
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
with open("../pyproject.toml", "rb") as f:
    pyproject = tomli.load(f)

_version: str = pyproject["tool"]["poetry"]["version"]
project = "shiki.py"
copyright = "2024, Snayt1k3"
author = "Snayt1k3"

release = _version
version = ".".join(_version.split(".", 2)[:2])

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
add_module_names = False
autosectionlabel_prefix_document = True
hoverxref_auto_ref = True
hoverxref_sphinxtabs = True

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "hoverxref.extension",
    "sphinx_search.extension",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "furo"
html_static_path = ["_static"]
autodoc_default_options = {"member-order": "bysource"}
intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
}
