class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        ListNode *temp=head->next;
        int s=0;
        ListNode *res=new ListNode(0);
        ListNode* temp1=res;
        while(temp)
        {
            if(temp->val!=0)
            {
                s+=temp->val;
            }
            else
            {
                ListNode *a=new ListNode(s);
                while(temp1->next!=NULL)
                {
                    temp1=temp1->next;
                }
                temp1->next=a;
                s=0;
            }
            temp=temp->next;
        }
        return res->next;
    }
};
