import unittest
from solution import ListNode, Solution


class TestMergeTwoLists(unittest.TestCase):
    def list_to_linkedlist(self, lst):
        # Helper function to convert list to linked list
        dummy = ListNode()
        current = dummy
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    def linkedlist_to_list(self, node):
        # Helper function to convert linked list to list
        lst = []
        while node:
            lst.append(node.val)
            node = node.next
        return lst

    def test_merge_two_empty_lists(self):
        solution = Solution()
        self.assertIsNone(solution.mergeTwoLists(None, None))

    def test_merge_one_empty_one_non_empty_list(self):
        solution = Solution()
        list1 = self.list_to_linkedlist([1, 2, 4])
        self.assertEqual(
            self.linkedlist_to_list(solution.mergeTwoLists(list1, None)), [1, 2, 4]
        )
        self.assertEqual(
            self.linkedlist_to_list(solution.mergeTwoLists(None, list1)), [1, 2, 4]
        )

    def test_merge_two_non_empty_lists(self):
        solution = Solution()
        list1 = self.list_to_linkedlist([1, 2, 4])
        list2 = self.list_to_linkedlist([1, 3, 4])
        merged_list = solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linkedlist_to_list(merged_list), [1, 1, 2, 3, 4, 4])

    def test_merge_lists_with_different_lengths(self):
        solution = Solution()
        list1 = self.list_to_linkedlist([1, 3, 5, 7])
        list2 = self.list_to_linkedlist([2, 4, 6])
        merged_list = solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linkedlist_to_list(merged_list), [1, 2, 3, 4, 5, 6, 7])


if __name__ == "__main__":
    unittest.main()
