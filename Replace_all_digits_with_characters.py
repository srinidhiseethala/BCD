def replaceDigits(self, s: str) -> str:
        res=''
        for i in range(len(s)):
            if s[i].isalpha():
                res+=s[i]
            else:
                num=ord(s[i-1])+int(s[i])
                res+=chr(num)
        return res
