class Solution(object):
    def defangIPaddr(self, a):
        """
        :type address: str
        :rtype: str
        """
        l=[]
        for i in range(len(a)):
            l.append(a[i])
        i=0
        while(i<len(l)):
            if l[i]==".":
                l.insert(i,"[")
                l.insert(i+2,"]")
                i=i+2
            else:
                i=i+1
        return "".join(l)
        
