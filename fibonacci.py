#fibonacci sequence
n=10
a=[0,1]
for i in range(n):
	x=a[i]+a[i+1]
	a.append(x)
print(a)