import unittest
from circle import area
from circle import perimeter

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)
       
    def test_square_mul(self):
        res = area(10)
        expected_res = 314.2
        decimal_places = 1
        rounded_res = round(res, decimal_places)
        self.assertEqual(rounded_res, expected_res)
    
    def test_perimeter_mul(self):
        res = perimeter(10)
        expected_res = 62.8
        decimal_places = 1
        rounded_res = round(res, decimal_places)
        self.assertEqual(rounded_res, expected_res)