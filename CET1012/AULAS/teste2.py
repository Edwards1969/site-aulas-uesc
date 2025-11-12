import numpy as np

A = np.identity(3)
B = np.array([[1,2,3],
            [4,5,5]])   
C = np.dot(A, B)

for row in C:
    print(row)
    