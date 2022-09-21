# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'IT Drafts'
copyright = '2022, Jeff Scrum'
author = 'Jeff Scrum'
language = 'en'
source_encoding = 'utf-8'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'sphinx.ext.githubpages', # Create .nojekyll file for gh-pages
	'sphinx_rtd_theme',
	'notfound.extension', #
	'sphinx_copybutton',
	'sphinx_sitemap',
	'sphinx-favicon'
	#'sphinx_last_updated_by_git'
	#'sphinx_togglebutton', # https://pypi.org/project/sphinx-togglebutton/
	#'sphinx_tabs.tabs' # https://sphinx-tabs.readthedocs.io/en/latest/
]

# -- sphinx-notfound-page --------------------------------------------------
# https://sphinx-notfound-page.readthedocs.io/en/latest/configuration.html
notfound_urls_prefix = None


# -- sphinx-sitemap --------------------------------------------------------
# https://pypi.org/project/sphinx-sitemap/
sitemap_filename = "sitemap.xml"


# -- sphinx-favicon --------------------------------------------------------
favicons = [
    {
        "rel": "icon",
        "href": "favicon/favicon.ico",
        "type": "image/x-icon",
    },
    {
        "rel": "icon",
        "sizes": "16x16",
        "href": "favicon/favicon-16x16.png",
        "type": "image/png",
    },
    {
        "rel": "icon",
        "sizes": "32x32",
        "href": "favicon/favicon-32x32.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "favicon/apple-touch-icon.png",
        "type": "image/png",
    },
]



# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
#html_favicon = '_static/images/favicon.ico'
html_baseurl = 'https://pages.ksomov.ru'
html_title = 'IT Drafts'
html_theme_options = {
    'analytics_id': 'G-NP47XWF3FQ',
    'analytics_anonymize_ip': False
}

# A list of paths that contain extra files not directly related to the documentation, such as robots.txt or .htaccess.
# Relative paths are taken as relative to the configuration directory. They are copied to the output directory.
# They will overwrite any existing file of the same name.
html_extra_path = ['robots.txt']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/theme.css',
]

#
html_copy_source = False


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# replace "view page source" with "edit on github" in Read The Docs theme
#  * https://github.com/readthedocs/sphinx_rtd_theme/issues/529
html_context = {
  'display_github': True,
  'github_user': 'jeffscrum',
  'github_repo': 'itdrafts',
  'github_version': 'master/source/',
}


