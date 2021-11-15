import unittest
from main import *


class Tests(unittest.TestCase):

    def test_reflect_room_top(self):
        o, t = reflect_room([3, 3], [1, 1], [2, 2], TOP)
        self.assertEqual(o, (1, 2))
        self.assertEqual(t, (2, 1))

    def test_reflect_room_bottom(self):
        o, t = reflect_room([3, 3], [1, 1], [2, 2], BOTTOM)
        self.assertEqual(o, (1, 2))
        self.assertEqual(t, (2, 1))

    def test_reflect_room_right(self):
        o, t = reflect_room([3, 3], [1, 1], [2, 2], RIGHT)
        self.assertEqual(o, (2, 1))
        self.assertEqual(t, (1, 2))

    def test_reflect_room_left(self):
        o, t = reflect_room([3, 3], [1, 1], [2, 2], LEFT)
        self.assertEqual(o, (2, 1))
        self.assertEqual(t, (1, 2))

    def test_foobar_1(self):
        d = solution([3, 2], [1, 1], [2, 1], 4)
        self.assertEqual(d, 7)

    def test_foobar_2(self):
        d = solution([300, 275], [150, 150], [185, 100], 500)
        self.assertEqual(d, 9)


if __name__ == '__main__':
    unittest.main()
