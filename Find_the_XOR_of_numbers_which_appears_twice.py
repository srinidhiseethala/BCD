def duplicateNumbersXOR(self, n: List[int]) -> int:
        d={}
        l=[]
        for i in n:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]==2:
                l.append(i)
        a=0
        for i in l:
            a=i^a
        return a
