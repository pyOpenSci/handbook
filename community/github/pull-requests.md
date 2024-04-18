# pyOpenSci pull request process

When possible, pull request and issue submissions and reviews should follow standard open source workflows. Below are guidelines for pull requests.

## Pull Requests

Authors of new pull requests should whenever possible, do their best to create clean pull requests. A clean pull request:

* is focused, and easy to review,
* can be more quickly reviewed (and in turn merged) so it saves everyone time.
* closes an existing issue (with the exception of new content such as blog posts that we manage internally using Asana)

:::{tip}
Review your own pull request before asking someone else to review it for you. You might be surprised that you notice things in the pull request that you didn't notice when working on the content locally.
:::

1. **Keep It Small**: Aim for one logical change per pull request to simplify review.
1. **Create descriptive PR Title and Summary**: Clearly state what the PR achieves and why, including any related issue numbers or discussions.
1. **Double check that the files committed to the pull request clearly align with the suggested changes being made in the pull request**. For example if a new guidebook page contains images, all images that are new to the guidebook should be included in the list of files in the pr. If the new page reuses images, then link to the existing images in the repository rather than re-adding them.
1. **Follow Coding / style guide and other organization Standards (if applicable)**: Stick to the project's coding guidelines for style and organization if they exist. This is more often relevant to code pull requests than text.
1. **Review Your Own Pull request first**: Look over your PR critically before requesting reviews to catch any mistakes early.
1. **Respond Respectfully**: Be open to feedback and discuss suggestions to improve  the project.
1. **Check CI for any red x's (more on CI below)**: If your pull request returns a red X in the "checks/CI" section, then it's worth seeing if you can figure out what is broken in the build. If you aren't sure - no problem. Leave a note for the reviewer to allow them to help you understand what needs to be fixed (if anything).

#### Highly Recommended

1. **Create clear Commit Messages**: Explain why changes are made, not just what was changed.
1. **Keep Your Branch Updated**: Regularly rebase your fork from the main branch (is possible) to avoid / clean up any merge conflicts and to keep your PR up to date.

:::{info}
* [tips for better pull requests](https://opensource.com/article/18/6/anatomy-perfect-pull-request)
:::

### Regular vs New Contributors

There is no right or wrong when it comes to building a website repository locally. pyOpenSci staff and other community members who contribute to pyOpenSci regularly will often opt to build online
resources locally for live interactive development and edits. Building locally
is an ideal way for internal contributors to double check website updates before pushing to github and looking at GitHub action updates.

Contributors making less-regular contributions, or those submitting quick fixes to pages on our website, might opt to use our continuous integration (CI) checks as a way to double check the website build and also to check for broken and bad links, missing alt tags and more within a pull request.

A large volume of the content in our GitHub repositories is text based
documentation and tutorials. For text based repositories such as our
website, packaging guide and peer review guide, we have CI platforms setup that allow a contributor to submit a pull request with a change, without needing to build the site locally.

### Supporting new contributors

pyOpenSci strives to support new and existing contributors in enhancing our online resources. As such we will support new contributors in this process. When a new pull request is submitted by someone we will do the following:

* Evaluate the contributors background if that is possible. If this is their first pull request submitted through a sprint, then support them in their efforts by pointing out CI and provide specific line-by-line feedback.
* If fixes to the existing pr are straight forward, the reviewer can "suggest inline changes" on the pull request by highlighting 1 or more modified lines, and suggesting edits in place. This approach of inline suggestions, is often a quick way to integrate feedback from a review
* If fixes to the existing PR are more involved, clearly articulate what is wrong in the pull request, and ask the contributor if they feel comfortable addressing it. If they don't, then someone in the core pyOpenSci team can support them in getting their pull request edited, reviewed and merged.

The above process is often implemented on a case by case basis depending on the contributors background.

:::{todo}
Did we address these questions above??


What are the expectations for an external contributor?
What should they have done locally?
Do we expect someone to have done all the wrangling with Ruby and Jekyll?
:::

## Pull requests and Continuous Integration

At the bottom of every pull request is the Continuous Integration (CI) block. This block contains a set of checks that pyOpenSci has setup. Each check will have a red X's or green check next to it.

### What is CI

Continuous Integration (CI) refers to checks and tests that run on every change (or commit) to a GitHub repository. In the pyOpenSci organization, each commit
triggers at least one or more automated CI workflows. For the website and sphinx books this build will:

* build the live rendered version of the online content with any changes added in the current commit(s) or pull requests.
* check the text for spelling issues, check images for missing alt tags and more

If the repository has code, it will check for code style.

Having a CI setup on each pyOpenSci github repository ensures that we detect issues such as bad links, or broken code, before it's merged into the main repository.

### What do the green and red checks mean?

The green and red checks in the CI block indicate the status of these automated
checks:

* **Green Checks**: These indicate that the code has passed the CI  checks. This means the code meets the project's standards and is likely
free from errors or issues related to the specific checks that have passed.

* **Red X's**: These indicate that the code has failed the associated CI   checks. This means there are issues that need to be addressed before the code can be merged. The issues could be related to code style, formatting, tests, or other criteria specified by the CI configuration.

#### If a CI check is red:

1. **Click on "Details"** next to the failed check to get more information about the failure.
2. **Review the logs or output** provided to understand what went wrong.
3. **Make the necessary changes** to fix the issue.
4. **Push the updated code** to the pull request to trigger the CI checks again.

If something isn't working as expected or you are having a hard time understanding why CI is failing (we've all been there!) please ping someone else in the organization for help. As a pyOpenSci community, we are always here to help each other.

