class Solution {
public:
    void lview(TreeNode* root,map<int,int>&m,vector<int>&v,int c)
    {
        if(root==NULL)
        {
            return;
        }
        if(m[c]==0)
        {
            v.push_back(root->val);
            m[c]=1;
        }
        lview(root->left,m,v,c+1);
        lview(root->right,m,v,c+1);
    }
    int findBottomLeftValue(TreeNode* root) {
        map<int,int>m;
        vector<int>v;
        lview(root,m,v,0);
        return v[v.size()-1];
    }
};
