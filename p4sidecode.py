	a1=int(palStr[5]) #1st digit etc
	a2=int(palStr[4])
	a3=int(palStr[3])	

	if a3==0:
		a3=9
		if a2==0:
			a2=9
			if a1>1:
				
				a1=a1-1
		else:
			a2=a2-1
	else:
		a3=a3-1
	
	palInt=100000*a1+a1+10000*a2+10*a2+1000*a3+100*a3
	palStr=str(palInt)
