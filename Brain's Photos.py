n,m = map(int,input().split())
color = False
for i in range(n) :
	x = input().split()
	if(x.__contains__('C')or x.__contains__('M')or x.__contains__('Y')):
		color=True

if(color):
	print('#Color')
else:
	print('#Black&White')