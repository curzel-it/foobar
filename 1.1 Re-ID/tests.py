import unittest
from main import *

class Tests(unittest.TestCase):

    def test_primes_list(self):
        numbers = []
        for prime in primes():
            numbers.append(prime)
            if len(numbers) == 10:
                break
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(numbers, expected)

    def test_primes_string_zero(self):
        s = primes_string(0)
        expected = '2'
        self.assertEqual(s, expected)

    def test_primes_string_single_digits(self):
        s = primes_string(4)
        expected = '2357'
        self.assertEqual(s, expected)

    def test_primes_string(self):
        s5 = primes_string(5)
        s6 = primes_string(6)
        expected = '235711'
        self.assertEqual(s5, expected)
        self.assertEqual(s5, s6)

if __name__ == '__main__':
    unittest.main()
