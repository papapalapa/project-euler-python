# Project Euler in Python

Inspired by this [blog](https://blog.usejournal.com/consider-yourself-a-developer-you-should-solve-the-project-euler-problems-ed8d13397c9c), I started this project.

Throughout my career as a software engineer, I'll be providing my solutions for the Project Euler problems.

## Problem 1
Find the sum of all the multiples of 3 or 5 *below* 1000.

Answer: `233168`

#### Solution

```python
class Problem1:
    def main(self, number):
        sum = 0
        for i in range(1, self.number):
            if i % 3 is 0 or i % 5 is 0:
                sum += i
        return sum
```
- Used a class-based approach to be consistent with my other solutions.
- Implemented for-loop to check for every number between 1 and 999
- Added the current iteration value to the 0-initialized sum variable if the modulus of 3 or 5 is 0
  - if the modulus is 0, the number is evenly divisible, which means it's a multiple of 3 (or 5)


## Problem 2
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

Answer: `4613732`

#### Solution

## Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Answer: `6857`

#### Solution
