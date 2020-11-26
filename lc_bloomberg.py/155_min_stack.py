class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        curr = self.stack.pop()
        if curr == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]


"""
    need 2 stacks - one to always push and pop, one to push only when it's min value and pop when popped stack val == last value in min stack
    
    push:
        append val to stack
        if min_stack is empty or x <= min_stack[-1]: append x to min stack
    
    pop:
        save popped stack val as a var
        if save == last val in min stack: pop min stack
    
    top:
        return last val in stack if there's any
    
    getmin:
        return last val in min stack if there's any

"""


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
