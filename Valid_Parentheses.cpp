class Solution {
public:
    bool isValid(string s) {
        stack<char>st;
        int i=0;
        for(i=0;i<s.size();i++)
        {
            if(s[i]=='('||s[i]=='{'||s[i]=='[')
            {
                st.push(s[i]);
            }
            else
            {
                if(s[i]==')')
                {
                    if(!st.empty() && st.top()=='(')
                    {
                        st.pop();
                    }
                    else
                    {
                        return false;
                        break;
                    }
                }
                else if(s[i]=='}')
                {
                    if(!st.empty() && st.top()=='{')
                    {
                        st.pop();
                    }
                    else
                    {
                        return false;
                        break;
                    }
                }
                else
                {
                    if(!st.empty() && st.top()=='[')
                    {
                        st.pop();
                    }
                    else{
                        return false;
                        break;
                    }
                }
            }
        }
        if(i==s.size() && st.empty()==true)
        {
            return true;
        }
        return false;
    }
};
