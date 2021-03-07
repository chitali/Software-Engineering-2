import unittest
import leapYear

class Testfullname(unittest.TestCase):
    def test_average(self):
        self.assertEqual(leapYear.calcYear(), 2020)
     
if __name__ ==  "__main__":
    unittest.main()