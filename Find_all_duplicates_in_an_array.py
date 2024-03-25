def findDuplicates(self, n):
        l=[]
        d={}
        for i in n:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]==2:
                l.append(i)
        return l
        
