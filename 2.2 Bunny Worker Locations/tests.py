import unittest
from main import *


class Tests(unittest.TestCase):

    def test_5_10(self):
        s = solution(5, 10)
        self.assertEqual(s, '96')

    def test_3_2(self):
        s = solution(3, 2)
        self.assertEqual(s, '9')


if __name__ == '__main__':
    unittest.main()
