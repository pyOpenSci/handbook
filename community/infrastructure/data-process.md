# pyOpenSci data workflows

Ever wondered how a new editor shows up on our website, or how a newly accepted package lands on our packages page? This page walks you through it. You'll learn which GitHub Actions workflow keeps each page on our website (and our peer review metrics dashboards) up to date, and how you can get a change onto the site right away instead of waiting.

:::{tip}
**In a hurry?** If you just changed an editorial team on GitHub and want the website to show it now, go to the **Actions** tab in [`pyopensci.github.io`](https://github.com/pyOpenSci/pyopensci.github.io/actions/workflows/update-editorial-board.yml), choose **Update editorial board**, and select **Run workflow**. Then review and merge the pull request it opens. That's it!

Adding or removing an editor? Start with the [onboarding guide](https://www.pyopensci.org/software-peer-review/how-to/onboarding-guide.html#onboarding-a-new-editor). The [editorial teams](editorial-teams) page will help you pick the right GitHub team. This page explains what happens behind the scenes.
:::

Behind the scenes, we use a Python package called [`pyosMeta`](https://github.com/pyOpenSci/pyosMeta) to gather data from GitHub, such as peer review issues and team membership. `pyosMeta` saves that data as [YAML](https://yaml.org/) files, a plain-text format that our website and dashboards can read.

You don't need to run `pyosMeta` yourself. Workflows in the [pyopensci.github.io](https://github.com/pyOpenSci/pyopensci.github.io) repository run it for you on a weekly schedule (sometimes called a "cron job"), and you can also start any of them by hand whenever you need to. Each time a workflow runs, it opens a pull request with the updated data. Once you (or another team member) merge that pull request, the website updates.

The PR's are generally merged by our [pyOpenSci infrastructure team](https://github.com/orgs/pyOpenSci/teams/pyopensci-repository-maintainers) who work on and maintain repositories across the organizations. If you have questions about something not getting updated, you can post in the `#pyos-maintainers-infrastructure` channel in our slack.

## What each page uses

| Page | File | Workflow | When it runs |
| --- | --- | --- | --- |
| [Our Community](https://www.pyopensci.org/our-community/index.html#pyopensci-community-contributors) | `data/contributors.yml` | [Update Contribs & reviewers](https://github.com/pyOpenSci/pyopensci.github.io/actions/workflows/update-contribs-reviews.yml) | Mondays, 03:21 UTC |
| [Python packages](https://www.pyopensci.org/python-packages.html) | `data/packages.yml` | Update Contribs & reviewers | Mondays, 03:21 UTC |
| [Editorial board](https://www.pyopensci.org/about-peer-review/index.html#meet-our-editorial-board) | `data/editorial-board.yml`, `data/emeritus-editors.yml`, and the editorial fields in `data/contributors.yml` | [Update editorial board](https://github.com/pyOpenSci/pyopensci.github.io/actions/workflows/update-editorial-board.yml). Monday's workflow refreshes these files too. | Wednesdays at 04:21 UTC, or any time you run it by hand |
| [Metrics dashboards](https://www.pyopensci.org/metrics) | CSVs in the [metrics](https://github.com/pyOpenSci/metrics) repository | [Update issue, pr and contrib metadata](https://github.com/pyOpenSci/metrics/actions/workflows/update-pr-data.yml) | 05:00 UTC on the 2nd, the 16th, and every Monday, plus December 31 |

A few things that are helpful to know:

* **Changed an editorial team member? Use the Update editorial board workflow .** It only looks at team membership, so it runs quickly and opens a small, easy-to-review pull request.
* **Update Contribs & reviewers does a lot more.** It checks every repository and review issue, so it takes longer and opens a much larger pull request.
* **The metrics dashboards update on their own schedule.** The editorial charts read the website's YAML files from the `data/` directory on the `main` branch. A separate [deploy workflow](https://github.com/pyOpenSci/metrics/actions/workflows/deploy.yml) rebuilds the dashboards every Sunday at 00:00 UTC using whatever has been merged by then, so you may see a short delay there.
* **You can update some fields in [`data/contributors.yml`](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/data/contributors.yml) by hand.** The Monday workflow keeps these once they are on `main`:
  * **Advisory status** (`advisory`). See [Update the advisory council](update-the-advisory-council).
  * **Leadership status** (`board`). Set this to `true` to list someone under Executive Council, Leadership & Staff.
  * **Title** (`title`), the role shown on their card. Editor titles still come from the [editorial workflow](editorial-teams). Other titles, such as Advisory Council or Executive Director, stay as you write them.
  * **Name** (`name`). Some people have no name on GitHub. Add their name here so the community page can list them. If a name is already in the file, the workflow does not replace it.
* [`data/manual-editorial-roster.yml`](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/data/manual-editorial-roster.yml) is also edited by hand, for editors who can't join our GitHub organization. The workflows overwrite `data/packages.yml`, `data/editorial-board.yml`, and `data/emeritus-editors.yml`.

## Where the data comes from

`pyosMeta` collects three kinds of data from GitHub:

1. **Contributor data** comes from the [All Contributors files](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/.all-contributorsrc) in each pyOpenSci repository.
2. **Peer review data** comes from the [review issues in software-submission](https://github.com/pyOpenSci/software-submission/issues). This includes the package name and repository URL, the editor and reviewers, and the maintainers and authors. `pyosMeta` reads the text people type into the review issue template. People fill out templates in all sorts of creative ways, so a missing field or an extra line can sometimes trip it up. If you notice that an action is failing please do the following:
     * Post in the `#pyos-maintainers-infrastructure` channel in slack. the error is likely already there via a slack automation but a post from you helps us elevate the importance of fixing it. Include a link to the logs. Sometimes that logs tell you what package it failed on - and if that is the case - look at the issue yaml at the top and see if you notice any quirks in the text! For example sometimes people put text in quotes `"like this"` that will break our ability to parse the text correctly.
3. **Editorial team membership** comes from our [GitHub teams](editorial-teams). Team membership decides whether someone is listed as a current or emeritus editor. Some teams also give their members access to the repositories they need for their peer review role.

:::{mermaid}
flowchart TD
  Contrib[All Contributors Bot files] --> Meta[pyosMeta]
  Issues[Peer review issues] --> Meta
  Teams[GitHub editorial team listings] --> Meta
  Meta --> Website[YAML files in pyopensci.github.io] --> Pages[Contributor, package, community and editorial listings]
  Website --> Dash[Metrics editorial dashboard]
:::

(update-the-website-right-away)=
## Update the website right away

You don't have to wait for the next scheduled run. If you have write access to `pyopensci.github.io` (the Editor in Chief team and the Software Review Lead do), you can run any of these workflows yourself:

1. Open the **Actions** tab in `pyopensci.github.io`.
2. Choose the workflow you need. If you changed an editorial team, pick **Update editorial board**. For contributor or package updates, pick **Update Contribs & reviewers**.
3. Select **Run workflow**.
4. When the pull request opens, take a quick look, and merge it if everything looks right.

Not sure whether you can change a team or run a workflow? The [editorial teams](editorial-teams) page explains who can do what.

(update-the-advisory-council)=
## Update the advisory council

The [Advisory Council](https://www.pyopensci.org/our-community/#advisory-council) on the Our Community page is maintained by the core team. There is no GitHub team for it, and no workflow to run. Edit [`data/contributors.yml`](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/data/contributors.yml) in the website repository, open a pull request, and merge it. The page updates on the next website deploy.

The website lists current members alphabetically by first name. Names in the file are stored as first name, then last name. You do not set `sort` for this section.

### Add a current member

Find the person in `data/contributors.yml`. If they are not in the file yet, add an entry for them. Set:

* `advisory: true`
* `emeritus_advisory: false`
* `title: Advisory Council`

If they already have a title, such as an editor title, make `title` a list and include `Advisory Council` as one item.

A new entry also needs:

* `name`, with the first name first
* `github_username`
* `github_image_id`, the numeric GitHub user id used for their photo. Read the `id` field from `https://api.github.com/users/USERNAME`

### When someone steps down

Set:

* `advisory: false`
* `emeritus_advisory: true`
* `title: Emeritus Advisory Council`

`emeritus_advisory: true` is what places someone in the Emeritus Leadership section. That section also includes other emeritus leadership, such as emeritus Executive Council. Leave the flag in place for anyone who should stay in that section.

### Keep the Monday workflow from dropping the change

Merge your pull request before Monday's **Update Contribs & reviewers** run. If that pull request is already open, add your edit to it. Merging an older bot pull request after your edit can drop it. After the change is on `main`, later runs keep advisory status, leadership status, title, and name.

## If something breaks

Don't worry, you won't break anything by running a workflow. If one fails, a message is posted automatically to the `#pyos-maintainers-infrastructure` Slack channel. If you get stuck, post there too, and the [pyOpenSci repository maintainers](pyopensci-maintainers-permissions) will be happy to help. If you'd like to dig in yourself, the `pyosMeta` [development guide](https://github.com/pyOpenSci/pyosMeta/blob/main/development.md) explains the tokens and permissions the workflows use.
