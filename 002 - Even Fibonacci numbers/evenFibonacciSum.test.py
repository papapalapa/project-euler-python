import unittest
from main import Problem2

class TestProblem2(unittest.TestCase):

    def test_evenFibonacciSum_limit_20(self):
        self.assertEqual(Problem2().evenFibonacciSum(20), 10)

    def test_evenFibonacciSum_limit_40(self):
        self.assertEqual(Problem2().evenFibonacciSum(40), 44)

    def test_evenFibonacciSum_limit_60(self):
        self.assertEqual(Problem2().evenFibonacciSum(60), 44)

    def test_evenFibonacciSum_limit_80(self):
        self.assertEqual(Problem2().evenFibonacciSum(80), 44)

    def test_evenFibonacciSum_limit_100(self):
        self.assertEqual(Problem2().evenFibonacciSum(100), 44)

    def test_evenFibonacciSum_limit_4000000(self):
        self.assertEqual(Problem2().evenFibonacciSum(4000000), 4613732)

if __name__ == '__main__':
    unittest.main()