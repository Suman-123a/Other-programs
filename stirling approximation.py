#stirling approximation
import numpy as np
import matplotlib.pyplot as plt
def f(n):
	m=1
	for i in range(1,n+1):
		m=m*i
	return m
yy,xx,zz,pp=[],[],[],[]

for i in range(1,60):
	y=np.log(float(f(i)))
	yy.append(y)
	x=i*np.log(i)-i
	xx.append(x)
	z=(abs(y-x)/y)*100
	zz.append(z)
	pp.append(i)
plt.plot(pp,zz)
plt.show()
	
    