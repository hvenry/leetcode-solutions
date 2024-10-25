"""
You are given an array of k linked-lists, each linked-list is sorted in
ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Explanation:
The linked lists are:
[
    1->4->5,
    1->3->4,
    2->6
]
merging mthem into one sorted list:
1->1->2->3->4->5->6


Solution

Merging 2 Sorted Linked lists:
- use a dummy node, and decided if you want to merge first node from list a or b (pick smaller of 2)
- continue until no more nodes, if you run out of nodes in one list, then just append the rest

Merging k Sorted Linked Lists
- use a dummy node, take the min of k starting nodes
- place node refrences into min heap, this can be done in log(k)
    - pick the next node pointer that is the smallest in the heap
    - move the pointer to the next value, and then store this value in the heap
    - continue until no more

"""

from typing import List, Optional
import heapq


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # first node of each linked list
        for i, node in enumerate(lists):
            # check if wit is a node (not none)
            if node:
                # push node value to heap, and node refrence
                # the i is important because it is used to break ties, if we forget this then it uses node (which will cause error)
                heapq.heappush(heap, (node.val, i, node))

        # dummy node
        D = ListNode()
        cur = D

        while heap:
            _, i, node = heapq.heappop(heap)
            # whatever the current node is, we want to set the current next equal to it
            # this will be the smallest value
            cur.next = node
            cur = node
            # move the selected list to the next refrence
            node = node.next

            # if it is a node, add it to the heap
            if node:
                heapq.heappush(heap, (node.val, i, node))

        return D.next
