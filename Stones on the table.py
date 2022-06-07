n = int(input())
s = list(input())
k = 0
i=0
while i < len(s)-1:
	if(s[i]==s[i+1]) :
		del s[i]
		k=k+1
		i = 0
	else:i+=1
print(k)