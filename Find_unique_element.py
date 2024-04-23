def findUnique(self, a, n, k): 
        #Code here
        d={}
        for i in a:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]%k!=0:
                return i
        return -1
