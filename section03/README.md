# Section 3 - Conditionals, Operators, and Loops

## Conditionals

* flow control
* code in the (`if` statement) control structure will run if the expression evaluates to `True`

### if
```
x = True
if x:
    print('x is True')
# outputs 'x is True'

# versus

x = False
if x:
    print('x is True')
# no output
```

### if, elif, else
```
x = False
y = True

if x:
    print('x is True')
elif y:
    print('y is True')
else:
    print('x and y are not True')
# outputs 'y is True'
```

## Operators

* special symbols used to perform operations
* Types:
    * arithmetic
    * assignment
    * comparison
    * logical
    * identity
    * membership

### Arithmetic

* Addition `+`
* Subtraction `-`
* Multiplication `*`
* Division `/`
* Modulo `%`
* Exponentiation `**`
* Floor Division `//`

### Assignment

```
+= Adds right to left
-= Subtracts right from left
*= Multiplies right with left
/= Divides left by right
%= Assigns the remainder of dividing left by right
//= Assigns integer result (quotient) from dividing left by right
**= Assigns result of raising left operand to the power of right operand
```

### Comparison

* Equal `==`
* Not Equal `!=`
* Greater Than `>`
* Less Than `<`
* Greater Than or Equal To `>=`
* Less Than or Equal To `<=`

### Logical Operators

```
and
or
not
```

### Identity Operators

```
is
is not
```

### Membership Operators
```
in
not in
```

## Loops

* execute multiple times

### For Loops

* can iterate over iterable objects (iterables) via a for loop

`for <var> in <iterable>:`

```
for i in 'string':
    print(i)


for i in range(10):
    print(i)
```

### While Loops

* used to iterate as long as test expression is True
* used when the number of iterations/executions is _unknown_

`while <expression>:`

```
i = 4
while i > 0:
    print(f'The value of i is {i}')
    i -= 1
```

### Loops with List

```
devices = ['router1', 'router2', 'router3', 'switch1']
for device in devices:
    print(device)
```

### Loops with Dict

```
keys()
values()
items() - key-value pairs
```

```
device = {'device': 'router', 'model': '3800', 'os': 'IOS-XE'}

for key in device.keys():
    print(key)

for value in device.values():
    print(value)

for item in device.items():
    print(item)
```

### Loops with Range

`range(start, stop, step)`

```
devices = ['router1', 'router2', 'router3', 'switch1']

for i in range(2, len(device)):
    print(device[i])
```

### Loops with Conditionals

```
devices = ['router1', 'router2', 'router3', 'switch1']

for i in range(len(devices)):
    if devices[i] == 'router3':
        print('This is router3 inside the if statement')
    print('This is outside the if statement')
```

#### Break

* break completely out of a loop
* terminates the loop

https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements

#### Continue

* skip code for the current iteration
* loop does not terminate, but continues with the next iteration

#### Else Clauses on Loops

https://docs.python.org/3/tutorial/controlflow.html#else-clauses-on-loops
