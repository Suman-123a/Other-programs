#gauss elimination
import numpy as np
A=np.array([[1,-2,1,0],[0,2,-8,8],[-4,5,9,-9]])
n=len(A)
for k in range(n-1):
    for i in range(k+1,n):
        e=A[i][k]
        for j in range(k,n+1):
            A[i][j]-=A[k][j]*(e/A[k][k])           
print("the upper triangular matrix=")
print(A)
#back substitution
b=A[:,-1]
x=np.array([0,0,0])
for i in range(n-1,-1,-1):	
	z=np.dot(A[i][i+1:n],x[i+1:n])
	x[i]=(b[i]-z)/A[i][i]
print("the solution=",x)
	
	