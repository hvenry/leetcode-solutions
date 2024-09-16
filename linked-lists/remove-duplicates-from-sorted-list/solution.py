from typing import Optional

"""
given the head of a sorted linked list, delete all duplicates such that each element
appears only once. Return the linked list sorted as well.

example:
head = [1, 1, 2, 3, 3]
output = [1,2,3]

solution:
- keep checking cur.next until it is not equal to the current node
- when next distinct node found, point cur.next to the distinct node

time: O(n)
memory: O(1)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        # continue until current is not null
        while current:
            # now keep iterating until there is a unique value for current.next
            while current.next and current.next.val == current.val:
                # this deletes the node (because it skip it)
                current.next = current.next.next
            current = current.next
        return head
