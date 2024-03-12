class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        l=[]
        res=""
        for i in a:
            i=i[::-1]
            l.append(i)
        for i in range(len(l)):
            res+=l[i]
            if i+1!=len(l):
                res+=" "
        return res
