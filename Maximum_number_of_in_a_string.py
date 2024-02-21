class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        l=[]
        for i in sentences:
            a=i.split()
            l.append(len(a))
        return max(l)
        
