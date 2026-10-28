# Update website and metrics data

:::{note}
This page is for editors, staff, and repository maintainers who keep our
website and dashboards up to date. You don't need it to contribute to
pyOpenSci. To learn how our websites and data fit together, see the
[infrastructure overview](github-intro).
:::

This page explains how community, package, and editorial data get updated on
the [pyOpenSci website](https://www.pyopensci.org) and our [metrics dashboards](https://www.pyopensci.org/metrics), and how you can update
the data yourself when needed. We use a Python package called [`pyosMeta`][pyosmeta] to collect data about
our peer review process and community contributors. `pyosMeta` saves this
data as [YAML](https://yaml.org/) files, a plain-text format that our website
and metrics dashboards can read. The action it runs in then creates a pull request with the updated data. GitHub Actions workflows run `pyosMeta` every
week on a schedule (a cron job), but you can also
[run a workflow by hand](update-the-website-right-away) whenever you need to.
The workflows live in two repositories:

* **Website:** the workflows are in the [pyopensci.github.io][website-repo]
  repository. They update the pages on pyopensci.org.
* **Metrics dashboards:** the workflows are in the
  [metrics][metrics-repo] repository. They update the dashboards. 
  (The dashboards are the subsection of the site found at [pyopensci.org/metrics](https://www.pyopensci.org/metrics/).

Each run opens a pull request with the updated data. Once that pull
request is merged, the website or dashboards update.

The [infrastructure team][infra-team] usually merges these pull
requests. If something isn't updating, post in the
`#pyos-maintainers-infrastructure` channel in Slack.

## Where the data comes from

`pyosMeta` collects three kinds of data from GitHub:

* **Peer review data.** `pyosMeta` parses the
  [peer review issues](https://github.com/pyOpenSci/software-submission/issues)
  in `software-submission`. It pulls out metadata such as the package
  name, repository URL, editor, reviewers, and maintainers. That data
  feeds the [Python packages page][page-packages].
* **Peer review roles.** We track editors, the Editor in Chief, and the
  triage team using GitHub teams. `pyosMeta` reads team membership to
  build the [editorial board listing][page-editorial], including who is
  current and who is emeritus. See [editorial teams](editorial-teams).
* **Contributors.** We use the [All Contributors bot](https://allcontributors.org/)
  to track contributors across our repositories. `pyosMeta` parses each
  repository's [All Contributors file](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/.all-contributorsrc)
  to build the contributor list on the [Our Community page][page-community].

:::{mermaid}
flowchart TD
  Contrib[All Contributors files] --> Meta[pyosMeta]
  Issues[Peer review issues in software-submission] --> Meta
  Teams[GitHub editorial teams] --> Meta
  Meta --> PR[Pull request with updated YAML files]
  PR -->|merged| Website[Website pages]
  Website -.->|editorial dashboard reads board data| Metrics[Metrics dashboards]
  Issues -.->|review data| Metrics
:::

## Which workflow updates which page

### Website workflows

These workflows are in the [pyopensci.github.io][website-repo]
repository.

* **[Our Community][page-community]**
  * File: `data/contributors.yml`
  * Workflow: [Update Contribs & reviewers][wf-contribs]
  * Runs: Mondays, 03:21 UTC
* **[Python packages][page-packages]**
  * File: `data/packages.yml`
  * Workflow: Update Contribs & reviewers
  * Runs: Mondays, 03:21 UTC
* **[Editorial board][page-editorial]**
  * Files: `data/editorial-board.yml`, `data/emeritus-editors.yml`, and
    the editorial fields in `data/contributors.yml`
  * Workflow: [Update editorial board][wf-editorial]
  * Runs: Wednesdays at 04:21 UTC, or any time you run it by hand. The
    Monday workflow refreshes these files too.

### Metrics workflows

These workflows are in the [metrics][metrics-repo] repository.

* **[Metrics dashboards][page-metrics]**
  * Files: CSVs in the `data/` directory of the metrics repository
  * Workflow: [Update issue, pr and contrib metadata][wf-metrics]
  * Runs: 05:00 UTC on the 2nd, the 16th, and every Monday, plus
    December 31

### Which workflow should I run?

* **Changed an editorial team member?** Run **Update editorial board**
  in `pyopensci.github.io`. It only looks at team membership, so it runs
  quickly and opens a small pull request that is easy to review.
* **Need contributor or package updates?** Run **Update Contribs &
  reviewers** in `pyopensci.github.io`. It checks every repository and
  review issue, so it takes longer and opens a much larger pull request.
* **Need fresh metrics data?** Run **Update issue, pr and contrib
  metadata** in `metrics`.

:::{note}
The editorial charts in the metrics dashboards read the website's YAML
files from the `data/` directory on the `main` branch. A separate
[deploy workflow][wf-deploy] in the `metrics` repository rebuilds the
dashboards every Sunday at 00:00 UTC using whatever has been merged by
then, so you may see a short delay.
:::

(update-the-website-right-away)=
## Run a workflow now

You don't have to wait for the next scheduled run. If you have write
access to the repository, you can run any of its workflows yourself.

### Update the website

The website workflows are in `pyopensci.github.io`. The Editor in Chief
team, the Software Review Lead, and the
[repository maintainers team](pyopensci-maintainers-permissions) have
write access there.

1. Open the **Actions** tab in [pyopensci.github.io][website-repo].
2. Choose the workflow you need. If you changed an editorial team, pick
   **Update editorial board**. For contributor or package updates, pick
   **Update Contribs & reviewers**.
3. Select **Run workflow**.
4. When the pull request opens, take a quick look and merge it if
   everything looks right.

### Update the metrics dashboards

The metrics workflows are in the `metrics` repository.

1. Open the **Actions** tab in [metrics][metrics-repo].
2. Choose **Update issue, pr and contrib metadata**.
3. Select **Run workflow**.
4. When the pull request opens, review it and merge it.

The dashboards show the new data after the next deploy. See the note
above about the Sunday rebuild.

Not sure whether you can change a team or run a workflow? The
[editorial teams](editorial-teams) page explains who can do what.

(edit-contributors-by-hand)=
## Fields you edit by hand

The workflows overwrite `data/packages.yml`, `data/editorial-board.yml`,
and `data/emeritus-editors.yml`, so don't edit those by hand.

You can edit these fields in
[`data/contributors.yml`][contributors-yml]. The Monday workflow keeps
them once they are on `main`:

* **Advisory status** (`advisory`). See
  [Update the advisory council](update-the-advisory-council).
* **Leadership status** (`board`). Set this to `true` to list someone
  under Executive Council, Leadership & Staff.
* **Title** (`title`), the role shown on their card. Editor titles still
  come from the [editorial workflow](editorial-teams). Other titles, such
  as Advisory Council or Executive Director, stay as you write them.
* **Name** (`name`). Some people have no name on GitHub. Add their name
  here so the community page can list them. If a name is already in the
  file, the workflow does not replace it.

Editors who can't join our GitHub organization go in
[`data/manual-editorial-roster.yml`][manual-roster]. See
[editorial teams](editorial-teams).

:::{important}
Merge your pull request before Monday's **Update Contribs & reviewers**
run. If that pull request is already open, add your edit to it. Merging
an older bot pull request after your edit can drop your change.
:::

(update-the-advisory-council)=
### Update the advisory council

The [Advisory Council](https://www.pyopensci.org/our-community/#advisory-council) on the Our Community page is maintained by the core team. There is no GitHub team for it, and no workflow to run. Edit [`data/contributors.yml`][contributors-yml] in the website repository, open a pull request, and merge it. The page updates on the next website deploy.

The website lists current members alphabetically by first name. Names in the file are stored as first name, then last name. You do not set `sort` for this section.

#### Add a current member

Find the person in `data/contributors.yml`. If they are not in the file yet, add an entry for them. Set:

* `advisory: true`
* `emeritus_advisory: false`
* `title: Advisory Council`

If they already have a title, such as an editor title, make `title` a list and include `Advisory Council` as one item.

A new entry also needs:

* `name`, with the first name first
* `github_username`
* `github_image_id`, the numeric GitHub user id used for their photo. Read the `id` field from `https://api.github.com/users/USERNAME`

#### When someone steps down

Set:

* `advisory: false`
* `emeritus_advisory: true`
* `title: Emeritus Advisory Council`

`emeritus_advisory: true` is what places someone in the Emeritus Leadership section. That section also includes other emeritus leadership, such as emeritus Executive Council. Leave the flag in place for anyone who should stay in that section.

## If something breaks

Don't worry, you won't break anything by running a workflow. If one fails, a message is posted automatically to the `#pyos-maintainers-infrastructure` Slack channel. If you get stuck, post there too, and the [pyOpenSci repository maintainers](pyopensci-maintainers-permissions) will be happy to help. If you'd like to dig in yourself, the `pyosMeta` [development guide](https://github.com/pyOpenSci/pyosMeta/blob/main/development.md) explains the tokens and permissions the workflows use.

### Review issues that don't parse

`pyosMeta` reads the text people type into the review issue template. People fill out templates in all sorts of creative ways, so a missing field or an extra line can trip it up. If a workflow fails:

* Post a link to the logs in `#pyos-maintainers-infrastructure`. The error may already be there from the Slack automation, but a post from you helps us prioritize the fix.
* Check the logs for the package it failed on. Then look at the YAML at the top of that review issue for quirks. For example, text in quotes `"like this"` can break parsing.

[pyosmeta]: https://github.com/pyOpenSci/pyosMeta
[website-repo]: https://github.com/pyOpenSci/pyopensci.github.io
[metrics-repo]: https://github.com/pyOpenSci/metrics
[infra-team]: https://github.com/orgs/pyOpenSci/teams/pyopensci-repository-maintainers
[contributors-yml]: https://github.com/pyOpenSci/pyopensci.github.io/blob/main/data/contributors.yml
[manual-roster]: https://github.com/pyOpenSci/pyopensci.github.io/blob/main/data/manual-editorial-roster.yml
[page-community]: https://www.pyopensci.org/our-community/index.html#pyopensci-community-contributors
[page-packages]: https://www.pyopensci.org/python-packages.html
[page-editorial]: https://www.pyopensci.org/about-peer-review/index.html#meet-our-editorial-board
[page-metrics]: https://www.pyopensci.org/metrics
[wf-contribs]: https://github.com/pyOpenSci/pyopensci.github.io/actions/workflows/update-contribs-reviews.yml
[wf-editorial]: https://github.com/pyOpenSci/pyopensci.github.io/actions/workflows/update-editorial-board.yml
[wf-metrics]: https://github.com/pyOpenSci/metrics/actions/workflows/update-pr-data.yml
[wf-deploy]: https://github.com/pyOpenSci/metrics/actions/workflows/deploy.yml
