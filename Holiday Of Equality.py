n = int(input())
s = list(map(int, input().split()))
ma = max(s)
sums = 0
for i in s:
    sums += (ma - i)
print(sums)
