n=int(input())
a=list(map(int,input().split()))
x=int(input())
y=int(input())
s=0
for i in range(x,y+1):
    s+=a[i]
print(s)
