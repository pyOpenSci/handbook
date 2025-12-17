(github-repos-overview)=
# pyOpenSci GitHub repositories

pyOpenSci manages multiple GitHub repositories to support various community
activities. Below is a description of each repository organized by program area.

## Website

### [pyopensci.github.io](https://github.com/pyOpenSci/pyopensci.github.io)

This repository contains code and content that builds and publishes our
pyOpenSci website. The website, [pyOpenSci](https://www.pyopensci.org/), is
hosted on GitHub and uses the [Jekyll Minimal
Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme. The Python
packages page, contributor page, and peer review team page are all updated
automatically using a GitHub action workflow that is supported by the pyosMeta
Python package discussed above. The workflow runs every other week but can be
triggered manually as a **workflow dispatch**.

Teams with access to this repository:

* [the pyOpenSci Editorial Board](https://github.com/orgs/pyOpenSci/teams/editorial-board)
* [the pyOpenSci Repository Maintainers team](https://github.com/orgs/pyOpenSci/teams/pyos-repo-maintainers)

#### Critical CI workflows in this repository

The [contributor workflow
action](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/.github/workflows/update-contribs-reviews.yml)
is a custom GitHub action that is used to update the following website pages:

* contributor page
* package listing page
* editorial, advisory council, and executive council listing

It runs as a cron job every other week but also can be run manually as a
workflow dispatch. If you need to update our package listing or contributor
list on the fly, please run this action.

The action will:

1. Parse through all of our accepted pyOpenSci packages.
2. Collect package names, authors, reviewers, and editors.
3. Collect metadata for the package authors, reviewers, and editors using the
   GitHub (REST) API.
4. Create 2 output YAML files discussed below.

The YAML output files are then used to populate content on the website.

#### Metadata stored in this repository

1. **Packages.yml**: Updates the [Python Packages
   page](https://www.pyopensci.org/python-packages.html) by parsing reviews
   from software-review repository issues.
2. **Contributors.yml**: Updates the [Our Community
   page](https://www.pyopensci.org/our-community/index.html) by parsing data
   from all organization repositories.

:::{todo}
Update the website contributors guide with general CI and specific Jekyll
information.
:::

### [handbook](https://github.com/pyOpenSci/handbook)

**Platform:** Sphinx book running the `pydata_sphinx_theme`

This is where we store our organization governance, code of conduct, and
processes around how we operate as an organization.

The [pyOpenSci Executive Council](https://www.pyopensci.org/our-community/index.html#executive-council-leadership--staff) has access to this repo.

### [metrics](https://github.com/pyOpenSci/peer-review-metrics)

The pyOpenSci peer review metrics repository contains the code for a dashboard
created using [MyST Markdown](https://mystmd.org/). Myst-md is a community
developed tool that makes it easier for scientists to create fully
reproducible (and interactive) workflows and reports that are easily shared.
This repository has a cron job that runs weekly to update review status
metrics.

Only pyOpenSci GitHub organization admins have direct access to modify this
repository.

### [lessons](https://github.com/pyOpenSci/lessons)

pyOpenSci is devoted to building diverse, supportive community around the
Python open source tools that drive open science. The lessons repository
contains the source files for all of the [pyOpenSci
tutorials](https://github.com/pyOpenSci/lessons).

The [pyOpenSci Lesson Development Team](https://github.com/orgs/pyOpenSci/teams/lesson-development) has access to this repo.

## Packaging education

### [python-package-guide](https://github.com/pyOpenSci/python-package-guide)

The [python-package-guide
repository](https://www.pyopensci.org/python-package-guide/) contains our
community-developed guidelines and tutorials on Python packaging. These
resources are beginner-friendly and reflect Python packaging best practices.

Teams with access to this repository:

* [the pyOpenSci Packaging Council](https://github.com/orgs/pyOpenSci/teams/packaging-council)
* [the pyOpenSci Repository Maintainers team](https://github.com/orgs/pyOpenSci/teams/pyos-repo-maintainers)

### [pyos-package-template](https://github.com/pyOpenSci/pyos-package-template)

A Python package template that supports the pyOpenSci pure [Python packaging
tutorial](https://www.pyopensci.org/python-package-guide/tutorials/intro.html).
This template can be used with [copier](https://copier.readthedocs.io) to
initialize a new Python package project structure following the practices
outlined in the [pyOpenSci pure Python packaging
tutorial](https://www.pyopensci.org/python-package-guide/tutorials/installable-code.html).

Teams with access to this repository:

* [the pyOpenSci Packaging Council](https://github.com/orgs/pyOpenSci/teams/packaging-council)

### [pyosPackage](https://github.com/pyOpenSci/pyosPackage)

The pyosPackage repo contains an example pure-Python package that complements
our package guide & tutorials. We will build this package example out over
time for folks that just want to see a working package without creating one
themselves.

Teams with access to this repository:

* [the pyOpenSci Packaging Council](https://github.com/orgs/pyOpenSci/teams/packaging-council)

## Peer review

### [software-submission](https://github.com/pyOpenSci/software-submission)

The software-submission repository is where community package submissions are
peer-reviewed. All submissions are made through GitHub Issues. [Learn more
about our peer review process here.](https://www.pyopensci.org/software-peer-review/)

Teams with access to this repository:

* [the pyOpenSci Editorial Board](https://github.com/orgs/pyOpenSci/teams/editorial-board)

:::{important}
Important: If a pyOpenSci core member identifies an issue with the review
submission template, consult both the editorial team and core team before
making any changes. This template's data are processed by a Python workflow,
and even small modifications could disrupt the language processing.
:::

### [software-peer-review](https://github.com/pyOpenSci/software-peer-review)

This repository hosts our [software peer review
guidebook](https://www.pyopensci.org/software-peer-review/), which documents
the processes and guidelines for authors, editors, the Editor in Chief, and
the peer review triage team as they manage our open peer review process. It
also details our peer review policies, partnerships, and the templates used in
the review process.

Individuals and teams with access to this repository include:

* [the pyOpenSci Editorial Board](https://github.com/orgs/pyOpenSci/teams/editorial-board)
* [the pyOpenSci Repository Maintainers team](https://github.com/orgs/pyOpenSci/teams/pyos-repo-maintainers)

## Infrastructure

### [pyosMeta](https://github.com/pyOpenSci/pyosMeta)

The pyosMeta repository contains a Python package published on PyPI that we
use to track our package review and contributor data. This data is used in a
GitHub action to update our website.

Teams with access to this repository:

* [the pyOpenSci Repository Maintainers team](https://github.com/orgs/pyOpenSci/teams/pyos-repo-maintainers)

:::{todo}
Add more information about the contributor data workflow ...
:::

### [pyos-sphinx-theme](https://github.com/pyOpenSci/pyos-sphinx-theme)

**Platform:** Sphinx book template that builds on top of the pydata_sphinx_theme

All of our pyOpenSci Sphinx books (handbook, packaging guide, software review
guide) have been customized to match our pyOpenSci branding. This repo
contains the start of a Sphinx theme that will incorporate all of our
branding, so we do not have to manually apply the branding and update it
individually in each repo. Instead, we can update branding in the theme, and
it will be applied across all of our repositories that use the theme.

Creating a theme was inspired by the
[2i2c Sphinx theme](https://sphinx-2i2c-theme.readthedocs.io/en/latest/).

Teams with access to this repository:

* [the pyOpenSci Repository Maintainers team](https://github.com/orgs/pyOpenSci/teams/pyos-repo-maintainers)
