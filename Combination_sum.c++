class Solution {
public:
    void Combination(vector<int>arr,int t,int i,vector<vector<int>>&ans,int s,int n,vector<int>temp)
    {
        if(s==t)
        {
            ans.push_back(temp);
            return;
        }
        if(i>=n || s>t)
        {
            return;
        }
        Combination(arr,t,i+1,ans,s,n,temp);
        temp.push_back(arr[i]);
        Combination(arr,t,i,ans,s+arr[i],n,temp);

    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>>ans;
        vector<int>temp;
        Combination(candidates,target,0,ans,0,candidates.size(),temp);
        return ans;
    }
};
