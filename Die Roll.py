s = max(map(int, input().split()))
k = (6 - s + 1)
if k == 0 or k == 6:
    print(f'{int(k / 6)}/1')
elif k == 2 or k == 4:
    print(f'{int(k / 2)}/3')
elif k == 1 or k == 5:
    print(f'{int(k)}/6')
else:
    print('1/2')
