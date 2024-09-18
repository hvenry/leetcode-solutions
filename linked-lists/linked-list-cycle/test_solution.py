import unittest
from solution import ListNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_no_cycle(self):
        # List: 1 -> 2 -> 3 -> 4
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        self.assertFalse(self.solution.hasCycle(head))

    def test_cycle_at_beginning(self):
        # List: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
        head = ListNode(1)
        second = ListNode(2)
        head.next = second
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = second
        self.assertTrue(self.solution.hasCycle(head))

    def test_cycle_in_middle(self):
        # List: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle)
        head = ListNode(1)
        head.next = ListNode(2)
        third = ListNode(3)
        head.next.next = third
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = third
        self.assertTrue(self.solution.hasCycle(head))

    def test_single_node_no_cycle(self):
        # List: 1
        head = ListNode(1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_single_node_with_cycle(self):
        # List: 1 -> 1 (cycle)
        head = ListNode(1)
        head.next = head
        self.assertTrue(self.solution.hasCycle(head))

    def test_empty_list(self):
        # List: None
        head = None
        self.assertFalse(self.solution.hasCycle(head))


if __name__ == "__main__":
    unittest.main()
