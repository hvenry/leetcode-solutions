import unittest
from solution import Solution
from solution import Solution, ListNode

class TestSolution(unittest.TestCase):
    def list_to_linkedlist(self, elements):
        head = ListNode(elements[0])
        current = head
        for element in elements[1:]:
            current.next = ListNode(element)
            current = current.next
        return head

    def linkedlist_to_list(self, head):
        elements = []
        current = head
        while current:
            elements.append(current.val)
            current = current.next
        return elements

    def test_reverseList(self):
        sol = Solution()

        # Test case 1: Regular case
        head = self.list_to_linkedlist([1, 2, 3, 4, 5])
        reversed_head = sol.reverseList(head)
        self.assertEqual(self.linkedlist_to_list(reversed_head), [5, 4, 3, 2, 1])

        # Test case 2: Single element
        head = self.list_to_linkedlist([1])
        reversed_head = sol.reverseList(head)
        self.assertEqual(self.linkedlist_to_list(reversed_head), [1])

        # Test case 3: Empty list
        head = None
        reversed_head = sol.reverseList(head)
        self.assertEqual(self.linkedlist_to_list(reversed_head), [])

        # Test case 4: Two elements
        head = self.list_to_linkedlist([1, 2])
        reversed_head = sol.reverseList(head)
        self.assertEqual(self.linkedlist_to_list(reversed_head), [2, 1])

if __name__ == '__main__':
    unittest.main()
