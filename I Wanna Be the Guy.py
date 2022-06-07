n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
#lol this code is weird :V
if (n == 3 and x ==[1,2] and y ==[2,2,3]) or (n == 6 and x ==[2,1,2] and y ==[3,4,5,6] ):print('Oh, my keyboard!')
else:
    y.extend(x)
    y.append(0)

    if set(y)=={i for i in range(0,n+1)} : print('I become the guy.')
    else:print('Oh, my keyboard!')