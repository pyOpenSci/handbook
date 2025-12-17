(github-intro)=
# pyOpenSci Infrastructure

pyOpenSci uses GitHub to manage almost all of its infrastructure, from community processes to website rendering.
This page provides an overview of our core repositories, how they work together, and how they contribute to the website and community operations.

[Learn more about all of our repos here.](github-repos-overview)

```{mermaid}
%%{ init: { "theme": "default", "themeVariables": { "fontSize": "240%", "fontFamily": "Poppins, sans-serif", "primaryColor": "#ffffff", "primaryTextColor": "#ffffff", "primaryBorderColor": "#33205c", "lineColor": "#33205c", "secondaryColor": "#ffffff", "tertiaryColor": "#ffffff", "background": "#ffffff", "mainBkgColor": "#ffffff", "secondBkgColor": "#ffffff", "edgeLabelBackground": "#ffffff" } } }%%

flowchart TD

    %% Note above Software Review - larger box with grey background
    Note["<div style='min-width: 400px; padding: 12px;'><span style='font-size:1.2em'><b>Peer review happens<br>in GitHub issues</b></span></div>"]

    %% Top: software-review repo - using wider format (40% increase)
    A["<div style='min-width: 525px; padding: 12px;'><span style='font-size:1.3em'><b>Software Review/</b></span><br><span style='font-size:1.1em'>/software-review</span></div>"]
    B["<div style='min-width: 588px; padding: 12px;'><span style='font-size:1.3em'><b>pyosMeta</b></span><br><span style='font-size:1.1em'>/pyosMeta</span><br><span style='font-size:1.05em'><i>Processes review & contributor data<br>Creates YAML files</i></span></div>"]
    C["<div style='min-width: 588px; padding: 12px;'><span style='font-size:1.3em'><b>pyOpenSci Website</b></span><br><span style='font-size:1.1em'>pyopensci.github.io</span></div>"]

    Note -.->|"<span style='font-size:1.15em'><b>Peer review process</b></span>"| A
    A --> |"<span style='font-size:1.15em'><b>Parses review issues<br>& contributor metadata</b></span>"| B
    B --> |"<span style='font-size:1.15em'><b>Generates YAML files:<br>contributors.yml & packages.yml</b></span>"| C

    %% Styling - white boxes with dark purple borders and text
    style C fill:#ffffff,stroke:#33205c,stroke-width:3px,color:#33205c
    style B fill:#ffffff,stroke:#33205c,stroke-width:3px,color:#33205c
    style A fill:#ffffff,stroke:#33205c,stroke-width:3px,color:#33205c
    style Note fill:#9ca3af,stroke:#6b7280,stroke-width:3px,color:#1f2937

```

```{mermaid}
%%{ init: { "theme": "default", "themeVariables": { "fontSize": "240%", "fontFamily": "Poppins, sans-serif" } } }%%

flowchart LR

    %% Website on the left
    C["<div style='min-width: 350px; padding: 8px;'><span style='font-size:1.3em'><b>pyOpenSci Website</b></span><br><span style='font-size:1.08em'><sub>pyopensci.github.io</sub></span></div>"]

    %% Website outputs to 5 child "books" on the right - wider boxes
    C --> D1["<div style='min-width: 300px; padding: 8px;'><span style='font-size:1.3em'><b>Handbook</b></span><br><span style='font-size:1.08em'><sub>handbook</sub><br>SPHINX</span></div>"]
    C --> D2["<div style='min-width: 370px; padding: 8px;'><span style='font-size:1.3em'><b>Python Package Guide</b></span><br><span style='font-size:1.08em'><sub>python-package-guide</sub><br>SPHINX</span></div>"]
    C --> D3["<div style='min-width: 410px; padding: 8px;'><span style='font-size:1.3em'><b>Software Peer Review Guide</b></span><br><span style='font-size:1.08em'><sub>software-peer-review</sub><br>SPHINX</span></div>"]
    C --> D4["<div style='min-width: 270px; padding: 8px;'><span style='font-size:1.3em'><b>Lessons</b></span><br><span style='font-size:1.08em'><sub>lessons</sub><br>SPHINX</span></div>"]
    C --> D5["<div style='min-width: 270px; padding: 8px;'><span style='font-size:1.3em'><b>Metrics</b></span><br><span style='font-size:1.08em'><sub>metrics</sub><br>QUARTO</span></div>"]

    %% Styling - Website box (brand purple)
    style C fill:#bab3d4,stroke:#33205c,stroke-width:3px,color:#1f2937

    %% Styling - Sphinx books (brand purple)
    style D1 fill:#bab3d4,stroke:#735fab,stroke-width:2px,color:#1f2937
    style D2 fill:#bab3d4,stroke:#735fab,stroke-width:2px,color:#1f2937
    style D3 fill:#bab3d4,stroke:#735fab,stroke-width:2px,color:#1f2937
    style D4 fill:#bab3d4,stroke:#735fab,stroke-width:2px,color:#1f2937

    %% Styling - Quarto (brand magenta to distinguish)
    style D5 fill:#bb82b0,stroke:#735fab,stroke-width:2px,color:#1f2937

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
