(editorial-roles)=
# Editorial teams

This page is for you if you're the Editor in Chief, the Software Review Lead, or anyone else who adds or removes editors. It explains which GitHub team to use and what each team does.

Looking for the full process of welcoming or thanking an editor, including Slack and the Community Manager? Use the [onboarding guide](https://www.pyopensci.org/software-peer-review/how-to/onboard-editors.html#onboarding-a-new-editor). This page covers the GitHub side.

## What teams control

When you add someone to a team, two separate things happen:

* **Repository access.** Editorial board members get repository access through this team. Membership lets them lead reviews and edit our peer review guide. Only `editorial-board` and `eic-team` grant it.
* **The public listing.** It decides who appears on the [editorial board page](https://www.pyopensci.org/about-peer-review/index.html#meet-our-editorial-board) and in the editorial dashboard in our [metrics](https://www.pyopensci.org/metrics). Every editorial team affects it. Two scheduled workflows read team membership to build the listing (see [data workflows](data-process)).

## Which team to add someone to

All editorial teams sit under the parent
[`peer-review-team`](https://github.com/orgs/pyOpenSci/teams/peer-review-team).
Add the person to **every team that matches their role**. Being on the parent
team alone doesn't list them.

:::{mermaid}
flowchart TB
  PR[peer-review-team]
  PR --> EB[editorial-board]
  PR --> EIC[eic-team]
  PR --> PRL[peer-review-lead]
  PR --> TRI[triage-team]
  PR --> EE[emeritus-editors]
  PR --> EEIC[emeritus-editor-in-chief]
  PR --> EPRL[emeritus-peer-review-lead]
  PR --> ETRI[emeritus-triage-team]
:::

| Role | Add them to | Repository access | Listed on the website as |
| --- | --- | --- | --- |
| Guest editor (first review, or one ad hoc review) | [`editorial-board`](https://github.com/orgs/pyOpenSci/teams/editorial-board), only while they're editing | Yes | Editor, while on the team |
| Editor | [`editorial-board`](https://github.com/orgs/pyOpenSci/teams/editorial-board) | Yes | Editor |
| Editor in Chief | `editorial-board` and [`eic-team`](https://github.com/orgs/pyOpenSci/teams/eic-team) | Yes | Editor in Chief |
| Software Review Lead | `editorial-board` and [`peer-review-lead`](https://github.com/orgs/pyOpenSci/teams/peer-review-lead) | Yes, through `editorial-board` | Software Review Lead |
| Triage volunteer | [`triage-team`](https://github.com/orgs/pyOpenSci/teams/triage-team) | No, unless they're also on `editorial-board` | Peer review triage |
| Emeritus editor | [`emeritus-editors`](https://github.com/orgs/pyOpenSci/teams/emeritus-editors) | No | Emeritus editor |
| Emeritus Editor in Chief | `emeritus-editors` and [`emeritus-editor-in-chief`](https://github.com/orgs/pyOpenSci/teams/emeritus-editor-in-chief) | No | Emeritus Editor in Chief |
| Emeritus Software Review Lead | `emeritus-editors` and [`emeritus-peer-review-lead`](https://github.com/orgs/pyOpenSci/teams/emeritus-peer-review-lead) | No | Emeritus Software Review Lead |
| Emeritus triage volunteer | `emeritus-editors` and [`emeritus-triage-team`](https://github.com/orgs/pyOpenSci/teams/emeritus-triage-team) | No | Emeritus peer review triage |

Someone can hold more than one role, such as editor and triage. Add them to every team that applies.

**Active membership wins over emeritus.** If someone is on both an active team and an emeritus team, the website lists them as active. To make them emeritus, remove them from the active team.

## Add or remove an editor

The step-by-step process for adding and offboarding editors is in the [onboarding guide](https://www.pyopensci.org/software-peer-review/how-to/onboard-editors.html#onboarding-a-new-editor). Use the table above to pick the right teams, then [update the website right away](data-process.md#update-the-website-right-away) if you don't want to wait for the next scheduled run.

## Guest editors

A guest editor leads one review, either as a new editor's first review or as an ad hoc editor. Add them to `editorial-board` for the length of their review. They get repository access and are listed on the website while they're on the team. Remove them when the review ends. Don't move them to emeritus unless they later serve on the board and step down.

## If someone can't join the organization

Add them to
[`data/manual-editorial-roster.yml`](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/data/manual-editorial-roster.yml)
in the website repository through a pull request. It's the only editorial file you ever edit by hand. If the person is later added to a team, their team membership wins. The `pyosMeta` [development guide](https://github.com/pyOpenSci/pyosMeta/blob/main/development.md) lists the keys the roster accepts.

Don't hand-edit `editorial-board.yml`, `emeritus-editors.yml`, or the editorial fields in `contributors.yml`. The workflows overwrite them.

## Who can make these changes

You need permission to:

* Invite people to the pyOpenSci organization, if the editor you want to add is not currently a pyOpenSci member. Only organization owners can do this.

* Change editorial team membership (an organization owner or a [team maintainer](https://docs.github.com/en/organizations/organizing-members-into-teams/assigning-the-team-maintainer-role-to-a-team-member) of the editorial teams).
* Merge pull requests in `pyopensci.github.io`, and run workflows there if you want the website to update right away (write access).

The Editor in Chief team and the Software Review Lead usually hold all the above permissions. If you're missing one, ask the [pyOpenSci repository maintainers](pyopensci-maintainers-permissions).

## Learn more

* [Onboarding guide](https://www.pyopensci.org/software-peer-review/how-to/onboard-editors.html): the full process, including Slack and introductions
* [Data workflows](data-process): schedules, files, and what to do if a workflow fails
* [GitHub permissions](permissions): repository access for every team
