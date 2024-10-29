import unittest
from solution import Solution


class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(
            sorted(self.solution.letterCombinations("23")),
            sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        )

    def test_empty_input(self):
        self.assertEqual(self.solution.letterCombinations(""), [])

    def test_single_digit(self):
        self.assertEqual(
            sorted(self.solution.letterCombinations("2")), sorted(["a", "b", "c"])
        )

    def test_multiple_digits(self):
        self.assertEqual(
            sorted(self.solution.letterCombinations("234")),
            sorted(
                [
                    "adg",
                    "adh",
                    "adi",
                    "aeg",
                    "aeh",
                    "aei",
                    "afg",
                    "afh",
                    "afi",
                    "bdg",
                    "bdh",
                    "bdi",
                    "beg",
                    "beh",
                    "bei",
                    "bfg",
                    "bfh",
                    "bfi",
                    "cdg",
                    "cdh",
                    "cdi",
                    "ceg",
                    "ceh",
                    "cei",
                    "cfg",
                    "cfh",
                    "cfi",
                ]
            ),
        )

    def test_invalid_digit(self):
        with self.assertRaises(KeyError):
            self.solution.letterCombinations("1")


if __name__ == "__main__":
    unittest.main()
