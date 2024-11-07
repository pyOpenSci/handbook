# External Communication

pyOpenSci uses a multitude of communication platforms to maintain and grow our community. Our external communications fall under the broad categories of:

* email,
* pyOpenSci blog,
* pyOpenSci newsletters, and
* social media platforms.

This section provides an overview of each category's purpose and use. It also provides relevant links and insights into each platform's purpose, strategy, and associated processes.

## Email

Emails from pyOpenSci are sent to communicate with potential volunteers, share the monthly version of the newsletter, and keep registered event participants up-to-date on logistics. pyOpenSci also contacts event attendees with pre and post-event surveys and follow-up reminders, as needed. We use SurveyMonkey to develop and send surveys to our event participants.

:::{important}
pyOpenSci does not send unsolicited bulk emails; all emails contain an unsubscribe link following GDPR guidelines.
:::

## SurveyMonkey

pyOpenSci uses [SurveyMonkey](https://www.surveymonkey.com/) to develop and send pre and post-surveys to pyOpenSci event attendees. Events include workshops, talks, and sprints, which may be in-person or online. SurveyMonkey is used due to its ease of use, integration with other platforms, and ability to send out survey reminder emails.

## EventBrite

pyOpenSci uses [EventBrite](https://eventbrite.com), which is provided by our fiscal sponsor, Community Initiatives, to manage event registration. Anyone who has registered for a pyOpenSci event through EventBrite will be contacted through the EventBrite service regarding event updates and logistics. pyOpenSci may also upload EventBrite contacts to SurveyMonkey to send out pre- and post-event surveys.

:::{todo}

## HubSpot

[HubSpot](https://hubspot.com/) is pyOpenSci's customer relationship management (CRM) platform. pyOpenSci also uses HubSpot as a catch-all bulk emailing service, for instance, to communicate with individuals who have signed up to volunteer as a [reviewer](https://forms.gle/Mps4UsRHTyF66cdg7) and/or [editor](https://forms.gle/aFAMBjrdU7f7zMP89) as part of our [open software peer review process](https://www.pyopensci.org/about-peer-review/index.html).

:::

## Linktree

Linktree is a social media landing page that allows users to share multiple links from a single page, which is useful for landing pages on social media sites that provide limited space for external links.

Our active sites, platforms, and social media accounts are documented in a Linktr.ee account. The [Linktr.ee link](https://linktr.ee/pyopensci) is shared in the **Description** of our social media sites.

Accessing and editing Linktr.ee:

* Login at [linktr.ee](https://linktr.ee/)
* Click on “Admin”
* Add new links by clicking on the “Add link” button, or edit existing links by clicking on the pencil next to the title and//or URL
* Current linktr.ee: <https://linktr.ee/pyopensci>

## Blog

The [pyOpenSci blog lives on our website](https://www.pyopensci.org/blog). The website is driven by Jekyll and hosted on GitHub pages. [The code for the website is stored in pyopensci.github.io GitHub repository](https://github.com/pyOpenSci/pyopensci.github.io).

### Blog goals

The goals of the pyOpenSci blog include:

* Promotion of pyOpenSci accepted scientific Python packages
* Celebration and recognition of pyOpenSci community members
* Discussion of modern topics, tools, and resources that are of use to the broader open science and scientific Python community
* Share pyOpenSci news and updates
* Promote pyOpenSci events
* Build domain authority around Python, open science, and open source through search engine optimization (SEO)

### How to add a new blog post

Currently, there are several groups of people who submit blog posts to the pyOpenSci blog: pyOpenSci staff, package authors/maintainers of [pyOpenSci packages](https://www.pyopensci.org/python-packages.html), and pyOpenSci community members and friends who have participated in a pyOpenSci event. If you are interested in submitting a blog post to pyOpenSci, please contact us at [media@pyopensci.org](mailto:media@pyopensci.org) to discuss your post before writing it and submitting a pull request to our GitHub repository.

#### Our blog post submission process

The pyOpenSci blog post submission process defined below should be used by everyone submitting a blog post.

1. Fork the pyOpenSci website GitHub repository: [https://github.com/pyOpenSci/pyopensci.github.io](https://github.com/pyOpenSci/pyopensci.github.io).
2. Work on your blog post locally.
    * Be sure to include alt text for all images submitted as a part of your blog post

````markdown
```{figure} filepath/to/your/image.png
:scale: 100 %
:alt: This text will appear as the alt text to your image.

This text will appear as the caption to your image.
```
````

3. Next, create an entry in the [authors.yml file](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/_data/authors.yml) if you do not already have one.
To create an author page, submit a pull request from your fork of the pyOpenSci website repository, with changes to the [authors.yml](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/_data/authors.yml) file. If you would like to include a headshot, you can add it to the [`people` directory in the `images` directory.](https://github.com/pyOpenSci/pyopensci.github.io/tree/main/images/people)

3. Submit a pull request from your fork of the website repo to [https://github.com/pyOpenSci/pyopensci.github.io](https://github.com/pyOpenSci/pyopensci.github.io).
4. Ensure the blog post passes CI (continuous integration) checks that look for spelling errors, broken links, and more. Please note that occasionally the `htmlproofer` check will fail because your new blog post URL does not exist yet online.
5. Once your post and the pull request adding it to our website is complete, request a review on GitHub. A member of the pyOpenSci team should always review any new content being added to the website.
6. Your pull request can be merged once you have an approving review. A member of pyOpenSci's staff or contributor team will merge your post.

:::{note}
pyOpenSci has GitHub organization-wide policies in place that require all pull requests are reviewed before being merged. Sometimes, we may bypass those if the PR is a small fix or critical update. In most cases a review is preferred.
:::

:::{admonition} Yaml elements required for blog posts
:class: tip

All package authors, maintainers (and users) of a pyOpenSci-accepted package are welcome and encouraged to submit a blog post (or series of blog posts) about their review experience and/or the use of the package. When submitting your blog post, please include the following YAML elements:

```
layout: single
title: "The title of your blog post"
excerpt: "One to three sentences summarizing your post. This text will appear on our [blog landing page](https://pyopensci.org/blog)"
author: "Your name"
permalink: /blog/url-for-your-post.html
header:
  overlay_image: images/headers/your-blog-post-header-image.png
  overlay_filter: rgba(20, 13, 36, 0.8)
categories:
  - blog-post
  - community
classes: wide
toc: true
last_modified: 2024-08-26 # update the date here!
comments: true
---
```

:::

For more information on how pyOpenSci uses GitHub, please refer to the [GitHub section of our handbook](https://www.pyopensci.org/handbook/community/github/intro.html).

### Promoting blog posts

All blog posts should be promoted, regardless of whether or not they were written by a guest or a pyOpenSci employee! For promotion, coordinate with the Community Manager to ensure that there’s a tailored message for each of the following platforms:

* Slack
* Discourse
* BlueSky
* LinkedIn
* Fosstodon

In addition to pyOpenSci social outreach, we monitor social media for any personal posts that authors have created. To promote these posts, we will repost.

### Blog post tone

While we encourage guest authors to use a tone of voice that is authentic to them, the pyOpenSci blog uses a friendly, engaging, and curious tone. Although there are times when a post is written from the pyOpenSci perspective and uses the terms "we" or even refers to pyOpenSci in the third person, it is more common for a post to be written from the author's perspective and incorporate the use of "I."

An example of this is the [pyOpenSci @ SciPy 2024 - Python Packaging Tutorials, Talks and Community post](https://www.pyopensci.org/blog/pyos-scipy-2024-recap.html), which incorporates personal anecdotes with data, images, and the author's reflections on the experience.

## Newsletters

The goals of the pyOpenSci newsletter are similar to our blog goals, with the addition of reaching a broader audience beyond website visitors. pyOpenSci uses LinkedIn as a newsletter platform, as many of our current (and future!) community members are on this platform. Using LinkedIn allows us to leverage our existing audience and create consistent communication to help further community connections.

We publish two newsletters:

* A weekly newsletter on LinkedIn, published on Thursdays
* A monthly newsletter published on LinkedIn and sent to all newsletter subscribers

The weekly LinkedIn newsletter has three main categories:

* The monthly round-up edition, sharing and celebrating pyOpenSci and community wins over the past month
* A monthly "Community News" edition, which shares conversations, discussions, and decisions that have taken place in Slack as well as on Discourse and GitHub, that are relevant to the broader community
* Re-posts of interesting pyOpenSci blog posts

These posts are all structured as blog posts, using appropriate heading and subheading formats within LinkedIn. In fact, all of our newsletters are first published on the pyOpenSci blog, and should follow the same tone and format.

When a newsletter post is a re-post from the pyOpenSci blog, it's important to include text and a link back to the original blog post, indicating where the post was originally published. This prevents link cannibalization, where different links with the same content compete for keyword rankings. We want all keyword rankings to be directed back to the pyOpenSci website wherever possible.

There are instances in which we publish content from another individual on our website, for example, Eric Ma's upcoming blog post for the [pyOpenSci Open Science Fall Festival 2024](https://www.pyopensci.org/events/pyopensci-2024-fall-festival.html). In these cases, we'd want to include a canonical meta element in the HTML for the version being posted on the pyOpenSci blog. This can be accomplished by including the `<link rel="canonical" href="www.original-post-web-url.com">` tag in the header of the post.

### Newsletter success metrics

Because pyOpenSci is still in the early days of its newsletter, our success metrics are focused primarily on growth and engagement rate. We are currently aiming for:

* 1.0% (or higher) monthly increase in newsletter subscribers
* 3.0% (or higher) average monthly engagement rates

This data is obtained through the LinkedIn Analytics dashboard, which is accessed from the pyOpenSci LinkedIn account. Within the Newsletter tab, you can filter the dates and also view engagement and follower metrics.

## YouTube

The [pyOpenSci YouTube channel](https://youtube.com/@pyopensci) is still under development and currently only has one published video. While we are still in the process of developing a YouTube strategy, the best practices for YouTube videos include the following:

* Provide accurate captions
* Create an eye-catching thumbnail for each video, using a similar design aesthetic for videos that occur in a series
* Use timestamps in the video description
* Promote the video on socials within the first 20 minutes of the video launching
* Use no more than two hashtags per video

At this point in time, there are no active goals or success metrics for the YouTube channel. We'll be sure to update this section once we're regularly updating our channel!

## Discourse

pyOpenSci also maintains a [public Discourse forum](https://pyopensci.discourse.group/). Unlike Slack, which has restricted access, anyone is able to join and participate in Discourse. Discourse is a place to announce new packages in our ecosystem, to post messages to the community, as well as to announce meetings and other events. We also want the community to use it to ask questions about peer review and packaging.

pyOpenSci is currently in the process of sunsetting Discourse as it has not proven to be a heavily used platform for our community. We are currently exploring the use of GitHub discussions.

## Zenodo

Zenodo is a general-purpose research repository where anyone can publish outputs and receive a citable DOI (digital object identifier).

pyOpenSci uses Zenodo to create citable entries for:

* GitHub software repositories
* Presentations by pyOpenSci staff and community members
* Online educational resources, like our [Packaging guide](https://www.pyopensci.org/python-package-guide/)

For GitHub repositories, pyOpenSci includes a Zenodo citation badge at the top of the README file, linking directly to the citation page. pyOpenSci also encourages all its software packages to use Zenodo for providing citation-ready references.

When major updates are made to resources, such as the Packaging guide, pyOpenSci creates a new release. Zenodo then generates an updated DOI specific to that release, allowing users to cite the latest version.

### pyOpenSci Zenodo Community

pyOpenSci maintains a [community group](https://zenodo.org/communities/pyopensci?q=&l=list&p=1&s=10&sort=newest) on Zenodo where both staff and community members can share content related to pyOpenSci, including presentations, blog posts, open education resources, software, and other materials. This allows contributors to receive a citable DOI while retaining ownership of their submissions.

The pyOpenSci Zenodo community is moderated by pyOpenSci staff, who review and approve all suggested additions to ensure relevance and quality.
