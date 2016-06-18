limit=996699 #999*998 gives us the largest candidate
palInt=limit # palindrome initial


total=1
divider=1 

while (total/divider)<99:
	total=1
	divider=1 

	
	

	
	lastFactor=palInt
	factor=palInt
	
	while factor<1000:
		divider=1 
		total=1
		lastFactor=factor
		
		while total<factor:
			divider=divider+1
			while not lastFactor % divider:
				lastFactor=lastFactor/divider
				total=divider*total
		factor=divider
	

print(palInt)
print(divider)
print(total/divider)
print(factor)
