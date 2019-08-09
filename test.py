from itertools import product

a = [1, 2, 3, 4, 5]
b = [10, 11, 12, 13, 14, 15]


c = [(x, y) for x in a for y in b]

print(c)
print(list(product(a, b)))
