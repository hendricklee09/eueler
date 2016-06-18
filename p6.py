#list of natural numer to n
def natN(n):
	return(range(1,n+1))

#sum of square
def sumS(numList):
	s=map(lambda x:x**2,numList)
	l=sum(s)
	return(l)

#square of sum
def squS(numList):
	s=sum(numList)
	l=s**2
	return(l)

n=natN(100)

a=squS(n)
b=sumS(n)
	
print(squS(n))
print(sumS(n))
print(a-b)
