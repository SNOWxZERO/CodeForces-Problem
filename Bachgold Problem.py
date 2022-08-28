n=int(input())
k = int(n/2)
print(k)
if n%2==0:
    print('2 '*k)
else:
    print('2 '*(k-1)+'3 ')

