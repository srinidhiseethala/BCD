n=int(input())
for i in range(n):
    a=int(input())
    s=input()
    res=s.rindex('B')-s.index('B')+1
    print(res)
