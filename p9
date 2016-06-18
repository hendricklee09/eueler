#generate initial tripplet
def genTriplet(numInt):
	numList=[1,2,numInt-3]
	return(numList)

#check pyth triplet
def checkTriplet(numList):
	x=numList[0]**2+numList[1]**2
	y=numList[2]**2
	if x==y:return True
	else: return False

#give you the next list of triplet to check
def cycleSum(total,numList):
	if numList[0]+numList[1]+numList[2]!=total:return False
	if not numList[1]-numList[0]>2:
		numList[2]=numList[2]-1
		numList[0]=1
		numList[1]=total-numList[2]-numList[0]
	else:
		numList[0]=numList[0]+1
		numList[1]=numList[1]-1
	return(numList)

isTriplet=False
a=1000
b=genTriplet(a)

while not isTriplet:
	b=cycleSum(a,b)
	isTriplet=checkTriplet(b)
answer=reduce(lambda x,y: x*y,b)
print(answer)
