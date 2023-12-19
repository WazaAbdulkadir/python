# Program to multiply two matrices using nested loops
import numpy as np 
# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)



dimensions = np.shape(Y)
row, column = dimensions

print(len(X))
print(column)
print(len(Y[0]))

A = [[2,3],
     [1,0]]
B = [[-1,3],
     [2,5]]

result2 = [[0,0],
           [0,0]]

for i in range(len(A)):
    for j in range(len(B)):
        for k in range(len(B[0])):
            result2[i][j] = A[i][k] * B[k][j] 

for c in result2:
    print(c)