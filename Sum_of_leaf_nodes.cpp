class Solution
{
    public:
        /*You are required to complete below method */
        void leafsum(Node* root,int &s)
        {
            if(root==NULL)
            {
                return;
            }
            if(root->left==NULL && root->right==NULL)
            {
                s+=root->data;
            }
            leafsum(root->left,s);
            leafsum(root->right,s);
        }
        int sumOfLeafNodes(Node *root ){
             /*Your code here */
             int s=0;
             leafsum(root,s);
             return s;
        }
};
