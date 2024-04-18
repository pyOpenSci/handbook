# GitHub



:::{todo}
1. for extra contributors - A pyopensci community member will reivew your post / contribution. you don't need to request a review.
1.
:::


pyOPenSci has a suite of GitHub repositories (repos) that support pyOpenSci processes and content including:

* website content
* tools that track contributors and keep the website up to date
* peer review

## Pull request & reviews associated with pyOpenSci GitHub repos

When possible, pull requests and issues should follow standards open source workflows. Below are guidelines for both issues and pull requests to consider.

### Guidelines for new issues

Issues in our repositories should be as specific as possible which will allow both the staff's future selves and outside contributors to understand the goal / desired outcome of addressing the issue.

In the case that an issue is opened that is unclear, a pyOpenSci staff member or designated community member can ask the issue author to provide more information.

If an issue opened is something that anyone in the community could potentially address, it's ideal to label the issue with `help-wanted`
and/or `sprintable`. A sprintable issue refers to an issue that could be completed or worked on during a 1-2 day sprint. As such this issue should be smaller / more confined in scope. A help-wanted issue is one that anyone is welcome to work on during whatever time they have available.

One the `help-wanted` or `sprintable` issue label is added, the issue will be automagically added to our [pyOpenSci help-wanted board](https://github.com/orgs/pyOpenSci/projects/3).

:::{todo}
Add section on labels
:::

#### Issue maintenance

Our goal at pyOpenSci is to keep the list of issues current and active. Monthly issue cleanup sessions will be implemented to ensure issues are either being actively addressed and/or to assess whether older / stale issues can be potentially closed.


## Pull Requests

### Elements of a clean pull request

Authors of new pull requests should whenever possible, do their best to create clean pull requests. A clean pull request:

* is focused, and easy to review,
* can be more quickly reviewed (and in turn merged) so it saves everyone time.

:::{tip}
Review your own pull request before asking someone else to review it for you. You might be surprised that you notice things in the pull request that you didn't notice when working on the content locally.
:::

1. **Keep It Small**: Aim for one logical change per pull request to simplify review.
1. **Create descriptive PR Title and Summary**: Clearly state what the PR achieves and why, including any related issue numbers or discussions.
1. **Double check that the files committed to the pull request clearly align with the suggested changes being made in the pull request**. For example if a new guidebook page contains images, all images that are new to the guidebook should be included in the list of files in the pr. If the new page reuses images, then link to the existing images in the repository rather than re-adding them.
1. **Follow Coding Standards (if applicable)**: Stick to the project's coding guidelines for style and organization if they exist. This is more often relevant to code pull requests than text.
1. **Review Your Own Code**: Look over your PR critically before requesting reviews to catch any mistakes early.
1. **Respond Respectfully**: Be open to feedback and discuss suggestions to improve  the project.
1. **Check CI for any red x's (more on CI below)**: If your pull request returns a red X in the "checks/CI" section, then it's worth seeing if you can figure out what is broken in the build. If you aren't sure - no problem. Leave a note for the reviewer to allow them to help you understand what needs to be fixed (if anything).

#### Highly Recommended

1. **Create clear Commit Messages**: Explain why changes are made, not just what was changed.
1. **Keep Your Branch Updated**: Regularly rebase your fork from the main branch (is possible) to avoid / clean up any merge conflicts and to keep your PR up to date.


https://opensource.com/article/18/6/anatomy-perfect-pull-request#:~:text=Large%20pull%20requests%20cause%20a,and%20do%20only%20one%20thing.


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


What are the expectations for an external contributor?
What should they have done locally?
Do we expect someone to have done all the wrangling with Ruby and Jekyll?

### Pull requests and CI

### Continuous Integration


At the bottom of every pull request is the CI block.  The images below show the block for the rdata blog. Here a few things need to happen.

Someone with organization permissions needs to approve and run CI. If you
have those super powers, please go ahead and allow CI to run for new contributors. You can’t break anything by running CI so always feel confident in our repos clicking that button if the PR is legitimate and submitted from a valid user!

Next to each CI step that was run there is a details button. Generally, if you click on that link, it will give you more information about what has run / not run as expected in the build. All of our website repositories have several CI builds including

1. a link checker
2. htmlproofer that checks both links and alt tags, images
3. a CI build that shows you what the rendered site looks like when built online. Currently we are using CircleCI for that build.


## Pre commit .ci bot

pyOpenSci uses pre-commit and the precommit.ci bot to style check our repositories.

For all repositories we enable hooks that:

* Look for extra spaces at the end of files
* Clean up trailing white space at the end of individual lines
* Check for spelling issues within the repository.

For code repositories, we have several additional checks including:

* code format & style checks (e.g. black, isort)

Notice pre-commit.ci has a red x. And notice next to each ci item there is a Details link. Click on details for pre-commit ci and it will take you to the image below…


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




### About pre-commit



* Setting it up locally (there must be a blog post somewhere or it could be in our guidebook )
* Using the bot instead (see below)


### About the pre-commit CI bot



* [Pre-commit CI bot](https://pre-commit.ci/) - more here about how this works and the bot!
* What the bot can fix
* What the bot can’t fix

In our GitHub, you will find several repositories with guides on how to submit packages to our interface.
