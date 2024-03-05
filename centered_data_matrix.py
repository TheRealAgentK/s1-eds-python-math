import numpy as np


# Calculate th center of a matrix
#
# X - input matrix
def center(X):
    return X - np.mean(X, axis=0)


# Calculate the covariance matrix of a matrix using matrix multiplication
#
# X - input matrix
def covmatrix(X):
    return (X.T @ X) / (X.shape[0])


# Check if a Matrix is symmetric
#
# X - input matrix
def is_symmetric(X):
    if np.array_equal(X, X.transpose()):
        return True
    return False


# Driver and test code
data_matrix = np.matrix([[0, 2, 1], [4, 4, 1], [7, 3, 4], [5, 3, 9]])
print(data_matrix)
print(center(data_matrix))

cov_matrix = covmatrix(center(data_matrix))
print(cov_matrix)
print(np.cov(data_matrix.T, bias="False"))
# Should be true
print(is_symmetric(cov_matrix))
