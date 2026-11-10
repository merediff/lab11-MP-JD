import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(7,7),14)
        self.assertEqual(add(0,10), 10)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3,2),1)
        self.assertEqual(subtract(0,2), -2)
        self.assertEqual(subtract(10,5),5)


    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 6), 0)

    def test_divide(self):
        self.assertEqual(div(4,4), 1)
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(-3, 15), -5)


    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10,1), 0)
        self.assertEqual(logarithm(10,10),1)
        self.assertEqual(logarithm(10, 100), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 100)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 0)
            logarithm(10, -1)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(10, 24), 26)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.asserEqual(square_root(0), 0)
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(4), 2)

# Do not touch this
if __name__ == "__main__":
    unittest.main()