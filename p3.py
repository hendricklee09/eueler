limit=600851475143
divider=1
total=1
lastFactor=limit

while total<limit:
	divider=divider+1
	while not lastFactor % divider:
		lastFactor=lastFactor/divider
		total=divider*total
	
print(divider)
