m,n = map(int,input().split())
s = m*n
if(s%2 == 1) :
	s-=1
print(int(s/2))