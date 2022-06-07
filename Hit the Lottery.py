x = int(input())
c = 0
s = [100,20,10,5,1]
for i in s :
    c+=int(x/i)
    x=x%i
    if x ==0 : break
print(c)