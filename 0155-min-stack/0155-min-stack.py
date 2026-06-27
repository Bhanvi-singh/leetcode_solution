class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, value):
        self.stack.append(value)

        if len(self.min_stack) == 0 or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) == 0:
            return "stack is empty"
        x = self.stack.pop()
        if x ==  self.min_stack[-1]:
             self.min_stack.pop()
        return x
    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return "stack is empty"
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return "stack is empty"
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()