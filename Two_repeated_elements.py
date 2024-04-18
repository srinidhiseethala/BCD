def twoRepeated(self, arr , n):
        #Your code here
        a=set()
        l=[]
        for i in arr:
            if i in a:
                l.append(i)
            else:
                a.add(i)
        return l
