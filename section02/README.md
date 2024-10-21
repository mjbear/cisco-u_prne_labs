# Section 2 - Data Types

## Basic Data Types

### String

* opening and closing single ' or double quote "
* can embed quotes (and escape them)
* use triple single or double quotes to span multiple lines

```
>>> type('Hello World')
<class 'str'>
>>> str('3.14')
'3.14'
```

### Integer

* whole number with no decimal places

```
>>> int(3.14)
3
>>> int('3.14')
3
```

### Float

* number with a decimal point
* character e (exponential) followed by a positive or negative number is also a
float

```
>>> float(3)
3.0
>>> float('3.14')
3.14
```

> [!TIP]
> Maximum floating point value before an exponential becomes infinity (`inf`)
> ```
> >>> 2e308
> inf
> >>> 2e307
> >>> 2e+307
> >>>
> >>> import sys
> >>> sys.float_info
> >>>
> >>> 1.7e309
> inf
> >>> 1.7e308
> 1.7e+307
> ```
> 
> * https://note.nkmk.me/en/python-sys-float-info-max-min/
> * https://juliensobczak.com/inspect/2019/03/10/floating-point-numbers-demystified/

### Boolean

* True or False
* titlecase matters (first letter capitalized)
* `bool()`
    * if numeric zero = `False`
    * non-zero = `True`

## type() Function

* returns data type of an object

> [!TIP]
> To make large numbers more readable, use underscores where commas would often be

```
>>> type(25000000)
<class 'int'>
>>>
>>> type(25_000_000)
<class 'int'>
```

## Complex Data Types

* lists
* tuples
* set
* dictionary

> [!TIP]
> Trailing commas within lists, tuples, sets, and dictionaries is a best practice.
>
> 1. makes it easier to work with
> 1. avoids situations where the comma is forgotten when adding a new item (causing a SyntaxError)
> 1. when the comma is already present, `git diff` for version control doesn't show that line as changed (since it didn't if the comma was there)

### Variables
* Assignment
    * uses a single equals sign
    * for contrast, equality uses double equals `==`
* Naming
    * lowercase names recommended
    * case-sensitive
    * single letter or one or more words
    * cannot start with a number
    * separate words with underscores `_`
    * self-explanatory, but not too long
    * cannot be **[Python keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)**
* Types (scopes)
    * Global
        * used throughout code
    * Local
        * limited to function where declared
* Dynamically Typed
    * data types are not declared
    * reason for Python being a "loosely typed language"

### Scopes and Object IDs

Python variables point to pyObjects.

A [pyObject](https://docs.python.org/3/c-api/structures.html) is stored in
memory and holds information about the data bound to the variables such as the
value and ref count.

Use `id()` to identify the memory location used to store an object.

```
>>> x = 100
>>> y = 200
>>>
>>> id(x)
139621976897736
>>> id(y)
139621976900936
```

### List

* grouping of objects stored in a single variable
* traits
    * start and end with square brackets `[]`
    * are ordered
    * contain any obj
    * can be indexed
    * are mutable (able of being changed)
    * are dynamic
* positive indexes work from the left (beginning)
    * indexes start at zero
* negative indexes work from the right (end)
    * last = -1
    * next to last = -2

```
>>> a = [1, 2, 3, 4]
>>> a[1]
2
```

#### Methods

```
append()
insert()
pop()
remove()
count()
len()
```

#### Functions
* `sorted()` - create a sorted/arranged list

### Tuple

* start and end with parentheses `()`
* similar to lists
   * both are a collection of ordered objects
   * both allow duplicate objects
* tuples are immutable though (unable to be changed once created)
* indexes work like those of lists (also start at zero, etc)

```
>>> a = (1, 2, 3, 4)
>>> a[1]
2
```

#### Methods

```
count()
index()
```

### Set

* start and end with curly braces `{}`
* store multiple objects
* unordered and unindexed
* no duplicate values

```
>>> a = {1, 2, 3, 4}
```

#### Methods

```
union()
intersection()
```

and [more set methods](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

### Dictionary

* start and end with curly braces `{}`
    * (sets also use curly braces, but they are different types)
* unordered list of key-value pairs
* mutable
    * grow or shrink as needed
    * can be nested

```
>>> a = {'a': 1, 'b': 'two'}
>>> a['a']
1
```

#### Methods

```
get()
items()
keys()
values()
pop()
update()
clear()
```

### Nested Data Types

* often a list or dictionary inside another list or dictionary

### String Manipulation

```
capitalize()
title()
upper()
lower()
swapcase()
```

#### String Splitting

`str.split(separator, maxsplit)`

```
>>> 'Hello World'.split()
['Hello', 'World']
>>>
>>> '1111:2222:3333'.split(':')
['1111', '2222', '3333']
>>>
>>> '1111:2222:3333'.split(':', 1)
['1111', '2222:3333']
```

#### String Modification

##### Slicing

* strings are indexed
* `str[beginning index, ending index, step]`

```
>>> ip = '10.1.2.3'
>>> ip[3:7]
'1.2.3'
```

* `[:3]`
    * beginning to index three
* `[-3:]`
    * third to last through to the end
* `[0:7:2]`
    * 0 to index 7, every second index

#### String Concatenation
* plus sign `+`
* cast other variables to string to avoid `TypeErrors`

#### Whitespace Stripping

```
str.strip()
str.lstrip()
str.rstrip()
```

#### Formatting and Templating

* `format()`
* format strings / f-strings
* Templates
* (additionally) old string formatting
* (additionally) manual string formatting

##### format()
```
>>> 'Hello World from {0}'.format('Bob')
'Hello World from Bob'
>>> 'Hello World from {name}'.format(name='Bob')
'Hello World from Bob'
```

##### format strings / f-strings
```
>>> name='Bob'
>>> f'Hello World from {name}'
'Hello World from Bob'
```

##### Templates

```
>>> from string import Template
>>> x = Template('Hello World from $name')
>>> x.substitute(name='Bob')
'Hello World, Bob'
```

##### Old String Formatting

https://docs.python.org/3/tutorial/inputoutput.html#old-string-formatting

```
>>> 'Hello World from %s' % ('Bob')
'Hello World from Bob'
>>>
>>> name='Bob'
>>> 'Hello World from %s' % (name)
'Hello World from Bob'
```

##### Manual String Formatting

https://docs.python.org/3/tutorial/inputoutput.html#manual-string-formatting

```
>>> print('Hello', 'World', 'Bob')
Hello World Bob
>>>
>>> print('Hello', 'World', 'Bob', end=' ')
Hello World Bob >>>
>>>
>>> print('Hello', 'World', 'Bob', sep=', ')
Hello, World, Bob
```

#### Escape Characters
* new line `\n`
* tab `\t`
* backslash `\\`
* backspace `\b`
* CR `\r`
    * (carriage return)
* can escape a single or double quote via a backslash `\'` or `\"`
* can escape octal and hex values too

#### String Methods

* `count()`
* `find()`
* `startswith()`

```
str.count(sub, start, stop)
str.find(sub, start, stop)
str.startswith(prefix, start, stop)
```
