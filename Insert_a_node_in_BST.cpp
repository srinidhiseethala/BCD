class Solution
{
    public:
        void BSTinsert(Node* root,int d)
        {
            if(root->data==d)
            {
                return;
            }
            if(root->data>d)
            {
                if(root->left==NULL)
                {
                    root->left=new Node(d);
                    return;
                }
                else
                {
                    return BSTinsert(root->left,d);
                }
            }
            else if(root->data<d)
            {
                if(root->right==NULL)
                {
                    root->right=new Node(d);
                    return;
                }
                else
                {
                    return BSTinsert(root->right,d);
                }
            }
            return;
            
        }
        Node* insert(Node* node, int d) {
        
            // Your code goes here
            BSTinsert(node,d);
            return node;
    }

};
