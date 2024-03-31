def delAlternate (ob, S):
        a=""
        for i in range(len(S)):
            if i%2==0:
                a+=S[i]
        return a
