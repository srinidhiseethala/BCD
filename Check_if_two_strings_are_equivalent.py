class Solution(object):
    def arrayStringsAreEqual(self, w1, w2):
        s1=""
        s2=""
        for i in w1:
            s1+=i
        for i in w2:
            s2+=i
        if s1==s2:
            return True
        else:
            return False

        
        
