arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
flag = True
x = 3
if x%2 == 0 :
    flag = False
else:
    flag = True

for i in range(0, x):
    print(i * ' ', end='')
    if i % 2 == 0:
        print(
            str(arr[i]) + (2*x - 3)  * ' ' + str(arr[i + (x - 1) * 2]) + (2*x - 3)  * ' ' + str(arr[i + (x - 1) * 4]))
    else:
        print(
            str(arr[i]) + (2*x - 3)  * ' ' + str(arr[i + (x - 1) * 2]) + (2*x - 3)  * ' ' + str(arr[i + (x - 1) * 4]))
