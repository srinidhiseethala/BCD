def findLatestTime(self, s: str) -> str:
        l = list(s)
        if l[0] == "?":
            l[0] = "1" if l[1] == "?" or int(l[1]) <= 1 else "0"
        if l[1] == "?":
            l[1] = "1" if l[0] == "1" else "9"
        if l[3] == "?":
            l[3] = "5"
        if l[4] == "?":
            l[4] = "9"
        return "".join(l)
