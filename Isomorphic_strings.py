def isIsomorphic(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]]=t[i]
            else:
                if d1[s[i]]!=t[i]:
                    return False
        for j in range(len(t)):
            if t[j] not in d2:
                d2[t[j]]=s[j]
            else:
                if d2[t[j]]!=s[j]:
                    return False
        return True
