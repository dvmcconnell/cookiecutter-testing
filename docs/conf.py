"""Sphinx configuration."""
project = "Cookiecutter Testing"
author = "dmc"
copyright = "2023, dmc"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
