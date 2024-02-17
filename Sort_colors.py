class Solution(object):
    def sortColors(self, n):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                if n[i]>=n[j]:
                    temp=n[i]
                    n[i]=n[j]
                    n[j]=temp
                     
