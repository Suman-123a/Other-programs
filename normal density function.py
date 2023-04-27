#normal density function
import matplotlib.pyplot as plt
import numpy as np
aa,kk=[],[]
for k in range(-5,6):
	a=(1/(np.pi*5)**0.5)*np.exp((-k**2)/5)
	kk.append(k)
	aa.append(a)
plt.bar(kk,aa)
plt.show()

	