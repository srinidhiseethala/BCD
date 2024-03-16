class Solution:
    def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        a.sort()
        min_abs_diff = float('inf')
        pairs = []
        for i in range(1, len(a)):
            abs_diff = a[i] - a[i-1]
            if abs_diff < min_abs_diff:
                min_abs_diff = abs_diff
                pairs = [[a[i-1], a[i]]]
            elif abs_diff == min_abs_diff:
                pairs.append([a[i-1], a[i]])

        return pairs
