from __future__ import annotations

import sys
from pathlib import Path

# add to path the root of the application
root = Path(__file__).parent.parent.parent / "src"
sys.path.insert(0, str(root))

# The import has warnings because it is not imported on top of the file
# Hence we add comments to avoid it refactored
# type: ignore
from setup import cfg  # noqa: E402

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = cfg["application"]["project"]
copyright = cfg["application"]["copyright"]
author = cfg["application"]["author"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.coverage", "sphinx.ext.napoleon"]

templates_path = ["_templates"]
exclude_patterns: list[str] = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "classic"
html_static_path = ["_static"]
