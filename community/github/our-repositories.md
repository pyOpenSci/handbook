# 1. Our Repositories

:::{todo}
Add repositories from the pyOpenSci organization.
:::

## pyOpenSci GitHub Repository Overview

pyOpenSci manages multiple GitHub repositories to support various community
activities. Below is a description of each core repository.

### [Software-review Repository](https://www.pyopensci.org/software-peer-review/)

The software-review repository is where community package submissions are
peer-reviewed. All submissions are made through GitHub Issues. [Learn more about
our peer review process here.](https://www.pyopensci.org/software-peer-review/)

:::{important}
Important: If a pyOpenSci core member identifies an issue with the review
submission template, consult both the editorial team and core team before making
any changes. This template's data are processed by a Python workflow, and even
small modifications could disrupt the language processing.
:::


### Software-peer-review Guidebook Repository

This repository hosts our [software peer review guide](https://www.pyopensci.org/software-peer-review/),
which includes instructions and guidelines for authors, editors, the editor in
chief, and the peer review triage team. It also details our peer review policies,
partnerships, and the templates used in the review process.

### Python-package-guide Repository

The [python-package-guide repository](https://www.pyopensci.org/python-package-guide/)
contains our community-developed guidelines and tutorials on Python packaging.
These resources are beginner-friendly and reflect best practices.

### [pyosMeta Repository](https://github.com/pyOpenSci/pyosMeta)

The pyosMeta repo contains a Python package published on PyPI that tracks our
package review and contributor data. This data is used in a GitHub action to
update our website.

### [pyopensci.github.io Repository](https://github.com/pyOpenSci/pyopensci.github.io)

Our website, [pyOpenSci](https://www.pyopensci.org/), is hosted on GitHub and
uses the Jekyll Minimal Mistakes theme. The python packages page, contributor page and peer review team page are all updated automagically using a
GitHub action workflow that is supported by the pyosMeta Python package. The workflow runs every other week but can be triggered manually as a **workflow
dispatch**.

1. **Packages.yml**: Updates the [Python Packages page](https://www.pyopensci.org/python-packages.html)
   by parsing reviews from software-review repository issues.
2. **Contributors.yml**: Updates the [Our Community page](https://www.pyopensci.org/our-community/index.html)
   by parsing data from all organization repositories.

:::{todo}
Update the website contributors guide with general CI and specific Jekyll
information.
:::

## [Handbook Repository](https://github.com/pyOpenSci/handbook)

The handbook repository hosts content that helps the community navigate our
online resources and communication channels.
