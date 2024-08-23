# 3. Continuous integration

## What is CI?

Continuous Integration (CI) refers to checks and tests that are triggered by
events that occur on GitHub such as commit pushes, pull requests, and even
merges to a GitHub repository. In the pyOpenSci organization, each commit
triggers at least one or more automated CI workflows. For the [pyOpenSci
website repository](https://www.pyopensci.org/) and our online books such as
the [Python packaging guidebook that is written using
Sphinx](https://github.com/pyopensci/python-package-guide), this build will:

* Build the live rendered version of the online content with any changes added
  in the current commit(s) or pull requests.
* Check the text for spelling issues, check images for missing alt tags, and
  more.

If the repository has code, it will check for code style.

Having a CI setup on each pyOpenSci GitHub repository ensures that we detect
issues such as bad links or broken code before they're merged into the main
repository.

### What do the green and red checks mean?

The green and red checks in the CI block indicate the status of these automated
checks:

* **Green checks**: These indicate that the code has passed the CI checks.
  This means the code meets the project's standards and is likely free from
  errors or issues related to the specific checks that have passed.
* **Red X's**: These indicate that the code has failed the associated CI
  checks. This means there are issues that need to be addressed before the code
  can be merged. The issues could be related to code style, formatting, tests,
  or other criteria specified by the CI configuration.

```{figure} /images/ci-images/contributor-ci-fail.png
:alt: A screenshot of the GitHub CI notifications for a sample pyOpenSci repository. There are four rows of information. The first row reads "1 workflow awaiting approval. This workflow requires approval from a maintainer. Learn more about approving workflows. 1 failing and 1 successful checks. To the far right of the row is linked text reading Hide all checks. The text Learn more about approving workflows is linked. The second row has a red x on the left, followed by the letter P in a gold square, and the text pre-commit.ci - pr -- checks completed with failures. To the far right is linked text reading Details. On the third row there is a green check mark followed by the Circle CI logo and the text ci/circleci: build_book -- Your tests passed on CircleCI! And to the far right there is linked text reading Details. The fourth and final row has a small white checkmark inside a large green circle with text reading This branch has no conflicts with the base branch. Only those with write access to this repository can merge pull requests. The text write access is linked.

When a CI check fails, you'll see a red 'X' next to the CI check that hasn't passed
```
#### If a CI check is red

1. **Click on "Details"** next to the failed check to get more information
   about the failure.
2. **Review the logs or output** provided to understand what went wrong.
3. **Make the necessary changes** to fix the issue.
4. **Push the updated code** to the pull request to trigger the CI checks
   again.

If something isn't working as expected or you are having a hard time
understanding why CI is failing (we've all been there!), please ping someone
else in the organization for help. As a pyOpenSci community, we are always
here to help each other.

If all CI checks are green, you are good to go. Ping a pyOpenSci repository
owner on GitHub to review your pull request. The pull request can be merged
once you have approval from another repository owner.

If you don't know who to ping, no worries. Someone from the pyOpenSci
organization will see your pull request and get back to you.

:::{note}
Generally, we require a single passing approval to merge a pull request.
However, in some cases, if you are a pyOpenSci staff member or community
member with admin/write access, it could be the case that you need to merge
something immediately (i.e., fixing a small piece of breaking code, a spelling
error, or adding a new piece of content that has already been agreed upon).
:::

## CI and outside contributors

If someone from outside of the pyOpenSci organization submits a pull request,
then someone within the organization needs to approve and run CI. If you have
those superpowers, please go ahead and allow CI to run for new contributors.
You can’t break anything by running CI, so always feel confident in our repos
when you click that button, assuming that the PR is legitimate and submitted
from a valid user!

Next to each CI step that was run, there is a details button. If you click on
that link, it will give you more information about what has run/not run as
expected in the build.

## Website CI checks

All of our website repositories have several CI builds, including:

1. A link checker.
2. `htmlproofer`, which checks both links and alt tags, as well as images.
3. A CI build that shows you what the rendered site looks like when built
   online. Currently, we are using [CircleCI](https://circleci.com/) for a
   live rendered build, as CircleCI allows for in-browser website build checks.
   GitHub requires you to download, unzip, and view an archive with the build
   site locally.

(pre-commit-ci)=
## About the Pre-Commit CI Bot

The [Pre-commit CI bot](https://pre-commit.ci/) is a continuous integration
service that automatically runs pre-commit hooks on each pull request. This
helps maintain code quality and consistency without requiring developers to
run pre-commit locally.

To run the bot on a PR, add the following command to a standalone comment:

`pre-commit autofix`

When you do this, the bot will run all of the hooks that it can, adding a new
commit to the pull request for you.

### What the bot can fix

The bot can in-place fix many linting and style issues in our content,
including:

* Automatically fixing formatting issues such as trailing whitespace and
  missing newlines.
* Applying code style adjustments as specified by hooks like
  [`black`](https://github.com/psf/black) and
  [`isort`](https://pycqa.github.io/isort/).

### What the bot can’t fix

The bot can't fix some things, such as:

* Logical errors or bugs in the code.
* Issues that require human judgment, such as resolving complex merge
  conflicts or making design decisions.
* Spelling errors.

If the bot finds errors that it can't fix, you will need to make those changes
locally.

### Using the bot instead of pre-commit hooks

pyOpenSci contributors may prefer not to set up pre-commit locally. In that
case, we can rely on the pre-commit.ci bot to fix things as needed.

### Bot setup

To set up the bot in a new repository:

1. **Enable pre-commit.ci** on your repository through the
   [pre-commit.ci website](https://pre-commit.ci/).
2. The pre-commit.ci bot will automatically run checks and apply fixes on
   pull requests.
3. Review the bot's output and ensure all checks pass before merging your
   code.

This approach ensures that all contributions meet our pyOpenSci code and text
quality standards without requiring each contributor to install and run
pre-commit locally.
