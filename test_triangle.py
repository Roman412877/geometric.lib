import unittest
from triangle import area
from triangle import perimeter

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
       
    def test_square_mul(self):
        res = area(10, 12)
        self.assertEqual(res, 60)
    
    def test_perimeter_mul(self):
        res = perimeter(10, 15, 20)
        self.assertEqual(res, 45)

