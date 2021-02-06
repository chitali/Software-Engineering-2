import unittest
import volume

class Testfullname(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(volume.calcVol(0, 0, 0),0)
        self.assertEqual(volume.calcVol("hello", "bye", 0),"Error")
        self.assertEqual(volume.calcVol(10.95, -5, -1),"Error")
        self.assertEqual(volume.calcVol(10, 20.9, 30.5), 6374.5)
        self.assertEqual(volume.calcVol("10", "20", 1),200)

if __name__ ==  "__main__":
    unittest.main()