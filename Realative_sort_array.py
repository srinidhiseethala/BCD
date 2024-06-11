def relativeSortArray(self, a1: List[int], a2: List[int]) -> List[int]:
        l1=[]
        l2=[]
        for i in a2:
            if i in a1:
                c1=a1.count(i)
                for j in range(c1):
                    l1.append(i)
        for i in a1:
            if i not in a2:
                l2.append(i)
        l2.sort()
        for i in l2:
            l1.append(i)
        return l1

        
