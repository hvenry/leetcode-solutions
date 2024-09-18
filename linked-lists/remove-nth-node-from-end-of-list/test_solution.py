import unittest
from solution import ListNode, Solution
from typing import Optional


class TestRemoveNthFromEnd(unittest.TestCase):
    def list_to_array(self, head: Optional[ListNode]) -> list:
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return array

    def array_to_list(self, array: list) -> Optional[ListNode]:
        if not array:
            return None
        head = ListNode(array[0])
        current = head
        for val in array[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def test_remove_nth_from_end(self):
        solution = Solution()

        # Test case 1
        head = self.array_to_list([1, 2, 3, 4, 5])
        n = 2
        expected = [1, 2, 3, 5]
        result = solution.removeNthFromEnd(head, n)
        self.assertEqual(self.list_to_array(result), expected)

        # Test case 2
        head = self.array_to_list([1])
        n = 1
        expected = []
        result = solution.removeNthFromEnd(head, n)
        self.assertEqual(self.list_to_array(result), expected)

        # Test case 3
        head = self.array_to_list([1, 2])
        n = 1
        expected = [1]
        result = solution.removeNthFromEnd(head, n)
        self.assertEqual(self.list_to_array(result), expected)

        # Test case 4
        head = self.array_to_list([1, 2])
        n = 2
        expected = [2]
        result = solution.removeNthFromEnd(head, n)
        self.assertEqual(self.list_to_array(result), expected)

        # Test case 5
        head = self.array_to_list([1, 2, 3, 4, 5])
        n = 5
        expected = [2, 3, 4, 5]
        result = solution.removeNthFromEnd(head, n)
        self.assertEqual(self.list_to_array(result), expected)


if __name__ == "__main__":
    unittest.main()
