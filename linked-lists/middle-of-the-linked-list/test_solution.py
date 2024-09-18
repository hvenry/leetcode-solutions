import unittest
from solution import ListNode, Solution


class TestMiddleOfLinkedList(unittest.TestCase):
    def list_to_linkedlist(self, elements):
        head = ListNode(elements[0])
        current = head
        for element in elements[1:]:
            current.next = ListNode(element)
            current = current.next
        return head

    def linkedlist_to_list(self, node):
        elements = []
        while node:
            elements.append(node.val)
            node = node.next
        return elements

    def test_middleNode_odd_length(self):
        head = self.list_to_linkedlist([1, 2, 3, 4, 5])
        solution = Solution()
        middle = solution.middleNode(head)
        self.assertEqual(self.linkedlist_to_list(middle), [3, 4, 5])

    def test_middleNode_even_length(self):
        head = self.list_to_linkedlist([1, 2, 3, 4, 5, 6])
        solution = Solution()
        middle = solution.middleNode(head)
        self.assertEqual(self.linkedlist_to_list(middle), [4, 5, 6])

    def test_middleNode_single_element(self):
        head = self.list_to_linkedlist([1])
        solution = Solution()
        middle = solution.middleNode(head)
        self.assertEqual(self.linkedlist_to_list(middle), [1])

    def test_middleNode_two_elements(self):
        head = self.list_to_linkedlist([1, 2])
        solution = Solution()
        middle = solution.middleNode(head)
        self.assertEqual(self.linkedlist_to_list(middle), [2])


if __name__ == "__main__":
    unittest.main()
