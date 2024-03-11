class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d={}
        a=""
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in order:
            if i in d:
                a+=i*d[i]
                del d[i]
        for i in d:
            a+=i*d[i]
        return a
        
