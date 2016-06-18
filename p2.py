# generate Fibonacci sequence 

n=1
m=2
sum=0
x=4000000 #limit

while m<=x:
	if not n % 2:
		sum=sum+n
	if not m % 2: 
		sum=sum+m
	n=n+m
	m=n+m
print(i)
