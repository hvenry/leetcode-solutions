import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        self.assertTrue(self.solution.canFinish(numCourses, prerequisites))

    def test_example2(self):
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        self.assertFalse(self.solution.canFinish(numCourses, prerequisites))

    def test_no_prerequisites(self):
        numCourses = 3
        prerequisites = []
        self.assertTrue(self.solution.canFinish(numCourses, prerequisites))

    def test_single_course(self):
        numCourses = 1
        prerequisites = []
        self.assertTrue(self.solution.canFinish(numCourses, prerequisites))

    def test_multiple_courses_no_cycle(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 1], [3, 2]]
        self.assertTrue(self.solution.canFinish(numCourses, prerequisites))

    def test_multiple_courses_with_cycle(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 1], [3, 2], [0, 3]]
        self.assertFalse(self.solution.canFinish(numCourses, prerequisites))

    def test_disconnected_graph(self):
        numCourses = 4
        prerequisites = [[1, 0], [3, 2]]
        self.assertTrue(self.solution.canFinish(numCourses, prerequisites))


if __name__ == "__main__":
    unittest.main()
