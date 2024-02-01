class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        m=max(candies)
        l=[]
        for i in candies:
            if i+extraCandies>=m:
                l.append(True)
            else:
                l.append(False)   
        return l     
