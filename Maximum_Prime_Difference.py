def maximumPrimeDifference(self, a: List[int]) -> int:
        def isprime(n):
            if n<=1:
                return False
            for i in range(2,n//2+1):
                if n%i==0:
                    return False
            return True
        l=[]
        for i in range(len(a)):
            if isprime(a[i]):
                l.append(i)
        return abs(l[0]-l[-1])
            
