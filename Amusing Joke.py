s2 = list(input()) +list(input())
st = list(input())

if len(s2)!=len(st) : print('NO')
else:
    s2.sort()
    st.sort()
    if s2 != st : print('NO')
    else:
        print('YES')
