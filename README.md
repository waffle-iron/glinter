# glinter
A project that attempts to introduce "CL - Continuous Linting" for all modern programming languages.

What is the purpose of this project? Often when colaborating with others a standard form of syntax or indentation is often agreed upon.
The goal of glinter is to automate the process of checking for errors in code such as improper indentation or other syntax mistakes. It
also aims to eventually automatically fix these errors.

# Current plans

* First the goal is to get this project set up to have a site that uses various popular linters for various popular programming languages
* The next goal is to integrate it with github/bitbucket and various CI tools such as travis CI
* The next goal is to allow customization of these linters and possibly write our own linters 
* The files checks and linted will be described in a text file similar to travis.yml file. Customization options will also be described there.
