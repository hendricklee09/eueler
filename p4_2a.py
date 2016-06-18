limit=999999

#convert list into int via http://stackoverflow.com/questions/489999/python-convert-list-of-ints-to-one-number
def list2int(numList):
	s = ''.join(map(str, numList))
	return int(s)
	
#convert integer into list of numbers
def int2list(numInt):
	s=[int(x) for x in str(palInt)] 
	return s
	
#find the next lower palindrome
def nextPal(numInt):
	s=int2list(numInt)
	i=int(len(s)/2)+1 #the middle digit
	while s[i]>0 
		s[i]=s[i]-1
		
		
			
	return nextInt


palInt=limit



palList[0]=palList[0]-1


	
palInt=list2int(palList)


print(palInt)
