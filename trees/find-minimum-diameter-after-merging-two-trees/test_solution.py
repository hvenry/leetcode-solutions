import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        edges1 = [[0, 1], [0, 2], [0, 3]]
        edges2 = [[0, 1]]
        self.assertEqual(self.solution.minimumDiameterAfterMerge(edges1, edges2), 3)

    def test_single_node_trees(self):
        edges1 = []
        edges2 = []
        self.assertEqual(self.solution.minimumDiameterAfterMerge(edges1, edges2), 1)

    def test_one_tree_is_line(self):
        edges1 = [[0, 1], [1, 2], [2, 3]]
        edges2 = [[0, 1], [1, 2]]
        self.assertEqual(self.solution.minimumDiameterAfterMerge(edges1, edges2), 4)

    def test_balanced_trees(self):
        edges1 = [[0, 1], [0, 2], [1, 3], [1, 4]]
        edges2 = [[0, 1], [0, 2], [1, 3], [1, 4]]
        self.assertEqual(self.solution.minimumDiameterAfterMerge(edges1, edges2), 5)


if __name__ == "__main__":
    unittest.main()
