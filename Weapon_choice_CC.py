# cook your dish here
t=int(input())
for i in range(t):
    h,x,y1,y2,k=map(int,input().split())
    if h<=y1*k:
        if h%y1==0:
            res=h//y1
        else:
            res=h//y1+1
    else:
        k1=h-(y1*k)
        if k1%y2==0:
            res=k1//y2+k
        else:
            res=k1//y2+1+k
    if h%x==0:
        res1=h//x
    else:
        res1=h//x+1
    print(min(res1,res))
    
