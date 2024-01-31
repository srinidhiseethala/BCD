t=int(input())
for i in range(t):
    p,l=map(int,input().split())
    res=(l/p)
    if res>=0.75:
        print("YES")
    else:
        print("NO")
