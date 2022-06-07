n=int(input())
tram = 0
maxs = 0
for i in range(0,n):
    a,b = map(int,input().split())
    tram = tram - a + b
    maxs = max(tram,maxs)
print(maxs)
