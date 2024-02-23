t=int(input())
for i in range(t):
    s=str(input())
    t=str(input())
    a=""
    for i in range(len(s)):
        if s[i]==t[i]:
            a+='G'
        else:
            a+='B'
    print(a)
