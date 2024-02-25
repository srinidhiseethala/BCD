def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
for i in range(n,0,-1):
    if n%i==0:
        if isprime(i)==1:
            print(i)
            break
