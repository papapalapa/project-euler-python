"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
class Problem3:
    # Sieve of Eratosthenes
    def primeNumbersList(self, limit):
        numbersList = [i for i in range(2, limit + 1)]
        for i in range(2, int(limit**0.5) + 1):
            prime = i
            for j in numbersList:
                if j % prime == 0 and j != prime:
                    del numbersList[numbersList.index(j)]
        
        return numbersList
            
print(Problem3().primeNumbersList(100))