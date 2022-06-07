s = input()
sr= input()
srr=[sr[k] for k in range(0,len(sr))]
for i in range(0,int(len(sr)/2)):
    srr[i] = sr[len(sr)-i-1]
    srr[len(sr) - i - 1] = sr[i]
sr = ''.join(srr)
if sr==s : print('YES')
else: print("NO")
