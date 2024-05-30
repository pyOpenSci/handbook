# pyOpenSci sprints

* TODO: https://github.com/actions/add-to-project?tab=readme-ov-file i think we want to set this up for all repos so this works for scipy.

## What is a sprint?
A sprint is an open session where contributors come together to contribute to an open source project. Contributors may range from beginners, who are new to sprints, GitHub, and git, to experienced developers. Below we review how pyOpenSci runs sprints.

There are three types of pyOpenSci sprint events:

1. **Community Sprint Events**: pyOpenSci hosts these at meetings it attends, such as PyCon US and the SciPy meeting.
2. **Online Sprint Events**: pyOpenSci may hold its own sprint events online to encourage global contributions.
3. **Community-Hosted Sprint Events**: Contributors and community members host pyOpenSci sprint events at meetings they attend.

During pyOpenSci sprints, contributors need tasks that are “sprintable.”
Sprintable tasks are those that can be worked on and potentially completed (or
partially completed) in a single sitting, whether that time is a half-day or a full day.

Sprints can span 1-4 days but are most often 1-2 days long.

### Tracking sprint contributions
Sprints often result in numerous pull requests and issues being opened by contributors. It’s important for pyOpenSci to track information around:

* who is attending,
* where they are from (country, state etc) and
* what contributions they make.

This information will support pyOpenSci's community impact and support and be
beneficial when we write grants and solicit sponsorships.

#### How we track sprint outcomes
pyOpenSci tracks issues and pull requests created through community events using project boards. More on project board use is below. We track participation metrics
using _____ TODO MORE HERE ____

#### pyOpenSci sprints are accessible

It's important to pyOpenSci's mission that sprints are accessible to both new
and seasoned contributors. We aim to ensure that all participants have a
successful experience with our community. Some participants are new and are
submitting their first-ever issue and/or pull request to an open source project.
These participants may need help using git and GitHub, or they may feel
intimidated by their first contribution. Others are more experienced and
comfortable in a sprint environment but may have questions about more technical
open issues and the outcomes that pyOpenSci wants to see for issue solutions.
Supporting all of these participants is crucial to our mission and can require
significant effort during a sprint event.

As such, it's important for anyone leading a sprint to come prepared!

### Sprint Participant Motivations

Sprint participants are often motivated by different things:

* Some come to learn.
* Some come to help and support a project they care about.
* Some come to connect and build community.

pyOpenSci supports and empowers all of these motivations, with an emphasis on
empowering contributors who are newer to contributing while greatly benefiting
from more experienced sprinters who can help move the organization forward.


### Sprint Infrastructure - GitHub Project Boards

To efficiently manage and track contributions during sprints, pyOpenSci utilizes
GitHub project boards. These boards help us organize tasks that participants can work on. This ensures that
contributors, whether new or experienced, can easily find and work on tasks
that suit their skills and interests. They also are used to track new contributions that we get during an event.

#### Help-Wanted Board

The pyOpenSci **Help-Wanted project board** is a organization level GitHub project board that provides a central place where contributors can
find tasks that pyOpenSci needs help with. We have two automated workflows setup
for the help-wanted project board:

* Any issue or pull request with the `help-wanted` label is automatically added to this board.
* When an issue or pull request is closed, it is automatically archived from the project board.

Tasks on this board are ideally smaller, well-defined, and can be completed or significantly advanced within the
duration of a sprint. The pyOpenSci Help-Wanted board is continuously updated to reflect
the current needs of pyOpenSci projects, making it easier for contributors to
jump in and start contributing.

#### Annual Sprint Project Board

