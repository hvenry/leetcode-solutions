from typing import Optional

"""
given the head of a singly linked list, reverse the list, and return the reversed list.

how to reverse a linked list:

two solutions:
iteratively:
- use two pointers
- go through the list, and swap the links

ie
1 --> 2 --> 3 
turns into
1 <-- 2  <-- 3
that is a reversed list!

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
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
