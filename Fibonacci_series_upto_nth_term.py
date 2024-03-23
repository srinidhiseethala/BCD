def series(self, n):
        l=[]
        l.append(0)
        l.append(1)
        for i in range(0,n-1):
            a=l[i]+l[i+1]
            l.append(a%(10**9+7))
        return l
