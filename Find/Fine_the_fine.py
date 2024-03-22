class Solution:
    def totalFine(self, n, d , car, fine):
        s=0
        if d%2==0:
            for i in range(len(car)):
                if car[i] %2!=0:
                    s+=fine[i]
        elif d%2!=0:
            for i in range(len(car)):
                if car[i]%2==0:
                    s+=fine[i]
        return s
                    
