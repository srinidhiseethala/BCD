t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    m=0
    l=[]
    for i in a:
        if i>=k:
            l.append(i%k)
    if (len(l)==0):
        print(-1)
    else:
        print(min(l))
        
