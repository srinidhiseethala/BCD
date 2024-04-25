
def isAcronym(self, words: List[str], s: str) -> bool:
    a=""
    for i in range(len(words)):
        a+=words[i][0]
    if a==s:
        return True
    else:
        return False
        
