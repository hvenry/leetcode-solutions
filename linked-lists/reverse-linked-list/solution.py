from typing import Optional

"""
given the head of a singly linked list, reverse the list, and return the reversed list.

Solution:
How to reverse a linked list (reverse pointers)

1 --> 2 --> 3 
turns into
1 <-- 2  <-- 3
that is a reversed list!

- Use three pointer: curr, prev and next
- traverse all nodes of linked list (from current)
- store next node
- reverse current nodes pointer (point current.next to prev)
- move both pointers PREVIOUS and CURRENT to the next posision

Complexity:
Time O(n)
Space O(1)
"""


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            # store next node
            next_node = curr.next

            # reverse current nodes pointer
            curr.next = prev

            # move both pointers one position ahead
            prev = curr
            curr = next_node

        return prev
