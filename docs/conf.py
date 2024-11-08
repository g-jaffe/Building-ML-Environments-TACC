# Configuration file for the Sphinx documentation builder.

import sphinx_rtd_theme

# -- Project information

project = 'Building ML Environments at TACC'
copyright = '2024, Texas Advanced Computing Center'
author = 'Texas Advanced Computing Center'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# TACC logo
html_logo = 'images/TACC-White-No-Mask.png'

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
