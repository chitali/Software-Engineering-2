import unittest
import fullname

class Testfullname(unittest.TestCase):
    def test_fullname(self):
        self.assertEqual(fullname.combName("Bob", "Joe"),"Bob Joe")
        self.assertEqual(fullname.combName(-10.95, 5),"Error")
        self.assertEqual(fullname.combName(10, "ten"),"Error")
        self.assertEqual(fullname.combName("Bob505", "Joe"), "Error")
        self.assertEqual(fullname.combName("Bob", "Joe11b"), "Error")
     
if __name__ ==  "__main__":
    unittest.main()