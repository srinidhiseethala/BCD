def countOccurence(self,arr,n,k):
        d={}
        c=0
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=n//k
        for i in d:
            if d[i]>l:
                c+=1
        return c
