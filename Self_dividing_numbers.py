class Solution:
    def selfDividingNumbers(self, l: int, r: int) -> List[int]:
        res=[]
        for i in range(l,r+1):
            c=0
            a=str(i)
            if '0' not in a:
                for j in range(len(a)):
                    if i%int(a[j])==0:
                        c+=1
                if c==len(a):
                    res.append(i)
        return res

        
