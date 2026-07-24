# Write a program to handle multi-dimensional array using numpy.
import numpy as np


A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8, 9],
              [10, 11, 12]])

print("Array A:\n", A)
print("Array B:\n", B)


print("\nAddition:\n", A + B)


print("\nElement-wise Multiplication:\n", A * B)


print("\nMatrix Multiplication:\n", np.dot(A, B.T))  # B.T is transpose