At the start of each year, the pyOpenSci community manager creates a new Sprint
GitHub Project Board. The board will have several columns or statuses each or wchih represents the name of a sprint event (example: pyconus-2024, scipy-2024, fall-festival-2024. This board is used to:

* **Track issues and pull requests opened during a sprint event**
* **Organize and Monitor Tasks**: Keep track of the progress of tasks during the sprint, ensuring clarity on which issues are being worked on and by whom.
- **Manage the Triage Process**: Keep track of which pull requests have been addressed and merged and which ones still need attention.
- **Calculate metrics**: Provide counts of activity that has occurred during a sprint event.

By using these boards, pyOpenSci ensures that sprints are organized, efficient,
and accessible to all participants.

### Year Round Sprint tasks

Below are tasks to stay on top of throughout the year. By working on
these items as they pop up, you are saving time spent in preparing for a sprint.

#### Maintain the the pyOpenSci help-wanted project board

pyOpenSci uses the GitHub [help-wanted project board](https://github.com/orgs/pyOpenSci/projects/3)
to keep track of tasks that volunteers can assist with. When you see an issue
opened or if you open an issue yourself in any of our GitHub repositories within
our [pyOpenSci GitHub organization](https://www.github.com/pyopensci), always
consider whether the issue is something that someone else could help us with.

If the issue is something that someone else in the community could do:

1. **Add a `help-wanted` Label**: Any issue or pull request with the `help-wanted`
   label in our organization will be automatically added to our [pyOpenSci
   help-wanted board](https://github.com/orgs/pyOpenSci/projects/3).

2. **Add a `sprintable` Label (if applicable)**: If the task could be completed
   during a sprint (meaning it is something that could be completed within an
   hour and up to a single day's worth of work), also add the label `sprintable`
   to the issue.

3. **Update the Status on the Project Board**: Once the issue has been added to
   the project board (it normally takes our CI workflow 30 seconds to a minute),
   update the status of the issue on the project board based on the type of skill
   needed.


The current types of tasks in our board include:

    * Python packaging
    * Beginner friendly / non technical
    * Dev Ops / GitHub actions (Continuous Integration)
    * Python programming
    * Website - css or ruby

:::{todo}
we should add content review and sphinx as a status options for people that review our guidebook, run through tutorials etc.
:::

:::{important}
If you are creating a new `help-wanted` issue it's critical that you include as much detailed information in the issue as possible. Imagine someone else reading the issue (that is not you!). In reading the issue, does an outside contributor have:

* clearly understand the problem? (be specific, provide examples, links etc)
* have enough information to solve the problem?
* know exactly where the problem is occurring (provide links if you can or code examples )
* have enough information needed to solve the problem?

When in doubt, more information is always better!
:::

Labeling issues with `help-wanted` / `sprintable` throughout the year as they are opened will save significant preparation time when a Sprint event arises. It will also make it easier for fly-by contributors to find things to help us with throughout the year.

### Pre-Sprint Event Tasks

#### Triage (Help-Wanted) Issues Across the pyOpenSci Organization

Before a sprint begins, someone on the pyOpenSci team should go through and
triage all of the open issues in the organization to determine:

* Whether some of them are sprintable.
* Whether they have enough specific and detailed information for someone to work
  on the issue without too much help during a sprint.

This could be a small team exercise at a pre-meeting event held online for
pyOpenSci staff and sprint community members (if there are any contributors
participating).

The information found in the body of an issue is critical to running an effective
sprint. If the issue has very specific information that gives a potential
contributor everything they need to know to begin working, they will have fewer
questions during the sprint. If you have a table of 10-20 people sprinting for
pyOpenSci, this means the person running the sprint will have less to do on-site!
Sprints are busy—please add as much specific information as you can to each issue!

#### THIS LIKELY WON'T WORK Ensure issue and pull request templates are up to date

A challenge of a successful sprint is that there will be many issues and pull requests to triage after the sprint. To keep track of new issues and pr's, during an event, every pyOpenSci GitHub repository should have a sprint issue and pull request template. Adding this template only needs to be completed once, however
if there is a new pyOpenSci Github repository (this rarely happens), make sure that repo has a template.

The sprint template will auto-populate a `sprint-event` label on the issue or pull request when it is opened. We will then setup a workflow on the sprint project board for that year to auto-add any issue or pull request with the `sprint-event` label on it to the sprint project board.

NOTE - i'm not sure this will work. i forgot that pr templates are not as straight forward as issue templates are. issue templates are easier.

### Tasks during a sprint

Below are tasks that should occur during a spring event.

#### Collect participant information

The person running the event should collect information from participants
at the event via ______ **TODO insert how we do that here** _____.

* dynamic qr code... that people can scan. with small table top signs?
* what do we collect?
* how do they opt out of future coms?


Metrics –
Number of pr’s
Number of issues
Who contributed
Where are the contributors from (country, place of work, other things??)

### Update the sprint issue and pull request board

During the event, the remote sprint support team (either community manager or a volunteer) , should

* label all issues and pull requests as `sprint-event` and with the label for the event - e.g. `pyconus-24` as they are opened.
* Once that the sprint-event label is applied to an issue or pr, they with automatically be added to the project sprint board.
* Finally, once on the sprint board, they can then move each issue and pull request to the event name status on the sprint board.

This process, if done during the sprint, will make triaging issues and pull requests after the event, easier.

:::{todo}
We create one issue and pr template that we can use across all our repos  – it has a label that automatically will be added to the board with “no status”
Jesse adds a label for the event and moves it to a column
:::

### Review and triage pull requests and issues

If you see small pull requests coming in that are clearly fixing things in a guidebook, please review them and approve if that makes sense. If
you see an issue opened that makes sense to work on, feel free to comment on it.



All-contributors bot
Tagging issues and pr’s with sprint / event name
Creating a project board for sprint events
Writing this all up  (let’s test drive for scipy)
Help for sprint event triage after the event
Event outputs
Blog post(s)
Social
Welcome new ppl to slack
Community Content “owners”
Related to above - help post event. We have a lot of issues and pr’s now. Can the community help with triage?

### After a sprint

* Followup with participants
* Send out an email thanking people after
* invite them to stay in touch / follow newsletter / follow linkedin,


## Meeting Metrics that pyOpenSci collects

* Number of pr’s
* Number of issues
* Who contributed
    * Where are the contributors from (country, place of work, other things??)

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
