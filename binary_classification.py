import numpy as np

# Calculate the pseudo-inverse of a matrix
#
# X - input matrix
def pseudo_inverse(X):
    return np.linalg.inv(X.T @ X) @ X.T

# Basic binary linear classification function
#
# w - weight vector
# w_0 - bias
# q - input vector
def classify(w, w_0, q):
    print (w @ q + w_0)
    return np.sign(w @ q + w_0)

# Driver and test code
w_0 = np.array([1,1,1,1,1])
w_age = np.array([23,17,43,68,32])
w_max_speed = np.array([180,240,246,173,110])
w_hp = np.array([70,145,120,59,100])

y = np.array([1,1,1,-1,-1])

extended_data = np.array([w_0, w_age, w_max_speed]).T
w_hat = pseudo_inverse(extended_data) @ y

q_1 = np.array([60, 190])
q_2 = np.array([60, 190])

print(classify(w_hat[1:], w_hat[0], q_1))
print(classify(w_hat[1:], w_hat[0], q_2))



