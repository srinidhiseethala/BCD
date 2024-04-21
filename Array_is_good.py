def isGood(self, nums: List[int]) -> bool:
        n=len(nums)
        l=[]
        for i in range(1,n):
            l.append(i)
        l.append(n-1)
        if sorted(nums)==l:
            return True
        else:
            return False
