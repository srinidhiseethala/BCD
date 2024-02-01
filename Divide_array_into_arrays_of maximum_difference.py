class Solution:
    def divideArray(self, n: List[int], k: int) -> List[List[int]]:
        lst=[] 
        n.sort()
        if len(n)%3==0:
            for i in range(0,len(n),3):
                l=[]
                if abs(n[i]-n[i+1])<=k and abs(n[i]-n[i+2])<=k:
                    l.append(n[i])
                    l.append(n[i+1])
                    l.append(n[i+2])
                else:
                    return []
                lst.append(l)
            return lst
        return l
                



        
        
