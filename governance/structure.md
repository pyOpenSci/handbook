(pyos-structure)=
# Organization Structure and Leadership

This page describes the organizational structure of pyOpenSci as it
relates to governance and operations.

There are two levels of leadership described below.
The first is the organizational level. The second is the program level.

## Governing councils

### Executive council

The [Executive Council](pyos-executive-council) defines and steers the high-level
mission, vision, and values of pyOpenSci. It also sets the strategic direction and vision for the organization.
The Executive Director (discussed below) is a voting member of the Executive Council.

[Click here to view current executive council members](https://www.pyopensci.org/our-community/#executive-council--leadership)

(advisory-council)=

### pyOpenSci advisory council

[Click here to view current advisory council members.](https://www.pyopensci.org/our-community/#pyopensci-advisory-council)

The Advisory Council is comprised of leaders in the Python scientific
open source ecosystem. This council advises the Executive Director
in both organization-level and day-to-day decision-making around

* Python packaging guidelines
* Peer review processes and guidelines
* Program development that supports pyOpenSci's mission
* Community engagement

Most of the communication supporting advisory council activities
happens in the pyOpenSci Slack. The Executive Director will also
organize monthly [Executive Council](pyos-executive-council) meetings that focus
on the high-level goals of pyOpenSci programs.

## Staff roles within the organization

(executive-director)=

### Executive director

The Executive Director creates and oversees the execution of the mission and
strategy of pyOpenSci supported by the Advisory Committee. The Executive Director
also:

* is the primary interface to the organization's fiscal sponsor;
* coordinates day-to-day activities
* develops programs that drive the organization's mission
* oversees staff and volunteers
* makes tie-breaking decisions if they are at an impasse.

The Executive Director reports to the Executive Council.

In the early stages of the organization's development, the Executive Director
will take on other responsibilities including:

* Managing the community in Slack and on social media.
* Serving as the de facto Software Peer Review Lead (below).

:::{todo}

### Community manager

The Community Manager is a future position to be created within the pyOpenSci
organization. This position will:

* Oversee social media communications
* Create strategic communication plans
* Write and oversee blog writing
* Manage website content
* Support communications within our online communication platforms (e.g. Slack, Discourse, Discord etc.)

The Community Manager is a paid position in the pyOpenSci organization.
:::

## Infrastructure and operations teams

The roles in this section are largely volunteer roles with a few leadership
positions becoming stipend based.

(pyopensci-maintainers)=
### pyOpenSci repository maintainers

The pyOpenSci maintainers team is responsible for the day-to-day
operational maintenance of pyOpenSci's infrastructure and repositories.
This team:

* Triage open issues across pyOpenSci repositories
* Approve and merge routine updates including:
  * Dependabot pull requests
  * Pre-commit CI updates
* Approve and merge automated data file updates:
  * Automated data file updates. Our [metrics](https://www.pyopensci.org/metrics) and [website](https://github.com/pyopensci.github.io/) are updated automatically using a GitHub Actions workflow that is supported by the pyosMeta Python package discussed above. A cron job runs this workflow daily to weekly and opens a PR. These PRs can be updated at whatever frequency is needed but should be updated at least once or twice a month.
* Ensure the smooth operation of pyOpenSci's technical infrastructure

#### Triaging issues and pull requests

Maintainers can triage open issues and pull requests as they have time.
When triaging issues:

* **High priority items**: Flag high-priority issues with an appropriate
  priority label (e.g., `priority: high`).
* **Community-contributable issues**: For issues that community members
  could work on:
  * Add the `help-wanted` label if the issue is suitable for community
    contribution
  * Add the `sprintable` label if the issue is suitable for sprint events
  * Add the issue to the [pyOpenSci help-wanted project
    board](https://github.com/orgs/pyOpenSci/projects/3)
  * Post about the issue in the `#open-source-general-chat` Slack channel
    to bring community attention to it

Issues with the `help-wanted` or `sprintable` labels are automatically
added to the help-wanted project board, which serves as a central location
for community members to find opportunities to contribute.

For information about GitHub team membership and repository access,
see the [pyOpenSci maintainers team section](pyopensci-maintainers-permissions)
in our permissions documentation.

[Click here to view the pyOpenSci maintainers GitHub
team](https://github.com/orgs/pyOpenSci/teams/pyopensci-repository-maintainers)

## Open peer review program: program-level leadership structure

Several roles and groups drive the peer review process:

(peer-review-lead)=
### Peer review lead

The peer review lead is responsible for overseeing the entire software
review process. They are responsible for:

* Ensuring a diverse and active [editorial board](peer-review-editorial-board)
* Onboarding and offboarding new editors
* Maintaining the [pyOpenSci Software Peer Review
  Guide](https://www.pyopensci.org/software-peer-review/)
* Updating [software peer review
  policies](https://www.pyopensci.org/software-peer-review/our-process/policies.html)
  as needed
* Helping editors find reviewers as necessary
* Keeping the review process moving forward by checking in on stalled
  reviews and supporting the editorial team
* Managing conflicts that may arise in the software peer review process

[More detailed guidance for the peer review lead role can be found in
the pyOpenSci Software Peer Review
Guide](https://www.pyopensci.org/software-peer-review/how-to/peer-review-lead.html).

(peer-review-editorial-board)=
### Peer review editorial board

[Click here to view the current editorial board](https://www.pyopensci.org/about-peer-review/#our-editorial-board)

The peer review editorial board is a group of volunteers who are
advocates for open source software peer review. This
group helps pyOpenSci make decisions about its open peer review process.
These decisions include, but are not limited to:

* Decisions about the scope of packages accepted into the ecosystem
* Decisions about how we enforce / support ongoing maintenance of accepted packages.
* Decisions about how we test for, evaluate and report package quality and health.
* Metrics that we collect surrounding the peer review process

Volunteers on the editorial board will serve for 1-2 years.

The editors oversee 3-4 packages a year.
[The editorial board can be found here.](https://www.pyopensci.org/about-peer-review/#our-editorial-board)

### Editor in chief

The Editor in Chief role is a rotating position
that is held by someone on the editorial board. [More on this position can be
found in the pyOpenSci software peer review guide here.](https://www.pyopensci.org/software-peer-review/how-to/editor-in-chief-guide.html)

### Volunteer reviewers

The review process is supported by volunteer reviewers.
[More on the role of reviewers can be found in our peer review guide.](https://www.pyopensci.org/software-peer-review/how-to/reviewer-guide.html)

## Fiscal sponsorship

pyOpenSci is a fiscally sponsored project of [Community
Initiatives](https://communityinitiatives.org).

pyOpenSci does not have its own standalone non-profit status. Instead,
it inherits this status by being a fiscally sponsored project. This
means that it relies on its fiscal sponsor for major administrative and
legal services, including 501(c)(3) status and financial management.
