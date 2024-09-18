from typing import Optional

"""
given the head of a linked list, remove the nth node from the end of the list
and return its head

** FROM THE END OF THE LIST (not index)

example:
head = [1, 2, 3, 4, 5]
n = 2
result: [1, 2, 3, 5]

this is because the 4 was removed (which is the 2nd node from the end of the list)

solution:
- use two pointers with an offset of n between them (left and right)
- left pointer is at dummy node, right pointer is at n distance
- shift them down the list, once right is at the end, left is now right before the node that needs to be removed
- assign left.next to be lext.next.next
- return the dummy pointer
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node starting at 0 pointing to head
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete node that is n spaces from the end
        left.next = left.next.next

        # return dummy.next (without the 0)
        return dummy.next
