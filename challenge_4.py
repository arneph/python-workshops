def orders(numbers): 	#takes a list and returns a list of lists with all possible orders
	n = len(numbers)
	results = []

	if n == 0:
		return NULL
	elif n == 1:
		return [numbers]

	for x in range(n):
		head = numbers[x]
		tail = numbers[:x] + numbers[x + 1:]
		
		suborders = orders(tail)

		m = len(suborders)

		for y in range(m):
			result = suborders[y]
			result.insert(0, head)

			results.append(result)

	return results

print('Word:')
word = input()
letters = list(word)

res = orders(letters)
n = len(res)

for x in range(n):
	r = res[x]
	print(''.join(r))