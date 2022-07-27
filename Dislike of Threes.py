arr = [i for i in range(1,1667)]
c=0
while(True):
    if arr[c] % 3 == 0 or arr[c] % 10 == 3:
        arr.pop(c)
        continue
    c+=1
    if c==len(arr):
        break

t= int(input())
for i in range(t):
    n= int(input())
    print(arr[n-1])


