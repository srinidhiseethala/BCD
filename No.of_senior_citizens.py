class Solution:
    def countSeniors(self, d : List[str]) -> int:
        c=0
        l=[]
        for i in d:
            l.append(i[11:13])
        for i in l:
            if int(i)>60:
                c+=1
        return c
        
