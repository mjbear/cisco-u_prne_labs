# Section 4 - Read and Writing Data to a File

## Reading and Writing Simple Text and CSV Files

### Modes
* r - the default
* w
* a
* r+
* w+
* a+
* b

And more detail on the modes
* https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
* https://docs.python.org/3/library/functions.html#open

### Reading

#### Manual

* requires opening **and** closing the file

```
fh = open(filename, mode)

text = fh.read()
print(text)

fh.close()
```

#### Context Manager (with)

* handles opening and closing the file

```
with open(filename, mode):
    text = fh.read()
    print(text)
    
    # or combined
    # print(fh.read())
```

#### Read, Readline, Readlines

* `read()` - read complete file or so many bytes
* `readline()` - returns a line at a time
* `readlines()` - returns a list of all the lines

```
# read four bytes
fh.read(4)
```

#### Read from CSV

##### As a List
```
import csv

with open('device.csv', 'r') as fh:
    devices = csv.reader(fh)
    header = next(devices)
    print(f'Headers: {header}')
    for row in devices:
        print(row)
```

##### As a Dictionary
```
import csv

with open('device.csv', 'r') as fh:
    devices = csv.DictReader(fh)
    for row in devices:
        print(row)
        print(row['Hostname'], row['Model'])
        print('-' * 30)
```

#### Write to Simple Text File

* `write(str)`
* `print(str, file=fh)`
* `writelines(list)`

##### Use write()

```
msg = 'Hello World from Bob'

with open('hw.txt', 'w') as fh:
    fh.write(msg)
```

##### Use print()

```
msg = 'Hello World from Bob'

with open('hw.txt', 'w') as fh:
    print(msg, file=fh)
```

##### Writing Data to a CSV File

```
import csv

data = [['Hostname', 'Vendor', 'Model', 'Location'],
        ['sw10', 'Cisco', '3800', 'Miami'],
        ['sw11', 'Cisco', '3800', 'Atlanta']]

with open('new_devices.csv', 'w') as fh:
    devices = csv.writer(fh, quoting=csv.QUOTE_NONNUMERIC)
    for row in data:
        devices.writerow(row)

with open('new_devices.csv', 'r') as fh:
    print(fh.read())
```

#### Traverse File Structure

* os.cwd()
* os.mkdir()
* os.walk()

> [!NOTE]
> ```
> for _ in os.walk('/tmp'):
>     print(_)
> ```
> 
> Underscore [variables] represent unimportant temporary data

#### Read CSV file with Pandas

* pandas.DataFrame (object)
    * two-dimensional tabular data structure
    * has rows and columns

```
import pandas

with open('router_info.csv') as fh:
    df = pandas.read_csv(fh)

# output entire DataFrame
print(df)

# output contents of ip column
print(df['ip'])

# output entire first row (row zero)
print(df.loc[[0]])

```

#### Writing CSV file with Pandas

`router_data.to_csv('new_file.csv', index=False)`

* index = write row names (indexes)

https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html

#### Requests for accessing REST API

https://requests.readthedocs.io/en/latest/

#### Read XML

```
from bs4 import BeautifulSoup

xml_data = '''
<outer>
    <one>one</one>
    <two>Two</two>
    <three>3</three>
</outer>
<outer>
    <one>uno</one>
    <two>Dos</two>
    <three>3</three>
</outer>
'''

soup = BeautifulSoup(xml_data, 'lxml')

print(soup)
print('=' * 80)

print(soup.prettify())

print(soup.outer)

for i in soup.find_all('outer'):
    # print(i)
    print(i.find('one').string)
    print(i.two)
    print('-' * 20)
```

https://www.w3schools.com/xml/default.asp

## Reading and Writing a JSON File

* json.load()
* json.loads()
* json.dump()
* json.dumps()

```
import json

# write to file
json.dump(data, file, indent=4)

# dump to Python object
json.dumps(data, indent=4)
```

https://docs.python.org/3/library/json.html#basic-usage
https://docs.python.org/3/library/json.html#json-to-py-table

## pprint

```
from pprint import pprint

pprint(obj, indent=4, width=80, depth=None)
```

https://docs.python.org/3/library/pprint.html
