import unittest
from main import Problem4

class Problem4Test(unittest.TestCase):
    def testPalindromeTest_110011(self):
        self.assertEqual(Problem4().palindromeTest(110011), True)

    def testPalindromeTest_111(self):
        self.assertEqual(Problem4().palindromeTest(111), True)

    def testPalindromeTest_12121(self):
        self.assertEqual(Problem4().palindromeTest(12121), True)

    def testFactorHandler(self):
        self.assertEqual(Problem4().factorHandler(), (836, 836))

if __name__ == '__main__':
    unittest.main()