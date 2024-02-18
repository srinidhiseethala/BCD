class Solution {
public:
    void depth(TreeNode* root,int &m,int level)
    {
        if(root==NULL)
        {
            return;
        }
        if(level>m)
        {
            m=level;
        }
        depth(root->left,m,level+1);
        depth(root->right,m,level+1);
    }
    int maxDepth(TreeNode* root) {
        int m=0;
        int level=1;
        depth(root,m,level);
        return m;
    }
};
