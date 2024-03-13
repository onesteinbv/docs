# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Onestein'
copyright = '2024, Onestein B.V.'
author = 'Onestein'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ["custom.css"]


html_short_title = 'Onestein'
html_title = 'Onestein'

html_logo = 'logo-blauw.png'
html_favicon = 'favicon.png'
html_show_sphinx = True
html_show_copyright = True
html_show_sourcelink = False
body_min_width = 0
body_max_width = 'none'

globaltoc_collapse = True