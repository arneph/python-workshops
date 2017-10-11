print('Pizza 1')
print('Diameter: ')
d1 = int(input())
print('Prize: ')
p1 = int(input())

print('Pizza 2')
print('Diameter: ')
d2 = int(input())
print('Prize: ')
p2 = int(input())

a1 = d1 * d1 / 4 * 3.141
a2 = d2 * d2 / 4 * 3.141

v1 = a1 / p1
v2 = a2 / p2

if v1 < v2:
	print('Buy pizza 2!')
elif v1 == v2:
	print('Buy either one!')
else:
	print('Buy pizza 1!')