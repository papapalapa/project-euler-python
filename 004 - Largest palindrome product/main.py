"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

class Problem4:
    def factorHandler(self):
        numbers = [1000, 1000]
        while numbers[0] is not 0:
            if (numbers[0] > numbers[1]):
                numbers[0] = numbers[0] - 1
            else:
                numbers[1] = numbers[1] - 1
            
            if self.palindromeTest(numbers[0] * numbers[1]):
                return numbers[0], numbers[1]

    def palindromeTest(self, number):
        number = str(number)
        digitNumber = len(number)

        for i in range(int(digitNumber / 2)):
            result = number[i] == number[digitNumber - i - 1]
            if (result == True):
                continue
            else:
                return False
        return True