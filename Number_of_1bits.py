class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        while n:
            c+=n&1
            n=n>>1
        return c
        
