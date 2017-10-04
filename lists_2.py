def isPrime(x):
	for y in range(2, x):
		if x % y == 0:
			return False
	return True

primes = []

i = 3
while len(primes) < 100:
	if isPrime(i):
		primes.extend([i])
	i += 1

print(primes)