import unittest
from solution import Codec


class TestCodec(unittest.TestCase):
    def setUp(self):
        self.codec = Codec()

    def test_encode_decode(self):
        test_cases = [
            (["Hello", "World"], ["Hello", "World"]),
            ([""], [""]),
            (["a", "b", "c"], ["a", "b", "c"]),
            (["abc", "def", "ghi"], ["abc", "def", "ghi"]),
            (["123", "456", "789"], ["123", "456", "789"]),
            (["", "", ""], ["", "", ""]),
            (
                ["longer string with spaces", "another one"],
                ["longer string with spaces", "another one"],
            ),
            (
                ["special!@#$%^&*()_+chars", "test"],
                ["special!@#$%^&*()_+chars", "test"],
            ),
        ]

        for input_strs, expected in test_cases:
            encoded = self.codec.encode(input_strs)
            decoded = self.codec.decode(encoded)
            self.assertEqual(decoded, expected)


if __name__ == "__main__":
    unittest.main()
