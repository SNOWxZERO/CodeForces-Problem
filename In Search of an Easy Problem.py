x = int(input())
s = input().split()
for i in range(0,x):
    if s[i]=='1':
        print('HARD')
        exit()
print('EASY')