class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        def fun(k):
                s="123456789"
                l=[]
                for j in range(0,len(s)-k+1):
                    a=""
                    for p in range(0,k):
                        a+=s[j+p]
                    l.append(a)
                return l
        l=str(low)
        h=str(high)
        lst=[]
        for i in range(len(l),len(h)+1):
            lst.append(fun(i))
        res=set()
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                a=int(lst[i][j])
                if a>=low and a<=high:
                    res.add(a)
        return sorted(res)
        
