from typing import List

"""
You are keeping scores for a baseball game with strange rules.

At the beginning of the game, you start wth an empty record.

You are given a list of strings 'operations', where operations[i] is
the ith operation you must apply to the record and is one of the following

int x: record a new score of x
+: record a new score that is the sum of the previous two scores
D: record a new score that is the double of the previous score
C: invalidate the previous score, removing it from the record

remove the sum of all the scores on the record after applying the operations

example:

operations = ["5", "2", "C", "D", "+"]
output: 30

"5" - adds 5 to the record: [5]
"2" - adds 2 to the record: [5, 2]
"C" - remove the previous: [5]
"D" - add 2 * 5 = 10 to the record: [5, 10]
"+" - add 5 + 10 = 15 to the record: [5, 10, 15]

return the sum of this record after operations: [5, 10, 15] = 30

solution:
use stack to track score, since we are only foc
"""


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == "+":
                stack.append(stack[-1] + stack[-2])
            elif operation == "D":
                stack.append(stack[-1] * 2)
            elif operation == "C":
                stack.pop()
            else:
                stack.append(int(operation))

        return sum(stack)
