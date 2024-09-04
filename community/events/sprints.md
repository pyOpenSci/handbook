# pyOpenSci Sprints

:::{todo}

* TODO: <https://github.com/actions/add-to-project?tab=readme-ov-file> i think we want to set this up for all repositories so this works for scipy.
:::

:::{admonition} TL;DR

**Before a sprint**

* pyOpenSci staff go through the pyOpenSci repository issues and ensure all relevant **help-wanted** and **printable** have appropriated labels and have been added to the [GitHub project](GitHub-project) in the appropriate column (beginner-friendly, Python, dev-ops/ci, Python, Sphinx).
* pyOpenSci staff ensures all issues on the project board have enough **specific** information for a new user to follow and complete the task needed to be done. The more specific the issue is, the fewer questions a sprinter/contributor will ask during a sprint. This saves significant time and energy for both the sprint attendee and whoever is leading the sprint.

**During a sprint**

* Label all newly submitted issues as `sprint-event`
* Merge small PRs that are mergeable without significant review. Examples include typo fixes and other easy-to-review contributions.
* For PRs, add contributors to the GitHub repository that they contributed to using the [All Contributors bot](https://allcontributors.org/) using the command: `@all-contributors add @githubusername for code, review` (if the contribution is a pull request) or  `@all-contributors add @githubusername for review` (if the contribution is an issue). [More on using the bot here.](all-contribs)
* **IMPORTANT:** Be sure to add all contributors to each repo they've contributed to using the all-contributors bot. Merge the PR immediately after it is opened  and before another contributor is added to avoid merge conflicts.

**After a sprint**

Triage issues and pull requests.
 • Ensure that all contributors are added to each repository they've contributed to using the all-contributors bot.
 • Prioritize replying to, addressing, and merging pull requests. If an issue has a lingering TODO, tag it with a help-wanted label for a future sprint.
 • Send follow-up thank you notes.
 • Collect, process, and aggregate sprint metrics.
:::

## What is a sprint?

A sprint is an open session where contributors come together to contribute to an open source project. Contributors may range from beginners, who are new to sprints, GitHub, and git, to experienced developers. Below we review how pyOpenSci runs sprints.

There are three types of pyOpenSci sprint events:

1. **Community Sprint Events**: pyOpenSci hosts these at meetings it attends, such as PyCon US and the SciPy meeting.
2. **Online Sprint Events**: pyOpenSci may hold its own sprint events online to encourage global contributions.
3. **Community-hosted Sprint Events**: Contributors and community members host pyOpenSci sprint events at meetings they attend.

During pyOpenSci sprints, contributors need tasks that are "sprintable."
`Sprintable` tasks can be worked on and potentially completed (or
partially completed) in a single sitting, whether that time is a half-day or a full day.

Sprints last 1-5 days but are usually 1-2 days long. PyCon US sprints last an entire week, and SciPy meeting sprints last two days on the weekend.

### Tracking sprint contributions

Contributors frequently open numerous pull requests and issues during pyOpenSci sprint events. It's essential for pyOpenSci to track information around the following:

* Who is attending,
* Where they are from (country, state, etc.) and
* What contributions they make.

This information will support pyOpenSci's community impact and support and be
beneficial when we write grants and solicit sponsorships.

pyOpenSci uses a combination of GitHub project boards and user surveys to track participation and success metrics. More on that below.

## What motivates sprint participants?

Sprint participants are often motivated by different things. Some come to:

* Learn
* Help and support a project they care about
* Connect and build community

pyOpenSci supports and empowers all of the above motivations. We thrive on empowering new contributors to make their first (or second) contributions to open source! This impact aligns well with our mission. We also greatly benefit
from more experienced sprinters who can help move the organization's infrastructure and needs forward.

Sprints are always a win/win for pyOpenSci.

### pyOpenSci sprints are accessible

PyOpenSci should always be accessible to new and seasoned contributors, aligning with our mission, vision, and values. We aim to ensure that all participants have a successful experience within our community. Some participants are new and may be submitting their first-ever issue or pull request to an open-source project.

These participants:

* may need help using git and GitHub, or
* they may feel intimidated by their first contribution (but they want to try!).

Others are more experienced and
comfortable in a sprint environment but may have questions about more technical
open issues and the outcomes that pyOpenSci wants to see in issue solutions.
Supporting all of these participants is crucial to our mission and can require
significant effort during a sprint event.

As such, it's essential for anyone leading a sprint to come prepared! In most cases, having community helpers will go a long way toward supporting beginner contributor success.

(github-project)=

## Sprint infrastructure - GitHub projects

To efficiently manage and track contributions during sprints, pyOpenSci utilizes
[GitHub projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects). We use projects to organize issues and pull requests that contributors could potentially address during or outside of a sprint. Label any discrete task that someone could complete during a sprint as `sprintable`.

An organized project ensures that
contributors, whether new or experienced, can easily find and work on tasks
that suit their skills and interests.

:::{not}
We also are testing out using [event projects](https://github.com/orgs/pyOpenSci/projects/12) to track new contributions in the form of pull requests and issues that we receive during an event such as a PyCon US or SciPy sprint.
:::

#### Help-wanted board

The pyOpenSci [**help-wanted project board**](https://github.com/orgs/pyOpenSci/projects/3) is an organization-level GitHub project board that provides a central place where contributors can
find tasks that pyOpenSci needs help with. We have two automated workflows set up for the [help-wanted project board](https://github.com/orgs/pyOpenSci/projects/3):

* Any issue or pull request with the `help-wanted` label is automatically added to this board.
* When an issue or pull request is closed, it is automatically archived from the project board.

Tasks on this board are ideally smaller, well-defined, and can be completed or significantly advanced within the
duration of a sprint. Someone on the pyOpenSci team should update the project board throughout the year as new issues are opened in our organization's GitHub repositories. Continual updates make it easier for:

* Contributors to jump in and start contributing and
* Sprint leaders to prepare for a sprint as the board will be more up-to-date.

#### Tracking annual contributions: the sprint project board

At the start of each year, the pyOpenSci community manager creates a new Sprint GitHub Project Board. Here is an example of the [2024 sprint project board](https://github.com/orgs/pyOpenSci/projects/12).

The board will have several columns or statuses, each of which represents the name of a sprint event (example: `pyconus-2024`, `scipy-2024`, `fall-festival-2024`. pyOpenSci uses this project board to:

* **Track issues and pull requests opened during a sprint event**
* **Organize and Monitor Tasks**: Keep track of the progress of tasks during the sprint, ensuring clarity on which issues are being worked on and by whom.

* **Manage the Triage Process**: Track which pull requests have been addressed and merged and which ones still need attention.

* **Calculate metrics**: Provide counts of activity that has occurred during a sprint event.

These boards allow pyOpenSci staff to easily monitor sprint activities and outcomes, enabling timely resolution of all sprint issues and pull requests.

### Year-round sprint tasks

Below are tasks to stay on top of throughout the year. By adding "sprintable" and "help-wanted" issues to the help-wanted project board as they are opened, you save time spent preparing for a sprint.

#### Maintain the pyOpenSci help-wanted project board

pyOpenSci uses the GitHub [help-wanted project board](https://github.com/orgs/pyOpenSci/projects/3)
to keep track of tasks that volunteers can assist with. When you see an issue
opened, or if you open an issue yourself in any of our GitHub repositories within
our [pyOpenSci GitHub organization](https://www.github.com/pyopensci), always
consider whether the issue is something that someone else could help us with.

If the issue is something that someone else in the community could do:

1. **Add a `help-wanted` Label**: any issue or pull request with the `help-wanted`
 label in our organization will be automatically added to our [pyOpenSci
 help-wanted board](https://github.com/orgs/pyOpenSci/projects/3).

2. **Add a `sprintable` Label (if applicable)**: if the task could be completed
 during a sprint (meaning it is something that could be completed within an
 hour and up to a single day's worth of work), also add the label `sprintable`
 to the issue.

3. **Update the Status on the Project Board**: once the issue has been added to
 the project board (it normally takes our CI workflow 30 seconds to a minute),
 update the status of the issue on the project board based on the type of skill
 needed.

The current types of tasks in our board include:

* Python packaging
* Beginner friendly / non technical
* Dev Ops / GitHub actions (Continuous Integration)
* Python programming
* Website - CSS or Ruby

:::{todo}
we should add content review and sphinx as a status options for people that review our guidebook, run through tutorials etc.
:::

:::{admonition} Make sure issues contain specific, detailed information before adding them to a project board
:class: important

If you are creating a new `help-wanted` issue, it's important to include as much detailed information in the issue as possible. Imagine someone else reading the issue (that is not you!). In reading the issue, does an outside contributor have:

* enough information to understand the problem? (be specific, provide examples, links runnable code, broken github action runs)
* enough information to solve the problem?
* know exactly where the problem is occurring (provide links if you can or code examples)

When in doubt, more information is always better!
:::

It is important to label issues with `help-wanted` / `sprintable` throughout the year and as they are opened as we can. This will save significant when preparing for a sprint. It will also make it easier for fly-by contributors to find things to help us with throughout the year.

## Pre-sprint tasks

### Triage (help-wanted) issues across the pyOpenSci organization

Before a sprint begins, someone on the pyOpenSci team should go through and
triage all of the open issues in the organization to determine:

* Whether some of them are sprintable.
* Whether they have enough specific and detailed information for someone to work
 on the issue without too much help during a sprint.
* Whether some open issues can be closed.

This could be a small team exercise at a pre-meeting event held online for
pyOpenSci staff and sprint community members (if there are any contributors
participating).

The information found in the body of an issue is critical to running an effective
sprint. If the issue has very specific information that gives a potential
contributor everything they need to know to begin working, they will have fewer
questions during the sprint. If you have a table of 10-20 people sprinting for
pyOpenSci, this means the person running the sprint will have less to do on-site!
Sprints are busy—please add as much specific information as you can to each issue!

### Ensure issue and pull request templates are up to date

One challenge of a successful sprint is that there will be many issues and pull requests to triage after the sprint. To keep track of new issues during an event, every pyOpenSci GitHub repository should have a sprint issue template. Adding this template only needs to be completed once. However, if there is a new pyOpenSci Github repository (this rarely happens), make sure that repo has a sprint issue template.

The sprint template will auto-populate a `sprint-event` label on the issue or pull request when it is opened. We will then setup a GitHub action on the sprint project board for that year to auto-add any issue or pull request with the `sprint-event` label on it to the sprint project board.

:::{todo}
NOTE: i have setup this workflow <https://github.com/actions/add-to-project> on most (but not all) of our repos now. so it does handle moving help-wanted issues to the project. BUT it is hard to think about events. This is because there is no easy to use pull request template. so while we could automagically update a workflow before an event we'd have to do it for every event AND it would only work on issues - not pull requests. As such my idea of automating event tags won't work.

For now - we should do that manually during the event. It would be an easy enough thing for jesse to do remotely i think? or i could do it IF the sprint slows down. it really didn't at pycon this year (2024)
:::

:::{todo}

Jesse will flesh this out when it's ready!

### Create a participant signup form

* create the form
* create a dynamic qr code that we can update (the is placed on our table top cards ) OR get a card that we can add a sticker to with the code and replace the stickers...

jesse will develop this process with whatever platform we end up using...
:::

## Tasks during a sprint

Below are tasks that should occur during a sprint event.

### Collect participant information

*This section will be fleshed out soon...*
:::{todo}
The person running the event should collect information from participants
at the event via ______ **TODO insert how we do that here** _____ following the process Jesse creates above....

* dynamic qr code... that people can scan. with small table top signs?
* what do we collect?
* how do they opt out of future coms?

What Metrics do we collect and how?
Number of PRs
Number of issues
Who contributed
Where are the contributors from (country, place of work, other things??)

:::

### Update the sprint issue and pull request board

During the event, the remote sprint support team (either Community Manager or a volunteer), should:

* label all issues and pull requests as `sprint-event` and with the label for the event - e.g. `pyconus-24` as they are opened.
* Once that the `sprint-event` label is applied to an issue or pr, they with automatically be added to the project sprint board.
* Finally, once on the sprint board, they can then move each issue and pull request to the event name status on the sprint board. (this also can be done from the issue itself. )

This process, if done during the sprint, will make triaging issues and pull requests after the event, easier.

:::{todo}
We create one issue and pull requesttemplate that we can use across all our repos  – it has a label that automatically will be added to the board with "no status"
Jesse adds a label for the event and moves it to a column
:::

### Review and triage pull requests and issues

If you see small pull requests coming in that are clearly fixing things (typos, etc) in a guidebook, please review them and approve if that makes sense. If
you see an issue opened that makes sense to work on remotely with a participant, feel free to comment on it.

:::{todo}
We will need to feel some of this out at scipy.
:::

(all-contribs)=

### Acknowledge sprint contributors - All-Contributors Bot

pyOpenSci uses the [All-Contributors bot](https://allcontributors.org/docs/en/bot/usage)
to recognize and celebrate the contributions of all our contributors. This bot
helps automate the process of adding contributors to the repository, making it
easier to maintain accurate records of everyone's efforts.

To add contributors to the repository using the All-Contributors bot:

**Use the Bot Command**: In a comment on an issue or pull request, use the following command to add a contributor as follows.

  `@all-contributors add @githubusername for <contribution types>`

If they have opened an issue only, or reviewed an open pull request use:

  `@all-contributors add @githubusername for review`

If they have opened a pull request use:
  `@all-contributors add @githubusername for code, review`

2. **Merge all-contributor bot Pull Requests Individually**: The bot will create a pull request to update the
contributors list when you call the commands above. IMPORTANT: Merge each all-Contributors bot pull request individually and immediately before adding another contributor to avoid merge conflicts.

By recognizing contributors for their efforts, we foster a positive and inclusive
community, encouraging more participation and collaboration.

## After a sprint tasks

### Issue and PR triage

The biggest effort after a sprint will be triaging & addressing issues and pull requests that have been submitted during the sprint. This could take 1-2 weeks and up to a month depending on the scope of each change submitted.

If there are new issues with no associated pull request, you can:

1. Invite the issue author to submit a PR if the change seems reasonable and they are up to the task.
2. If the issue is one that we agree should be addressed, then label the issue with `help-wanted` / `sprintable` so someone else can tackle it at our next pyOpenSci sprint.

Review each pull request submitted (or invite community members to review) and determine if the pull request looks good as is or requires changes following the standard GitHub review process.

Merge the pull request when it is complete and ready to be merged.

### Followup thank you notes

After a sprint, we will follow up with participants to show our appreciation
and encourage continued engagement with the pyOpenSci community. Here are the key
steps to take:

1. **Send a Thank You Email**: Send an email to all sprint participants thanking them for their contributions. Express gratitude for their time and effort, highlighting any significant achievements or milestones reached during the sprint.

2. **Provide Feedback**: Include any relevant feedback or outcomes from the sprint. This could involve sharing metrics, such as the number of issues closed, pull requests merged, or any specific contributions that stood out.

3. **Invite Continued Engagement**:
   * **Newsletter**: Encourage participants to subscribe to the [pyOpenSci newsletter](https://eepurl.com/iM7SOM)
 to stay updated on future events, news, and opportunities.
   * **LinkedIn**: Invite them to follow [pyOpenSci on LinkedIn](https://www.linkedin.com/company/pyopensci) for professional updates
 and community highlights.
   * **GitHub**: Remind them to continue following and contributing to pyOpenSci
     [repositories on GitHub](https://github.com/pyopensci).
:::{todo}

* Discourse?
:::

4. **Stay Connected**:
   * **Upcoming Events**: Inform participants about upcoming sprints, webinars,
 workshops, or any other events they might be interested in.

By thanking contributors you are helping to maintain the momentum generated during the sprint, while also
fostering a sense of community, and encourage ongoing contributions to pyOpenSci projects.

### Final wrap up activities

We will have several outcome tasks to do to wrap up a sprint. These
are listed below:

* Blog post about the event with stats around activity (number of participants, pull requests, issues, etc). This post might highlight wins both big and "small"!
* Social media promoting the success of the event and above metrics
* LinkedIn newsletter reusing that blog post content

### Welcome new contributors to slack

Because some participants come to sprints to learn, they may not stage engaged with pyOpenSci after a sprint event. As such it's best to invite
people who continue to stay engaged with us either via GitHub or some
other mechanism (becoming a reviewer, editor, submitting a package, etc).

:::{admonition} Meeting metrics that pyOpenSci collects
:class: info

* Number of pull request submitted
* Number of issues submitted
* Number of contributors contributed
  * Where are the contributors from (country, place of work / organization)
  * Type of user - student, professional, non profit/ public sector.
  * Optional - demographics
:::

:::{todo}
SPRINTS: Collecting information during - sprints, etc - process so we can work together?
GDPR compliant database
Attendees - where do we keep this info?
Name
State / country
Company / org? (Affiliation)
Email address
GH username
Domain(s) of expertise
Survey data
Current role
Workshops attended
Social handles
:::
