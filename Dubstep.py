x = input()
x=x.replace('WUB',' ')
i=0
k=True
while(k):
	if(x[i]==' ' and x[i+1]==' '):
		x=x.replace('  ',' ')
	else:i+=1
	if(i>len(x)-2):
		break
if(x[0]==' 'and x[-1]==' ') :
	print(x[1:-1])
elif(x[0]==' '):
	print(x[1:len(x)])
elif(x[-1]==' '):
	print(x[0:len(x) - 1])
else:print(x)

