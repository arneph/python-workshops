def fizzbuzz(x):
	a = (x % 3 == 0)
	b = (x % 5 == 0)
	if a and b:
		print('Fizz Buzz')
	elif a:
		print('Fizz')
	elif b:
		print('Buzz')
	else:
		print(x)

for x in range(1, 50):
	fizzbuzz(x)
