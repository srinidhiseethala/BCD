def minRow(self,n,m,a):
        #code here
        l=[]
        for i in a:
            c=i.count(1)
            l.append(c)
        m=min(l)
        res=l.index(m)
        return res+1
