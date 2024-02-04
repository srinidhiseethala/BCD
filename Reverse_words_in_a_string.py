class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s.split()
        b=a[::-1]
        s1=""
        for i in range(len(b)):
            s1=s1+b[i]
            if i+1!=len(b):
                s1+=" "
        return s1
