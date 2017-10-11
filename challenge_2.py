from random import *

number = randint(1, 100)
guess = 0

attempts = 0

while guess != number:
	print('Your guess:')
	guess = int(input())
	attempts += 1

	if guess == number:
		break
	elif guess < number:
		print('Too low!')
	else:
		print('Too high!')

print('Correct!')
print('That just took ', attempts, ' attempts.')