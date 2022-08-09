s= input()
i=0
ans=''
while(i<len(s)):
    if s[i]=='.':
        ans+='0'
        i+=1
        continue
    if s[i+1]=='.':
        ans+='1'
        i+=2
        continue
    ans+='2'
    i+=2
print(ans)

