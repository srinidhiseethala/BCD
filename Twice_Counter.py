class Solution:
    def countWords(self,a, n):
        #code here
        d={}
        c=0
        for i in a:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]==2:
                c+=1
        return c
