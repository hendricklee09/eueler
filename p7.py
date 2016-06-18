#prime factorization

def factorPrime(numInt):
	a=[True]*numInt
	a[0]=a[1]=False 
	for (i,isPrime) in enumerate(a):
		if isPrime:
			yield i
			for n in xrange(i*i,numInt,i):
				a[n]=False 



#take a prime list and extend it to a new max
#def extendPrime(maxPlus,primeList):
#	lastPrime=primeList[len(primeList)-1]
#	a=[True]*maxPlus
#	for i in xrange(0)


a=factorPrime(999999999)
list(a)
print(a(10000))