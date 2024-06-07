# pyOpenSci Sprints

:::{todo}
* TODO: https://github.com/actions/add-to-project?tab=readme-ov-file i think we want to set this up for all repos so this works for scipy.
:::

:::{admonition} TL;DR

**Before a sprint**

* pyOpenSci staff go through the pyOpenSci repo issues and ensure all relevant **help-wanted** and/or **sprintable**  both have appropriated labels and have been added to the the project board in the appropriate column (beginner-friendly, python, dev-ops/ci, Python, Sphinx).
* pyOpenSci staff ensure all issues on the project board have enough **specific** information for a new user to follow and complete the task needed to be done. The more specific the issue is, the fewer questions a sprinter / contributor will ask during a sprint. This saves significant time and energy for both the sprint attendee and whomever is leading the sprint.

**During a sprint**

* Label all newly submitted issues as `sprint-event`, `sprint-name-year` (example: `sprint`, `pyconus-24`)
* Merge small PRs that are clearly mergeable without significant review. Examples might include: typo fixes and other easy-to- review contributions.
* For PRs, add contributors to the GitHub repository that they contributed to using the [All Contributors bot](https://allcontributors.org/) using the command: `@all-contributors add @githubusername for code, review` (if the contribution is a pull request) or  `@all-contributors add @githubusername for review` (if the contribution is an issue
* **IMPORTANT:** Merge each all-contributor-bot PR's individually and immediately after they have been opened to avoid merge conflicts

**After a sprint**

* Triage issues and pull requests
* Make sure all contributors have been added to each repo they've contributed to using the all-contributors bot.
* Focus on replying, addressing and merging pull requests as we can. If an issue has a lingering TODO - consider tagging it with a `help-wanted` label for a future sprint.
* Send followup *thank you for participating* notes
* Collect / process / aggregate sprint metrics
:::


## What is a sprint?
A sprint is an open session where contributors come together to contribute to an open source project. Contributors may range from beginners, who are new to sprints, GitHub, and git, to experienced developers. Below we review how pyOpenSci runs sprints.

There are three types of pyOpenSci sprint events:

1. **Community Sprint Events**: pyOpenSci hosts these at meetings it attends, such as PyCon US and the SciPy meeting.
2. **Online Sprint Events**: pyOpenSci may hold its own sprint events online to encourage global contributions.
3. **Community-hosted Sprint Events**: Contributors and community members host pyOpenSci sprint events at meetings they attend.

During pyOpenSci sprints, contributors need tasks that are “sprintable.”
Sprintable tasks are those that can be worked on and potentially completed (or
partially completed) in a single sitting, whether that time is a half-day or a full day.

Sprints can span 1-4 days but are most often 1-2 days long.

### Tracking sprint contributions
Sprints often result in numerous pull requests and issues being opened by contributors. It’s important for pyOpenSci to track information around:

* Who is attending,
* Where they are from (country, state etc) and
* What contributions they make.

This information will support pyOpenSci's community impact and support and be
beneficial when we write grants and solicit sponsorships.

pyOpenSci uses a combination of GitHub project boards and user surveys to track participation and success metrics. More on that below.

## What motivates sprint participants?

Sprint participants are often motivated by different things. Some come to:

* learn
* help and support a project they care about
* connect and build community

pyOpenSci supports and empowers all of the above motivations. We thrive on empowering new
empowering contributors to make their first (or second) contributions! This impact aligns well with our mission. We also greatly benefit
from more experienced sprinters who can help move the organization's infrastructure and needs forward.

Sprints are always a win/win for pyOpenSci.

### pyOpenSci sprints are accessible

It's important to pyOpenSci's mission that sprints are accessible to both new
and seasoned contributors. We aim to ensure that all participants have a
successful experience with our community. Some participants are new and are
submitting their first-ever issue and/or pull request to an open source project.
These participants:

* may need help using git and GitHub, or
* they may feel intimidated by their first contribution (but they want to try!).

Others are more experienced and
comfortable in a sprint environment but may have questions about more technical
open issues and the outcomes that pyOpenSci wants to see in issue solutions.
Supporting all of these participants is crucial to our mission and can require
significant effort during a sprint event.

As such, it's important for anyone leading a sprint to come prepared! In most cases having community helpers will go along way to supporting beginner contributor success.

## Sprint infrastructure - GitHub projects

To efficiently manage and track contributions during sprints, pyOpenSci utilizes
[GitHub projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects). We use projects to organize issues and pull requests that contributors could potentially address during or outside of a sprint. Tasks that are discrete enough to complete during a sprint are labeled with the `sprintable` label.

An organized project ensures that
contributors, whether new or experienced, can easily find and work on tasks
that suit their skills and interests.

:::{not}
We also are testing out using [event projects](https://github.com/orgs/pyOpenSci/projects/12) to to track new contributions in the form of pull requests and issues that we receive during an event such as a PyCon US or SciPy sprint.
:::

#### Help-wanted board

The pyOpenSci [**help-wanted project board**](https://github.com/orgs/pyOpenSci/projects/3) is an organization-level GitHub project board that provides a central place where contributors can
find tasks that pyOpenSci needs help with. We have two automated workflows setup
for the help-wanted project board:

* Any issue or pull request with the `help-wanted` label is automatically added to this board.
* When an issue or pull request is closed, it is automatically archived from the project board.

Tasks on this board are ideally smaller, well-defined, and can be completed or significantly advanced within the
duration of a sprint. The pyOpenSci help-wanted board should be updated throughout the year as new issues are opened in our organization GitHub repositories. Continual updates makes it easier for:

* Contributors to jump in and start contributing and
* Sprint leaders to prepare for a sprint as the board will be more up to date.

#### Tracking annual contributions: the sprint project board

At the start of each year, the pyOpenSci community manager creates a new Sprint
GitHub Project Board. Here is an example of the [2024 sprint project board](https://github.com/orgs/pyOpenSci/projects/12).

The board will have several columns or statuses, each of which represents the name of a sprint event (example: pyconus-2024, scipy-2024, fall-festival-2024. This board is used to:

* **Track issues and pull requests opened during a sprint event**
* **Organize and Monitor Tasks**: Keep track of the progress of tasks during the sprint, ensuring clarity on which issues are being worked on and by whom.
- **Manage the Triage Process**: Keep track of which pull requests have been addressed and merged and which ones still need attention.
- **Calculate metrics**: Provide counts of activity that has occurred during a sprint event.

By using these boards, pyOpenSci staff can easily keep tabs of sprint activities and outcomes. It also helps us ensure that all sprint issues and pull requests are addressed in a timely manner.

### Year round sprint tasks

Below are tasks to stay on top of throughout the year. By working on
these items as they pop up, you are saving time spent in preparing for a sprint.

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
NOTE: i have setup this workflow https://github.com/actions/add-to-project on most (but not all) of our repos now. so it does handle moving help-wanted issues to the project. BUT it is hard to think about events. This is because there is no easy to use pull request template. so while we could automagically update a workflow before an event we'd have to do it for every event AND it would only work on issues - not pull requests. As such my idea of automating event tags won't work.

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
We create one issue and pull requesttemplate that we can use across all our repos  – it has a label that automatically will be added to the board with “no status”
Jesse adds a label for the event and moves it to a column
:::

### Review and triage pull requests and issues

If you see small pull requests coming in that are clearly fixing things (typos, etc) in a guidebook, please review them and approve if that makes sense.  If
you see an issue opened that makes sense to work on remotely with a participant, feel free to comment on it.

:::{todo}
We will need to feel some of this out at scipy.
:::

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
2. If the issue is one that we agree should be addressed, then label the issue with `help-wanted` / `sprintable`  so someone else can tackle it at our next pyOpenSci sprint.

Review each pull request submitted (or invite community members to review) and determine if the pull request looks good as is or requires changes following the standard GitHub review process.

Merge the pull request when it is complete and ready to be merged.

### Followup thank you notes

After a sprint, we will follow up with participants to show our appreciation
and encourage continued engagement with the pyOpenSci community. Here are the key
steps to take:

1. **Send a Thank You Email**: Send an email to all sprint participants thanking them for their contributions. Express gratitude for their time and effort, highlighting any significant achievements or milestones reached during the sprint.

2. **Provide Feedback**: Include any relevant feedback or outcomes from the sprint. This could involve sharing metrics, such as the number of issues closed, pull requests merged, or any specific contributions that stood out.

3. **Invite Continued Engagement**:
   - **Newsletter**: Encourage participants to subscribe to the [pyOpenSci newsletter](https://eepurl.com/iM7SOM)
     to stay updated on future events, news, and opportunities.
   - **LinkedIn**: Invite them to follow [pyOpenSci on LinkedIn](https://www.linkedin.com/company/pyopensci) for professional updates
     and community highlights.
   - **GitHub**: Remind them to continue following and contributing to pyOpenSci
     [repositories on GitHub](https://github.com/pyopensci).
    - Discourse?

4. **Stay Connected**:
   - **Upcoming Events**: Inform participants about upcoming sprints, webinars,
     workshops, or any other events they might be interested in.

By thanking contributors you are helping to maintain the momentum generated during the sprint, while also
fostering a sense of community, and encourage ongoing contributions to pyOpenSci projects.





Help for sprint event triage after the event
Event outputs
Blog post(s)
Social
Welcome new ppl to slack
Community Content “owners”
Related to above - help post event. We have a lot of issues and pr’s now. Can the community help with triage?



:::{admonition} Meeting metrics that pyOpenSci collects
:class: info
* Number of pull request submitted
* Number of issues submitted
* Number of contributors contributed
    * Where are the contributors from (country, place of work, other things??)
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
