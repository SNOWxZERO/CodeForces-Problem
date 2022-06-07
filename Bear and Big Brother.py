x= input().split(" ")
a=int(x[0])
b= int(x[1])
if a == b :
    print(1)
else:
    for i in range(1,500) :
        a= a*3*i
        b= b*2*i
        if a>b:
            print(i)
            break
