#factor into primes	
def factorPrime(numInt):
	total=1
	divider=1
	factors=[]
	lastFactor=numInt
	while total<numInt:
		divider=divider+1
		while (lastFactor % divider)==0:
			factors.append(divider)
			lastFactor=lastFactor/divider
			total=divider*total
	return(factors)

#merge prime. take two lists of prime factorization and keep the highest power
def mergeFactor(p1,p2):
	m=max(max(p1),max(p2))
	p3=[]
	for x in range(2,m+1):
		c1=p1.count(x)
		c2=p2.count(x)
		p0=[x]*max(c1,c2)
		p3.extend(p0)
	return(p3)

#find lowest common multiple 
def lcm(numInt):
	p0=[]
	p1=[1]
	for x in range(2,numInt+1):
		p0=factorPrime(x)
		p1=mergeFactor(p0,p1)
	return(p1)


#muktiply all numbers from a list

def multiP(numList):
	return(reduce(lambda x,y:x*y,numList))



	
print(multiP(lcm(20)))
