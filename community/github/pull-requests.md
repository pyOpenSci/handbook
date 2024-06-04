# 2. pyOpenSci pull request process

When possible, pull request and issue submissions and reviews should follow standard open source workflows. Below are guidelines for pull requests.

## Pull Requests

New pull requests should:

* be created from a fork rather than the pyOpenSci owned parent repository.
* never be submitted from the `main` branch of your fork.

Authors of new pull requests should, whenever possible, do their best to create clean pull requests.

A clean pull request:

* is focused, and easy to review,
* can be more quickly reviewed (and in turn merged), saving everyone time, and
* closes an existing issue (with the exception of new content such as blog posts, which we manage internally using Asana)

:::{tip}
Review your own pull request before asking someone else to review it for you. You might be surprised that you notice things in the pull request that you didn't notice when working on the content locally.
:::

### Pull request content

Below are some guidelines for pull request content. Clean pull requests lead to simpler reviews & faster merging!

1. **Keep It Small**: Aim for one logical change per pull request to simplify review.
1. **Create a descriptive PR Title and Summary**: Clearly state what the PR achieves and why, including any related issue numbers or discussions.
1. **Double check that the files committed to the pull request clearly align with the suggested changes being made in the pull request**. For example, if a new guidebook page contains images, all images that are new to the guidebook should be included in the list of files in the pr. If the new page reuses images, then link to the existing images in the repository rather than re-adding them.
1. **Follow coding / style guide and other organization standards (if applicable)**: Stick to the project's coding guidelines for style and organization, if they exist. This is more often relevant to code pull requests than text.
1. **Review Your Own Pull request first**: Look over your PR critically before requesting reviews, in order to catch any mistakes early.
1. **Respond Respectfully**: Be open to feedback and discuss suggestions to improve  the project.
1. **Check CI for any red X's (more on CI below)**: If your pull request returns a red X in the "checks/CI" section, then it's worth seeing if you can figure out what is broken in the build. If you aren't sure, no problem. Leave a note for the reviewer to allow them to help you understand what needs to be fixed (if anything).

### Highly Recommended

1. **Create clear commit messages**: Explain why changes are made, not just what was changed.
1. **Keep your branch updated**: Regularly rebase your fork from the main branch (if possible) to avoid / clean up any merge conflicts and to keep your PR up to date.

:::{info}

* [tips for better pull requests](https://opensource.com/article/18/6/anatomy-perfect-pull-request)
* pyOpenSci has also enabled an "update branch" feature in the pull request, which will update your branch to be in sync with main. In most cases, this creates a merge commit rather than a rebase.
:::

### Regular vs New Contributors

There is no right or wrong when it comes to building a website repository locally. pyOpenSci staff and other community members who contribute to pyOpenSci regularly will often opt to build online
resources locally for live interactive development and edits. Building locally
is an ideal way for internal contributors to double check website updates before pushing to GitHub and looking at GitHub action updates.

Contributors making less-regular contributions, or those submitting quick fixes to pages on our website, might opt to use our continuous integration (CI) checks as a way to double check the website build and also to check for broken and bad links, missing alt tags and more within a pull request.

A large volume of the content in our GitHub repositories is text-based
documentation and tutorials. For text-based repositories, such as our
website, packaging guide and peer review guide, we have CI platforms set up that allow a contributor to submit a pull request with a change, without needing to build the site locally.

### Supporting new contributors

pyOpenSci strives to support new and existing contributors in enhancing our online resources. As such, we will support new contributors in this process. When a new pull request is submitted by someone, we will do the following:

* Evaluate the contributors background, where possible. If this is their first pull request submitted through a sprint, then we'll support them in their efforts by pointing out CI and providing specific line-by-line feedback.
* If fixes to the existing pr are straight forward, the reviewer can "suggest inline changes" on the pull request by highlighting one or more modified lines, and suggesting edits in place. This approach of inline suggestions is often a quick way to integrate feedback from a review.
* If fixes to the existing PR are more involved, clearly articulate what is wrong in the pull request and ask the contributor if they feel comfortable addressing it. If they don't, then someone in the core pyOpenSci team can support them in getting their pull request edited, reviewed and merged.

The above process is often implemented on a case-by-case basis depending on the contributor's background.

:::{todo}
Did we address these questions above??

What are the expectations for an external contributor?
What should they have done locally?
Do we expect someone to have done all the wrangling with Ruby and Jekyll?
:::

## Pull requests and Continuous Integration

At the bottom of every pull request is the Continuous Integration (CI) block. This block contains a set of checks that pyOpenSci has set up. Each check will have a red X or green check next to it.

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
setup in our CI workflows. However, if you are a pyOpenSci staff member regularly contributes, we suggest that you set it up locally in our repos to ensure
spell check errors (that the pre-commit CI bot cannot fix in a PR) are addressed.

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

### About the pre-commit CI Bot

The [Pre-commit CI](https://pre-commit.ci/) bot is a continuous integration service that automatically
runs pre-commit hooks on each pull request. It also allows you to call the bot
to fix any issues with the pull request (with the exception of misspelled words).

This helps maintain code quality
and consistency without requiring contributors to run pre-commit locally.

[Learn more about pre-commit ci in our CI section here](pre-commit-ci)

### Acknowledging New Contributors

We use the [All-contributors bot](https://allcontributors.org/) to acknowledge
contributors across all of our GitHub repositories. Contributor information
is then published on [our website](https://www.pyopensci.org/our-community/index.html#pyopensci-community-contributors).

### Who we acknowledge

pyOpenSci is liberal in acknowledging all contributions, regardless of their size. When
someone new submits an issue or PR, add them as a contributor to the repo using
the bot.

* It is ok if their name is already on our website as a contributor,
if this is their first contribution to a different repo, or a different type of contribution, add them. We will acknowledge the different types of contributions that our wonderful volunteers make.
* If they are already added as a contributor to the repo where the pull request is, that is ok too. The bot will inform you!

To add a contributor, at the bottom of a pull request or an issue, call the
following command:

`@all-contributors please add @kiersi for code, review`

replaceing `@kiersi` with `@contributors-username`.

When you add a user, the bot will open a pull request that can be squashed
and merged. Once merged, their profile image and name will appear in the
README file of that repository.

pyOpenSci then has an automated build that will parse contributors across all of
our repos, adding them to
the contributor list and noting the type(s) of contributions that they have made
(e.g., packaging guide, peer review guide).

:::{todo}

## GitHub & CI

* CI (Continuous integration) will be run on each new commit added to all of our public repositories (that have content).

### Permissions to run CI

In general, things are setup so CI doesn’t run automagically for new contributors. Rather, someone with triage rights will need to approve the workflow to run by hitting the approve and run button that will appear (see image below). We have things set up this way to avoid spam PRs and commits that will abuse our CI use. We could potentially adjust in the future, but also can adjust by allowing more people with “access levels” that can approve CI.
:::
