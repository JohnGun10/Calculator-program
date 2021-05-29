This is a Calculator package, which acts as a normal calculator by adding, subtracting, multiplying and dividing through representative commands.
The package contains calculator.py module that has a Calculator class with methods(add, subtract, multiply, divide, allocate) and instantiation of it, tests.py to check all the method validity with values from -1000 to 1000, dockerfile to install the package to run the module when creating container from the image, intitialization python files (__init__), .dockerignore to ignore several files.
To run the the calculator.py module you will need to have python 3.8.5 installed on your OS. When you run "python calculator.py" command in terminal at the folder that contains the module (in host or through docker) you'll get this output:
"TestResults(failed=0, attempted=6)"
In order to run the module and play with it - you'll have to first open python (or python3 or bpython) in terminal. Then import calculator.py: depending on whether you access the package through terminal in your host OS or docker the commands should be either:
>>> from calculator import *
>>> from calculator.calculator import * 
When you import everything, you then run the commands add(n), subtract(n), multiply(n), divide(n), root(n) (where n is an integer and m is expected to return a float) or simply allocate (to reset memory) by the following syntax in the python prompt:
>>> calculator.add(2)
2
>>> calculator.allocate()
0
>>> calculator.subtract(10)
-10
>>> calculator.multiply(-10)
100
>>> calculator.divide(10)
10.0
>>> calculator.root(64)
8.0

Numbers can vary.
That's the basic interface.

If you want to change the default value then you'll have to instantiate a new object in python (or bpython) which can be done like this:
>>> example = Calculator(45)
To run operation then you simply write the command (instance.operation). Like this:
>>> example.add(2)
47
>>> example.multiply(11)
517
>>> example.subtract(17)
500
>>> example.divide(230000)
0.002173913043478261

Tests:
Doc Test is included when you run python calculator.py, but you can also run it by python -m doctest -v calculator.py which will show that all tests are passed.
For source files for error we used pyflakes calculator.py and mypy tests.py.
For typing we ran mypy calculator.py and mypy tests.py.
