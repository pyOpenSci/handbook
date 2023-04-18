# Contributing Guide for pyOpenSci

This guide is a high level contributing guide that provide guidelines for
contributing to resources across our organization. You will find specific contributing guidelines in each of the repositories that
we maintain.

pyOpenSci develops and maintains numerous community resources including:

- [Python packaging guide]()
- Python [software peer review guide](https://github.com/pyOpenSci/software-peer-review)
- Our [pyopensci.org website](https://github.com/pyOpenSci/pyopensci.github.io)
- Our [software review repo](https://github.com/pyOpenSci/software-submission): contains templates templates for software submission and a small ci build

This document applies to any of our online content that you
contribute to. Most of our content lives in the [pyOpenSci
GitHub organization](https://github.com/pyopensci).

## High level guidelines

1. Anyone contributing to pyOpenSci must follow our [organization-wide code of conduct](https://www.pyopensci.org/governance/CODE_OF_CONDUCT.html).
2. Please open an issue before submitting a pull request with new or revised content. Issues will allow us to discussed the changes with you before they are submitted. Submitting an issue first will expedite the speed at which your pull request is merged.

- In some instances, if your pull request is a simple fix of a link or typo, we may accept it without an issue being opened.

3. If you submit a pull request please be sure to use a branch in your fork. Do not use the `main` branch from your fork to submit a pull request.
4. Please try to spell check and editor pull requests before opening them in our repository. This will save us time when reviewing your suggested change(s)!

## Contributor attributions

We welcome and value contributions of all kinds. Some ways that
you can contribute to pyOpenSci include:

- Identifying typos / issues in our online documentation
- Fixing bad urls and references in our issue and peer review templates
- Opening issues about content in our peer review and packaging guides
- Reviewing pull requests that update content on our website
- Contributing to the peer review process
- and more

We use the [all-contributors bot](https://allcontributors.org/) to track contributions of all kinds
across our GitHub repositories. When you contribute to our organization, we will add you to the all-contributors `.json` file
using the all-contributors bot. Approximately once a month, we aggregate the contributor `.json` files across the organization to update [our community contributors
list](https://www.pyopensci.org/our-community/#pyopensci-community-contributors).

## Contributor authorship

We are deeply thankful to everyone who has helped develop and review the pyOpenSci
online documentation. here, we establish guidelines
for giving credit to contributors for their work.

Our [peer-review-guide](https://zenodo.org/record/7101778) and [packaging-guide](https://zenodo.org/record/7786869) can be cited using a
Zenodo DOI. As such, we periodically update authorship for those documents prior to a new release.

Every time we make a release, we will review our .zenodo file and contributors for both reviews, edits and other contributions to our content. In many cases because discussions around content happen in other forums - discourse, discord, slack, email, we will do our best to capture all contributors.

Those who have contributed directly to updating the content will be added as authors. Otherwise you will be added as a contributor. Both categories are listed in the zenodo citation.

Every time we make a release, everyone who has made a commit to the repository since the previous release will be mentioned in the changelog entry using their GitHub handle. This is a way of saying "Thank you".

> **Note**: These policies may be adapted or changed to
> accommodate the growth of our organization and the preferences of our community over time.

## Instructions for local development

Some of our online content may need to be built locally.
On this general contributing guidelines page, you will only find general contribution guidelines. Each repository contains instructions for local development setup
in the `CONTRIBUTING.md` file for that specific repository.

### Development guide our guidebooks

This repo (governance), our peer review guide and python packaging guidebook are built using the `pydata_sphinx_theme`. We have created builds
for those repositories using `nox`.

If you wish to contribute by working on the guide book locally, you
will first need to

1. Fork this repository
2. Clone it locally
3. Build the documentation locally

## Instructions for building the documentation locally on your computer

The easiest way to build the documentation in this repository is to use `nox`,
a tool for quickly building environments and running commands within them.
Nox ensures that your environment has all the dependencies needed to build the documentation.

If you plan to submit a pull request with changes to the guide, you can chose to submit a pr and view the associated build online in Circle CI. Or you can choose to build the documentation locally to test a pull request.

To build locally, follow these steps:

1. Install `nox` into the environment where you plan to work. Nox will create a virtual environment that you can use to build the docs.

   ```
   pip install nox
   ```

This should create a local environment in a `.nox` folder, build the documentation (as specified in the `noxfile.py` configuration), and the output will be in `_build/html`.

2. Once nox is installed, you can build the documentation. You have two options, to build the documentation once and look at the output in a browser use:

   ```
   nox -s docs
   ```

To build live documentation that updates when you update local files, run::

    ```
    nox -s docs-live
    ```

The `docs-live` command will provide ou with a url that you can enter into your
browser to see the docs update as you make updates to files.

### CircleCI Previews

Each book is setup with a GitHub action redirect that will take you to a online
build of the current pull request in CircleCI. To view the build, click on
the GitHub action after it's run at the bottom of your pull request. It will
take you directly to circle ci. The home page of the guidebook will be called:

`output/index.html`

### Website build

Our website is a `jekyll`/`markdown` driven site. Thus, you will need to install `ruby`, and the gems needed to build the website following the contributing guide in our pyopensci.github.io repository.

```

```
