import pdb
import unittest
from main import *


class Tests(unittest.TestCase):

    def testsss(self):
        self.assertEqual(solution('5'), '19')
        self.assertEqual(solution('8'), '47')
        self.assertEqual(solution('12'), '104')
        self.assertEqual(solution('20'), '287')
        self.assertEqual(solution('77'), '4208')

    def test_aganist_sqrt(self):
        values = [
            ('1000', '707813'),
            ('1000000', '707107488291'),
            ('5785454', '23667913151250'),
            ('57854548', '2366791601490674'),
            ('578545483', '236679158921787335'),
        ]

        for n, v in values:
            s = solution(n)
            self.assertEqual(s, v)


if __name__ == '__main__':
    unittest.main()
