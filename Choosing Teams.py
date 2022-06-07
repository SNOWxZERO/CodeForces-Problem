n,k=map(int,input().split())
k=int(input().split()[1])

y=list(map(int,input().split()))
count=0
for i in y:
    if i+k <=5:
        count+=1

print(int(count/3))

