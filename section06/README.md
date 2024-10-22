# Section 6 - Code Reuse

## Overview

* DRY
    * software principle
    * Don't Repeat Yourself
    * benefits
        * reusing code makes code more readable and saves development time
        * one place to update code
    * downsides
        * no guarantee for good code and/or has no security issues
    * only reuse if the code is good code

* Ways to Reuse
    1. function
    1. import modules

## Functions

* self-contained block of code that performs a specific task
* examples of built-in functions
    * type()
    * print()
    * len()
* just need to know what arguments are needed to use them
* components
    * function name (`def`)
    * code
    * return value (optional)

```python
def <func_name>([<params>]):
    <statements>
    return <value>
```

* function call parameters must match in number and correct order [positional]
    * named and default args are possible when defining a function

## Code Commenting

* Code Description
    * explain the intent
* Algorithmic Description
    * explain how it works or how it was implemented
* Tagging
    * for known issues or areas of improvement

* Format
    * Types
        * single line (with `#` symbol)
        * multiline (with `"""` symbols)
    * brief statements
    * at most a few sentences
    * first word of comment should begin with an uppercase letter
    * should be no longer than 72 characters, otherwise use multiple lines
    * Suggestions ([from Jeff Atwood](https://blog.codinghorror.com/when-good-comments-go-bad/))
        * keep comments as close to the code being described as possible
        * don't use complex formatting (such as ASCII figures)
        * don't include redundant information
        * write the code so it is readable - easiest way to understand code is
        by reading it
    * https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/

### Docstring

* string literal that occurs as the first statement in a module, function,
class, or method
* [PEP 257 on docstrings](https://peps.python.org/pep-0257/)
* surrounded by triple double quotes `"""`
* single or multiline comment
* unless it fits on a line, place the closing quotes on a line by themselves
* begins with a captial letter and ends with a period
* provides overview of the object
* concise enough to easily maintain, but detailed enough for understanding

### Namespaces and Scopes

#### Namespace

* collection of currently defined names and objects
* Four types of namespaces
    * built-in
        * created when the interpreter starts up
        * `dir(__builtins__)`
        * terminates when the interpreter does
    * global
        * contains names defined in the main program or module loaded with
        import statement
        * terminates when interpreter does
    * enclosing
        * names in the outer function of a nested function
        * terminates when the interpreter does
    * local
        * names at the function level
        * terminates when the **function** does
        * also includes non-nested functions
#### Scopes

* namespaces have scopes
    * checked in order: **local, enclosed, global, built-in**
    * looks inside out for variable definitions
    * NameError will be raised if a variable is only used in a function,
    but is called in the main program

### Main Contruct

* an execution or starting point for the Python script
* conditional so if the code is imported the main code won't automatically
execute
* best practice to define all functions at the top after the import statements

```python
def main():
    # do something


if __name__ == '__main__':
    main()
```

## Classes, Methods, and Inheritance

### Classes and Methods

* Python is an object-oriented programming language
* everything is an object
* objects can have attributes and methods linked to them
* objects are an ***instance*** of a class
    * classes can be thought of as a blueprint

```python
class Dog:
    def __init__(self, name, breed, color, size):
        self.name = name
        self.breed = breed
        self.color = color
        self.size = size


if __name__ == '__main__':
    dog1 = Dog('Sparky', 'labrador', 'tan', 'medium')
    
    print(f'{dog1.name} is a {dog1.size}, {dog1.color} {dog1.breed}')
```

* https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes
* https://docs.python.org/3/tutorial/classes.html

### Inheritance

* allows a class to inherit all the methods and attributes from another class
* promotes code reusability and represents real-world relationships
* class that inherits from another is a derived class or child class
* cleaner code and faster development

## Python Modules and Packages

### Python Standard Library

* standard library is a collection of functions, types, and services
* distributed with the Python interpreter
* `import` modules as needed
* https://docs.python.org/3/library/index.html

```python
import sys
sys.path
```

#### Built-in Functions

Examples:
* `len()`
* `type()`
* `input()`
* `print()`

#### Standard Modules

Examples:
* Date and Time
    * datetime
    * calendar
* Mathematical
    * math
    * random
* File System
    * os.path
    * filecmp
* Operating System
    * os
    * logging
* Read/Write Data Formats
    * json
    * base64
* Internet Protocol
    * urllib
    * ftplib
    * requests
* Multimedia Data
    * wave
    * imghdr
* Run time
    * sys
    * traceback

### Import Standard Module

`import re`

### Import External Module

```python
from netmiko import ConnectHandler
import pandas as pd
import requests
```

### Python Package Management via pip

```bash
pip list
pip list | grep privy

# upgrade pip
python -m pip install --upgrade pip

pip install privy

pip list
```

### Create a Python Module

* can import a nearby Python file as a custom module
* specify the name without the *.py extension

```bash
ls -1
my_module.py

python
>>> import my_module
```

### Virtual Environments

* initial Python install is global (for all users)
* separate dependencies between different projects
* creates an isolated environment for Python objects
* own set of environment binaries and packages, but share standard libraries
with base Python install
* remove by deleting the virtual environment (venv) directory and its contents

Site Packages:
```python
import site

site.getsitepackages()
```

```
py -m venv env-name

.\env-name\Scripts\activate
```

```bash
python3 -m env env-name

source env-name/bin/activate
```

* `pip list`
* `deactivate`
* `pip freeze > requirements.txt`
* `pip install -r requirements.txt`
