#Lissajous figures
import matplotlib.pyplot as plt
import numpy as np
def LS(a,n1,n2):
	t=np.linspace(0,10,1000)
	w1=2*np.pi*n1
	w2=2*np.pi*n2
	xx=a*np.cos(w1*t)
	yy=a*np.sin(w2*t)
	return xx,yy
z1,z2=LS(2,1,3)
plt.plot(z2,z1)
plt.show()