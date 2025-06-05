# pyOpenSci GitHub issue process

When possible, GitHub pull requests, issue submissions, and reviews should follow
standard open source workflows. Below are guidelines for handling issues in the
pyOpenSci GitHub organization.

## Guidelines for new issues

**Issues should be as specific as possible:** Specificity within an issue helps
both our future selves and outside contributors understand the goal or desired
outcome associated with addressing the issue. This is important both internally
and for issues tagged as `help-wanted`, which we hope community members will
address in pyOpenSci sprints.

To ensure an issue is well-written and specific, include the following details:

- **Clear title:** A concise and descriptive title summarizing the issue or
  feature request helps us scan through issues and understand what each issue is
  about. Below are some example titles that are specific:

  - `Bug: broken link in link-to-page-here / name of page / document etc`
  - `Fix: confusing paragraph on Python packaging with Hatch`
  - `Add: page on using pixi for dependencies`

- **Description:** A detailed explanation of the issue or feature request,
  including context, background information, and the reason for the request.
  Explain why the issue is important and what problem it solves.

- **Screenshots/code samples:** Include screenshots, code snippets, links, or
  any other relevant files that can help others in understanding the issue
  better.

- **Possible solutions/recommendations:** It's helpful to provide any ideas or
  suggestions for how to address the issue, which can help guide contributors
  towards a solution.

- **Related issues or pull requests:** Add references to any related issues or
  pull requests, which provides additional context and understanding of the
  broader scope of the issue.

### If you are reporting a code bug

- **Steps to reproduce (for bugs):** A step-by-step guide (generally a list or
  narrative) on how to reproduce the issue, including relevant code snippets,
  commands, or configurations.

- **Expected vs. actual behavior (for bugs):** A description of what you
  expected to happen and what actually happened. This helps in understanding
  the discrepancy and the impact of the bug.

- **Environment details (for bugs):** Details about the environment where the
  issue was observed, such as operating system, Python version, library
  versions, and any other relevant software/hardware details.

### If you have permissions, label the issue

While outside contributors will not have permission to label issues, pyOpenSci
core team members and volunteers will. Be sure to add appropriate labels to
issues to make them easier to triage.

## Help-wanted / sprintable issues

If an issue is something that anyone in the community could potentially address,
it's ideal to label the issue with `help-wanted` and/or `sprintable`. A
sprintable issue refers to an issue that could be completed or worked on during
a 1-2 day sprint, thus it should be smaller and more confined in scope. A
help-wanted issue is one that anyone is welcome to work on during whatever time
they have available.

Once the `help-wanted` or `sprintable` issue label is added, the issue will be
automatically added to our
[pyOpenSci help-wanted board](https://github.com/orgs/pyOpenSci/projects/3).
This automation is implemented currently for a single repository (the packaging
guide), but we plan to implement it for other repositories using the
add-to-project GitHub action.

:::{note}
The issue will be archived from the project board once it is closed.
:::

:::{seealso}
[Learn more about pyOpenSci sprint events.](/community/events/sprints)
:::

If an issue is unclear, a pyOpenSci staff member or designated community member
can ask the issue author to provide more information.

:::{todo}
Add section on labels once we have things synced up across repos.
:::

## Issue maintenance

Our goal at pyOpenSci is to keep our list of issues current and active.
Quarterly issue cleanup sessions are implemented to ensure issues are either
being actively addressed or to assess whether older or stale issues can
potentially be closed.
