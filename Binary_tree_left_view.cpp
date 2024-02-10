void lview(Node* root,map<int,int>&m,vector<int>&v,int levelcount)
{
    if(root==NULL)
    {
        return;
    }
    if(m[levelcount]==0)
    {
        v.push_back(root->data);
        m[levelcount]=1;
    }
    lview(root->left,m,v,levelcount+1);
    lview(root->right,m,v,levelcount+1);
}
vector<int> leftView(Node *root)
{
   // Your code here
   map<int,int>m;
   vector<int>v;
   lview(root,m,v,0);
   return v;
   
}
