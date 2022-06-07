k,r = map(int,input().split())
#((k*s)-r)%10==0)
i=True
s=1
while i :
	if ((k * s) % 10 == 0):
		i = False
		print(s)
	elif(((k*s)-r)%10==0) :
		i = False
		print(s)
	else:s +=1
