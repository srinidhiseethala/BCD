class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]>=2:
                l.append(i)
                a=len(nums)
                nums.remove(i)
        s1=a*(a+1)//2
        s2=sum(nums)
        l.append(s1-s2)
        return l

        
