(github-intro)=
# pyOpenSci Infrastructure


pyOpenSci uses GitHub to manage almost all of its infrastructure, from community processes to website rendering.
This page provides an overview of our core repositories, how they work together, and how they contribute to the website and community operations.

[Learn more about all of our repos here.](github-repos-overview)


```{mermaid}
%%{ init: { "theme": "default", "themeVariables": { "fontSize": "200%" } } }%%

flowchart TD

    %% Note above Software Review
    Note["Peer review happens<br>in GitHub issues"]

    %% Top: software-review repo
    A(<b>Software Review</b><br><sub>github.com/pyOpenSci/software-review</sub>) --> B{{pyosMeta<br><sub>github.com/pyOpenSci/pyosMeta</sub><br><i>A Python package that processes review<br>and contributor data and creates YML files</i>}}
    C(<b>pyOpenSci Website</b><br><sub>pyopensci.github.io</sub>)
    A --> |"pyosMeta parses review issues<br>and contributor metadata<br>to create YAML files"| B
    B --> |"_data/contributors.yml & packages.yml are used to populate website package and contributor pages."| C

    %% Website outputs to 4 child "books"
    C --> D1(Handbook<br><sub>github.com/pyOpenSci/handbook<br>SPHINX</sub>)
    C --> D2(Python Package Guide<br><sub>github.com/pyOpenSci/python-package-guide<br>SPHINX</sub>)
    C --> D3(Software Peer Review Guide<br><sub>github.com/pyOpenSci/software-peer-review-guidebook<br>SPHINX</sub>)
    C --> D4(Lessons<br><sub>github.com/pyOpenSci/software-peer-review-guidebook<br>SPHINX</sub>)
    C --> D5(Peer Review Metrics<br><sub>github.com/pyOpenSci/peer-review-metrics<br>QUARTO</sub>)

    %% Style for Website box (light purple)
    style C fill:#f3e8ff,stroke:#7e22ce,stroke-width:1px
    style B fill:#fef9c3,stroke:#ca8a04,stroke-width:1px
    style Note fill:#f3f4f6,stroke:#9ca3af,stroke-width:1px

```
## pyOpenSci data flow and continuous integration

pyOpenSci uses a set of **Continuous Integration (CI)** jobs (GitHub Actions) to:

* Collect data from our open peer review process
* Collect contributor data from across all of our GitHub repositories

The [`pyosMeta`](https://github.com/pyOpenSci/pyosMeta) package is a Python package that **parses review and contributor data** and transforms it into **machine-readable YAML files** used by our website.

### Summary of flow

* `pyosMeta` parses the **Markdown data** within review issues in the [`software-review`](https://github.com/pyOpenSci/software-review) GitHub repository. It:
    * Gathers review editors, reviewers, and maintainers’ GitHub usernames, and uses the GitHub API to retrieve contributor names, emails, and other public GitHub profile information
    * Extracts the GitHub URL of each reviewed package and retrieves basic repository statistics (number of forks, stars, contributors)
    * Stores this peer review information in `packages.yml`

* `pyosMeta` also parses **contributor data** from across all pyOpenSci repositories. It:
    * Parses `all-contributors` bot files to compile a list of contributors and their associated repositories/projects
    * Parses peer review metadata to populate roles such as reviewers, editors, and other contributor roles within our organization
    * Stores this contributor information in `contributors.yml`

* The `packages.yml` and `contributors.yml` files generated by `pyosMeta` are updated **daily** via a GitHub Action **cron job** in the [`pyopensci.github.io`](https://github.com/pyOpenSci/pyopensci.github.io/tree/main/_data) repository. This data is used to populate:
    * The **Our Community** page
    * The **Packages** page

### Sphinx books and publishing

* The **Python Package Guide**, **Peer Review Guide**, and **Handbook** are all **Sphinx books** that use the `pydata_sphinx_theme`. These books are built separately but are served under the `pyopensci.org` domain.
* All Sphinx books use the [`pyos-sphinx-theme`](https://github.com/pyOpenSci/pyos-sphinx-theme`), which is a Sphinx theme built on top of `pydata_sphinx_theme`.
* The final site is published at [pyopensci.org](https://www.pyopensci.org) using **GitHub Pages**.
