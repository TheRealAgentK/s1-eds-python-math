# imports
import numpy as np
from math import *
from decimal import Decimal

# Calculate the arithmetic mean of a numeric list
def arithmetic_mean(data):
    return sum(data) / len(data)

# Calculate the geometric mean of a numeric list
def geometric_mean(data):
    return np.prod(data) ** (1 / len(data))

# Calculate the harmonic mean of a numeric list
def harmonic_mean(data):
    return len(data) / sum(1/x_i for x_i in data)

# Calculate the p-trimmed mean of a numeric list
def trimmed_mean(data, p):
    n = len(data)
    return sum(sorted(data)[p:n-p]) / (n - 2 * p)

# Calculate the weighted mean of a numeric list
def weighted_mean(data,weights):
    return sum(x_i * w_i for x_i, w_i in zip(data, weights)) / sum(weights)

# Calculate a generic Hölder mean of a numeric list
def hoelder_mean(data, p):
    return (sum(x_i ** p for x_i in data) / len(data)) ** (1 / p)

# Calculate the median of a numeric list
def median(data):
    n = len(data)
    sorted_data = sorted(data)
    if n % 2 == 0:
        return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        return sorted_data[n//2]

# Calculate the mode of a numeric list
def mode(data):
    counts = {}
    for x_i in data:
        if x_i in counts:
            counts[x_i] += 1
        else:
            counts[x_i] = 1
    max_count = max(counts.values())
    return [x for x, count in counts.items() if count == max_count]

# Driver and test code
data = [1, 2, 3, 4, 5, 6]
print(f'Arithmetic: {Decimal(arithmetic_mean(data))}')
print(f'Geometric: {Decimal(geometric_mean(data))}')
print(f'Harmonic: {Decimal(harmonic_mean(data))}')
print(f'Trimmed 1: {Decimal(trimmed_mean(data, 1))}')
print(f'Trimmed 2: {Decimal(trimmed_mean(data, 2))}')
print(f'Weighted (111111): {Decimal(weighted_mean(data, [1, 1, 1, 1, 1, 1]))}')
print(f'Weighted (321123): {Decimal(weighted_mean(data, [3, 2, 1, 1, 2, 3]))}')
print(f'Hoelder 2: {Decimal(hoelder_mean(data, 2))}')
print(f'Hoelder 1 (arith): {Decimal(hoelder_mean(data, 1))}')
print(f'Hoelder -1 (harm): {Decimal(hoelder_mean(data, -1))}')
print(f'Median: {Decimal(median(data))}')
print(f'Mode: {mode(data)}')