""" 
Implement a stack, which can support push, pop operations,
and get the smallest item, with time complexity of O(1).

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();
minStack.pop();
minStack.top();
minStack.getMin();
--> Returns 0.
--> Returns -2.

Thought: Need two stacks, one to keep minimun item.
"""


class MinStack(object):
    def __init__(self):
        self.stack = []  # for normal operations
        self.minStack = []  # for min item

    def push(self, x):
        self.stack.append(x)
        if not self.minStack:
            self.minStack.append(x)
        else:
            if self.minStack[-1] >= x:
                self.minStack.append(x)

    def pop(self):
        res = []
        if self.minStack:
            if self.minStack[-1] == self.stack[-1]:
                res.append(self.minStack.pop())
            res.append(self.stack.pop())
        return res

    def top(self):
        if self.stack:
            return self.stack[-1]  # get item, not remove

    def getMin(self):
        if self.minStack:
            return self.minStack[-1]  # get item, not remove


minStack = MinStack()
minStack.push(4)
minStack.push(5)
minStack.push(1)
minStack.push(3)
print(minStack.getMin() == 1)
print(minStack.pop())
print(minStack.pop())
print(minStack.top() == 5)

# Output
# True
# [3]
# [1, 1]
# True
