def differenceOfSum(self, nums: List[int]) -> int:
        es=sum(nums)
        ds=0
        s=''
        for i in nums:
            s+=str(i)
        for i in s:
            ds+=int(i)
        return abs(es-ds)
