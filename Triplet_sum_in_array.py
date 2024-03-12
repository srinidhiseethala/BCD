class Solution:
    def find3Numbers(self,A, n, X):
        A.sort()
        for i in range(len(A)):
            j=i+1
            k=len(A)-1
            while(j<k):
                if A[j]+A[k]==X-A[i]:
                    return 1
                elif A[j]+A[k]<X-A[i]:
                    j+=1
                else:
                    k-=1
        return 0
            
