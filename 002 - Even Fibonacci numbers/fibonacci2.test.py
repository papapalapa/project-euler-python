import unittest
from main import Problem2

# Test runtime 0.001s
class TestProblem2(unittest.TestCase):

    def test_fibonacci2_1st_term(self):
        self.assertEqual(Problem2().fibonacci2(1), 1)

    def test_fibonacci2_2nd_term(self):
        self.assertEqual(Problem2().fibonacci2(2), 2)

    def test_fibonacci2_3rd_term(self):
        self.assertEqual(Problem2().fibonacci2(3), 3)

    def test_fibonacci2_10th_term(self):
        self.assertEqual(Problem2().fibonacci2(10), 89)

    def test_fibonacci2_20th_term(self):
        self.assertEqual(Problem2().fibonacci2(20), 10946)

    def test_fibonacci2_40th_term(self):
        self.assertEqual(Problem2().fibonacci2(33), 5702887)

if __name__ == '__main__':
    unittest.main()