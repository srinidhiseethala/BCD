def leftRightDifference(self, n: List[int]) -> List[int]:
        a=[]
        b=[]
        res=[]
        s1=0
        s2=0
        for i in n:
            a.append(s1)
            s1+=i
        for i in range(len(n)-1,-1,-1):
            b.append(s2)
            s2+=n[i]
        b.reverse()
        for i in range(len(a)):
            res.append(abs(a[i]-b[i]))
        return res
