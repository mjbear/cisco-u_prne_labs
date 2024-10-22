# Section 8 - Troubleshooting

## Errors and Exceptions

* syntax error
    * parser identifies incorrect structure or syntax
    * ex: mispelled keyword or missing colon `:` at the end of a function or
    unterminated string (missing closing quote)
    * error message contains the line number where the error occurred

### Common Exceptions

| Name              | Description |
| :---------------- | :---------- |
| AttributeError    | attribute reference assignment fails
| IOError           | system-related I/O error
| ImportError       | import statement fails to load a module
| IndexError        | sequence subscript is out of range
| KeyError          | mapping (dictionary) key is not found
| KeyboardInterrupt | user pressed interrupt key (normally Ctrl+C or Delete)
| NameError         | local or global name is not found
| OverflowError     | result of an arithmetic operation is too large to be represented
| OSError           | function returns a system-related error
| TypeError         | operation or function is applied to an incorrect object type
| ValueError        | built-in operation or function receives an argument of the right type, but with an inappropriate value while the situation isn't described by a more precise exception
| ZeroDivisionError | second argument for division or modulo is zero

### Error Types

* syntax errors
* runtime errors
* semantic errors

## Managing Exceptions

* handle with try-except and try-except-finally
* can include `else` for try-except-else and try-except-else-finally
* `finally` always runs regardless of outcome (as a cleanup)
    * will even run when `sys.exit()` is called
* check for specific exceptions first
* recommended to avoid bare except statements (catches all exceptions)
* can use a bare except after more specific checks

```python
devices = {'r1': '192.168.5.5', 'r2': '192.168.20.2', 'r3': '192.168.50.2'}
try:
    devices['r4']
except KeyError:
    print('Router not in device dictionary')
```

```python
x = 1
y = 0
try:
    z = x / y
except ZeroDivisionError as e:
    print(e)
```

```python
import requests

ip = 'https://10.254.0.1:443'
dn = '/restconf/data/Cisco-IOS-XE-native:native/interface/'
auth = ('cisco', 'cisco')
dash = '-' * 80
headers = {}

try:
    response = requests.get(ip + dn, headers=headers, auth=auth, verify=False)
    response.raise_for_status()
except requests.HTTPError as e:
    filename = 'errors.log'
    data = e
else:
    filename = 'success.log'
    data = response.content
finally:
    with open(filename, 'a') as fh:
        print(data, dash, sep='\n', file=fh)
```

If you know what you're doing, silence security warnings emitted from requests.
`requests.packages.urllib3.disable_warnings()`

```python
response = requests.get(ip + dn, headers=headers, auth=auth, verify=False)
print(response.status_code)
print(response.content)
```

## Assertions

* statements used for debugging unrecoverable errors
* assert statement evaluated to see if the condition is True or False
* can be used as a debugging aid

`assert <condition>,<error_message>`

```python
response = requests.get(ip + dn, headers=headers, auth=auth, verify=False)

assertion_message = f'{response.status_code} {response.reason}'
assert response.status_code == 200, assertion_message
```

## Debugging Process

1. identify the error
1. identify the source
1. identify the cause
1. fix and validate
    * one change at a time to help isolate the fix

## Python Debugging Functions

Provide basic debugging information:
* print()
* assert
* break
* exit - sys.exit()
    * `sys.exit('some error message')`

## Logging

```python
import logging

logging.basicConfig(
    filename='test.log',
    format=f'%(asctime)s \n%(levelname)s: %(message)s \n{'-' * 80}',
    datefmt='%x %X %Z',
    level=logging.INFO
)
```

https://docs.python.org/3/library/logging.html

## Debugging

### Debuggers

* most IDEs have a debugger integrated into them
* allow devs to
    * run code step-by-step
    * set breakpoints
    * watch variable values change
    * change the variable values
    * provides exception information
    * break at the point the exception was detected

https://code.visualstudio.com/docs/python/debugging

### Simple Debugging

* print() function
* Python REPL
    * for small blocks of code

## Python pdb

[Debugging with Python pdb](section08/08e_pdb_debugging/README.md) in exercise 08e
