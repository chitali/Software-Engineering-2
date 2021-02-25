import unittest
import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fibonacci.fib(0, 0)
        self.assertEqual(fibonacci.fib(1,1)
        self.assertEqual(fibonacci.fib(2,1)
        self.assertEqual(fibonacci.fib(6,8)
        self.assertEqual(fibonacci.fib(100, 354224848179261915075)
        self.assertEqual(fibonacci.fib("Random String1", "Error")
     
if __name__ ==  "__main__":
    unittest.main()