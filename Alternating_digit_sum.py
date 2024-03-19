class Solution:
    def alternateDigitSum(self, n: int) -> int:
        a=str(n)
        s=0
        for i in range(len(a)):
            if i%2==0:
                s+=int(a[i])
            else:
                s-=int(a[i])
        return s        
