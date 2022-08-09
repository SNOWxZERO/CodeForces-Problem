n= int(input())
s = list(map(int,input().split()))
Out1 = 0
Out2 = 0
Looper = 1
while(True):
    m = max(s[0],s[-1])
    if Looper == 1 :
        Out1+=m
    else:
        Out2+=m
    s.remove(m)
    Looper*=-1
    if len(s)==0:
        break
print(f'{Out1} {Out2}')
