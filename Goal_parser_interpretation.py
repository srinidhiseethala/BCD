class Solution:
    def interpret(self, c: str) -> str:
        s=""
        for i in range(len(c)):
            if c[i]=='G':
                s+=c[i]
            else:
                if c[i]=='(':
                    if c[i+1]==')':
                        s+='o'
                    elif c[i+1]=='a' and c[i+2]=='l':
                        s+='al'
        return s
