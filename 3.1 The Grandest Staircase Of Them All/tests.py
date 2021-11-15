import unittest
from main import *


class Tests(unittest.TestCase):

    def test_foobar(self):
        self.assertEqual(solution(200), 487067745)
        self.assertEqual(solution(3), 1)

    def test_one(self):
        self.assertEqual(solution(3), 1)
        self.assertEqual(solution(4), 1)
        self.assertEqual(solution(5), 2)
        self.assertEqual(solution(6), 3)


if __name__ == '__main__':
    unittest.main()
