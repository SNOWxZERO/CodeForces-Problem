n = int(input())
for i in range(n):
    s = int(input())
    if (s / 2) % 2 != 0:
        print('NO')
    else:
        print('YES')
        for k in range(2, s + 1, 2):
            print(k,end=' ')
        for k in range(1, s - 1, 2):
            print(k,end=' ')
        print(str((s + int(s / 2)) - 1))
        #this code works faster but with 5000KB memory which means list comperhensive is faster in exectutions but uses alot of memorey for big range numbers :D
        '''print(' '.join([str(k) for k in range(2, s + 1, 2)]) + ' ' + ' '.join(
            #[str(k) for k in range(1, s - 2, 2)]) + ' ' + str((s + int(s / 2)) - 1))'''
