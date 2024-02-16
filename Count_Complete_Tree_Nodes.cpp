
class Solution {
public:
    void mycount(TreeNode * root,vector<int>&v)
    {
        if(root==NULL)
        {
            return;
        }
        mycount(root->left,v);
        v.push_back(root->val);
        mycount(root->right,v);

    }
    int countNodes(TreeNode* root) {
        vector<int>v;
        mycount(root,v);
        return v.size();
    }
};
