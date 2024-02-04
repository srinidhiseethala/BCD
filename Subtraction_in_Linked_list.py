class Solution:
    def subLinkedList(self, l1, l2): 
        # Code here
        # return head of difference list
        s1=""
        s2=""
        while(l1):
            s1+=str(l1.data)
            l1=l1.next
        while(l2):
            s2+=str(l2.data)
            l2=l2.next
        d=str(abs(int(s1)-int(s2)))
        head=Node(0)
        temp=head
        for i in range(0,len(d)):
            temp.next=Node(int(d[i]))
            temp=temp.next
        return head.next
