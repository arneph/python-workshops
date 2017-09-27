for x in range(2, 40):
	prime = True
	for y in range(2, x):
		if x % y == 0:
			prime = False
			break		#Break out of inner for-loop
	if prime == False:
		continue		#Continue with next item in
	print(x)			#outer for-loop
