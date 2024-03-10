import math
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x*x==2*y:
        print("YES")
    else:
        print("NO")
