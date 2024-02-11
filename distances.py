# import math library
from math import *
from decimal import Decimal


def p_root(value, root):
    root_value = 1 / float(root)
    return Decimal(value) ** Decimal(root_value)


def minkowski_distance(x, y, p_value):
    return p_root(sum(pow(abs(a - b), p_value) for a, b in zip(x, y)), p_value)


def euclidean_distance(x, y):
    return minkowski_distance(x, y, 2)


def manhattan_distance(x, y):
    return minkowski_distance(x, y, 1)


# Driver and test code
vector1 = [0, 2, 3, 4]
vector2 = [2, 4, 3, 7]
p = 2

print(minkowski_distance(vector1, vector2, p))
print(euclidean_distance(vector1, vector2))
print(manhattan_distance(vector1, vector2))
