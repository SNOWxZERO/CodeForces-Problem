n = [input().split(),
     input().split(),
     input().split(),
     input().split(),
     input().split()]

for i in range(0, 5):

    for j in range(0, 5):

        if n[i][j] == '1':
            print(abs(j - 2) + abs(i - 2))
            break
