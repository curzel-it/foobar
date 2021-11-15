import unittest
from main import *


class Tests(unittest.TestCase):

    def test_1234_15(self):
        s = solution([1, 2, 3, 4], 15)
        self.assertEqual(s, [-1, -1])

    def test_431028_15(self):
        s = solution([4, 3, 10, 2, 8], 12)
        self.assertEqual(s, [2, 3])

    def test_list_of_1(self):
        s = solution([1], 12)
        self.assertEqual(s, [-1, -1])
        s = solution([1], 1)
        self.assertEqual(s, [0, 0])


if __name__ == '__main__':
    unittest.main()
