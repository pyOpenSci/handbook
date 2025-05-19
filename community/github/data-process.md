# pyOpenSci Infrastructure Overview

This page will help you understand how we collect and process peer review and contributor data to:

* Highlight pyOpenSci contributors
* Track our peer review process
* Showcase peer-reviewed Python packages

## How it works

We use a Python package called `pyosMeta` to **extract and transform contributor and peer review data** into machine-readable formats (`.yml` and `.csv`).

This data allows us to **automatically update**:

* our [public website contributor listing](https://www.pyopensci.org/our-community/index.html)
* our [website accepted package listing](https://www.pyopensci.org/python-packages.html)
* our [metrics dashboard](https://www.pyopensci.org/metrics)

with up-to-date contributor and review information, directly from GitHub.

## Data collection and processing

We collect two types of data from GitHub:

1. **Contributor data**
   Parsed from [All Contributors bot config files](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/.all-contributorsrc) found in each pyOpenSci repo.

2. **Peer review submission data**
   Extracted from [issues in the software-submission repo](https://github.com/pyOpenSci/software-submission/issues), including:
   * package name and repo URL
   * editor and reviewers
   * maintainers and authors

This data is processed by `pyosMeta`, which generates:

* `_data/contributors.yml`
* `_data/packages.yml`
* `.csv` files for metrics

## Where the data goes

The processed data files are used in two main parts of our website:

* **Website GitHub Repo**
  * A cron job reads the `.yml` files to populate our
    👉 [Contributors page](https://www.pyopensci.org/our-community/index.html#pyopensci-community-contributors)
    👉 [Packages page](https://www.pyopensci.org/python-packages.html)

* **Metrics GitHub Repo**
  * A cron job reads `.csv` files to generate the
    👉 [Peer review status dashboard](https://www.pyopensci.org/metrics/peer-review/current-review-status.html)

## Workflow diagram

The diagram below explains the basic workflow that we use.

:::{mermaid}
graph TD
    subgraph Sources
        A1[All Contributors Bot]
        A2[Peer Review Submissions *GitHub Issues*]
    end

    subgraph pyosmeta
        A3[pyosmeta]
    end

    A1 --> A3
    A2 --> A3

    A3 -->|DATA:
    _data/contributors.yml,
    _data/packages.yml| B1[Website GitHub Repo]
    A3 -->|DATA:
    _/*.CSV | B2[Metrics GitHub Repo]

    B1 -->|Cron job reads YAML| C1[🔗 Contributor listing page]
    B2 -->|Cron job reads CSV| C2[Generate metric plots]

    click C1 "https://www.pyopensci.org/our-community/index.html#pyopensci-community-contributors" "View pyOpenSci Contributor Page"
:::
