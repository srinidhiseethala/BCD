class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)
        if n%2==0:
            res=(nums1[(n-1)//2]+nums1[(n-1)//2+1])/2
            return res
        else:
            res=(nums1[(n-1)//2])
            return res
        
