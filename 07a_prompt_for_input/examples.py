#!/usr/bin/env python

print('use the underscore for temporary/unimportant variables')
for _ in range(10):
    print(_)

print()

print('assign multiple variables with a list as the source')
x, y, z = [1, 2, 3]
print(f'x is: {x}')
print(f'y is: {y}')
print(f'z is: {z}')