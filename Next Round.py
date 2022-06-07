n,k = map(int,input().split())
x = list(map(int,input().split()))
suc = 0
for i in range(0,len(x)):
    if x[i]>=x[k-1] and x[i]>0 :
        suc+=1
print(suc)