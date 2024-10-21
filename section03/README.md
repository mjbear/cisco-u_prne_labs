# Section 3 - Conditionals and Operators

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
