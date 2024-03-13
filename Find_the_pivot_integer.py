class Solution(object):
    def pivotInteger(self, n):
        l=[]
        for i in range(1,n+1):
            l.append(i)
        t=0
        s=sum(l)
        for i in l:
            if s-i==t:
                return i
            s=s-i
            t+=i
        else:
            return -1
        
        
