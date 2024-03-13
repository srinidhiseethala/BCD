class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=[]
        for i in d:
            if d[i]>=2:
                for j in range(2):
                    l.append(i)
            else:
                l.append(i)
        for i in range(len(l)):
            nums[i]=l[i]
        return len(nums)-(len(nums)-len(l))
        
