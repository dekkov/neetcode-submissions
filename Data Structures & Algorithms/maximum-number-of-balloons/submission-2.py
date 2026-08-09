class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        balloon = Counter("balloon")
        freq = Counter(text)
        res = float('inf')
        for letter, needed in balloon.items():
            res = min(res, freq[letter] // needed)
        
        return res
