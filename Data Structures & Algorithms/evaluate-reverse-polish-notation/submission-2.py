class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        final = []
        for num in tokens:
            if num == "+" :
                num_1 = int(final.pop())
                num_2 = int(final.pop())
                function = num_2 + num_1
                final.append(function)
            elif num == "-" :
                num_1 = int(final.pop())
                num_2 = int(final.pop())
                function = num_2 - num_1
                final.append(function)
            elif num == "*" :
                num_1 = int(final.pop())
                num_2 = int(final.pop())
                function = num_2 * num_1
                final.append(function)
            elif num == "/":
                num_1 = int(final.pop())
                num_2 = int(final.pop())
                function = num_2 / num_1
                final.append(int(function))
            else:
                final.append(int(num))
        return final[0]


        