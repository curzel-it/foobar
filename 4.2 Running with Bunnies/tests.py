import unittest
from main import *

class Tests(unittest.TestCase):
      
    """
    def test_foobar_1(self):
      d = solution(
        [
          [0, 1, 1, 1, 1], 
          [1, 0, 1, 1, 1], 
          [1, 1, 0, 1, 1], 
          [1, 1, 1, 0, 1], 
          [1, 1, 1, 1, 0]
        ], 3
      )
      self.assertEqual(d, [0, 1])
    """
    def test_foobar_2(self):
      d = solution(
        [
          [0, 2, 2, 2, -1], 
          [9, 0, 2, 2, -1],
          [9, 3, 0, 2, -1], 
          [9, 3, 2, 0, -1], 
          [9, 3, 2, 2,  0]
        ], 1
      )
      self.assertEqual(d, [1, 2])
if __name__ == '__main__':
    unittest.main()
