import unittest
import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fibonacci.fib(0), 0)
        self.assertEqual(fibonacci.fib(1),1)
        self.assertEqual(fibonacci.fib(2),1)
        self.assertEqual(fibonacci.fib(6),8)
        self.assertEqual(fibonacci.fib(100), 354224848179261915075)
        self.assertEqual(fibonacci.fib("Random String1"), "Error")

    def test_factorial(self):
        self.assertEqual(fibonacci.factorial(0),1)
        self.assertEqual(fibonacci.factorial(1),1)
        self.assertEqual(fibonacci.factorial(2),2)
        self.assertEqual(fibonacci.factorial(5),120)
        self.assertEqual(fibonacci.factorial(10),3628800)


if __name__ ==  "__main__":
    unittest.main()