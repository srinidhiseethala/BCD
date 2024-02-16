class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int i=0;
        int j=0;
        int m=0;
        for(i=0;i<nums.size();i++)
        {
            if(nums[i]==0)
            {
                k--;
            }
            while(k<0)
            {
                if(nums[j]==0)
                {
                    k++;
                }
                j+=1;
            }
            m=max(m,(i-j+1));
        }
        return m;
    }
};
