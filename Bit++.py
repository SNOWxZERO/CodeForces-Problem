n = int(input())
k = 0
for i in range(0,n) :
	s = input()
	if("++" in s) :
		k+=1
	elif("--" in s)	:
		k-=1

print(k)