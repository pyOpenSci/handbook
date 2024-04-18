# Our repositories

:::{todo}
Add other repositories that live in the pyOpenSci organization including
:::

## pyOpenSci GitHub repository overview

pyOpenSci manages a suite of GitHub repositories that support various
community activities. A description of each of our core repositories
is below.

###  [Software-review repository](https://www.pyopensci.org/software-peer-review/)

The software-review repo is where peer review happens. Here, the community submits packages for
open review. All review submissions happen through GitHub Issues. [You can read more about peer review in our guide here.](https://www.pyopensci.org/software-peer-review/)

:::{important}
Important: if a pyOpenSci core member finds an issue with the review submission template be sure to talk with both the editorial team and the core team before submitting a change to this template. The data in each issue are parsed via a Python workflow and small changes to the issue template could break the language processing that happens in that parse workflow.
:::

:::{todo}
we really could use a tutorial on how to submit a package to pyOpenSci. While the form may change in the future the process won't change in any dramatic way.
:::

### Software-peer-review Guidebook repository

The software-peer-review guidebook repository is where we host our online
[software peer review guide](https://www.pyopensci.org/software-peer-review/).
This guidebook provides instructions and guidelines for the various roles
associated with our open peer review process including guides for authors,
editors, editor in chief and the peer review triage team. This guidebook also
provides an overview of our peer review policies, peer review partnerships and
templates that support peer review processing.


### Python-package-guide repository

The python-package-guide Github repo is where the content for our
[pyOpenSci Python packaging guide](https://www.pyopensci.org/python-package-guide/)
lives. The pyOpenSci packaging guidebook includes community-developed guidelines
around best practices for Python packaging. It also contains a set of community
developed, beginner-friendly Python packaging tutorials.


### [pyosMeta](https://github.com/pyOpenSci/pyosMeta)

The pyosMeta repo stores a Python package that is published on PyPI. This package contains code that captures and tracks our package review and contributor data. The code from this repo is what is run in the GitHub action mentioned below that updates our website

### [pyopensci.github.io repository](https://github.com/pyopensci/pyopensci.github.io)

Our website repo [pyOpenSci](https://www.pyopensci.org/) is hosted on GitHub at
[github.com/pyopensci/pyopensci.github.io](https://github.com/pyopensci/pyopensci.github.io). It runs on Jekyll with the Minimal Mistakes theme, a flexible two-column theme
designed for GitHub Pages. The website updates peer review and contributor data
automatically through CI actions. Updates occur bi-weekly, or via a manually
triggered workflow_dispatch in GitHub Actions.

1. **Packages.yml**: Populates [Python Packages](https://www.pyopensci.org/python-packages.html) by parsing reviews in the software-review repository issues.
2. **Contributors.yml**: Populates [Our Community](https://www.pyopensci.org/our-community/index.html) by parsing contributors across all repositories in the organization.


:::{todo}
I think our website contributors guide will need to be updated with links to this document for general CI stuff and then more specific jekyll stuff.
:::
