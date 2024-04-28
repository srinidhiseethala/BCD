def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        a=sum(nums1)
        b=sum(nums2)
        return (b-a)//len(nums1)  
