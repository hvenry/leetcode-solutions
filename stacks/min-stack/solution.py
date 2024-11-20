"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack(): initializes the stack object
- void push(int val): pushes the element val onto the stack
- void pop(): removes the element on the top of the stack
- int top(): gets the top element of the stack
- int getMin(): retrieves the minimum element in the stack

Example:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

returns: [null,null,null,null,-3,null,0,-2]

Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();                  // return -3
minStack.pop();
minStack.top();                     // return 0
minStack.getMin();                  // return -2


Solution:
- Stacks can already add a value, pop a value, get top value in O(1) time.
- To implement min_value with with O(n) time, just go through all numbers and track a max value.

    - O(1) IMPROVEMENT: Track the min value inside of the stack object WITH ANOTHER STACK
        - if there is no min_stack, set the min to val
        - if there is a min_stack, set the min to min(val, self.min_stack[-1]
        - we can now get the min value by popping the min_stack, O(1) time

Complexity
- Time: O(1)
- Space: O(n) -> size of stack
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
