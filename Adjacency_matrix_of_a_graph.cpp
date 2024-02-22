#include<bits/stdc++.h>
using namespace std;
class Node
{
    public:
	int data;
	Node* left;
	Node* right;
	Node(int data)
	{
		this->data=data;
		this->left=NULL;
		this->right=NULL;
	}
};
void adjacency(Node* root,map<int,vector<int>>&m)
{
	if(root==NULL)
	{
		return;
	}
	if(root->left!=NULL)
	{
		m[root->data].push_back(root->left->data);
		m[root->left->data].push_back(root->data);
	}
	if(root->right!=NULL)
	{
		m[root->data].push_back(root->right->data);
		m[root->right->data].push_back(root->data);
	}
	adjacency(root->left,m);
	adjacency(root->right,m);
}
void createTree(Node* root,vector<int>v,int i,int n)
{
	if(i*2+1>=n)
	{
		return;
	}
	if(2*i+1<n)
	{
		Node* a=new Node(v[2*i+1]);
		root->left=a;
	}
	if(2*i+2<n)
	{
		Node* b=new Node(v[2*i+2]);
		root->right=b;
	}
	createTree(root->left,v,2*i+1,n);
	createTree(root->right,v,2*i+2,n);
	
}
int main()
{
	vector<int>v={10,20,30,40,50};
	Node* x=new Node(v[0]);
	createTree(x,v,0,v.size());
	map<int,vector<int>>m;
	adjacency(x,m);
	for(auto it:m)
	{
		cout<<it.first<<"   ";
		vector<int>res=it.second;
		for(int i=0;i<res.size();i++)
		{
			cout<<res[i]<<" "; 
		}
		cout<<endl;
	}
}
