def countConsistentStrings(self, a: str, w: List[str]) -> int:
        a=set(a)
        c=0
        for i in w:
            for j in i:
                if j not in a:
                    c+=1
                    break
        return len(w)-c
