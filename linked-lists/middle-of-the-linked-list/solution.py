from typing import Optional

"""
given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

example:
head = [1, 2, 3, 4, 5]
res: [3, 4, 5]

this is because the middle node is '3', the rest is returned with 3 because they are linked.

use the Floyd's tortoise and hare algorithm.
- two pointers fast and slow traverse linked list
- fast moves 2 spaces, slow moves 1
- when fast pointer reaches the end, return the slow pointer (this is the middle of the list)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
