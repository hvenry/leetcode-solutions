from typing import Optional

"""
a linked list of length n is given such that each node contains an additional 
random pointer, which could point to any node in the list, or null.

construct a deep copy (meaning a fully copy de-refrencing each pointer).

The deep copy should consist of exactly n brand new nodes, where each new node has
its value set to the value of its corresponding original node.

Both the 'next' and 'random' pointer of the new nodes should point to new nodes in
the copied list such that the pointers in the original list and copied list represent
the same list state.

None of the pointers in the new list should point to nodes in the original list.

for example, if there are two nodes 'X' and 'Y' in the original list, where 
X.random --> Y, then for the corresponding two nodes 'x' and 'y' in the copied
list, x.random --> y.

return the head of the copied linked list.

the linked list is represented in the input/output as a list of 'n' nodes. Each node
is represented as a pair of [val, random_index] where
- 'val': an integer representing Node.val
- random_index: the index of the node (range from 0 to n-1) that the random pointer
points to, or 'null' if it does not point to any node.

example:
singly linked list, but every node has 1 extra pointer that is RANDOM (could be pointing anywhere including null)


solution:
- all we need to do is create a copy

two passe algorithm
- first pass, create a deep copy of each node
- map every old node to the new node with a hashmap

- second pass, do all the pointer connecting (pointer to the next node and random pointers)
- we can do this with the hashmap that we create in the first pass

time: O(n)
space: O(n) --> hashmap
"""


# node definition
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # if he have an old node that is Null, we want the copy to also be Null
        old_to_copy = {None: None}

        cur = head

        # first pass
        # keep going until curr reaches the end of the linked list (when current node becomes null)
        while cur:
            # create deep copy of node
            copy = Node(cur.val)
            # cur is the old node
            old_to_copy[cur] = copy
            cur = cur.next

        cur = head

        # second pass
        # set the pointers
        while cur:
            copy = old_to_copy[cur]
            # map to the copy of current.next
            copy.next = old_to_copy[cur.next]
            copy.random = old_to_copy[cur.random]
            cur = cur.next

        return old_to_copy[head]
