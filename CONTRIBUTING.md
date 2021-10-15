# Contributing Guidelines

## Before Contributing
Welcome to [Data_and_Finance](https://github.com/aditya172926/Data_and_Finance)! Before sending your pull requests __read the whole guidelines__. If you have any doubt on the contributing guide, please feel free to [state it clearly in an issue](https://github.com/aditya172926/Data_and_Finance/issues)

# Contributing

## Contributor
We are very happy that you consider implementing algorithms and programs for application of Python in Finance and Data Science! This public repository will be used for strictly learning purposes.

To make a successful Pull Request to contribute in this repository, and considered valid for maintainers to merge, please follow the steps provided:
- Your primary programming language must be Python. Jupyter notebooks are also accepted. (you can make anything from a single script to a complete application)
- Make a separate directory of your project, containing the following:-
  1) Your project files or folders (program files, datasets (less than 100 MB), logs etc.)
  2) README.md file describing your work in detail.
  3) requirements.txt file of your project dependencies.

Being one of our contributors, you agree and confirm that:
- You did your work and understand how your code works completely.
- Your work will be distributed under MIT License once your pull request is merged.
- Your submitted work is of good standards and pragramming practice.

__New implementations__ are welcome! For example, new solutions for a problem, different representations for a graph data structure or algorithm designs with different complexity but __identical implementation__ of an existing implementation is not allowed. Please check whether the solution is already implemented in the repository or not before submitting your pull request.

__Improving comments__ and __writing proper tests__ are also welcome and much appreciated.

## Contribution
We appreciate any contribution, from fixing a grammar mistake in a comment to implement algorithms. 
Please help us keep our issue list small by adding fixes: #{$ISSUE_NO} to the commit message of pull requests that resolve open issues. GitHub will use this tag to auto close the issue when the PR is merged.


### An Algorithm is one or more functions (or classes) that:
take one or more inputs,
perform some internal calculations or data manipulations,
return one or more outputs,
have minimal side effects (Ex. print(), plot(), read(), write()).
Algorithms should be packaged in a way that would make it easy for readers to put them into larger programs.

### Algorithms should:

- have intuitive class and function names that make their purpose clear to readers
- use Python naming conventions and intuitive variable names to ease comprehension
- be flexible to take different input values
- have Python type hints for their input parameters and return values
- raise Python exceptions (ValueError, etc.) on erroneous input values
- have docstrings with clear explanations and/or URLs to source materials
- contain doctests that test both valid and erroneous input values
- return all calculation results instead of printing or plotting them

__Algorithms in this repo should not be how-to examples for existing Python packages. Instead, they should perform internal calculations or manipulations to convert input values into different output values. Those calculations or manipulations can use data types, classes, or functions of existing Python packages but each algorithm in this repo should add unique value.__

## Coding Style
- We want your work to be readable by others, therefore we encourage you to keep your code formatted and neat while giving proper justice to explanatory comments as well.
- Write your code in Python 3.4+ versions only.
- Focus hard on naming conventios of functions, classes and variables. Help your reader by using descriptive names that will help you to remove redundant comments.
- Code submission require docstrings or comments to describe your work.
- If you used a Wikipedia article or some other source material to create your algorithm, please add the URL in a docstring or comment to help your reader.
