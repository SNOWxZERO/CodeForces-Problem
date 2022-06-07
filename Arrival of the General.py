n = int(input())
s = list(map(int, input().split()))
maxs=max(s)
mins=min(s)
maxi = min([idx for idx, val in enumerate(s) if val == maxs])
mini = max([idx for idx, val in enumerate(s) if val == mins])
if maxi > mini : print((maxi-1)+(n-mini)-1)
else:print((maxi-1)+(n-mini))

