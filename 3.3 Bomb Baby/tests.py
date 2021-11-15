import unittest
from main import *


class Tests(unittest.TestCase):

    def test_foobar(self):
        self.assertEqual(solution(139, 1222), '21')
        self.assertEqual(solution(25995, 15904), '23')
        self.assertEqual(solution(4, 7), '4')
        self.assertEqual(solution(2, 1), '1')
        self.assertEqual(solution(1, 1), '0')
        self.assertEqual(solution(-1, 1), 'impossible')
        self.assertEqual(solution(2, 2), 'impossible')
        self.assertEqual(solution(2, 0), 'impossible')
        self.assertEqual(solution(0, 2), 'impossible')
        self.assertEqual(solution(2, 4), 'impossible')
        self.assertEqual(solution(4, 2), 'impossible')


if __name__ == '__main__':
    unittest.main()
