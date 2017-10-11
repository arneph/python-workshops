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

numbers = [1, 2, 3, 4, 5]
res = orders(numbers)

for x in range(120):
	print(res[x])