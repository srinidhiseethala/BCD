class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>>res;
        if(root==NULL)
        {
            return res;
        }
        queue<TreeNode*>q;
        q.push(root);
        while(q.empty()==false)
        {
            int levelsize=q.size();
            vector<int>v;
            for(int i=0;i<levelsize;i++)
            {
                TreeNode* temp=q.front();
                q.pop();
                v.push_back(temp->val);
                if(temp->left!=NULL)
                {
                    q.push(temp->left);
                }
                if(temp->right!=NULL)
                {
                    q.push(temp->right);
                }
            }
            res.push_back(v);
        }
        return res;
    }
};
