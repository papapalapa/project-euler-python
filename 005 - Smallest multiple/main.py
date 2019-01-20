"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
class Problem5:

    # Sieve of Eratosthenes
    def __init__(self, limit):
        self.limit = limit
        self.numberList = [i for i in range(2, self.limit + 1)]
        self.primeList = self.getPrimeList()
        self.factorList = []
        self.commonFactors = []
        

    def getPrimeList(self):
        numberList = self.numberList[:]
        for i in range(2, int(self.limit**0.5) + 1):
            for number in numberList:
                if number % i == 0 and number != i:
                    del numberList[numberList.index(number)]
        return numberList
    

    def primeFactorize(self, number):
        for prime in self.primeList:
            if number % prime == 0:
                self.factorList.append(prime)
                number /= prime
                self.primeFactorize(number)
                break
        return self.factorList
            

    def getAllFactors(self):
        for number in self.numberList:
            # Empty the object list
            self.factorList = []
            factors = self.primeFactorize(number)
            # Converting a list to a set gives a uniqued value
            for factor in set(factors):
                self.commonFactors.append(factor)
        return self.commonFactors


    # def getLeastCommonMultiple(self):
    #     commonFactors = self.getAllFactors()
    #     lcm = 1
    #     for factor in commonFactors:
    #         lcm *= factor
    #     return lcm