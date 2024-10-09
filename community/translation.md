# pyOpenSci GitHub processes for translation teams

This document outlines the process for managing translation of pyOpenSci content in our [python-package-guide](https://github.com/pyOpenSci/python-package-guide) repository. It covers:

1. How teams are defined
2. What roles and permissions a team has
3. The review process for a translation PR

## Guidelines for a translation-related Pull Request

* When a translation-related PR has been submitted, it should be reviewed and ultimately approved by at least one other person (who is not the PR owner) on the language team associated with the submitted PR.
* A PR can not be merged without at least one approval from someone on the relevant code-owner team.
* All questions, errors, and suggestions must be addressed before the PR is merged.

These are the checks a reviewer should incorporate into their review.
* Verify that the translation can be built in the PR branch without warnings
    * Example for Spanish translation: `nox -s docs-live-lang -- es`
    * The command can be used for any language by swapping out the language tag at the end. A list of Sphinx language tags can be [found here](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language).
* Go through the file and ensure that the translation makes sense, using the following checks:
    * There are no typos
    * Technical terms can be easily understood
    * Sentence structure makes sense for the target language
* Use suggestions for any errors that are found. This has two purposes:
    * It makes it easier for the contributor to make changes
    * It gives credit to the PR reviewer as a coauthor in the final commit to main

## GitHub infrastructure for the translation teams

pyOpenSci will create and maintain a team for each language using CODEOWNERS files. This ensures that every time there is a PR, and some `*.po` files are modified, the appropriate team is requested to review the PR. All members of the translation team will have merge permissions.

The current translation teams consist of:

### Spanish
* [Felipe Moreno](https://github.com/flpm)
* [Roberto Pastor Muela](https://github.com/RobPasMue)

### Japanese
* [Tetsuo Koyama](https://github.com/tkoyama010)
* [Kozo Nishida](https://github.com/kozo2)

Current translation teams can expand their teams and add additional members by updating the CODEOWNERS file.

## Additional automations for consideration

Use CI to automatically tag the PR with the translation and the proper language tags.
