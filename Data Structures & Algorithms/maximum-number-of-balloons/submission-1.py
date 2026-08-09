from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        string = "balloon"
        count = Counter(string)
        cur_count = Counter(text)

        ans = 10000

        for c in string:
            ans = min(ans, cur_count[c] // count[c])
        return ans

        
        