If all CI checks are green, you are good to go. Ping someone to review your pull request. The pull request can be merged once you have a approval from another repository owner.

:::{note}
Generally we require a single passing approval in order to merge a pull request. however, in some cases, if you are a pyOpenSci staff member or community member with admin / write access, it could be the case that you need to merge something immediately (ie fixing a small piece of breaking code, a spelling error, or adding a new piece of content that has already been agreed upon).
:::





## CI and outside contributors

Someone with organization permissions needs to approve and run CI. If you
have those super powers, please go ahead and allow CI to run for new contributors. You can’t break anything by running CI so always feel confident in our repos clicking that button if the PR is legitimate and submitted from a valid user!

Next to each CI step that was run there is a details button. Generally, if you click on that link, it will give you more information about what has run / not run as expected in the build. All of our website repositories have several CI builds including

1. a link checker
2. htmlproofer that checks both links and alt tags, images
3. a CI build that shows you what the rendered site looks like when built online. Currently we are using CircleCI for that build.


## Pre-commit hooks and pre-commit.ci bot

pyOpenSci uses pre-commit and the precommit.ci bot to style check our repositories. This ensures our codebase remains clean, consistent, and free
from common errors.

For all repositories we enable hooks that:

* Look for extra spaces at the end of files
* Clean up trailing white space at the end of individual lines
* Check for spelling issues within the repository.

For code repositories, we have several additional checks including:

* Code format & style checks (e.g. black, isort)

### About pre-commit.ci
add text here about the prec-mmit ci bot and a link to it.
Notice pre-commit.ci has a red x. And notice next to each ci item there is a Details link. Click on details for pre-commit ci and it will take you to the image below…

### About Pre-commit

[Pre-commit](https://pre-commit.com/) is a framework for managing and
maintaining multi-language pre-commit hooks. It ensures that code follows
specified style and format rules before it gets committed to the repository.

We generally use the following hooks:

* **Autoformat**: Makes sure files end in a newline and only a newline.
  - `end-of-file-fixer`
* **Lint**: Check for files with names that would conflict on a
  case-insensitive filesystem like MacOS HFS+ or Windows FAT.
  - `check-case-conflict`
* **Whitespace**: Clean up trailing white space at the end of individual lines.
  - `trailing-whitespace`
* **Spelling**: Check for spelling issues within the repository.
  - `codespell`

### Setting Up Pre-commit Locally

To set up pre-commit locally, follow these steps:

1. **Install pre-commit**:
   ```bash
   pip install pre-commit


### About the pre-commit CI Bot

The Pre-commit CI bot is a continuous integration service that automatically
runs pre-commit hooks on each pull request. This helps maintain code quality
and consistency without requiring developers to run pre-commit locally.

#### What the bot can fix:

* Automatically fix formatting issues such as trailing whitespace and missing
  newlines.
* Apply code style adjustments as specified by hooks like `black` and `isort`.

#### What the bot can’t fix:

* Logical errors or bugs in the code.
* Issues that require human judgment, such as resolving complex merge
  conflicts or making design decisions.

### Using the Bot Instead

If you prefer not to set up pre-commit locally, you can rely on the
pre-commit.ci bot. It automatically runs the pre-commit hooks on each pull
request, ensuring the codebase remains clean and consistent.

#### Using the bot is simple:

1. **Enable pre-commit.ci** on your repository through the
   [pre-commit.ci website](https://pre-commit.ci/).
2. The bot will automatically run checks and apply fixes on pull requests.
3. Review the bot's output and ensure all checks pass before merging your code.

This approach ensures that all contributions meet the project's code quality
standards without requiring each developer to install and run pre-commit
locally.


### Tools used in our GitHub repo

[All-contributors bot](https://allcontributors.org/) – how we track contributors



* TO use - when someone new submits an issue or pr please add them to that repo as a contributor.  We track how people contribute so even if they have contributed to another repo please add them in a repo. If they are already added as a contributor, the bot will tell you!
* To do this - use the syntax below replacing @usernamehere for the @GitHubusername of the person who contributed
* When you add a user, the bot will open a pull request that can be squashed and merged. Once merged, their profile image and name will appear in the README file of that repository.
* Our automated build will parse contributors across our repos and add them to the contributor list also adding the type(s) of contributions they have made (packaging guide, peer review guide etc).



## GitHub & CI



* Ci (Continuous integration)  will be run on each new commit added to all of our public repositories (that have content).


### Permissions to run CI

In general, things are setup so CI doesn’t run automagically for new contributors. Rather, someone with triage (?) rights will need to approve the workflow to run by hitting the approve and run button that will appear (see image below). We have things setup this way to avoid spam pr’s commits that will abuse our CI use. We could potentially adjust in the future - but also we could adjust but allowing more people with “access levels” that can approve CI.
