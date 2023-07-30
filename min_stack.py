class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minimum = None

    def push(self, val):
        if len(self.stack) == 0:
            self.minimum = val
        else:
            if val < self.minimum:
                self.minimum = val
        self.stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.minimum and len(self.stack) > 0:
            self.minimum = min(self.stack)

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minimum
