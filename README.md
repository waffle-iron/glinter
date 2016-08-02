# glinter
A project that attempts to introduce "CL - Continuous Linting" for all modern programming languages.

[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/tacocats/glinter/blob/master/LICENSE)

## What is the reason for this project? ##

Often when collaborating with others a standard form of syntax or indentation is often agreed upon. The goal of glinter is to automate the process of checking for errors in code such as improper indentation or other syntax mistakes. It also aims to eventually automatically fix these errors.


----------

## How does this project aim to address the current problems listed above? ##

Similar to Continuous Integration, where projects are often merged several times a day in order to run tests on the code in hopes of finding bugs, this project aims to have code continuously checked for syntax and styling errors. This will allow for code to stay in a consistent style for entire projects and help to avoid messy coding style.


----------
## What glinter is not

While glinter may find possible bugs in your code caused by syntax errors, it is not a debugger. It is simply a tool to ensure coding style is maintained and stays the same throughout entire projects. 

----------

## Quick Documentation ##

glinter.py:

* This is the main file. Running this will start the server.

glint_io.py 

* This module contains various classes for connections to github through it's API and validating the URL's and repo's. It allows for easily grabbing files and getting information about github repos.

glint_tool.py

* This module contains various classes for linting files. While it only lints generically at the current time, specific checks will be added for certain programming languages in the future.

----------

## API ##
Currently there is no documentation on the modules, classes, or methods. However, as I write the code I will be documenting them with comments. In the future I plan on updating this section to allow for various parts of this project to be used for other projects.






# Current plans

* First the goal is to get this project set up to have a site that uses various popular linters for various popular programming languages
* The next goal is to integrate it with github/bitbucket and various CI tools such as travis CI
* The next goal is to allow customization of these linters and possibly write our own linters 
* The files checks and linted will be described in a text file similar to travis.yml file. Customization options will also be described there.
