def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        a=next(iter(d.values()))
        for i in d.values():
            if i!=a:
                return False
        return True
