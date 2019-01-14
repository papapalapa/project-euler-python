"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
class Problem3:
    def __init__(self, dividend):
        self.limit = 10
        self.primeList = self.primeNumbersList(self.limit)
        self.primeFactors = []
        self.dividend = dividend

    # Get next set of prime numbers
    def nextPrimeSet(self):
        self.limit *= 2
        self.primeList = self.primeNumbersList(self.limit)

    # Sieve of Eratosthenes
    def primeNumbersList(self, target):
        numbersList = [i for i in range(2, target + 1)]
        terminatorNumber = int((len(numbersList) + 1)**0.5) + 1
        for i in numbersList:
            if (i**2 > target):
                break
            for j in numbersList:
                if j % i == 0 and j != i:
                    del numbersList[numbersList.index(j)]
        return numbersList

    def largestPrimeFactor(self):
        for primeNumber in self.primeList:
            if self.dividend % primeNumber == 0:
                self.primeFactors.append(primeNumber)
                self.dividend /= primeNumber
                self.largestPrimeFactor()
        if self.dividend != 1.0:
            self.nextPrimeSet()
            self.largestPrimeFactor()

        return max(self.primeFactors)


print(Problem3(1000000000000000000000).largestPrimeFactor())
