def find(self, a, n, x):
        l=[]
        p=[]
        for i in range(len(a)):
            if a[i]==x:
                l.append(i)
                break
        for j in range(len(a)-1,-1,-1):
            if a[j]==x:
                l.append(j)
                break
        if len(l)!=0:
            return l
        else:
            p.append(-1)
            p.append(-1)
            return p
