def rotateArr(self,a,d,n):
l=[]
if d%n==0:
    return a
else:
    for i in range(d,len(a)):
        l.append(a[i])
    for i in range(0,d+1):
        l.append(a[i])
return a
