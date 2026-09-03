class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        For every open parentheses left we can either use it or skip
        If no open parentheses left we have to use close parentheses
        """
        ans = []
        cur = []
        def backtrack(opens, closes):
            if not closes:
                ans.append("".join(cur))
            
            if opens:
                cur.append("(")
                backtrack(opens - 1, closes)
                cur.pop()

            if opens < closes:
                cur.append(")")
                backtrack(opens, closes-1)
                cur.pop()
        backtrack(n,n)
        return ans