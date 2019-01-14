# Meeting Notes - 11 Jan 2019

https://hackmd.io/KbpsxAGrQ8CyMgCuUnVxzw

Attendees
=========

* Leah Wasser
* Max Joseph
* Jenny Palomino
* Kylen Solvik
* Chris Holdgraf
* Paige Bailey
* Luiz Irber


Agenda Items
============

* Tasks for Kylen (presubmission process, submission process, etc)
    * review of rOpenSci documentation and modify to Python community needs
        * rOpenSci has a very clear scope:
            * e.g. no data visualization, no machine learning (difficult to review), etc (more from Kylen here)
        * rOpenSci also provides guidelines for dependencies
    * start google doc to start outlining on submission and review process
        * still create issues in Github to track tasks and status and decisions that need to be made surrounding the content
    * Python Software Template repo of some sort
        * Repository template -- Chris Suggested:
            * shablona: https://github.com/uwescience/shablona
            * ariel rokem: https://github.com/arokem 
        * provide template and suggested guidelines for testing (e.g. use of pytest for testing earthpy)
            * Cookie cutter for Python: https://github.com/audreyr/cookiecutter 
            * Other examples for R
                * Use this for R: https://github.com/r-lib/usethis
                * Good practice for R: https://github.com/MangoTheCat/goodpractice
    * Max suggested that it could be nice to have automated ways to check for the basics in a Python repo... i think things like docs and format, etc etc. We should consider this as a part of the review process. leah question: Does R do anything like this??
    
* Karthik recommends to focus on areas of expertise: 
    * CU Boulder: open geospatial, open education (teach people how to contribute to OS and also to the review process) 
* Reach out to JOSS (and existing reviewers at rOpenSci) to learn how to teach people to review packages
    * Paige has contact at JOSS: Lorena Barba
        * Paige will reach out to Lorena for us! Lorena also works on JOSE 
    * Arfon Smith (JOSS editor) is very approachable too

JOSE - journal of open source education -- fast track with education technology...

* Kylen asked about our decision making process. 
    * Decisions we need to make and how we make them
    * more formal process to be outlined in future; for now, decisions during these meetings and commenting on documentation as it gets developed
* Updates: domain names, twitter, etc
    * https://twitter.com/pyopensci
    * github.com/pyopensci
    * we also have pyopensci.org !!
* Paper Idea 
    * Survey of software:
        * how many of there?
            * Repeated functionality?
        * how many of them have robust testing?
        * group likes the idea but should be second priority to creating guidelines (from R)
        * Relevant reference for documentation: https://link.springer.com/article/10.1007/s10606-018-9333-1
        * Existing surveys that ask about Python use:
            * These are both about developers, not scientists
                * https://insights.stackoverflow.com/survey/2017
                * https://www.jetbrains.com/research/python-developers-survey-2017/
        * Ideas for questions
            * Leah
                * comfort contributing to OS software
                * ability to find packages
                * Is it easy for people to find the resources they need (e.g. finding packages, education resources for writing Python code)?
            * Max
                * recognize the need for pyOpenSci
                * What would you like to see the organization do?
* New participants (Paige, Luiz): welcome!
* Moore one pager: for next meeting
* our first presubmission inquiry!! : need to determine scope but it appears not to be within the domain of expertise of the group
* Jenny: send out a doodle poll to determine a new meeting date/time

Resources
============

* https://github.com/pyopensci  (the previous one was pyopenscience)
* https://ropensci.github.io/dev_guide/policies.html#package-categories 
* https://github.com/uwescience/shablona
    * https://github.com/uwescience/shablona/issues/77
    * "I know that I've previously made a distinction between shablona and cookie-cutter, but I really like this cookie-cutter (and particularly its documentation): https://nsls-ii.github.io/scientific-python-cookiecutter/. I've recently taught a workshop using this, and it made a lot of sense. I'm thinking of deprecating shablona, and pointing to that instead. Thoughts from anyone?"
* https://link.springer.com/article/10.1007/s10606-018-9333-1 
    * The Types, Roles, and Practices of Documentation in Data Analytics Open Source Software Libraries