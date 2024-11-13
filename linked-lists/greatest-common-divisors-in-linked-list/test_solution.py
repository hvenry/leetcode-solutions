import unittest
from solution import ListNode, Solution


def linked_list_to_list(head: ListNode) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def list_to_linked_list(lst: list) -> ListNode:
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        head = list_to_linked_list([18, 6, 10, 3])
        expected = [18, 6, 6, 2, 10, 1, 3]
        result = self.solution.insertGreatestCommonDivisors(head)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_single_node(self):
        head = list_to_linked_list([5])
        expected = [5]
        result = self.solution.insertGreatestCommonDivisors(head)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_two_nodes(self):
        head = list_to_linked_list([8, 12])
        expected = [8, 4, 12]
        result = self.solution.insertGreatestCommonDivisors(head)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_no_common_divisor(self):
        head = list_to_linked_list([7, 11])
        expected = [7, 1, 11]
        result = self.solution.insertGreatestCommonDivisors(head)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_multiple_nodes(self):
        head = list_to_linked_list([24, 36, 48])
        expected = [24, 12, 36, 12, 48]
        result = self.solution.insertGreatestCommonDivisors(head)
        self.assertEqual(linked_list_to_list(result), expected)


if __name__ == "__main__":
    unittest.main()
