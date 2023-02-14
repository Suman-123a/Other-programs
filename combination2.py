def f(n,r):#function of permutation
	m=1
	for i in range(r):
		m=m*(n-i)
	return m
def g(r):#function of factorial
	fact=1
	for i in range(1,r+1):
		fact=fact*i
	return fact
def k(n,r):#function of combination
	return f(n,r)/g(r)
z1=0
r=0
a=0.4
b=1
#calculation of (a+b)^n
for i in range(150):
	z1=z1+k(0.7,r)*a**r*b**(0.7-r)
	r=r+1
	
print(z1)
