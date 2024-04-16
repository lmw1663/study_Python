import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

# Given raw data
M = np.array([
    [90, 60, 90],
    [90, 90, 30],
    [60, 60, 60],
    [60, 60, 90],
    [30, 30, 30]
])
S = np.array([
    [90, 60, 90],
    [90, 90, 30],
    [60, 60, 60],
    [60, 60, 90],
    ])
# Number of data points
n = M.shape[0]

# Create a vector of ones
one_vector = np.ones((n, 1))

# Calculate the transformed data matrix
d = M - (1/n) * np.dot(one_vector, one_vector.T).dot(M)

# Print the transformed data matrix
print("Transformed data matrix:")
print(d)
print()

# Calculate the deviation sums of squares and cross products matrix for the transformed data
dd = np.dot(d.T, d)

# Print the deviation sums of squares and cross products matrix
print("Deviation sums of squares and cross products matrix:")
print(dd)
print()

# Calculate the variance-covariance matrix
V = dd / n

# Print the variance-covariance matrix
print("Variance-covariance matrix:")
print(V)

covariance_matrix = np.cov(M, rowvar=False, bias=True)
covariance_matrix_s = np.cov(S, rowvar=False,bias=True)
print("use numpy population covariance matrix")
print(covariance_matrix)
sn.heatmap(covariance_matrix, annot=True, fmt='g')
plt.show()
print("use numpy Sample covariance matrix ")
print(covariance_matrix_s)
sn.heatmap(covariance_matrix_s,annot=True,fmt='g')
plt.show()