t=int(input())
for i in range(t):
    n=int(input())
    if n%2==0:
        if n%3==0:
            print((n//2),(n//3))
        else:
            print((n//2),(n//3)+1)
    else:
        if n%3==0:
            print(n//2+1,n//3)
        else:
            print(n//2+1,n//3+1)
