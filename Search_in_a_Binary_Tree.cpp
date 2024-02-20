class Solution {
public:
    
    TreeNode* searchBST(TreeNode* root, int mydata) {
        if(root==NULL)
        {
            return NULL;
        }
        if(root->val==mydata)
        {
            return root;
        }
        else if(root->val>mydata)
        {
            root=root->left;
            return searchBST(root,mydata);

        }
        else if(root->val<mydata)
        {
            root=root->right;
            return searchBST(root,mydata);
        }
        return root;

    }
};
