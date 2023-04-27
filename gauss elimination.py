#Q.Solution of linear system :
#x-2y+z=0
#2y-8z=8
#-4x+5y+9z=-9 ;by Gauss elimination

import numpy as np
def GE(A):
		n=len(A)
		for k in range(n-1):
		    for i in range(k+1,n):
		        e=A[i][k]
		        for j in range(k,n+1):
		            A[i][j]-=A[k][j]*(e/A[k][k]) 
		x=[0,0,0]
		b=A[:,-1]
		for i in range(n-1,-1,-1):
			x[i]=b[i]
			for j in range(i+1,n):
				x[i]=x[i]-A[i][j]*x[j]
			x[i]=x[i]/A[i][i]
		return x,A
A=np.array([[1,-2,1,0],[0,2,-8,8],[-4,5,9,-9]])
z1,z2=GE(A)
print(z2)
print("the solutions are=",z1)
