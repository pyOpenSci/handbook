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

from datetime import datetime
import subprocess

current_year = datetime.now().year
organization_name = "pyOpenSci"

# -- Project information -----------------------------------------------------

project = "pyOpenSci Handbook"
copyright = f"{current_year}, {organization_name}"
author = "pyOpenSci"

# Get the latest Git tag - there might be a prettier way to do this but...
try:
    release_value = (
        subprocess.check_output(["git", "describe", "--tags"])
        .decode("utf-8")
        .strip()
    )
    release_value = release_value[:4]
except subprocess.CalledProcessError:
    release_value = "0.1"  # Default value in case there's no tag

# Update the release value
release = release_value

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_sitemap",
    "sphinxext.opengraph",
    "sphinx_favicon",
]

# colon fence for card support in md
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "attrs_block",
]

myst_heading_anchors = 3
# Link to our repo

# Sphinx_favicon is used now in favor of built in support
# https://pypi.org/project/sphinx-favicon/
favicons = [
    {"href": "https://www.pyopensci.org/images/favicon.ico"},
]

html_theme_options = {
    "announcement": "<p><a href='https://www.pyopensci.org/software-peer-review/about/intro.html'>Submit Your Python Package for Peer Review - Learn More!</a></p>",
    "external_links": [
        {
            "url": "https://www.pyopensci.org",
            "name": "pyOpenSci Website",
        },
        {
            "url": "https://www.pyopensci.org/python-package-guide",
            "name": "Packaging Guide",
        },
        {
            "url": "https://pyopensci.org/peer-review-guide",
            "name": "Peer Review Guide",
        },
    ],
    "icon_links": [
        {
            "name": "Mastodon",
            "url": "https://fosstodon.org/@pyOpenSci",
            "icon": "fa-brands fa-mastodon",
        },
    ],
    "logo": {
        "text": "Handbook",
        "image_dark": "logo-dark-mode.png",
        "image_light": "logo-light-mode.png",
        "alt_text": "pyOpenSci Handbook. The pyOpenSci logo is a purple flower with pyOpenSci under it. The o in open sci is the center of the flower",
    },
    "header_links_before_dropdown": 4,
    "use_edit_page_button": True,
    "show_nav_level": 2,
    "navigation_depth": 3,
    "show_toc_level": 1,
    # "navbar_align": "left",  # [left, content, right] For testing that the navbar items align properly
    "github_url": "https://github.com/pyopensci/governance",
    "footer_start": ["copyright"],
    "footer_end": [],
}

# html_theme_options["analytics"] = {
#     "google_analytics_id": "UA-141260825-1",
# }

html_context = {
    "github_user": "pyopensci",
    "github_repo": "governance",
    "github_version": "main",
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".github",
    ".nox",
    "README.md",
    "reference/2018-2020-orig-meeting-notes",
]

# For sitemap generation
html_baseurl = "https://www.pyopensci.org/governance/"
sitemap_url_scheme = "{link}"

# -- Options for HTML output -------------------------------------------------

html_theme = "pyos_sphinx_theme"
html_title = "pyOpenSci Handbook"
html_js_files = ["matomo.js"]


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Social cards
ogp_site_url = "https://www.pyopensci.org/governance/"
ogp_social_cards = {
    "line_color": "#6D597A",
    "image": "_static/logo-dark-mode.png",
}
