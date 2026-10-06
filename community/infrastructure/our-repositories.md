(github-repos-overview)=
# pyOpenSci GitHub repositories

pyOpenSci manages multiple GitHub repositories to support various community
activities. Below is a description of each repository organized by program area.

## Website

### [pyopensci.github.io](https://github.com/pyOpenSci/pyopensci.github.io)

This repository contains code and content that builds and publishes our
pyOpenSci website, [pyopensci.org](https://www.pyopensci.org/). The website is
built with [Hugo](https://gohugo.io/) and hosted on GitHub Pages. The Python
packages page, contributor page, and editorial board listing are updated by
scheduled GitHub Actions workflows that run the
[pyosMeta](#pyosmeta) Python package.

Teams with access to this repository:

* [the pyOpenSci Editorial Board](https://github.com/orgs/pyOpenSci/teams/editorial-board)
* [the Editor in Chief team](https://github.com/orgs/pyOpenSci/teams/eic-team)
* [the pyOpenSci Repository Maintainers team](https://github.com/orgs/pyOpenSci/teams/pyopensci-repository-maintainers)

#### Critical CI workflows in this repository

Two scheduled workflows keep the website's data up to date. Each one opens a
pull request, and the website changes once you merge it. You can also run
either one by hand.

* [**Update Contribs & reviewers**](https://github.com/pyOpenSci/pyopensci.github.io/actions/workflows/update-contribs-reviews.yml)
  updates the contributor and package listings from All Contributors files
  and peer review issues. The same job also refreshes the editorial board
  listing.
* [**Update editorial board**](https://github.com/pyOpenSci/pyopensci.github.io/actions/workflows/update-editorial-board.yml)
  only reads editorial team membership, so it's much faster. Run this one
  after you change an editorial team.

For when each one runs, which files it writes, and who can run them, see
[data workflows](data-process).

#### Metadata stored in this repository

1. **packages.yml**: Updates the [Python Packages
   page](https://www.pyopensci.org/python-packages.html) by parsing reviews
   from software-submission repository issues.
2. **contributors.yml**: Updates the [Our Community
   page](https://www.pyopensci.org/our-community/index.html) by parsing data
   from all organization repositories.
3. **editorial-board.yml** and **emeritus-editors.yml**: Update the
   [editorial board
   listing](https://www.pyopensci.org/about-peer-review/index.html#meet-our-editorial-board)
   from our GitHub editorial teams.
4. **manual-editorial-roster.yml**: The only editorial file edited by hand,
   for someone who can't join the GitHub organization.

:::{todo}
Update the website contributors guide with general CI and specific Hugo
information.
:::

### [handbook](https://github.com/pyOpenSci/handbook)

**Platform:** Sphinx book running the [`pyos-sphinx-theme`](#pyos-sphinx-theme)

This is where we store our organization governance, code of conduct, and
processes around how we operate as an organization.

The [pyOpenSci Executive Council](https://www.pyopensci.org/our-community/index.html#executive-council-leadership--staff) has access to this repo.

### [metrics](https://github.com/pyOpenSci/metrics)

The pyOpenSci metrics repository contains the code for our [metrics
dashboards](https://www.pyopensci.org/metrics), built with
[Quarto](https://quarto.org/). Scheduled workflows refresh the peer review
data and rebuild the site. The editorial dashboard reads the editorial board
files from the website repository. See [data workflows](data-process) for
details.

Teams with access to this repository:

* [the Editor in Chief team](https://github.com/orgs/pyOpenSci/teams/eic-team)
* [the pyOpenSci Repository Maintainers team](https://github.com/orgs/pyOpenSci/teams/pyopensci-repository-maintainers)

### [lessons](https://github.com/pyOpenSci/lessons)

The lessons repository contains the source files for all of the [pyOpenSci
tutorials](https://www.pyopensci.org/lessons/).

The [pyOpenSci Lesson Development Team](https://github.com/orgs/pyOpenSci/teams/lesson-development) has access to this repo.

## Packaging education

### [python-package-guide](https://github.com/pyOpenSci/python-package-guide)

The [python-package-guide
repository](https://www.pyopensci.org/python-package-guide/) contains our
community-developed guidelines and tutorials on Python packaging. These
resources are beginner-friendly and reflect Python packaging best practices.

Teams with access to this repository:

* [the pyOpenSci Packaging Council](https://github.com/orgs/pyOpenSci/teams/packaging-council)
* [the pyOpenSci Repository Maintainers team](https://github.com/orgs/pyOpenSci/teams/pyopensci-repository-maintainers)

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
* [the Editor in Chief team](https://github.com/orgs/pyOpenSci/teams/eic-team)
* [the pyOpenSci Repository Maintainers team](https://github.com/orgs/pyOpenSci/teams/pyopensci-repository-maintainers)

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
* [the Editor in Chief team](https://github.com/orgs/pyOpenSci/teams/eic-team)
* [the pyOpenSci Repository Maintainers team](https://github.com/orgs/pyOpenSci/teams/pyopensci-repository-maintainers)

## Infrastructure

### [pyosMeta](https://github.com/pyOpenSci/pyosMeta)

The pyosMeta repository contains a Python package published on PyPI that we
use to track our package review, contributor, and editorial board data. The
website's scheduled workflows use it to update our website. See
[data workflows](data-process) for how the data moves.

Teams with access to this repository:

* [the pyOpenSci Repository Maintainers team](https://github.com/orgs/pyOpenSci/teams/pyopensci-repository-maintainers)

### [pyos-sphinx-theme](https://github.com/pyOpenSci/pyos-sphinx-theme)

**Platform:** Sphinx book template that builds on top of the pydata_sphinx_theme

This repo contains our branded Sphinx theme, which the handbook and software
peer review guide use. Because the branding lives in one theme, we can update
it in one place instead of in each repository, and the change applies
everywhere the theme is used.

Creating a theme was inspired by the
[2i2c Sphinx theme](https://sphinx-2i2c-theme.readthedocs.io/en/latest/).

Teams with access to this repository:

* [the pyOpenSci Repository Maintainers team](https://github.com/orgs/pyOpenSci/teams/pyopensci-repository-maintainers)
