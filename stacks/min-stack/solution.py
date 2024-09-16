"""
design a stack that supports push, pop, top, and retrieving
the minimum element in constant time

MinStack()
- initializes the stack object

void push(int val)
- pushes the element val onto the stack

void pop()
- removes the element on the top of the stack

int top()
- gets teh top element of the stack

int getMin()
- retrieves the minimum element in the stack

example
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Result:
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2



Solution:
stacks can already add a value, pop a value, get top value in O(1) time

how can we get min value in O(1) time?
- to implement with O(n) time, just go through all numbers and track a max value

better implementation:
track the min value inside of the stack object WITH ANOTHER STACK
- the stack gets pushed the minimum value so far, if the next value added to the stack is smaller, then add that to the min stack
- now we can pop it (get the minimum value) in O(1) time
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # set the min to either val or top of min_stack if min_stack exists
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
