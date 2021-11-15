import unittest
from main import *


class Tests(unittest.TestCase):

    def test_foobar(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6]), 3)
        self.assertEqual(solution([1, 1, 1]), 1)

    def test_additionals(self):
        self.assertEqual(solution([1, 1]), 0)
        self.assertEqual(solution([3, 6]), 0)
        self.assertEqual(solution([3, 7]), 0)
        self.assertEqual(solution([1, 3, 7]), 0)
        self.assertEqual(solution([]), 0)

    def test_longest_list(self):
        l = list(range(1, 2001))
        self.assertEqual(solution(l), 40888) 

    def test_1111(self):
        l = [1, 1, 1, 1]
        self.assertEqual(solution(l), 4)

    def test_111111(self):
        l = [1, 111111, 222222, 333333, 444444,
             555555, 666666, 777777, 888888, 999999]
        self.assertEqual(solution(l), 21)

    def test_unsorted_list(self):
        self.assertEqual(solution([3, 4, 1, 2, 6, 5]), 1)


if __name__ == '__main__':
    unittest.main()
