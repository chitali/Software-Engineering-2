import unittest
import leapYear

class Testfullname(unittest.TestCase):
    def test_average(self):
        self.assertEqual(leapYear.calcYear(2020),"Leap year")
        self.assertEqual(leapYear.calcYear(2021),"Not a leap year")
        self.assertEqual(leapYear.calcYear(1900),"Not a leap year")
        self.assertEqual(leapYear.calcYear(2000),"Leap year")
     
if __name__ ==  "__main__":
    unittest.main()