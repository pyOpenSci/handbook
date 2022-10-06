# Meeting Notes - 7 Dec 2018

https://hackmd.io/421E2mvqRWy9yHzFGXnueA

Attendees
=========

* Leah Wasser
* Max Joseph
* Jenny Palomino
* Kylen Solvik


Agenda Items
============

* pyopensci repo
* 1-pager - Moore funding
* chat with Tracy Teal (Carpentries)
* Meet our new GRA!! Kylen!

## pyopensci repo
* will meet with Stefan (current owner) next week or the week after??

## Notes from conversation with Tracy
* Write a good 1 pager
* Don't worry to much about governance for the 1 pager but do include initial staffing needs
    * Community person
    * Developer
    * Leadership time (% salary)
    * rOpenSci is run through UC Berkeley for these positions
        * good to find out details (e.g. does UCB receive overhead funds? ask for an example budget?)
* Our one pager can be pitched to Moore Foundation
* Possibility of more opensci communities (e.g. *opensci or xopensci)
    * we can think about this as we design our process (e.g. guidelines for review and inclusion), so that working together in the future would be easier
* One pager: https://docs.google.com/document/d/1OETzG9OASXIH3WdxyUUl_IDa4Ozfabj6T0HDDSqmkv4/edit
* Leah to ask Tracy what should be prioritized on the 1 pager

## Concept Ideas for 1 pager
* difference fom rOpenSci:
    * capacity building for training scientists on:
        * how to contribute to open source
        * partnership with Carpentries by providing content and leveraging their training capabilities
* have a developer that helps with improving/building packages as needed
* focus on expanding package ownership and community around packages, rather than on building tools
* provide concrete examples of how we intend to build community and what the community can accomplish

# Meeting Notes - 16 Nov 2018

https://hackmd.io/mpaocsIZSbSBO_31iIbEdg#

Attendees
=========

* Chris Holdgraf
* Leah Wasser
* Max Joseph
* Jenny Palomino

Agenda Items
============

* GRA spring 2019 hire!
    * identify a few packages that would be willing to be the first to work on this; get some package maintainers on board
    * collect some data on state of Python for scientists
    * draft of review process
* Inviting others to join (Matt Perry? GeoPandas - Joris or James or both)
    * having a more final version of the scope document would be helpful for this
    * have a meeting with rOpenSci and adopt their structure, so we can present this formally to interested parties
    * we can start with that and then reach out to people to find editors and package reviewers
        * We know rOpenSci has an onboarding process -- and we will need to identify editors
        * GRA Task: get him to work on the onboarding process as derive from Ropensci
* Everyone should review the relevant documentation from rOpenSci and then we should have a meeting with Karthik and Carl
    * Relevant docs from rOpenSci:
        * Repository that contains the package review etc. (see issues) https://github.com/ropensci/onboarding
        * Repository that contains the information on how to package libraries, review, edit, etc.: https://github.com/ropensci/dev_guide
    * Potentially ask them to serve on a advisory board
* Scoping out the code review for the spring that our gra will work on and what the paper will look like generally  (to ensure we collect the right data)
* Brainstorm funding opportunities
    * Kek 1 pager (I don’t have high hopes for it but it’s worth formalizing our ideas to use for other opportunities)
    * Sloan, more, mozilla, others??
    * Budget should include some funded leadership
        * rOpenSci has 3 funded developers and a position that organizes and mobilizes the community
        * sustainability needs to be in mind early on


## Next Steps

### Fall 2018 Tasks
- [ ] Meeting with Carl and Karthik - suggest if they'd like to be on our board -- Leah will email Carl and Karthik --  
- [ ] Grab pyopenscience twitter ??

### Spring 2019 Tasks
- [ ] GRA -- could convert the R docs dev, testing, etc?? to jupyter books implementation



# Meeting Notes - 26 Oct 2018

https://hackmd.io/NrTiwrktQ0WsWQp8lBJpcg

Attendees
=========

* Chris Holdgraf
* Leah Wasser
* Max Joseph
* Carson Farmer
* Jenny Palomino

Agenda Items
============

