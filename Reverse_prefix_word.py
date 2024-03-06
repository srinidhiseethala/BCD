class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s1=""
        s2=""
        if ch not in word:
            return word
        else:
            ind=word.index(ch)
            for i in range(ind+1):
                s1=word[i]+s1
            for j in range(ind+1,len(word)):
                s2+=word[j]
        return s1+s2
        
