import unittest
from solution import ListNode, Solution


def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_mergeKLists(self):
        lists = [
            list_to_linkedlist([1, 4, 5]),
            list_to_linkedlist([1, 3, 4]),
            list_to_linkedlist([2, 6]),
        ]
        result = self.solution.mergeKLists(lists)
        self.assertEqual(linkedlist_to_list(result), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_mergeKLists_empty(self):
        lists = []
        result = self.solution.mergeKLists(lists)
        self.assertIsNone(result)

    def test_mergeKLists_single_list(self):
        lists = [list_to_linkedlist([1, 2, 3])]
        result = self.solution.mergeKLists(lists)
        self.assertEqual(linkedlist_to_list(result), [1, 2, 3])

    def test_mergeKLists_all_empty_lists(self):
        lists = [None, None, None]
        result = self.solution.mergeKLists(lists)
        self.assertIsNone(result)

    def test_mergeKLists_mixed_empty_and_non_empty_lists(self):
        lists = [
            None,
            list_to_linkedlist([2, 3, 5]),
            None,
            list_to_linkedlist([1, 4, 6]),
        ]
        result = self.solution.mergeKLists(lists)
        self.assertEqual(linkedlist_to_list(result), [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
