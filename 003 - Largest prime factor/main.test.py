import unittest
from main import Problem3

class Problem3Test(unittest.TestCase):
    def testPrimeNumbersList_10(self):
        self.assertEqual(Problem3(0).primeNumbersList(10), [2,3,5,7])

    def testPrimeNumbersList_20(self):
        self.assertEqual(Problem3(0).primeNumbersList(20), [2,3,5,7,11,13,17,19])

    def testNextPrimeSet_10(self):
        problem3 = Problem3(0)
        primeList = problem3.primeList
        self.assertEqual(primeList, [2,3,5,7])
    
    def testNextPrimeSet_20(self):
        problem3 = Problem3(0)
        problem3.nextPrimeSet()
        primeList = problem3.primeList
        self.assertEqual(primeList, [2,3,5,7,11,13, 17,19])

    def testLargestPrimeFactor_13195(self):
        self.assertEqual(Problem3(13195).largestPrimeFactor(), 29)
    
    def testLargestPrimeFactor_25101(self):
        self.assertEqual(Problem3(25101).largestPrimeFactor(), 2789)

    def testLargestPrimeFactor_1000000000000000000000(self):
        self.assertEqual(Problem3(1000000000000000000000).largestPrimeFactor(), 5)

if __name__ == '__main__':
    unittest.main()