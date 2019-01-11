import unittest
from main import Problem2

# Test runtime 0.740s
class TestProblem2(unittest.TestCase):

    def test_fibonacci1_1st_term(self):
        self.assertEqual(Problem2().fibonacci1(1), 1)

    def test_fibonacci1_2nd_term(self):
        self.assertEqual(Problem2().fibonacci1(2), 2)

    def test_fibonacci1_3rd_term(self):
        self.assertEqual(Problem2().fibonacci1(3), 3)

    def test_fibonacci1_10th_term(self):
        self.assertEqual(Problem2().fibonacci1(10), 89)

    def test_fibonacci1_20th_term(self):
        self.assertEqual(Problem2().fibonacci1(20), 10946)

    def test_fibonacci1_40th_term(self):
        self.assertEqual(Problem2().fibonacci1(33), 5702887)

if __name__ == '__main__':
    unittest.main()