"""Sphinx configuration."""
project = "Cookiecutter Testing"
author = "Default Author"
copyright = "2023, Default Author"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
