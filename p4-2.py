
#convert list into int via http://stackoverflow.com/questions/489999/python-convert-list-of-ints-to-one-number
def list2int(numList):
	s = ''.join(map(str, numList))
	return int(s)

#convert integer into list of numbers
def int2list(numInt):
	s=[int(x) for x in str(numInt)] 
	return s

#check if a number is a palendrome
def checkPal(numInt):
	numList=int2list(numInt)
	l=len(numList)/2
	if len(numList) % 2: l=l+1
	for x in range(0,l):
		if not numList[x]==numList[len(numList)-1-x]:
			return(0)
			break
	return(1)
	

#check if a number is a palendrome
def checkCal(numList):
	if len(numList)<=1:return(1)
	if not numList[0]==numList[len(numList)-1]:return(0)
	numList.pop(0)
	numList.pop(len(numList)-1)
	if len(numList)<=1:return(1)
	return(checkCal(numList))
	

palList=[]
for x in range(999,99,-1):
	for y in range(999,99,-1):
		if checkCal(int2list(x*y))==1: 
			palList.append(x*y)
	if checkCal(int2list(x*y))==1:break

print(max(palList))
