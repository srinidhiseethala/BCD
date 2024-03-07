class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, a, N, P):
        # code here
        d={}
        for i in range(len(a)):
            if a[i] not in d:
                d[a[i]]=1
            else:
                d[a[i]]+=1
        for i in range(1,N+1):
            if i not in d:
                a[i-1]=0
            else:
                a[i-1]=d[i]
