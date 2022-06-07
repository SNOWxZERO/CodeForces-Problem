x=list(input())
x.sort()
j=True
i=0
while(j) :
	if(x[i]==x[i+1]):
		del x[i]
		i=0
	else:i+=1
	if (i >= len(x)-1):
		j = False
		break
if(len(x)%2==0):
	print('CHAT WITH HER!')
else:print('IGNORE HIM!')