def prefixDistinct(self, n : int, a : List[int]) -> List[int]:
        # code here
        
        # for i in range(len(a)):
        #     l.append(len(list(set(a[:i+1]))))
        # return l
        l=[]
        d={}
        for i in a:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            l.append(len(d))
        return l
