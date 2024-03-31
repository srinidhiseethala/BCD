def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        a=str(x)
        s=0
        for i in range(len(a)):
            s+=int(a[i])
        if x%s==0:
            return s
        else:
            return -1
