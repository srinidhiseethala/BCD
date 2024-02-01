def checkPangram(self,s):
        #code here
        a=set()
        s=s.lower()
        for i in s:
            if i.isalpha():
                a=a.union(i)
        if len(a)==26:
            return 1
        else:
            return 0
                
