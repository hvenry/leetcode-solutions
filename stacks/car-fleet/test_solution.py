import unittest
from solution import Solution


class TestCarFleet(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        target = 12
        position = [10, 8, 0, 5, 3]
        speed = [2, 4, 1, 1, 3]
        self.assertEqual(self.solution.carFleet(target, position, speed), 3)

    def test_single_car(self):
        target = 10
        position = [3]
        speed = [3]
        self.assertEqual(self.solution.carFleet(target, position, speed), 1)

    def test_two_cars_same_speed(self):
        target = 10
        position = [3, 5]
        speed = [2, 2]
        self.assertEqual(self.solution.carFleet(target, position, speed), 2)

    def test_two_cars_different_speed(self):
        target = 10
        position = [3, 5]
        speed = [2, 1]
        self.assertEqual(self.solution.carFleet(target, position, speed), 1)

    def test_multiple_fleets(self):
        target = 100
        position = [10, 20, 30, 40, 50]
        speed = [10, 9, 8, 7, 6]
        self.assertEqual(self.solution.carFleet(target, position, speed), 5)

    def test_all_cars_same_speed(self):
        target = 100
        position = [10, 20, 30, 40, 50]
        speed = [5, 5, 5, 5, 5]
        self.assertEqual(self.solution.carFleet(target, position, speed), 5)


if __name__ == "__main__":
    unittest.main()
