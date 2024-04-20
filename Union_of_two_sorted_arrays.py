def findUnion(self,arr1,arr2,n,m):
        res=list(set(arr1)|set(arr2))
        return sorted(res)
