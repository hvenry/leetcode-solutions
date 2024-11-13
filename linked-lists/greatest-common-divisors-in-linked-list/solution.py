"""
Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greates common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer taht evenly divides both numbers.

Example:
18 -> 6 -> 10 -> 3

Turns into
18 -> 6 -> 6 -> 2 -> 10 -> 1 -> 3

6 is the GCD for 18 and 6, 2 is the GCD for 6 and 10, 1 is the GCD for 10 and 3.

Solution:
Use prev and cur pointers, and set a 'g' node inbetween them to be the gcd of the 2 values, then shift up the pointers.

Time Complexity:
- O(n * (complexity of gcd function))
- Space: O(1) -> we are not using any space
"""

from typing import Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev = head
        cur = head.next

        while cur:
            gcd = math.gcd(cur.val, prev.val)
            g = ListNode(gcd)

            prev.next = g
            g.next = cur

            # move pointers over
            prev = cur
            cur = cur.next

        return head
