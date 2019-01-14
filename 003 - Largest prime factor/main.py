"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
class Problem3:
    def __init__(self, dividend):
        self.primeList = self.primeNumbersList(10000)
        self.primeFactors = []
        self.dividend = dividend

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
        
        return self.primeFactors, self.dividend, max(self.primeFactors)


print(Problem3(600851475143).largestPrimeFactor())