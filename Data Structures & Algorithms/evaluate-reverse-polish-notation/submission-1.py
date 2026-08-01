class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        ops = ["+", "*", "-", "/"]
        for s in tokens:
            if s not in ops:
                stack.append(int(s))
                continue
            if s == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1+num2)
            
            elif s == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1*num2)
            
            elif s == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2-num1)
            
            elif s == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
        return stack[0]
