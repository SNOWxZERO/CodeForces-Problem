t = int(input())
counter = 0
for i in range(t):
    m,c = list(map(int,input().split()))
    if m == c :
        continue
    if m > c :
        counter+=1
    else:
        counter-=1
if counter ==0 :
    print('Friendship is magic!^^')
elif counter > 0 :
    print('Mishka')
else:
    print('Chris')
