class Solution:
    def maxProfit(self, p: List[int]) -> int:
        s=0
        minn=p[0]
        for i in range(1,len(p)):
            if p[i]<minn:
                minn=p[i]
            else:
                s=max(s,p[i]-minn)
        return s
