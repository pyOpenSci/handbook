# <img src="https://www.pyopensci.org/handbook/_static/logo-dark-mode.png" width=150 /> pyOpenSci Handbook

[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors-)  ![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyopensci/governance?color=purple&display_name=tag&style=plastic)  [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7120880.svg)](https://doi.org/10.5281/zenodo.7120880)
[![CircleCI](https://circleci.com/gh/pyOpenSci/handbook.svg?style=svg)](https://circleci.com/gh/pyOpenSci/handbook)

## What is pyOpenSci?

pyOpenSci is a vibrant and diverse open science and open source community of practice. We are file down open science and open source pain points associated with sharing and writing better, more maintainable code and software.

Our community runs several programs:

* [Open peer review of scientific Python software](https://www.pyopensci.org/about-peer-review/index.html)
* [Development of open online education resources for anyone to use.](https://www.pyopensci.org/learn.html)
* [online and in-person training events](https://www.pyopensci.org/events/index.html).

pyOpenSci is an independent organization, fiscally sponsored by Community
Initiatives.


## How to setup

This repository contains the source files for the [pyOpenSci governance handbook](https://pyopensci.org/handbook).

## Build the governance document locally

Our governance documentation is built with [Sphinx](https://sphinx-doc.org), a documentation tool.

The easiest way to build our documentation is to use [`nox`](https://nox.thea.codes/), a tool for quickly building environments and running commands within them.
Using `nox` ensures that your environment has all the dependencies needed to build the documentation.

To build, follow these steps:

1. Install `nox`

```console
$ pip install nox
```

2. Build the documentation:

```console
$ nox -s docs
```

This should create a local environment in a `.nox` folder, build the documentation (as specified in the `noxfile.py` configuration), and the output will be in `_build/html`.

To build live documentation that updates when you update local files, run the following command:

```console
$ nox -s docs-live
```
The governance page should automatically open in a new browser window. If it does not, check your terminal for the text "Serving on http://XXX.X.X.X:XXXX". The HTTP address is a link that you can click (or copy and paste into your browser) to open the handbook page for live editing.

## Contributing to this guide

We welcome issues and pull requests to improve the content of this guide.
If you'd like to see an improvement, please [open an issue](https://github.com/pyOpenSci/governance/issues/new/choose).

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://karencranston.ca/"><img src="https://avatars.githubusercontent.com/u/312034?v=4?s=100" width="100px;" alt="Karen Cranston"/><br /><sub><b>Karen Cranston</b></sub></a><br /><a href="https://github.com/pyOpenSci/governance/commits?author=kcranston" title="Code">💻</a> <a href="#design-kcranston" title="Design">🎨</a> <a href="https://github.com/pyOpenSci/governance/pulls?q=is%3Apr+reviewed-by%3Akcranston" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tracykteal"><img src="https://avatars.githubusercontent.com/u/889238?v=4?s=100" width="100px;" alt="Tracy Teal"/><br /><sub><b>Tracy Teal</b></sub></a><br /><a href="https://github.com/pyOpenSci/governance/commits?author=tracykteal" title="Code">💻</a> <a href="https://github.com/pyOpenSci/governance/pulls?q=is%3Apr+reviewed-by%3Atracykteal" title="Reviewed Pull Requests">👀</a> <a href="#design-tracykteal" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.leahwasser.com"><img src="https://avatars.githubusercontent.com/u/7649194?v=4?s=100" width="100px;" alt="Leah Wasser"/><br /><sub><b>Leah Wasser</b></sub></a><br /><a href="https://github.com/pyOpenSci/governance/commits?author=lwasser" title="Code">💻</a> <a href="https://github.com/pyOpenSci/governance/pulls?q=is%3Apr+reviewed-by%3Alwasser" title="Reviewed Pull Requests">👀</a> <a href="#design-lwasser" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kierisi"><img src="https://avatars.githubusercontent.com/u/23085445?v=4?s=100" width="100px;" alt="Jesse Mostipak"/><br /><sub><b>Jesse Mostipak</b></sub></a><br /><a href="https://github.com/pyOpenSci/governance/commits?author=kierisi" title="Code">💻</a> <a href="https://github.com/pyOpenSci/governance/pulls?q=is%3Apr+reviewed-by%3Akierisi" title="Reviewed Pull Requests">👀</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!
