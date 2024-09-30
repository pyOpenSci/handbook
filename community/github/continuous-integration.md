# 3. Continuous integration

## What is CI?

Continuous Integration (CI) refers to checks and tests that are triggered by
events that occur within a GitHub repository such as pushing a commit, opening a pull request, and
merging a pull request. In the pyOpenSci organization, each commit that is pushed 
to a GitHub repository triggers at least one or more automated CI workflows. For the [pyOpenSci
website repository](https://www.pyopensci.org/) and our online books such as
the [Python packaging guidebook](https://github.com/pyopensci/python-package-guide), this build will:

* Build the live rendered version of the online content with any changes added
  in the current commit(s) or pull requests.
* Check the text for spelling issues,
* Check images for missing alt tags, incorrect image paths and more.

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

```{figure} /images/ci-images/maintainer-approve-workflow.png
:alt: A screenshot of the GitHub CI notifications for a sample pyOpenSci repository. There are four rows of information. The first row reads "1 workflow awaiting approval. This workflow requires approval from a maintainer. Learn more about approving workflows. 1 failing and 1 successful checks. Underneath this text is a button that says "Approve and run." To the far right of the row is linked text reading Hide all checks. The text Learn more about approving workflows is linked. The second row has a red x on the left, followed by the letter P in a gold square, and the text pre-commit.ci - pr -- checks completed with failures. To the far right is linked text reading Details. On the third row there is a green check mark followed by the Circle CI logo and the text ci/circleci: build_book -- Your tests passed on CircleCI! And to the far right there is linked text reading Details. The fourth and final row has a small white checkmark inside a large green circle with text reading This branch has no conflicts with the base branch. Only those with write access to this repository can merge pull requests. The text write access is linked.

When a new contributor from outside of the pyOpenSci organization submits a pull request, this notification will appear. You can click the "Approve and run" button to approve and run continuous integration.
```

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

## pyOpenSci checks for broken links and missing alt tags: HTMLProofer

[HTMLProofer](https://github.com/gjtorikian/html-proofer) is a ruby-based HTML validation tool that checks for:

* correct image references
* accessibility including alt tags for each image
* broken links.

For a full list of checks, please refer to the [HTMLProofer documentation](https://github.com/gjtorikian/html-proofer).

The HTMLProofer tool is integrated into all pyOpenSci website GitHub repositories including the core website, the packaging guide, our peer review guide and this handbook that you are reading now. You can view the outputs from HTMLProofer on a pull request, by clicking on the Details section of CI build for each repository. 
For all of our sphinx books, the CI build that you will need to check is called **Build Push github pages / build-book (pull_request)** line. It looks like this:

```{figure} /images/github-images/htmlproofer-pass.png
:alt: A screenshot of the GitHub CI notifications for a sample pyOpenSci repository. There is a header that reads All checks have passed, with the text 3 successful checks beneath it. To the right side of the header is linked text reading Hide all checks. Below the header are three rows of information. The first row reads Build Push github pages / build-book (pull_request), the second reads ci/circleci: build_book -- Your tests passed on CircleCI!, and the third reads pre-commi.ci - pr -- checks completed successfully. There is a green checkmark next to each line of text. Beneath these rows is the text This branch has no conflicts with the base branch. Merging can be performed automatically. There is also a green Merge pull request button.

A screenshot from a GitHub PR where all checks have passed.
```

Once you click on the CI output Details, you'll be taken to the `build-book` jobs screen, which looks like this:

```{figure} /images/github-images/htmlproofer-build-book.png
:alt: A screenshot of the build-book jobs page in GitHub. There's a white column to the left with the job name and run details, and a large black box to the right with all of the various dropdowns within the build-book job. The htmlproofer dropdown is just over halfway down the page.

A screenshot of the build-book jobs page in GitHub.
```

When you expand the htmlproofer line, which reads Check HTML using htmlproofer, you will see the following:

```{figure} /images/github-images/htmlproofer-build-book.png
:alt: A screenshot of the build-book jobs page in GitHub with htmlproofer expanded. There's a white column to the left with the job name and run details, and a large black box to the right with all of the various dropdowns within the build-book job. The htmlproofer dropdown is just over halfway down the page and expanded to reveal information such as the run details, which checks were run, how many links were checked, whether or not HTMLProofer was successful, and how long the run took.

A screenshot of the build-book jobs page in GitHub with htmlproofer expanded.
```

If all of the HTMLProofer checks pass, you won't see any errors. Instead, you will see a bright green checkmark. However, sometimes you may encounter an error. 
Below is an image the shows a CI error associated with the build:

```{figure} /images/github-images/htmlproofer-fail.png
:alt: A screenshot of the GitHub CI notifications for a sample pyOpenSci repository. There is a header that reads All checks have passed, with the text 3 failing checks beneath it. To the right side of the header is linked text reading Hide all checks. Below the header are three rows of information. The first row reads Build Push github pages / build-book (pull_request), the second reads ci/circleci: build_book -- Your tests failed on CircleCI!, and the third reads pre-commi.ci - pr -- checks completed with failures. There is a red check next to each line of text. Beneath these rows is the text This branch has no conflicts with the base branch. Merging can be performed automatically. There is also a green Merge pull request button.

A screenshot from a GitHub PR where all checks have passed.
```

When there is an error in the pyOpenSci CI build, there are a few things to consider. 

1. Are the CI errors are unrelated to your pull request? pyOpenSci's CI builds run on all of the files in the repository by default. In some cases, a link might become broken simply because of the website being down. And that break has nothing to do with your pull request! In that case pyOpenSci repository maintianers can still merge the pull request, even if there are failed checks. 
2. There are also other CI checks that are happening within each repository in addition to HTML proofer. If more than one build fails, there may be more going on here than just an HTMLProofer error.

Below is an example of a broken build due to HTMLProofer. When you click on the details for the build, you see this:

```{figure} /images/github-images/htmlproofer-error-message.png
:alt: A screenshot of the build-book jobs page in GitHub with htmlproofer expanded. There's a white column to the left with the job name and run details with a large red X next to build-book, and a large black box to the right with all of the various dropdowns within the build-book job. The htmlproofer dropdown has a red X next to it, and is just over halfway down the page. When expanded, it reveals information such as the run details, which checks were run, how many links were checked, whether or not HTMLProofer was successful, and how long the run took.

A screenshot of the build-book jobs page in GitHub with htmlproofer expanded.
```

In this case, HTMLProofer told you that none of the images submitted with this PR could be found. In this case you should go back and double check that the images are in the correct folder and that their paths' are correct. In this case, the author forgot the leading forward slash in the image paths.

If you see a broken HTMLProofer build, you can continue to make updates to the pull request either locally or through inline comments, until no
errors are returned by HTMLProofer. Once you have a green check next to the build, it's time to submit your pull request for review!

:::{note}
In some cases you may be unsure as to why HTMLProofer or any part of our pyOpenSci CI checks are failing. In these cases, feel free to ping a pyOpenSci 
repository maintianer for help. We understand that Continuout Integration (CI) can be confusing to navigate even for seasoned GitHub users.
:::

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
