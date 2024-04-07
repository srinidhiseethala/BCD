def modify(self, s):
        # code here
        v="aeiouAEIOU"
        a=""
        for i in s:
            if i in v:
                a+=i
        A=reversed(a)
        b=""
        for i in s:
            if i not in v:
                b+=i
            else:
                for i in A:
                    b+=i
                    break
        return b
