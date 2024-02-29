class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        maxx=math.prod(nums[-2:])
        minn=math.prod(nums[:2])
        return maxx-minn
        
