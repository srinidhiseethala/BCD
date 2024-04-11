def removeKdigits(self, n: str, k: int) -> str:
        l=[]
        for i in n:
            while k>0 and l and l[-1]>i:
                l.pop()
                k-=1
            l.append(i)
        if k>0:
            l=l[:-k]
        s=''.join(l).lstrip('0')
        return s if s else '0'
