# Section 7 - User Input

## User Input

### input module

* `input()` - reads input from a keyboard
    * also accepts prompt text as an argument
* displays the text as it is typed
* values from user input are always strings
    * requires type casting (type conversion) from string to the desired type
    * if the user input cannot be converted, a ValueError will be thrown

```python
ip = input('Enter an IPv4 address:')

count = input('Enter the number of pings to send: ')
count = int(count)

member_count = int(input('Number of switch stack members: '))
```

### getpass module

* does **NOT** display the text as it is typed
* ideal for passwords

```python
import getpass

password = getpass.getpass('Password"')
```

> [!NOTE]
> Commonly imported as `from getpass import getpass`
> 
> Then usage requires only a single `getpass` reference (ex: `p = getpass()`)

## Basic Validation Check

* Type Check
    * check the data type
* Length Check
    * check the length of a sequence
* Range Check
    * does the value fall within a range of numbers

### Password Length Check

* example code uses a flag check (with a boolean variable)

```python
password_is_too_short = True

while password_is_too_short:
    password = input('Enter password of at least 5 characters:')
    if len(password) >= 5:
        password_is_too_short = False
    else:
        print('The password entered is too short')

print(f'The password you entered is: {password}')
```

## Command-line Arguments

* sys.argv from the sys module
* argparse module

### sys.argv

* first item in the argument list (at index zero) is the file name
    * https://docs.python.org/3/library/sys.html#sys.argv
* can slice the list to exclude the file name
* simple and easy to use
* however help or error checking must be manually coded

When ran as a script from the command line...
```python
import sys

print(f'Argument List: {sys.argv}')
```

### argparse

* supports required and optional arguments
* auto-generates help information
* available since Python 3.2

Usage:
* `import argparse`
* initialize the parser
* add help statement
* add required or optional arguments
    * short option
        * short representation
    * long option
        * long representation
    * help
    * action
        * if set to `store_true`, arg is optional
* https://docs.python.org/3/howto/argparse.html
* https://docs.python.org/3/library/argparse.html

```python
# note this has not been tested
import argparse

from netmiko import ConnectHandler


text = 'Configure hostname on an IP address based on input'
parser = argparse.ArgumentParser(description=text)
parser.add_argument('-name', help='host name')
parser.add_argument('-ip', help='IP address')

args = parser.parse_args()

device = {
    'host': args.ip,
    'username': 'cisco',
    'password': 'cisco',
    'device_type': 'cisco_xe',
}

with ConnectHandler(**device) as conn:
    print(f'The current host name is {conn.find_prompt()}')

    conn.send_config_set([f'hostname {args.name}'])
    print('New name has been configured')

    new_name = conn.send_command('show run | include hostname')
    print('New host name is {new_name.split()[1]}')
```

Details/examples for Netmiko
* https://pynet.twb-tech.com/blog/netmiko-python-library.html
* https://pynet.twb-tech.com/blog/netmiko-and-what-constitutes-done.html
