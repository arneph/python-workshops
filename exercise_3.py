A = 0
B = 1

print(B)

for x in range(0, 20):
	C = A + B
	A = B
	B = C

	print(C)