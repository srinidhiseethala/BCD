class Solution(object):
    def restoreString(self, s, a):
        res=""
        for i in range(len(a)):
            res+=s[a.index(i)]
        return res
