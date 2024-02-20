import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    l=[]
    rows=len(players.index)
    columns=len(players.columns)
    l.append(rows)
    l.append(columns)
    return l
