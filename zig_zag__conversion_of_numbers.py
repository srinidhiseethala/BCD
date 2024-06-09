def zigZag(self, n : int, a : List[int]) -> None:
        # code here
        for i in range(len(a)-1):
            if i%2==0 and a[i]>a[i+1]:
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
            if i%2==1 and a[i]<a[i+1]:
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
        return 
                
