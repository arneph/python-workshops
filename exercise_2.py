def isPrime(x):
	for y in range(2, x):
		if x % y == 0:
			return False
	return True

for x in range(2, 50):
	if isPrime(x) == False:
		continue
	print(x)
