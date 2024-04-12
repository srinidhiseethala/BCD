def trappingWater(self, arr,n):
        #Code here
        m=0
        m1=[]
        m2=[]
        for i in arr:
            if i>=m:
                m=i
            m1.append(m)
        m=0
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>m:
                m=arr[i]
            m2.append(m)
        m2=m2[::-1]
        s=0
        for i in range(len(arr)):
            if arr[i]<m1[i] and arr[i]<m2[i]:
                s+=min(m1[i],m2[i])-arr[i]
        return s
            
           
                
                
            
            
            
