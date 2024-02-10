class Solution {
public:
    void btrightview(TreeNode* root,map<int,int>&m,vector<int>&v,int levelcount)
    {
        if(root==NULL)
        {
            return;
        }
        if(m[levelcount]==0)
        {
            v.push_back(root->val);
            m[levelcount]=1;
        }
        btrightview(root->right,m,v,levelcount+1);
        btrightview(root->left,m,v,levelcount+1);

    }
    vector<int> rightSideView(TreeNode* root) {
        map<int,int>m;
        vector<int>v;
        btrightview(root,m,v,0);
        return v;
    }
};
