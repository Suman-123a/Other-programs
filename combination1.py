def f(m):#function of factorial
	fact=1
	for i in range(1,m+1):
		fact=fact*i
	return fact
def nCr(n,r):
	z=f(n)/(f(n-r)*f(r))
	return z
n=10
r=0
s=0
for i in range(n+1):
	zz=nCr(n,r)
	s=s+zz
	r=r+1
	
print(s)
