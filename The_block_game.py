t=int(input())
for i in range(t):
    n=int(input())
    a=str(n)
    if a==a[::-1]:
        print("wins")
    else:
        print("loses")
