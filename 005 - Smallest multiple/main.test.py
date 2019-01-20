import unittest
from main import Problem5


class Problem5Test(unittest.TestCase):
    def testPrimeNumbersList_10(self):
        primeList = Problem5().primeList(10)
        self.assertEqual(primeList, [2, 3, 5, 7])

    def testPrimeNumbersList_20(self):
        primeList = Problem5().primeList(20)
        self.assertEqual(primeList, [2, 3, 5, 7, 11, 13, 17, 19])

if __name__ == '__main__':
    unittest.main()