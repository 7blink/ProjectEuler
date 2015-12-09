"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sumofsquares(max):
    total = 0
    sumofrange = 0
    for i in range((max + 1)):
        #For each number in range, add the square, and also add the numbers together
        total = total + (i * i)
        sumofrange = sumofrange + i
        #sumofSquares gets squared, and total gets subtracted.
    return ((sumofrange * sumofrange) - total)

if __name__ == "__main__":
	print(sumofsquares(100))
