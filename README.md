# Calculator

This is a Calculator package that contains 2 Jupyter notebooks, 6 modules (3 of which are not __init__.py), Dockerfile, LICENSE, .gitignore and .dockerignore. 
The written calculator.py module acts as a normal calculator by adding, subtracting, multiplying, dividing and taking the nth root of a number. This module also contains mehods of reseting memory, allocating memory from what you want to start, setting and getting a memory value. Please refer Installataion and Requiremnts bfore looking into the examples.

# Table of contents

- [Calculator](#Calculator)
- [Table of contents](#table-of-contents)
- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [Tests](#tests)
- [Docker](#docker)
- [License](#license)

# Installation
[(Back to top)](#table-of-contents)

To run the package you'll have to first download and install it by running this command on colab, jupyter notebook, terminal or docker:
> pip install git+git://github.com/aurimas13/calculator
When it is downloaded navigate to python shell. When there import the module by:
>>> from calculator.calculator import Calculator
or 
>>> from calculator.calculator import *

# Requirements
[(Back to top)](#table-of-contents)

Python 3.8.5 is required to run package's modules.

# Usage
[(Back to top)](#table-of-contents)

After installation is done the you'll have to instantiate a Calculator class and play with it by running methods:
'''python
calc = Calculator()
'''
>>> calc.add(10)
10
>>> calc.subtract(5)
5
>>> calc.multiply(50)
250
>>> calc.divide(2)
125.0
>>> calc.divide(4.5)
27.77777777777778
>>> calc.multiply(4.5)
125.0
>>> calc.subtract(25)
100.0
>>> calc.root(2)
10.0
>>> calc.reset()
0
>>> calc.allocate(7)
7
>>> calc.set_memory(6)
>>> calc.get_memory()
6

# Tests
[(Back to top)](#table-of-contents)

First navigate to where calculator.py or tests.py is held.

For DocTest run in terminal or docker this command:
> python -m doctest -v calculator.py

To check source files for error run:
> pyflakes calculator.py
> pyflakes tests.py

For typing run:
> mypy calculator.py
> mypy tests.py

# Docker
[(Back to top)](#table-of-contents)

To build docker image run:
> docker build -t calculatorapp .

To enter python prompt through docker:
> docker run -it calculatorapp python 

Then the commands to run are given in #usage


# License
[(Back to top)](#table-of-contents)

<!-- Adding the license to README is a good practice so that people can easily refer to it.

Make sure you have added a LICENSE file in your project folder. **Shortcut:** Click add new file in your root of your repo in GitHub > Set file name to LICENSE > GitHub shows LICENSE templates > Choose the one that best suits your project!

I personally add the name of the license and provide a link to it like below. -->