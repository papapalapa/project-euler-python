"""
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
3, 5, 6
Find the sum of all the multiples of 3 or 5 below 1000.
"""
class Problem1:
    def __init__ (self, number):
        self.number = number

    def main(self):
        sum = 0
        for i in range(1, self.number):
            if i % 3 is 0 or i % 5 is 0:
                sum += i
        return sum

print(Problem1(1000).main())