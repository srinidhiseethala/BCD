class Solution(object):
    def maximumOddBinaryNumber(self, s):
        r=""
        for i in s:
            a=s.count('1')
            b=s.count('0')
        for i in range(a-1):
            r+='1'
        for i in range(b):
            r+='0'
        return r+'1'

        
