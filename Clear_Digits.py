def clearDigits(self, s: str) -> str:
        c=0
        for i in s:
            if i.isalpha():
                c+=1
        if len(s)==c:
            return s
        else:
            while any(k.isdigit() for k in s):
                for j in range(len(s)):
                    if s[j].isdigit():
                        if i==0:
                            s=s[1:]
                        else:
                            s=s[:j-1]+s[j+1:]
                        break
            return s
        
