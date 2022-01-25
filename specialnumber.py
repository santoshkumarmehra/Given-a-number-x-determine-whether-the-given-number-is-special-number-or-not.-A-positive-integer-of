def pow(a,b):
	sum=0
	for i in n:
		sumt=1
		for j in range(b):
			sumt=sumt*int(i)
		sum=sum+sumt
		sumt=1
	print(sum)
	if sum==int(n):
		return (1+t)
	else:
		return (0+t)

n="5342"
t=len(n)
res=pow(n,t)
print(res)