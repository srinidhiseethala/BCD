class Solution {
public:
    int maxDepth(string s) {
        stack<char>st;
        vector<int>v;
        int i=0;
        int pc=0;
        int nc=0;
        for(i=0;i<s.size();i++)
        {
            if(s[i]=='(')
            {
                pc+=1;
            }
            else
            {
                nc+=1;
            }
        }
        if(pc==0 && nc!=0)
        {
            return 0;
        }
        else if(nc==0 && pc!=0)
        {
            return pc;
        }
        else
        {
            for(i=0;i<s.size();i++)
            {
                if(s[i]=='(')
                {
                    st.push(s[i]);
                }
                else if(s[i]==')')
                {
                    v.push_back(st.size());
                    if(!st.empty() && st.top()=='(')
                    {
                        st.pop();
                    }
                }
            }
            return *max_element(v.begin(), v.end());    
        }
    }
};
