# Slack - Day to Day communication

We use Slack to communicate both as paid staff and within our community organization. Slack is a valuable tool for both asynchronous, synchronous, and remote communication.

We have automatic feeds setup in Slack to track various GitHub and Discourse activities as follows:

* **#discourse-updates:** this channel flags new Discourse posts so that we can keep track of them in a single place. This channel also announces a new package when it’s posted in the Discourse pyOpenSci packages forum. The bot was built and maintained by Chiara Marmo.
* **#feed-software-review:** this channel tracks new review submissions in our software-submission GitHub repo. This feed helps pyOpenSci staff and its editorial team keep track of the cadence of submissions in a centralized location.
* **#github-issues:** this channel was created to make it easier to follow issues and pull requests opened in our core Github repositories, as given the volume of activity it’s easy to miss new items.

## Setting up a Slack bot using Slack Workflows

Administrators in the pyOpenSci Slack space can set up [workflows](https://slack.com/help/articles/16583775096083-Automations--What-is-a-Slack-workflow), which are automated bots that complete tasks based on automatic triggers. We currently use a workflow to onboard new members to the Slack space, and if there are additional bots you feel would be helpful, please reach out to Leah or Jesse.

## Setting up an automatic feed to post from GitHub into Slack:

* First, grant permission to the Slack app from within GitHub (this has been completed, and can be further configured [here](https://github.com/pyOpenSci/software-submission/settings/installations). The bot was initially added via the [Slack-GitHub integration](https://slack.github.com/)). Then you can customize which Slack channels you want to use in order to track new activity on GitHub. 
* To use this integration, you can provide commands directly in the channel to connect it to a specific feed of events on GitHub. Some useful commands are:
    * **`/GitHub subscribe pyopensci/python-package-guide issues`** will allow you to subscribe to issues in the python-package-guide channel
    * **`/GitHub unsubscribe pyopensci/python-package-guide pulls`** will unsubscribe you
    * **`/GitHub help`** provides you with all of the options in terms of subscribing and unsubscribing

## Slack’s limitations - nonprofit plan

pyOpenSci currently has a Slack paid plan that is provided at no cost for nonprofits. It allows up to 250 users and unlimited saved messages. While this solution currently meets our needs, it will become a challenge in the future as pyOpenSci continues to grow. The main concern is the loss of message history.

We initially chose Slack as most of our community members already had organizations on Slack, and many did not like Discord. As we look ahead and consider our future needs, it’s worth noting that some of our partners have moved to platforms such as Mattermost and Zulip.

## Slack for pyOpenSci Community Discussion

Slack is also used for broader pyOpenSci community discussion. However, it is currently invitation-only, which models the same processes used by rOpenSci. An invite-only model is important as pyOpenSci grows because:
* It allows us to grow carefully and slowly
* It allows us to create an inclusive environment that is evolving into a self-moderating community. This is significantly more challenging to do in an online community with large influxes of members.
* Everyone invited to Slack has generally already contributed to pyOpenSci in some way, and therefore have a vested interest in the community upon joining.

### Who we invite to the community:

We invite people to Slack who have contributed to pyOpenSci in some way. This can include attending and contributing via a sprint, submitting a package (normally this happens after the package has been accepted, but may occur earlier on an ad-hoc basis. Invites are rarely sent before the review is finished), being a reviewer or editor, contributing to a guidebook, or signing up to become involved. Often if someone signs up we meet with them prior to sending a Slack invitation.

We also occasionally invite people that would be valuable contributors to our community in some way, even if they haven’t already contributed! These might be people from a partner community, folks doing work that is mission aligned, or even those who express interest in the work we are doing and who want to learn more or get involved.

We have also strategically invited people with expertise in the field, including core packaging experts, community members and others with knowledge that is incredibly valuable to our community’s development.

### How we invite new community members

Generally speaking, the Executive Director invites individuals who have not already contributed to pyOpenSci. These invitations are at their discretion, while package developers are usually invited by a pyOpenSci editor as part of the review process.

* Whenever a new package is added to the pyOpenSci community, the pyOpenSci Community Manager double checks to ensure that all package authors have been added to Slack.
* In instances where package authors & reviewers have not yet been added, the Community Manager will send invites within three business days of the package being accepted.

The Community Manager may also invite new members based on a variety of factors, including editor and reviewer recruitment.

## pyOpenSci Slack channels

The pyOpenSci Slack space is also a central place for communicating with the pyOpenSci community. The community channels in our slack are as follows:

* **#bug-bash:** when pyOpenSci runs bug bashes, we use this channel to announce them as well as discuss any questions people may have while working through the bug bash.
* **#coding-help:** community members can use this channel to ask questions related to code. This channel is helpful for members of all stages, and not only for beginners.
* **#community-announcements:** community members can make announcements in this channel about future conference presentations, events, projects or collaborations that members are looking to create. Any community member can post in this channel.
* **#dei-accessibility:** this channel is for discussion around issues related to diversity, equity, inclusion, and accessibility in open source.
* **#discourse-updates:** a bot-generated channel that shares updates from the pyOpenSci Discourse forum.
* **#education-training:** This is a channel to discuss learning materials, training events and other education-related topics.
* **#feed-software-review:** this is a bot-generated feed of GitHub issues.
* **#food:** why share your food photos on Instagram when you can share them here? We love to see what you’re making and eating!
* **#games-and-gaming:** there are quite a few gamers in the pyOpenSci community, and this is a space to chat about all things games (board, video, tabletop, etc.)
* **#github-issues:** the posts in this channel are bot-generated, and used to track activity in the pyOpenSci repositories.
    * If this channel gets too noisy, you can run `/github unsubscribe pyopensci/python-package-guide deployments` to unsubscribe.
* **#jobs:**  this space is for sharing job listings that may be relevant to the pyOpenSci community.
* **#meetings:** this space is for use during meetings to coordinate, and can be used to collaborate and communicate with any other pyOpenSci members that are also attending the same meeting. The meeting does not have to be related to pyOpenSci.
* **#open-source-general-chat:** this channel is a fantastic resource for developing conversations with other members in the community.
* **#oss-work-life-mental-health-balance:** this is a space to talk about mental health issues in science and tech.
* **#petzzz:** show us your fur-babies! We love to see everyone’s pets, and this is the purrrfect place to show them off.
* **#private-editorial-team:** this is a private channel for the editor team only. Here we have conversations about peer review, issues with review, etc. The community manager is also in this channel.
    * When editors are off-boarded they are removed from this channel.
    * Open, community-wide conversations about the review process occur in the **#software-review channel**.
* **#pyos-socials:** the community manager shares links to any social media posts from the pyOpenSci community in this channel.
* **#pyos-updates:** here is where we communicate any updates from the pyOpenSci core team. Some of our editors also have permission to post here, for the purposes of announcing new packages as they join the pyOS ecosystem.
* **#python-packaging-maintenance:** this is where we discuss best practices around maintaining python libraries; questions are occasionally asked here.
* **#random:** as the name suggests, anything not covered in the other channels tends to take place here. This can range from social, getting-to-know-you conversations to sharing articles to updates on community events.
* **#software-review:** This is where we openly discuss new reviews and review issues. Because this is a public channel, we only discuss items that are not  sensitive in nature. For individuals who have recently submitted a Python library for review, there are also helpful resources and feedback to be found here.
* **#welcome:** this is where new members introduce themselves. When someone new enters Slack, we post here, welcome them and ask them to introduce themselves. There is a welcome bot maintained by the community manager that shares the pyOpenSci [Code of Conduct](https://www.pyopensci.org/handbook/CODE_OF_CONDUCT.html), and helps new members introduce themselves.
    * The welcome bot is set up through a Slack workflow under the pyOpenSci organizational account.
