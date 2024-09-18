import unittest
from solution import Node, Solution


class TestCopyRandomList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertIsNone(self.solution.copyRandomList(None))

    def test_single_node_no_random(self):
        node = Node(1)
        copied_list = self.solution.copyRandomList(node)
        self.assertEqual(copied_list.val, 1)
        self.assertIsNone(copied_list.next)
        self.assertIsNone(copied_list.random)

    def test_single_node_with_random(self):
        node = Node(1)
        node.random = node
        copied_list = self.solution.copyRandomList(node)
        self.assertEqual(copied_list.val, 1)
        self.assertIsNone(copied_list.next)
        self.assertEqual(copied_list.random, copied_list)

    def test_two_nodes_no_random(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.next = node2
        copied_list = self.solution.copyRandomList(node1)
        self.assertEqual(copied_list.val, 1)
        self.assertEqual(copied_list.next.val, 2)
        self.assertIsNone(copied_list.random)
        self.assertIsNone(copied_list.next.random)

    def test_two_nodes_with_random(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.next = node2
        node1.random = node2
        node2.random = node1
        copied_list = self.solution.copyRandomList(node1)
        self.assertEqual(copied_list.val, 1)
        self.assertEqual(copied_list.next.val, 2)
        self.assertEqual(copied_list.random.val, 2)
        self.assertEqual(copied_list.next.random.val, 1)

    def test_multiple_nodes_with_random(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.next = node2
        node2.next = node3
        node1.random = node3
        node2.random = node1
        node3.random = node2
        copied_list = self.solution.copyRandomList(node1)
        self.assertEqual(copied_list.val, 1)
        self.assertEqual(copied_list.next.val, 2)
        self.assertEqual(copied_list.next.next.val, 3)
        self.assertEqual(copied_list.random.val, 3)
        self.assertEqual(copied_list.next.random.val, 1)
        self.assertEqual(copied_list.next.next.random.val, 2)


if __name__ == "__main__":
    unittest.main()
