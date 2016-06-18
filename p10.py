
#basic prime factorization
def factorPrime(numInt):
	a=[True]*numInt
	a[0]=a[1]=False 
	for (i,isPrime) in enumerate(a):
		if isPrime:
			yield i
			for n in xrange(i*i,numInt,i):
				a[n]=False 

s=2000000
			
primeList=list(factorPrime(s))
primeSum=reduce(lambda x,y:x+y,primeList)
print(primeSum)