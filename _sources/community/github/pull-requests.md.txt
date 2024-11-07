# 2. pyOpenSci Pull Request Process

When possible, pull request (PR) and issue submissions and reviews of pull requests should follow
standard open source workflows. Below are guidelines for pull requests submitted to pyOpenSci.

## Pull Requests

New pull requests should:

* Be created from a fork rather than the pyOpenSci-owned parent repository.
* [Never be submitted from the `main` branch of your fork.](https://hynek.me/articles/pull-requests-branch/)

Authors of new pull requests should, whenever possible, do their best to
create clean pull requests.

A clean pull request:

* Is focused on fixing or adding a single thing or a single related set of
  things.
* Is easy to review, meaning it doesn't have too many files and too much
  new content.
* Can be more quickly reviewed (and in turn merged), saving everyone time.
* Closes an existing issue (with the exception of new content such as blog
  posts, which we manage internally using Asana).

:::{tip}
Please look over your own pull request before asking someone else to review it for you.
You might be surprised that you notice things in the pull request that you
didn't notice when working on the content locally.
:::

### Pull Request Checklist

Please follow this pull request review checklist when submitting a pull request to a pyOpenSci GitHub repository.
This checklist will make the pull request review process easier and more efficient for you as the pull request author and for the
repository maintainers.

* Check that the files in the PR align with those you changed locally (or want to suggest changes to).
* Review your own code and/or text changes for each file. Do the changes look correct to you? Are there typos?
* Check that the pull is coming from a branch on your fork, and not the main of your repo fork.

```{figure} /images/github-images/pr-comparison-branch.png
:alt: A screenshot of a GitHub PR. The text reads: Open a pull request, and beneath that, Create a new pull request by comparing changes across two branches. If you need to, you can also compare across forks. Learn more about diff comparisons here. Beneath the text is a grey box with four dropdowns arranged in a single row. From left to right the dropdowns read: base repository:pyOpenSci/handbook, base: main, head repository: kierisi/handbook, and compare: pr-checklist. Underneath this box is more text which reads: Able to merge. These branches can be automatically merged.

This is what a PR to the `pyOpenSci/handbook` repository, made from an individual contributor's (kierisi) branch, `pr-checklist`, looks like. If this were from kierisi's main repository, the text in the far-right dropdown would read "main."
```

* Check that all continuous integration checks have passed. If they haven't passed, identify and address the points of failure.
* Check the PR title to ensure that it describes what your PR is changing.

### Pull Request Content

Below are some guidelines for pull request content. Clean pull requests
lead to simpler reviews and faster merging!

1. **Keep It Small**: Aim for one logical change per pull request to
   simplify review.
2. **Create a Descriptive PR Title and Summary**: Clearly state what the
   PR achieves and why, including any related issue numbers or discussions.
3. **Double-Check Files**: Ensure the files committed clearly align with
   the changes in the pull request. For example, if a new guidebook page
   contains images, all new images should be included in the PR. Reuse
   existing images by linking to them rather than re-adding them.
4. **Follow Coding/Style Guidelines**: Stick to the project's coding and
   style guidelines, if applicable. This is more relevant to code PRs
   than text.
5. **Review Your Own PR First**: Look over your PR critically before
   requesting reviews to catch mistakes early.
6. **Respond Respectfully**: Be open to feedback and discuss suggestions
   to improve the project.
7. **Check CI for Any Red X's**: If your pull request returns a red X in
   the "checks/CI" section, try to figure out what is broken in the build.
   If you're unsure, leave a note for the reviewer to help understand what
   needs fixing.

### Highly Recommended

1. **Create Clear Commit Messages**: Explain why changes are made, not
   just what was changed.
2. **Keep Your Branch Updated**: Regularly rebase your fork from the main
   branch (if possible) to avoid/clean up merge conflicts and keep your PR
   up to date.

:::{note}

* [Tips for Better Pull Requests](https://opensource.com/article/18/6/anatomy-perfect-pull-request)
* pyOpenSci has also enabled an "update branch" feature in the pull request,
  which will update your branch to be in sync with main. In most cases,
  this creates a merge commit rather than a rebase.
:::

### Regular vs. New Contributors

There is no right or wrong when it comes to building a website repository
locally. pyOpenSci staff and regular contributors often opt to build
resources locally for live interactive development and edits. Building
locally is an ideal way for internal contributors to double-check website
updates before pushing to GitHub and checking GitHub action updates.

Contributors making less-regular contributions, or those submitting quick
fixes to website pages, might opt to use our continuous integration (CI)
checks as a way to double-check the website build and also to check for
broken links, missing alt tags, and more within a pull request.

A large volume of the content in our GitHub repositories is text-based
documentation and tutorials. For text-based repositories, such as our
website, packaging guide, and peer review guide, we have CI platforms set
up that allow a contributor to submit a pull request with a change, without
needing to build the site locally.

### Supporting New Contributors

pyOpenSci strives to support new and existing contributors in enhancing our
online resources. We will support new contributors in this process. When a
new pull request is submitted by someone, we will do the following:

* Evaluate the contributor's background, where possible. If this is their
  first pull request submitted through a sprint, then we'll support them
  by pointing out CI and providing specific line-by-line feedback.
* If fixes to the existing PR are straightforward, the reviewer can
  "suggest inline changes" on the pull request by highlighting one or more
  modified lines and suggesting edits in place. This approach is often a
  quick way to integrate feedback from a review.
* If fixes to the existing PR are more involved, clearly articulate what is
  wrong in the pull request and ask the contributor if they feel comfortable
  addressing it. If they don't, then someone from the core pyOpenSci team
  can support them in getting their pull request edited, reviewed, and
  merged.

The above process is often implemented on a case-by-case basis depending on
the contributor's background.

:::{todo}
Did we address these questions above??

What are the expectations for an external contributor?
What should they have done locally?
Do we expect someone to have done all the wrangling with Ruby and Jekyll?
:::

## Pull Requests and Continuous Integration

At the bottom of every pull request is the Continuous Integration (CI) block.
This block contains a set of checks that pyOpenSci has set up. Each check
will have a red X or green check next to it.

## Pre-commit hooks and pre-commit.ci bot

pyOpenSci uses [pre-commit](https://pre-commit.com/) and the [precommit.ci bot](https://pre-commit.ci/) to style-check our repositories. This ensures our codebase remains clean, consistent, and free
from common errors.

For all repositories, we enable hooks that:

* Look for extra spaces at the end of files.
* Clean up trailing white space at the end of individual lines.
* Check for spelling issues within the repository.

For code repositories, we have several additional checks including:

* Code format & style checks (e.g. black, isort).

### About Pre-commit

[Pre-commit](https://pre-commit.com/) is a framework for managing and
maintaining multi-language pre-commit hooks. It ensures that code follows
specified style and format rules before it gets committed to the repository.

We generally use the following hooks:

* **Autoformat**: Makes sure files end in a newline and only a newline.
  * `end-of-file-fixer`
* **Lint**: Check for files with names that would conflict on a
  case-insensitive filesystem like MacOS HFS+ or Windows FAT.
  * `check-case-conflict`
* **Whitespace**: Clean up trailing white space at the end of individual lines.
  * `trailing-whitespace`
* **Spelling**: Check for spelling issues within the repository.
  * `codespell`

Setting up pre-commit locally is optional because we have the pre-commit bot
setup in our CI workflows. However, if you are a pyOpenSci staff member
regularly contributes, we suggest that you set it up locally in our repos to
ensure spell check errors (that the pre-commit CI bot cannot fix in a PR) are
addressed.

### Setting Up Pre-commit Locally

To set up pre-commit locally, follow these steps:

1. **Install pre-commit** if it's not already installed on your computer.

   ```bash
   pip install pre-commit
   ```

2. From the root of the pyOpenSci repository that you wish to run pre-commit
hooks on, run

   ```bash
   pre-commit install
   ```

This will install all of the hooks that pyOpenSci has setup for that repository.
Most often there is a spell checker, and several markdown file formatters, which
will remove excess white space.

3. To run pre-commit on all files in the repository -

  ```bash
  pre-commit run --all-files
  ```

4. pre-commit will run on all files that you modify

pre-commit will run after you add and commit a change to the repository locally.
Sometimes you may need to override pre-commit—for example if you have a
spelling issue that you know is correct, but pre-commit thinks is wrong, you
may want to force commit that change and ask for help in the repo when you
open a pr.

If you need to skip a local pre-commit check when you commit changes locally,
use:

  ```bash
  git commit "commit message here" --no-verify
  ```

### About the pre-commit CI bot

The [Pre-commit CI](https://pre-commit.ci/) bot is a continuous integration
service that automatically runs pre-commit hooks on each pull request. It
also allows you to call the bot to fix any issues with the pull request
(with the exception of misspelled words).

This helps maintain code quality and consistency without requiring
contributors to run pre-commit locally.

[Learn more about pre-commit CI in our CI section here](pre-commit-ci).

### Acknowledging new contributors

We use the [All-contributors bot](https://allcontributors.org/) to
acknowledge contributors across all of our GitHub repositories. Contributor
information is then published on
[our website](https://www.pyopensci.org/our-community/index.html#pyopensci-community-contributors).

### Who we acknowledge

pyOpenSci is liberal in acknowledging all contributions, regardless of
their size. When someone new submits an issue or PR, add them as a
contributor to the repo using the bot.

* It is okay if their name is already on our website as a contributor. If
  this is their first contribution to a different repo or a different type
  of contribution, add them. We will acknowledge the different types of
  contributions that our wonderful volunteers make.
* If they are already added as a contributor to the repo where the pull
  request is, that is okay too. The bot will inform you!

To add a contributor, at the bottom of a pull request or an issue, call the
following command:

   `@all-contributors please add @kiersi for code, review`

   Replace `@kiersi` with `@contributors-username`.

When you add a user, the bot will open a pull request that can be squashed
and merged. Once merged, their profile image and name will appear in the
README file of that repository.

pyOpenSci then has an automated build that will parse contributors across
all of our repos, adding them to the contributor list and noting the type(s)
of contributions that they have made (e.g., packaging guide, peer review
guide).

:::{todo}

## GitHub & CI

* CI (Continuous Integration) will be run on each new commit added to all
  of our public repositories (that have content).

### Permissions to run CI

In general, things are set up so CI doesn’t run automatically for new
contributors. Instead, someone with triage rights will need to approve the
workflow to run by hitting the "approve and run" button that will appear
(see image below). We have set things up this way to avoid spam PRs and
commits that might abuse our CI use. We could potentially adjust this in
the future, but we can also adjust by allowing more people with access
levels that can approve CI.
:::
