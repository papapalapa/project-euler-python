"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
class Problem3:
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
            
print(Problem3().primeNumbersList(10000))