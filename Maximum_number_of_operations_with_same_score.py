class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        a=nums[0]+nums[1]
        c=0
        while(len(nums)>1):
            s=nums[0]+nums[1]
            if s==a:
                c+=1
                nums.remove(nums[0])
                nums.remove(nums[0])
            else:
                break
        return c

        
        
