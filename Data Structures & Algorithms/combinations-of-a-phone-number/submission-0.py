class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return []
        ans = []
        def backtrack(i, cur):
            if len(cur) >= len(digits):
                s = "".join(cur)
                ans.append(s)
                return
            digit = digits[i]
            for c in digitToChar[digit]:
                cur.append(c)
                backtrack(i+1, cur)
                cur.pop()
        
        backtrack(0, [])
        return ans