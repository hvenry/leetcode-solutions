import unittest
from solution import Solution


class TestCourseScheduleII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertTrue(result in [[0, 1, 2, 3], [0, 2, 1, 3]])

    def test_no_prerequisites(self):
        numCourses = 3
        prerequisites = []
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertEqual(result, [0, 1, 2])

    def test_single_course(self):
        numCourses = 1
        prerequisites = []
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertEqual(result, [0])

    def test_impossible_case(self):
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertEqual(result, [])

    def test_harder_example(self):
        numCourses = 6
        prerequisites = [[2, 0], [1, 0], [0, 3], [3, 4], [3, 5]]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertTrue(result in [[4, 5, 3, 0, 1, 2], [5, 4, 3, 0, 1, 2]])

    def test_disconnected_graph(self):
        numCourses = 4
        prerequisites = [[1, 0], [3, 2]]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertTrue(result in [[0, 1, 2, 3], [2, 3, 0, 1]])


if __name__ == "__main__":
    unittest.main()
