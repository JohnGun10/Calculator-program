This is a Calculator package, which acts as a normal calculator by adding, subtracting, multiplying and dividing through representative commands.
The package contains calculator.py module that has a Calculator class with methods(add, subtract, multiply, divide, allocate, reset) and instantiation of it, tests.py to check all the method validity, dockerfile to install the package to run the module when creating container from the image, intitialization python files (__init__), .dockerignore to ignore several files.

To run the the calculator.py module you will need to have python 3.8.5 installed on your OS. When you run *python calculator.py* command in terminal at the folder that contains the module (in host or through docker) you'll get this output:
"TestResults(failed=0, attempted=9)"

In order to run the module and play with it - you'll have to first open python (or python3 or bpython) in terminal. Then import calculator.py: depending on whether you access the package through terminal in your host OS or docker the commands should be either:

>>> from calculator import * (host OS)
>>> from calculator.calculator import * (Docker) 

When you import everything, you then run either one of the commands add(n), subtract(n), multiply(n), divide(n), root(n) (where n and m are floats) or simply allocate(a) (to change default value to a) or reset() (to reset memory) by the following syntax in the python prompt:
>>> calculator.add(2) returns 2 || >>> calculator.reset() returns 0 || >>> calculator.subtract(10) returns -10 || >>> calculator.multiply(-8) returns 80
|| >>> calculator.allocate(100) return 100 || >>> calculator.divide(10) returns 10.0 || >>> calculator.root(64) returns 8.0

Numbers can vary and that's the basic interface.

If you want to change the default value then you'll have to instantiate a new object in python (or bpython) which can be done like this:

>>> example = Calculator(45)

To run operation then you simply write the command (instance.operation). Like this:

>>> example.add(2) returns 47 || >>> example.multiply(11) returns 517 || >>> example.subtract(17) returns 500 || >>> example.divide(230000) returns 0.002173913043478261

**Tests:**

Doc Test is included when you run python calculator.py, but you can also run it by *python -m doctest -v calculator.py* which will show that all tests are passed.
For source files for error we used *pyflakes calculator.py* and *pyflakes tests.py*.
For typing we ran *mypy calculator.py* and *mypy tests.py*.
When tests are inititiated given that the package is downloaded on your local machine - there they will generate __pycache__, .mypy_cache and .pytest_cache

**Docker:**

To build docker image run *docker build -t calculatorapp .* where a template is calculatorapp
To enter python prompt through docker run - *docker run -it calculatorapp python* 
Then the commands on python prompt are as described above. Examples would be:
>>> calculator.add(2) returns 2 || >>> calculator.root(225) returns 15.0 || >>> calculator.subtract(6) returns 9.0 || >>> calculator.allocate(44) returns 44 || >>> calculator.divide(22) returns 2.0

**pip & Colab**

Installable through pip by *pip install git+git://github.com/aurimas13/calculator* and also with this command you can load the package on google colab. 
When you load the package on google colab then you write *from calculator.calculator import ** and you are free to play with the package as the class is already initiated (calculator = Calculator()). So all methods can be run like this calculator.add(value), calculator.subtract(value) and so on where value is an int or a float you input. To change the default value you run calculator.allocate(default) where you input default value. Also you are free to create a new object.