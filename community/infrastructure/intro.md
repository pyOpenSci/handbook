(github-intro)=
# pyOpenSci website infrastructure

pyOpenSci uses GitHub to manage almost all of its infrastructure, from
community processes to website rendering. This page gives a high-level
overview of how our repositories work together to build our websites
and keep community data up to date.

:::{note}
For details on each part of our infrastructure, see the
[Learn more](#learn-more) section below.
:::

## How our websites fit together

The pyOpenSci website at [pyopensci.org](https://www.pyopensci.org) is
built from six repositories. Each one is built separately and published
under the `pyopensci.org` domain using GitHub Pages with Netlify setup for
previews:

* **Core website:** [`pyopensci.github.io`](https://github.com/pyOpenSci/pyopensci.github.io),
  built with [Hugo](https://gohugo.io/). It is the central hub that links
  to every sub-site.
* **Sphinx books:** the [Python Package Guide](https://github.com/pyOpenSci/python-package-guide),
  [Software Peer Review Guide](https://github.com/pyOpenSci/software-peer-review),
  [Handbook](https://github.com/pyOpenSci/handbook), and
  [Lessons](https://github.com/pyOpenSci/lessons). Most use our branded
  [`pyos-sphinx-theme`](https://github.com/pyOpenSci/pyos-sphinx-theme).
* **Metrics dashboards:** [`metrics`](https://github.com/pyOpenSci/metrics),
  built with [Quarto](https://quarto.org/).

```{figure} /images/diagrams/website-repositories-structure.svg
:name: website-repositories-structure

pyOpenSci website structure diagram showing the main website and its
sub-sites (Handbook, Python Package Guide, Software Peer Review Guide,
Lessons, and Metrics).
```

## How data flows from our community programs to the website

Some parts of our websites update automatically using data from GitHub.
This includes the peer review numbers in our
[metrics dashboards](https://www.pyopensci.org/metrics), and the package
listings, community contributors, and editorial board on the main Hugo
website.

We wrote a Python package called
[`pyosMeta`](https://github.com/pyOpenSci/pyosMeta) to collect this data.
It saves the data as YAML files, a plain-text format that our websites
can read. `pyosMeta` collects three kinds of data:

* **Peer review data.** `pyosMeta` parses the
  [peer review issues](https://github.com/pyOpenSci/software-submission/issues)
  in `software-submission`. It pulls out metadata such as the package
  name, repository URL, editor, reviewers, and maintainers. That data
  feeds the [Python packages page](https://www.pyopensci.org/python-packages.html).
* **Peer review roles.** We track editors, the Editor in Chief, and the
  triage team using GitHub teams. `pyosMeta` reads team membership to
  build the
  [editorial board listing](https://www.pyopensci.org/about-peer-review/index.html#meet-our-editorial-board).
  See [editorial teams](editorial-teams).
* **Contributors.** We use the [All Contributors bot](https://allcontributors.org/)
  to track contributors across our repositories. `pyosMeta` parses each
  repository's All Contributors file to build the contributor list on
  the [Our Community page](https://www.pyopensci.org/our-community/index.html).

The diagram below shows how this data moves from GitHub to the website
and metrics dashboards:

:::{mermaid}
flowchart LR
  Contrib[All Contributors files] --> Meta[pyosMeta]
  Issues[Peer review issues in software-submission] --> Meta
  Teams[GitHub editorial teams] --> Meta
  Meta --> PR[Pull request with updated YAML files]
  PR -->|merged| Website[Website pages]
  Website -.->|editorial dashboard reads board data| Metrics[Metrics dashboards]
  Issues -.->|review data| Metrics
:::

Scheduled workflows run `pyosMeta` and open a pull request with the
updated YAML files. The website updates once that pull request is merged.
The metrics dashboards run on their own schedule. A few fields, such as
[Advisory Council](update-the-advisory-council) and leadership roles,
are [edited by hand](edit-contributors-by-hand). For
schedules, how to run a workflow, and hand-edited fields, see
[website & metrics data](data-process).

## Learn more

For details on each part of our infrastructure, see:

* **[All repositories](our-repositories):** Complete list and description of all pyOpenSci GitHub repositories
* **[Website & metrics data](data-process):** Schedules, files, and troubleshooting for contributor, package, and editorial data
* **[Editorial teams](editorial-teams):** Which GitHub team to use when you add or remove an editor
* **[Permissions](permissions):** Repository access management and team structures

To contribute to our repositories, see:

* **[Issues](issues):** Issue management and labeling workflows
* **[Pull requests](pull-requests):** How to work with pull requests in pyOpenSci repos
* **[Continuous integration](continuous-integration):** CI/CD workflows and GitHub Actions
