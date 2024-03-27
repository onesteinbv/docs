# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Curq'
copyright = '2024, Onestein B.V.'
author = 'Onestein'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = []
extensions = [
    "sphinx_github_changelog",
]
sphinx_github_changelog_token = os.environ.get("GIT_ACCESS_KEY") or ''

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ["custom.css"]


html_short_title = 'Curq'
html_title = ''

html_logo = 'Curq_Banner.png'
html_favicon = 'Curq_favicon.png'
html_show_sphinx = False
html_show_copyright = True
html_show_sourcelink = False
body_min_width = 0
body_max_width = 'none'

globaltoc_collapse = True
