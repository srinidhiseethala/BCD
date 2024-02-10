class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        int c=0;
        ListNode *temp=head;
        ListNode *prev;
        while(temp!=NULL)
        {
            c+=1;
            temp=temp->next;
        }
        int a=c/2;
        if(head==NULL || head->next==NULL)
        {
            return NULL;
        }
        ListNode *temp1=head;
        for(int i=0;i<a;i++)
        {
            prev=temp1;
            temp1=temp1->next;
        }
        prev->next=temp1->next;
        temp1->next=NULL;
        return head;
    }
};
