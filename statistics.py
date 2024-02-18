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

# Calculate p-quantiles of a numeric list
def quantile(data, p):
    sorted_data = sorted(data)
    n = len(data)
    i = p * (n + 1)
    if i.is_integer():
        return sorted_data[int(i-1)]
    else:
        return sorted_data[int(i)-1] + (sorted_data[int(i)] - sorted_data[int(i)-1]) * (i - int(i))

# Calculate IQRs
def iqr(data):
    return quantile(data, 0.75) - quantile(data, 0.25)

# Calculate the median absolute deviation of a numeric list
def MAD(data):
    median_data = median(data)
    distances = [abs(x_i - median_data) for x_i in data]
    return median(distances)

# Calculate variance of a numeric list
def variance(data):
    n = len(data)
    mean_data = arithmetic_mean(data)
    return sum((x_i - mean_data) ** 2 for x_i in data) / (n - 1)

# Calculate standard deviation of a numeric list
def standard_deviation(data):
    return sqrt(variance(data))

# Calculate the covariance of two numeric lists
def covariance(data1, data2):
    if len(data1) != len(data2):
        raise Exception('Lists must have the same length')
    n = len(data1)
    mean_data_1 = arithmetic_mean(data1)
    mean_data_2 = arithmetic_mean(data2)
    return sum((x_i - mean_data_1) * (y_i - mean_data_2) for x_i, y_i in zip(data1, data2)) / n

# Calculate correlation of two numeric lists
def correlation(data1, data2):
    if len(data1) != len(data2):
        raise Exception('Lists must have the same length')
    return covariance(data1, data2) / (standard_deviation(data1) * standard_deviation(data2))


def execute_samples(data):
    print(f'Arithmetic: {Decimal(arithmetic_mean(data))}')
    print(f'Geometric: {Decimal(geometric_mean(data))}')
    print(f'Harmonic: {Decimal(harmonic_mean(data))}')
    print(f'Trimmed 1: {Decimal(trimmed_mean(data, 1))}')
    print(f'Trimmed 2: {Decimal(trimmed_mean(data, 2))}')
    print(f'Weighted (1s): {Decimal(weighted_mean(data, [1] * len(data)))}')
    print(f'Hoelder 2: {Decimal(hoelder_mean(data, 2))}')
    print(f'Hoelder 1 (arith): {Decimal(hoelder_mean(data, 1))}')
    print(f'Hoelder -1 (harm): {Decimal(hoelder_mean(data, -1))}')
    print(f'Median: {Decimal(median(data))}')
    print(f'Mode: {mode(data)}')
    print(f'Quantile 0.1: {Decimal(quantile(data, 0.1))}')
    print(f'Quantile 0.25: {Decimal(quantile(data, 0.25))}')
    print(f'Quantile 0.5: {Decimal(quantile(data, 0.5))}')
    print(f'Quantile 0.75: {Decimal(quantile(data, 0.75))}')
    print(f'Quantile 0.8: {Decimal(quantile(data, 0.8))}')
    print(f'IQR: {Decimal(iqr(data))}')
    print(f'MAD: {Decimal(MAD(data))}')
    print(f'Variance: {Decimal(variance(data))}')
    print(f'Standard deviation: {Decimal(standard_deviation(data))}')
    print(f'Covariance: {Decimal(covariance(data, data))}')
    print(f'Correlation: {Decimal(correlation(data, data))}')

# Driver and test code
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

data2 = [
    2.85,  3.19,  3.50,  3.69,  3.90,  4.14,  4.32,  4.50,  4.80,  5.20,
    2.85,  3.20,  3.54,  3.70, 3.96,  4.16,  4.44,  4.56,  4.80,  5.30,
    2.98,  3.30,  3.54,  3.70,  4.05,  4.20,  4.47,  4.68,  4.90,  5.43,
    3.04,  3.39,  3.57,  3.75,  4.08,  4.20,  4.47,  4.70,  5.00,
    3.10,  3.42,  3.60,  3.78,  4.10,  4.30,  4.47,  4.71,  5.10,
    3.10,  3.48,  3.60,  3.83,  4.14,  4.30,  4.50,  4.78,  5.10
]

print('----------- data -----------')
execute_samples(data)

print('----------- data 2 -----------')
execute_samples(data2)