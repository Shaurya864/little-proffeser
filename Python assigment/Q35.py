#Write a program to perform matrix addition and multiplication using nested lists.
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]


result_add = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("Matrix Addition:")
for row in result_add:
    print(row)


result_mul = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
print("\nMatrix Multiplication:")
for row in result_mul:
    print(row)