* GRA at CU Boulder description
https://docs.google.com/document/d/1VUJFcXNTrqDYEtV-ocyFuJmhtXz8GTE5Gq-CSngfacw/edit

* pyOpenSci Scoping Document
https://docs.google.com/document/d/10SRfCMSk85uqVhShyOspngJ9wx3C38k1XmhblpQrt5M/edit#

* Hackmd: https://hackmd.io/oXbNwO0UTkKZWjaf6PRPHw !! let’s use this for notes and transfer to github each time!!

* Repository Documents
    * Make repository pyopenscience/governance
        * Chris will do this and throw up docs?
        * Jenny will create hack.md for the two meeting notes so far:
            * Today’s notes: https://hackmd.io/NrTiwrktQ0WsWQp8lBJpcg
            * Notes From 9 October 2018 meeting: https://hackmd.io/3CwpAEFRRbGJ1CuS3B2R7g
    * Readme with link to scope google doc (for now)
    * Review and add to Timeline -- hack.md <- https://hackmd.io/oXbNwO0UTkKZWjaf6PRPHw?both <- write with the GRA in mind!
        * Now:
        * Upcoming:
            * Birds of a feather (BOF) - propose one of these??? (https://scipy2018.scipy.org/ehome/299527/648142/); Proposal deadline for 2018 for BOF was June 25, 2018
        * Sometime:

* Creating official avenues for organization to engage with pyOpenSci:
    * Satisfy reporting requirements
    * Prevent it from being a hodge-podge of developers with spare time
    * Maybe look to the Carpentries as a model (they have a member organization program where companies/organizations can buy in: https://carpentries.org/membership/)

* Governance for pyOpenSci:
    * How are decisions made
    * What happens when someone shows up with a $10m grant and they want to engage
    * Carpentries info: http://static.carpentries.org/governance/
    * NumFocus info: https://numfocus.org/community/people
    * How to make the project more inclusive (avenues to get involved)
    * Jupyter governance research: https://github.com/jupyter/governance/issues/60
    * QGIS: https://qgis.org/en/site/getinvolved/governance/index.html
    * Python PEP 8000 for governance: https://www.python.org/dev/peps/pep-8000/
    * Voting: https://www.python.org/dev/peps/pep-8001/
    * Survey: https://www.python.org/dev/peps/pep-8002/
    * List of governance models for other projects: https://www.python.org/dev/peps/pep-8002/



# 2018-10-09 JOSS / pyopensci Collaboration

Attendees
* Leah, Kylen, Arfon

## Meeting Goals
To establish a relationship wtih JOSS so that the review process for packages submitted to pyOpenSci are by default "accepted" by JOSS. JOSS then reviews the paper submitted and determines if the package is in scope.


## Joss' Review process varies from rOpenSci As Follows
* no required autotesting autotesting
* And there are a few other items. Essentially JOSS' process is a bit less strict then what ours will be.


## Joss's primary goal
* to provide career credit for people developing software. Thus the paper component of the review process is emphasized a bit more than the technical component. rOpenSci and pyOpenSci have to consider long term maintenance therefore the technical pieces are a bit more important


## Joss has some additional checks including
* authorship, the paper about the software which becomes a citable item and finally the scope of the package

JOSS' submission requirements for what tools are accepted is a bit stricter
* ropensci accepts some things that joss won't accept - example:
* API wrappers -- if that is a very small contribution it's a minor utility category - joss doesn't publish this  - to avoid peopel submititng 50 lines of code to joss
    * When people submit to ropensci they check if they want to publish in JOSS. At some point during the review, they write the ppaper if they check "yes".
    * If would be interesting to add something to ensure that the submittor verifies the criteria of JOSS to ensure it fits into the scope. we just want to ensure that they KNOW there is no guarantee that it will be accepted by JOSS.
    * Arfon will send a link to their submission criteria -- this hasn't happened yet with ropensci -- but it could happen someday. so we should set expectations upfront about it. language in our submission template should confirm this...

* https://joss.readthedocs.io/en/latest/review_criteria.html

## Next Steps

* We will send Arfon our review process documentation. He will discuss that with the editorial team who meet in 2ish weeks. We should know in 2-3 weeks what the outcome is.
