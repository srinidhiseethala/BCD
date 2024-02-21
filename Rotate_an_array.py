class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l=[]
        a=len(nums)
        k=(a-k)%a
        for i in range(k,len(nums)):
            l.append(nums[i])
        for i in range(0,k):
            l.append(nums[i])
        for i in range(a):
            nums[i]=l[i]
        return;


        
