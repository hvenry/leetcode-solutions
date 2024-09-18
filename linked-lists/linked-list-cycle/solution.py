from typing import Optional

"""
given head, the head of a linked list, determine if the linked list has a cycle.

there is a cycle in a linked list if there is some node in the list that can be reached again by continuously
following the next pointer.

internally, 'pos' is used to denote the index of the node that tail's 'next' pointer is connected to.

return True if there is a cycle in the linked list, otherwise return false.

example:
head = [3, 2, 0, -4], pos = 1
3 --> 2 --> 0 --> -4
    also: -4 --> 2

returns True (cycle from -4 to 2)

solution:
use a hashset to see if any nodes are revisited
- time O(n), space O(n)

NOT OPTIMAL


Floyd's Tortoise & Hare
- have a slow pointer 's' and a fast pointer 'f'
- slow pointer is shifted by 1, fast pointer is shifted by 2

if fast pointer gets to null first, then there is not a cycle.
if the pointers meet, then there is a cycle.

- time O(n), space O(1)
    This is because, the gap is being closed by -1 on each iteration (2 - 1 = -1)
    The gap is at max n-1 length, and it will take roughly n iterations to catch up (-1)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
