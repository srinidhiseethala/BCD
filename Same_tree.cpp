class Solution {
public:

    bool ans=true;
    void inorder(TreeNode *p,TreeNode *q)
    {
        if(p==NULL && q!=NULL) ans=false;
        if(p!=NULL && q==NULL) ans=false;
        if(p==NULL) return;
        if(q==NULL) return;
        if(p->val!=q->val)
        {
            ans=false;
        }
        inorder(p->left,q->left);
        inorder(p->right,q->right);
    }
    bool isSameTree(TreeNode* p, TreeNode* q) {
        inorder(p,q);
        return ans;                
    }
};
