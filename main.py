from functools import reduce
from math import gcd
import unittest


# function for calculating the Least Common Multiple (LCM) of given input
def lcm(*args):
    return reduce(lambda a, b: a * b // gcd(a, b), args)


# Unit Test Class
class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(lcm(2, 5), 10)

    def test_2(self):
        self.assertEqual(lcm(2, 3, 4), 12)

    def test_3(self):
        self.assertEqual(lcm(9), 9)

    def test_4(self):
        self.assertEqual(lcm(0), 0)

    def test_5(self):
        self.assertEqual(lcm(0, 1), 0)

    def test_6(self):
        self.assertEqual(lcm(2, 3, 4, 10, 20), 60)

    def test_7(self):
        self.assertEqual(lcm(5, 2, 8, 24, 60), 120)


if __name__ == "__main__":
    unittest.main()
