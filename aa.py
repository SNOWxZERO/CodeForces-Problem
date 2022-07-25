'''
Not CodeForces Problem
'''

def zigzag(s, x):
    i = 0
    j = 0
    d = 1
    output = [[' ' for i in range(0, len(s))] for i in range(x)]
    while (1):
        output[i][j] = s[j]
        if i == x - 1:
            d = -1
        elif i == 0:
            d = 1
        i += d
        if j < len(s) - 1:
            j += 1
        else:
            break
    for i in output:
        print(''.join(i))


'''
Helping Methods
'''

def lines_Counter():
    c = 0
    while (1):
        a = input()
        if a == '..':
            break
        c += 1
    print(c)
def Answer_Checker():
    n = int(input())
    Output = []
    Answer = []
    for i in range(n):
        Output.append(input())
    for i in range(n):
        Answer.append(input())

    print([i for i, (x, y) in enumerate(zip(Output, Answer)) if x != y])




'''
Executions
'''
# zigzag('dasdasssssdasfdgdfsghfghfghfghdasd',5)
#lines_Counter()
Answer_Checker()