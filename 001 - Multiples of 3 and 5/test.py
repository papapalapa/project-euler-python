import unittest
from main import Problem1

class TestProblem1(unittest.TestCase):
    def test_main_below_7(self):
        self.assertEqual(Problem1(7).main(), 14)

    def test_main_below_10(self):
        self.assertEqual(Problem1(10).main(), 23)

    def test_main_below_1000(self):
        self.assertEqual(Problem1(1000).main(), 233168)
    
if __name__ == '__main__':
    unittest.main()