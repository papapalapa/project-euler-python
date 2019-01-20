import unittest
from main import Problem5


class Problem5Test(unittest.TestCase):
    def test_getPrimeList_10(self):
        primeList = Problem5(10).getPrimeList()
        self.assertEqual(primeList, [2, 3, 5, 7])

    def test_getPrimeList_20(self):
        primeList = Problem5(20).getPrimeList()
        self.assertEqual(primeList, [2, 3, 5, 7, 11, 13, 17, 19])

    def test_primeFactorize_9(self):
        factorList = Problem5(20).primeFactorize(9)
        self.assertEqual(factorList, [3, 3])

    def test_primeFactorize_12(self):
        factorList = Problem5(20).primeFactorize(12)
        self.assertEqual(factorList, [2, 2, 3])

    def test_primeFactorize_20(self):
        factorList = Problem5(20).primeFactorize(20)
        self.assertEqual(factorList, [2, 2, 5])

    def test_getAllFactors_to_5(self):
        allFactors = Problem5(5).getAllFactors()
        self.assertEqual(allFactors, [2, 3, 2, 5])

    def test_getAllFactors_to_10(self):
        allFactors = Problem5(10).getAllFactors()
        self.assertEqual(allFactors, [2, 3, 2, 5, 2, 3, 7, 2, 3, 2, 5])

    # def test_getLeastCommonMultiple_10(self):
    #     number = Problem5(10).getLeastCommonMultiple()
    #     self.assertEqual(number, 2520)

if __name__ == '__main__':
    unittest.main()