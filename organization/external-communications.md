# External Communications

pyOpenSci uses a multitude of platforms for external communication, in order to both maintain communication with our current community, as well as grow our community. Our external communications fall under the broad categories of email, the pyOpenSci blog, pyOpenSci newsletters, and social media platforms. This section details each of those broad categories, as well as the specific platforms used within each, and provides relevant links and insights into the purpose, strategy, and associated processes for each platform.

## Email

pyOpenSci does not send unsolicited bulk emails, and all emails contain an unsubscribe link. Emails from pyOpenSci are sent to communicate with potential volunteers, share the monthly version of the newsletter, and to keep registered event participants up-to-date on logistics. pyOpenSci will also reach out to event attendees with pre- and/or post-surveys, along with follow-up reminders, as needed.

### Mailchimp

pyOpenSci uses [Mailchimp](https://mailchimp.com/) as a catch-all bulk emailing service. Anyone interested in subscribing to the pyOpenSci mailing list and receiving our monthly newsletter can do so by [signing up here](https://eepurl.com/iM7SOM). We also use Mailchimp to communicate with individuals who have signed up to volunteer as a [reviewer](https://forms.gle/Mps4UsRHTyF66cdg7) and/or [editor](https://forms.gle/aFAMBjrdU7f7zMP89) as part of our [open software peer review process](https://www.pyopensci.org/about-peer-review/index.html).

### EventBrite

pyOpenSci uses [EventBrite](https://eventbrite.com) to manage event sign-ups. Anyone who has registered for a pyOpenSci event through EventBrite will be contacted through the EventBrite service regarding event updates and logistics. pyOpenSci may also upload EventBrite contacts to Mailchimp or SurveyMonkey for the purposes of sending out pre- and/or post-surveys.

### SurveyMonkey

[SurveyMonkey](https://www.surveymonkey.com/) is used to send out pre- and/or post-surveys to attendees of pyOpenSci events. This can include in-person or online events such as workshops, talks, and sprints. SurveyMonkey is used due to its ease of use, integration with HubSpot, and ability to send out survey reminder emails.

### HubSpot

[HubSpot](https://hubspot.com/) is pyOpenSci's customer relationship management (CRM) platform. Although HubSpot has email capabilities, pyOpenSci does not currently use this functionality.

## Linktree

All of our active sites, platforms, and social media accounts are located in a Linktr.ee account, which is shared in the Description of our social media sites where applicable. 

Accessing and editing Linktr.ee:
* Login at linktr.ee (credentials are in Bitwarden)
* Click on “Admin”
* Add new links by clicking on the “Add link” button, or edit existing links by clicking on the pencil next to the title and//or URL
* Current linktr.ee: https://linktr.ee/pyopensci

## Blog

Our [blog lives on our website](https://www.pyopensci.org/blog), which is driven by Jekyll and hosted currently on GitHub pages. [The repo url is here](https://github.com/pyOpenSci/pyopensci.github.io).   

### Blog goals  

The goals of our blog include:  
* Writing for the broader open science community  
* Sharing news and updates related to pyOpenSci  
* Build domain authority through SEO strategies  

### How to add a new blog post 

There are two main groups of people who submit blog posts to the pyOpenSci blog: pyOpenSci employees, and package authors/maintainers for packages that have been accepted into the [pyOpenSci ecosystem](https://www.pyopensci.org/python-packages.html). If you are not in one of these two groups, but would like to submit a blog post to pyOpenSci, please reach out to us at [media@pyopensci.org](mailto:media@pyopensci.org) to discuss your post prior to writing it and submitting a PR.   

**Writing a blog post**  

The following processes for writing a blog post should be used by both pyOpenSci employees as well as guest posts:  
1. Fork the pyOpenSci website repo: [https://github.com/pyOpenSci/pyopensci.github.io](https://github.com/pyOpenSci/pyopensci.github.io).  
2. Work on your blog post locally. Be sure to include alt text as needed, and create an author page if you do not already have one.    
3. Submit a pull request from your fork of the website repo to [https://github.com/pyOpenSci/pyopensci.github.io](https://github.com/pyOpenSci/pyopensci.github.io).  
4. Make sure that the blog post passes CI checks that look for spelling errors, broken links and more. Please note that occasionally the `htmlproofer` check will fail because the URL does not exist yet. We have implemented a fix for this, but it occasionally does not work.   
5. Request review of the blog post. A member of the pyOpenSci staff should always review any new content being added to the website.  
6. Once you have an approving review, the pull request can be merged. In the case of guest blog posts, a memember of the pyOpenSci team will merge your post.  

pyOpenSci has GitHub organization-wide policies in place that ensure all pull requests are generally reviewed prior to being merged. In some instances we may bypass those if the PR is a small fix or critical update. In most cases a review is preferred. Please contact the Executive Director and Founder, Leah Wasser, with any questions or needs for clarification.  

**A note on guest blog posts**  

Anyone who has had their package accepted into the pyOpenSci ecosystem is encouraged to submit a blog post (or series of blog posts) about their review experience and/or their package. When submitting your blog post, please include the following YAML elements:

```
layout: single
title: "The title of your blog post"
excerpt: "One to five sentences summarizing your post. This text will appear on our [blog landing page](https://pyopensci.org/blog)"
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
comments: true
---
```

For more information on how pyOpenSci uses GitHub, please refer to the [GitHub section of our handbook](https://www.pyopensci.org/handbook/community/github/intro.html).

### Promoting blog posts

All blog posts should be promoted, regardless of whether or not they were written by a guest or a pyOpenSci employee! For promotion, coordinate with the Community Manager to ensure that there’s a tailored message for each of the following platforms:
* Slack
* Discourse
* BlueSky
* LinkedIn
* Fosstodon

In addition to pyOpenSci promotions, we monitor social media for any personal posts authors have created to promote their post, boost accordingly.

## Newsletters

We publish two newsletters:
* A weekly newsletter on LinkedIn, published on Thursdays
* A monthly newsletter published on LinkedIn and sent to all Mailchimp subscribers

The weekly LinkedIn newsletter has three main categories:
* The monthly round-up edition, sharing and celebrating pyOpenSci and community wins over the past month
* A monthly "Community News" edition, which shares conversations, discussions, and decisions that have taken place in Slack as well as on Discourse and GitHub, that are relevant to the broader community
* Re-posts of interesting pyOpenSci blog posts

When a newsletter post is a re-post from the pyOpenSci blog, it's important to include text and a link back to the original blog post, indicating where the post was originally published. This prevents link cannibalisation, where different links with the same content compete for keyword rankings. We want all keyword rankings to be directed back to the pyOpenSci website wherever possible.

## YouTube

The [pyOpenSci YouTube channel](https://youtube.com/@pyopensci) is still under development, and currently only has one published video. While we are still in the process of developing a YouTube strategy, the best practices for YouTube videos include the following:
* Provide accurate captions
* Create an eye-catching thumbnail for each video, using a similar design aesthetic for videos that occur in a series
* Use timestamps in the video description
* Promote the video on socials within the first 20 minutes of the video launching
* Use no more than two hashtags per video

## Discourse

pyOpenSci also maintains a [public Discourse forum](https://pyopensci.discourse.group/). Unlike Slack, which has restricted access, anyone is able to join and participate in Discourse. Discourse is a place to announce new packages in our ecosystem, to post memos to the community, as well as to announce meetings and other events. We also want the community to use it to ask questions around peer review and packaging.  

At this point in time pyOpenSci has not developed a robust Discourse strategy for community engagement, but continues to discuss the platform and how we would like to use it in our quarterly social media strategy meetings.  

## Zenodo

Zenodo is a general-purpose research repository where any research output can be shared by its users, where pyOpenSci maintains a [community group](https://zenodo.org/communities/pyopensci?q=&l=list&p=1&s=10&sort=newest). When pyOpenSci staff give a presentation, they will update the community group with their talk materials. In addition, when community members give presentations, they have the option of adding them to the pyOpenSci Zenodo community group.
