class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int c1=0;
        int c2=0;
        ListNode *temp1=headA;
        ListNode *temp2=headB;
        while(temp1!=NULL)
        {
            c1+=1;
            temp1=temp1->next;
        }
        while(temp2!=NULL)
        {
            c2+=1;
            temp2=temp2->next;
        }
        int d=abs(c1-c2);
        ListNode *mynode;
        if(c1>=c2)
        {
            mynode=headA;
        }
        else
        {
            mynode=headB;
        }
        while(d)
        {
            mynode=mynode->next;
            d--;
        }
        if(c1>=c2)
        {
            while(mynode!=NULL && headA!=NULL)
            {
                if(mynode==headB)
                {
                    return mynode;
                }
                mynode=mynode->next;
                headB=headB->next;
            }
        }
        else
        {
            while(mynode!=NULL && headB !=NULL)
            {
                if(mynode==headA)
                {
                    return mynode;
                }
                mynode=mynode->next;
                headA=headA->next;
            }
        }
        return NULL;
    }
};
