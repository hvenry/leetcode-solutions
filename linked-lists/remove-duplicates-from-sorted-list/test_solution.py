import unittest
from solution import ListNode, Solution


class TestSolution(unittest.TestCase):
    def list_to_linkedlist(self, elements):
        if not elements:
            return None
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

    def test_deleteDuplicates(self):
        solution = Solution()

        # Test case 1
        head = self.list_to_linkedlist([1, 1, 2, 3, 3])
        expected_output = [1, 2, 3]
        self.assertEqual(
            self.linkedlist_to_list(solution.deleteDuplicates(head)), expected_output
        )

        # Test case 2
        head = self.list_to_linkedlist([1, 1, 1])
        expected_output = [1]
        self.assertEqual(
            self.linkedlist_to_list(solution.deleteDuplicates(head)), expected_output
        )

        # Test case 3
        head = self.list_to_linkedlist([1, 2, 3])
        expected_output = [1, 2, 3]
        self.assertEqual(
            self.linkedlist_to_list(solution.deleteDuplicates(head)), expected_output
        )

        # Test case 4
        head = self.list_to_linkedlist([])
        expected_output = []
        self.assertEqual(
            self.linkedlist_to_list(solution.deleteDuplicates(head)), expected_output
        )

        # Test case 5
        head = self.list_to_linkedlist([1, 1, 2, 2, 3, 3, 4, 4])
        expected_output = [1, 2, 3, 4]
        self.assertEqual(
            self.linkedlist_to_list(solution.deleteDuplicates(head)), expected_output
        )


if __name__ == "__main__":
    unittest.main()
