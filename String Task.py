k = input()
k = k.lower()
s = ""
L = ['a', 'e', 'i', 'o', 'u', 'y']
for i in range(0, len(k)):
	if k[i] not in L:
		s += '.'
		s += k[i]

print(s)
