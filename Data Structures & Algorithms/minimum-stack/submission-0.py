class MinStack:

    def __init__(self):
        self.stack = [] # val, min

    def push(self, val: int) -> None:
        if not self.stack:
            cur_min = val
        
        else:
            cur_min = min(val, self.stack[-1][1])
        
        self.stack.append([val, cur_min])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
