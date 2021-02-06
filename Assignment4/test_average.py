import unittest
import average

class Testfullname(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average.calcAvr([1,"Bob", "Joe"]),"Error")
        self.assertEqual(average.calcAvr([1.50,3.4,5.3,6.9,3.45,667.888]),114.73966666666666)
        self.assertEqual(average.calcAvr([]),"Error")
        self.assertEqual(average.calcAvr([-10,-50, -30]), -30)
        self.assertEqual(average.calcAvr([1, '2', "900"]), 301.0)
        self.assertEqual(average.calcAvr([1, 'f', "9050"]), "Error")
     
if __name__ ==  "__main__":
    unittest.main()