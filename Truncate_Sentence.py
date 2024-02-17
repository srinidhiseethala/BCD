class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        a=s.split()
        s1=""
        for i in range(0,k):
            s1+=a[i]
            if i+1!=k:
                s1+=" "
        return s1

        
        
