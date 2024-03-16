class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(i):
            s=list(str(i))
            m=max(s)
            res=[m]*len(s)
            a=int("".join(res))
            return a
            
        s=0
        for i in nums:
            s+=encrypt(i)
        return s
    
        
