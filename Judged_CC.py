# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d,e=map(int,input().split())
    if (a+b+c+d+e)>=4:
        print("YES")
    else:
        print("NO")
