"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
class Problem5:
    # Sieve of Eratosthenes
    def primeList(self, limit):
        numberList = [i for i in range(2, limit + 1)]
        for i in range(2, int(limit**0.5) + 1):
            for number in numberList:
                if number % i == 0 and number != i:
                    del numberList[numberList.index(number)]
        return numberList