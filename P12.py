# triangle number generator

def triNum(numInt):
	n=numInt
	ans=0
	while n>0:
		ans=ans+n
		n=n-1
	return(ans)
	
def factor(numInt):
	l=[]
	i=1
	while i*i<=numInt:
		if not numInt % i:
			if i in l:break
			l.append(i)
			if numInt/i in l:break
			l.append(numInt/i)
		i+=1
	return(l)

divsor=500
x=[]
n=1
while not len(x)>=divsor:
	x=factor(triNum(n))
	n=n+1


print(x)