# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
#
# Astropy documentation build configuration file.
#
# This file is execfile()d with the current directory set to its containing
# dir.
#
# Note that not all possible configuration values are present in this file.
#
# All configuration values have a default. Some values are defined in
# the global Astropy configuration which is loaded here before anything else.
# See sphinx_astropy.conf for which values are set there.

import datetime
import os
import sys
from pkg_resources import get_distribution

# Load all of the global Astropy configuration
try:
    from sphinx_astropy.conf.v1 import *  # noqa
except ImportError:
    print('ERROR: the documentation requires the sphinx-astropy package '
          'to be installed')
    sys.exit(1)

# Get configuration information from setup.cfg
from configparser import ConfigParser
conf = ConfigParser()
conf.read([os.path.join(os.path.dirname(__file__), '..', 'setup.cfg')])
setup_cfg = dict(conf.items('metadata'))

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.2'

# To perform a Sphinx version check that needs to be more specific than
# major.minor, call `check_sphinx_version("x.y.z")` here.
# check_sphinx_version("1.2.1")

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns.append('_templates')  # noqa

# This is added to the end of RST files - a good place to put substitutions to
# be used globally.
rst_epilog += """
"""

# -- Project information ------------------------------------------------------

# This does not *have* to match the package name, but typically does
project = setup_cfg['name']
author = setup_cfg['author']
copyright = f'{datetime.datetime.now().year}, {author}'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The full version, including alpha/beta/rc tags.
release = get_distribution(project).version
# The short X.Y version.
version = '.'.join(release.split('.')[:2])

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['stsynphot.']

# -- Options for HTML output --------------------------------------------------

# A NOTE ON HTML THEMES
# The global astropy configuration uses a custom theme, 'bootstrap-astropy',
# which is installed along with astropy. A different theme can be used or
# the options for this theme can be modified by overriding some of the
# variables set in the global configuration. The variables set in the
# global configuration are listed below, commented out.

# Add any paths that contain custom themes here, relative to this directory.
# To use a different custom theme, add the directory containing the theme.
# html_theme_path = []

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes. To override the custom theme, set this to the
# name of a builtin theme or the name of a custom theme in html_theme_path.
# html_theme = None

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Logo
html_logo = '_static/stsci_logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = ''

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = ''

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = f'{project} v{release}'

# Output file base name for HTML help builder.
htmlhelp_basename = project + 'doc'

# -- Options for LaTeX output -------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual])
latex_documents = [('index', project + '.tex', project + u' Documentation',
                    author, 'manual')]


# -- Options for manual page output -------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [('index', project.lower(), project + u' Documentation',
              [author], 1)]


# -- Options for intersphinx --------------------------------------------------

intersphinx_mapping.update({
    'astropy': ('https://docs.astropy.org/en/latest/', None),
    'synphot': ('https://synphot.readthedocs.io/en/latest/', None)})


# -- Options for linkcheck output ---------------------------------------------
linkcheck_retry = 5
linkcheck_ignore = ['https://hsthelp.stsci.edu',
                    'http://ssb.stsci.edu',
                    'http://www.stsci.edu',
                    'https://www.as.arizona.edu/observing',
                    'https://phoenix.ens-lyon.fr/simulator/index.faces',
                    'https://wfirst.gsfc.nasa.gov/science/WFIRST_Reference_Information.html']
linkcheck_timeout = 180
linkcheck_anchors = False
